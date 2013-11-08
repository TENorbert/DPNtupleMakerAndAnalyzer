// -*- C++ -*-
//
// Package:    GenStudy
// Class:      GenStudy
// 
/**\class GenStudy GenStudy.cc EXO/GenStudy/src/GenStudy.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Shih-Chuan Kao
//         Created:  Thu Mar 15 12:51:07 CDT 2012
// $Id: GenStudy.cc,v 1.15 2012/12/31 22:45:14 sckao Exp $
//
//

#include "GenStudy.h"
#include "Ntuple.h"

using namespace edm;

GenStudy::GenStudy(const edm::ParameterSet& iConfig) {
   //now do what ever initialization is needed
   genSrc         = iConfig.getParameter<edm::InputTag> ("genParticles"); 
   tau            = iConfig.getParameter<double> ("tau");

   expPDF = new TRandom();
   expPDF->SetSeed( 123 );

}


GenStudy::~GenStudy() {
 
}

//
// member functions
//

// ------------ method called for each event  ------------
void GenStudy::PrintGenEvent(const edm::Event& iEvent ) {

   Handle<edm::HepMCProduct> HepMCEvt;
   iEvent.getByLabel("generator", "", HepMCEvt);
   const HepMC::GenEvent* MCEvt = HepMCEvt->GetEvent();
   printf( " ======================================== \n ") ;
   for ( HepMC::GenEvent::particle_const_iterator it = MCEvt->particles_begin(); it != MCEvt->particles_end(); ++it ) {
       if ( (*it)->pdg_id() != 1000022 ) continue ;
       HepMC::FourVector p4 = (*it)->momentum();
       HepMC::FourVector v1 = (*it)->production_vertex()->position() ;
       cout<<" PID: "<< (*it)->pdg_id() <<" m:"<< (*it)->generatedMass() <<" E:"<< p4.e()<<" stat:"<<(*it)->status() ;
       cout<<"   from : "<< v1.z() <<" @T: "<< v1.t() ;
       if ( (*it)->status() == 3) {
          HepMC::FourVector v2 = (*it)->end_vertex()->position() ;
          cout<<"   to "<< v2.z() <<" @T: "<< v2.t() << endl;
       }

       // trace its parents
       HepMC::GenVertex* v_in = (*it)->production_vertex() ;
       for ( HepMC::GenVertex::particles_in_const_iterator i1 = v_in->particles_in_const_begin(); i1 != v_in->particles_in_const_end(); i1++) {
           cout<<"  <=== pid: "<< (*i1)->pdg_id() <<" E:"<< (*i1)->momentum().e()<<" stat:"<<(*i1)->status() <<endl ;
       }
       // trace its children
       if ( (*it)->status() == 3) {
          HepMC::GenVertex* v_out = (*it)->end_vertex() ;
          for ( HepMC::GenVertex::particles_out_const_iterator i1 = v_out->particles_out_const_begin(); i1 != v_out->particles_out_const_end(); i1++) {
              cout<<"  ===> pid: "<< (*i1)->pdg_id() <<" E:"<< (*i1)->momentum().e()<<" stat:"<<(*i1)->status() <<endl ;
          }
       }
       //cout<<" PID: "<< (*it)->pdg_id() <<" P:"<< p4.pz() <<endl ;
   }
    
}

// From GenEvent , time in ns, length in mm
void GenStudy::GetGenEvent(const edm::Event& iEvent, Ntuple& leaves, bool debug ) {

   Handle<edm::HepMCProduct> HepMCEvt;
   iEvent.getByLabel("generator", "", HepMCEvt);
   const HepMC::GenEvent* MCEvt = HepMCEvt->GetEvent();
   int i = 0 ;
   if (debug) printf(" ================================================= \n");
   for ( HepMC::GenEvent::particle_const_iterator it = MCEvt->particles_begin(); it != MCEvt->particles_end(); ++it ) {
       // tag neutrilino(1000022)
       if ( (*it)->pdg_id() != 1000022 || (*it)->status() != 3 ) continue ;
       HepMC::FourVector p4 = (*it)->momentum();

       leaves.pdgId[i] = (*it)->pdg_id() ;
       leaves.momId[i] = -1 ;
       leaves.genPx[i] = p4.px() ;
       leaves.genPy[i] = p4.py() ;
       leaves.genPz[i] = p4.pz() ;
       leaves.genE[i]  = p4.e() ;
       leaves.genM[i]  = (*it)->generatedMass() ;

       HepMC::FourVector v2 = (*it)->end_vertex()->position() ;
       leaves.genVx[i] = v2.x() / 10. ;
       leaves.genVy[i] = v2.y() / 10.;
       leaves.genVz[i] = v2.z() / 10.;
       if ( debug ) {
          HepMC::FourVector v1 = (*it)->production_vertex()->position() ;
          printf(" X[%d] v1[%.2f,%.2f,%.2f] -> v2[%.2f,%.2f,%.2f]\n", i, v1.x(), v1.y(), v1.z(), v2.x(), v2.y(), v2.z() ) ;
          printf("       p4: (%.1f,%.1f,%.1f,%.1f) \n", p4.px(), p4.py(), p4.pz(), p4.e() ) ;
          printf(" --------------------------------------------- \n");
       }
       //leaves.genT[i]  = ( v2.t() - v1.t() ) / 300. ; still zero ... useless
       int xi = i ;
       i++ ;

       double beta  = sqrt( (p4.px()*p4.px()) + (p4.py()*p4.py()) + (p4.pz()*p4.pz()) ) / p4.e() ;
       // trace its children, photon(22) and gravitino(1000039)
       // looping over the particles at the end vertex of the mother particle
       HepMC::GenVertex* v_out = (*it)->end_vertex() ;
       for ( HepMC::GenVertex::particles_out_const_iterator i1 = v_out->particles_out_const_begin(); i1 != v_out->particles_out_const_end(); i1++) {
           HepMC::GenVertex* v1_out = (*i1)->end_vertex() ;
           if ( (*i1)->pdg_id() != 22 &&  (*i1)->pdg_id() != 1000039 ) continue ;
           for ( HepMC::GenVertex::particles_out_const_iterator i2  = v1_out->particles_out_const_begin(); 
                                                                i2 != v1_out->particles_out_const_end(); i2++) {
               if ( (*i2)->status() != 1 ) continue ;
	       leaves.pdgId[i] = (*i2)->pdg_id() ;
	       leaves.momId[i] = xi ;
	       leaves.genPx[i] = (*i2)->momentum().px() ;
	       leaves.genPy[i] = (*i2)->momentum().py() ;
	       leaves.genPz[i] = (*i2)->momentum().pz() ;
	       leaves.genE[i]  = (*i2)->momentum().e() ;
	       leaves.genM[i]  = (*i2)->generatedMass() ;
	       leaves.genVx[i] = v1_out->position().x() / 10. ;
	       leaves.genVy[i] = v1_out->position().y() / 10. ;
	       leaves.genVz[i] = v1_out->position().z() / 10. ;
	       leaves.genT[xi]  = (v1_out->position().t() - v_out->position().t()) / 300. ; // this is tau*gamma for neutralino
	       leaves.genT[i]  = -1 ;  // this is lifetime(tau*gamma) for photon and gravitino
               if ( debug ) {
                  HepMC::FourVector v_x =  v_out->position() ;
                  HepMC::FourVector v_g =  v1_out->position() ;
                  double dx = v1_out->position().x() - v_out->position().x() ;
		  double dy = v1_out->position().y() - v_out->position().y() ;
		  double dz = v1_out->position().z() - v_out->position().z() ;
		  double dr = sqrt( (dx*dx) +  (dy*dy) + (dz*dz) ) ;

                  HepMC::FourVector g4 = (*i2)->momentum() ;
                  printf("   g[%d] v1[%.2f,%.2f,%.2f] -> v2[%.2f,%.2f,%.2f]\n", 
                              i-xi, v_x.x(), v_x.y(), v_x.z(), v_g.x(), v_g.y(), v_g.z() ) ;
                  printf("         p4 (%.1f,%.1f,%.1f,%.1f) , dT = %.3f , dr/beta = %.3f \n", 
                                     g4.px(), g4.py(), g4.pz(), g4.e(), v_g.t() - v_x.t() , dr/beta ) ;
                  printf("   --------------------------------------------- \n");
		  //cout<<"  <"<< i <<">  PID: "<<(*i2)->pdg_id() <<" from "<< xi <<" beta:"<< beta ;
		  //cout<<"  t: "<< v1_out->position().t() - v_out->position().t() <<" ctg: "<< dr/beta <<" ctbg: "<< dr  <<endl;
               }
	       i++ ;
           }
       }
   }
   leaves.nGen = i ;      
   //cout<<" nGen = "<< leaves.nGen <<endl ;
}

// From GenParticles
void GenStudy::GetGen(const edm::Event& iEvent, Ntuple& leaves ) {

   Handle< std::vector<reco::GenParticle> > genParticles;
   iEvent.getByLabel( genSrc , genParticles );

   //printf( " ======================================== \n ") ;
   int i = 0 ;
   for (std::vector<reco::GenParticle>::const_iterator it = genParticles->begin(); it != genParticles->end(); it++ ){

       if ( it->pdgId() == 1000022 && it->status() == 3 ) {
          
          leaves.pdgId[i] = it->pdgId() ;
          leaves.momId[i] = -1 ;
          leaves.genPx[i] = it->p4().Px() ;
          leaves.genPy[i] = it->p4().Py() ;
          leaves.genPz[i] = it->p4().Pz() ;
          leaves.genE[i]  = it->p4().E() ;
	  leaves.genVx[i] = it->vx() ;
	  leaves.genVy[i] = it->vy() ;
	  leaves.genVz[i] = it->vz() ;
           
          double lifeTime = expPDF->Exp( tau ) ;
          double gamma = it->p4().E() / it->mass() ;
          leaves.genT[i]  = lifeTime ;
  
          i++ ;

          //printf( " PID = %d ,  status: %d", it->pdgId(), it->status() ) ;
          //printf( " M: %.2f  P: %.2f, E: %.2f gamma: %.2f \n", it->mass(), it->p(), it->energy(), it->energy()/it->mass() )  ;
          //printf( "  Vtx=( %.2f, %.2f, %.2f ) \n" , it->vx(),  it->vy(), it->vz() ) ;
          double x1 = it->vx() ;
          double y1 = it->vy() ;
          double z1 = it->vz() ;
          double t1 = 0 ;
          bool insideEcal =  Propagator( it->p4(), x1, y1, z1, t1, lifeTime*gamma ) ;
          /*if ( insideEcal ) {
             cout<<"  ctau gamma : "<< lifeTime * gamma /10. <<" L = "<< sqrt( (x1*x1) + (y1*y1) + (z1*z1) ) <<endl; 
             cout<<"  ctau z = "<< lifeTime * gamma*cos(it->theta() ) <<"  Lz = "<< z1 <<endl ; 
             cout<<"  ctau x = "<< lifeTime * gamma*sin(it->theta())*cos(it->phi() ) <<"  Lx = "<< x1 <<endl ; 
             cout<<"  ctau y = "<< lifeTime * gamma*sin(it->theta())*sin(it->phi() ) <<"  Ly = "<< y1 <<endl ; 
             cout<<"  lifetime = "<< lifeTime * gamma /300 <<"   T = "<< t1 <<endl;
          }*/
          //printf( "  beta: %.2f, ctau: %.3f, T: %.2f \n" , it->p()/it->energy(),  lifeTime, t1 ) ;
          //if ( insideEcal ) cout<<" ** Still Inside Ecal ** "<<endl ;

          for (size_t q=0; q< it->numberOfDaughters(); ++q) {
              const reco::Candidate *dau = it->daughter(q) ;
              if( abs(dau->pdgId()) != 22 ) continue;
              //printf( "   pID = %d ,  status: %d  E: %.2f \n" , dau->pdgId(),  dau->status(), dau->energy() ) ;
              //printf( "   vtx=( %.2f, %.2f, %.2f ) \n" , dau->vx(),  dau->vy(), dau->vz() ) ;
              
              leaves.genPx[i] = dau->px() ;
              leaves.genPy[i] = dau->py() ;
              leaves.genPz[i] = dau->pz() ;
              leaves.genE[i]  = dau->energy() ;
              leaves.genVx[i] = x1 ;
              leaves.genVy[i] = y1 ;
              leaves.genVz[i] = z1 ;
              leaves.momId[i]  = i-1 ;
              leaves.pdgId[i]  = 22 ;
              
              Propagator( dau->p4(), x1, y1, z1, t1 ) ;
              double t0 = sqrt( (x1*x1) + (y1*y1) + (z1*z1) ) /30. ;
              //printf( "   pos:( %.2f, %.2f, %.2f),  T: %.2f  T0: %.2f \n" , x1, y1, z1, t1, t0 ) ;
              double delayTime = t1 - t0 ; 
              if ( !insideEcal ) delayTime = -99 ;
              leaves.genT[i] = delayTime ;
              i++ ; 
          }
       }
   }
   leaves.nGen = i ;      

}

bool GenStudy::Propagator( LorentzVector v, double& x, double& y, double& z, double& t, double ctaugamma ) {

    double bx = v.Px() / v.E() ;
    double by = v.Py() / v.E() ;
    double bz = v.Pz() / v.E() ;

    double dt = 0.01 ;
    double r = sqrt( (x*x) + (y*y ) );
    bool insideEcal = true ;
    bool alived     = true ;
    do { 
       t = t + dt ;
       x = x + (bx*dt*30) ;
       y = y + (by*dt*30) ;
       z = z + (bz*dt*30) ;
       r = sqrt( (x*x) + (y*y ) ) ;
       //double trace = sqrt( (r*r) + (z*z ) ) ;
       //alived     = ( trace < (ctaugamma/10.)    ) ? true : false ;
       alived     = ( t < (ctaugamma/300.)     ) ? true : false ;
       //insideEcal = ( r < 129 && fabs(z) < 293.5 ) ? true : false ;
       insideEcal = ( r < 155 && fabs(z) < 350 ) ? true : false ;

    } while ( insideEcal && alived ) ;
 
    return insideEcal ;
}

//define this as a plug-in
//DEFINE_FWK_MODULE(GenStudy);
