#ifndef Ntuple_h
#define Ntuple_h

#include "TChain.h" 

#define MAXVTX 30
#define MAXJET 20
#define MAXPHO 12
#define MAXMU 5
#define MAXELE 5
#define MAXGEN 20

struct Ntuple
{
  
  unsigned int runId;
  unsigned int lumiSection;
  unsigned int orbit;
  unsigned int bx;
  unsigned int eventId;
  int triggered ;
  int L1a;  

  int nOutTimeHits ;
  int nHaloTrack ;
  //float haloPhi ;
  //float haloRho ;

  // vertex variables
  int   totalNVtx ;
  int   nVertices;
  float vtxNTracks[MAXVTX];
  float vtxChi2[MAXVTX];
  float vtxNdof[MAXVTX];
  float vtxRho[MAXVTX];
  float vtxZ[MAXVTX];

  float z0Ratio;
  //int   nTrkZ0[33];
  
  // reco variables
  int   nJets ;
  float jetPx[MAXJET];
  float jetPy[MAXJET];
  float jetPz[MAXJET];
  float jetE[MAXJET];
  int   jetNDau[MAXJET];
  int   jetCM[MAXJET];
  float jetCEF[MAXJET];
  float jetCHF[MAXJET];
  float jetNHF[MAXJET];
  float jetNEF[MAXJET];
  float jecUnc[MAXJET];
  float jerUnc[MAXJET];
  //float jecUncU[MAXJET];
  //float jecUncD[MAXJET];

  float jseedtime1[MAXJET];
  float jseedtime2[MAXJET];
  float jseedChi2[MAXJET];
  float jseedE[MAXJET];
  float jseedOOtChi2[MAXJET];
  float jseedBCtime[MAXJET];
  float jseedtimeErr[MAXJET];
  float jWavetime[MAXJET];
  float jWavetimeErr[MAXJET];
  float jfspike[MAXJET];
  float jtChi2[MAXJET];
  int jnXtals[MAXJET];
  int jnBC[MAXJET];
  int jnseedXtals[MAXJET];
  int jnspikes[MAXJET];
  float jseedBCEnergy[MAXJET];
  float jseedBCEt[MAXJET];
  float jseedBCPt[MAXJET];
 // float jCandVx[MAXJET];
 // float jCandVy[MAXJET];
 // float jCandVz[MAXJET];
  float jCandEcalE[MAXJET];
  float jCandHcalE[MAXJET];
  float jCandHoE[MAXJET];
  float jgammaE[MAXJET];
  float jdR[MAXJET];
  int jnUnMatched[MAXJET];
  

  float metPx;
  float metPy;
  float met;
  float met0Px;
  float met0Py;
  float met0;
  float met_dx1;
  float met_dy1;
  float met_dx2;
  float met_dy2;
  float met_dx3;
  float met_dy3;

  float t_metPx;
  float t_metPy;
  float t_met;
  float t_metdR;
  float t_phoPx;
  float t_phoPy;
  float t_phoPz;
  float t_phoE;
  float t_phodR;

  int   nElectrons ;
  float elePx[MAXELE];
  float elePy[MAXELE];
  float elePz[MAXELE];
  float eleE[MAXELE];
  int   eleNLostHits[MAXELE] ;
  float eleEcalIso[MAXELE];
  float eleHcalIso[MAXELE];
  float eleTrkIso[MAXELE] ;
  float e_cHadIso[MAXELE] ;
  float e_nHadIso[MAXELE] ;
  float e_photIso[MAXELE] ;

  int   nMuons ;
  float muPx[MAXMU];
  float muPy[MAXMU];
  float muPz[MAXMU];
  float muE[MAXMU];
  float muIso[MAXMU];

  int   nPhotons ;
  float phoPx[MAXPHO];
  float phoPy[MAXPHO];
  float phoPz[MAXPHO];
  float phoE[MAXPHO];
  float phoEcalIso[MAXPHO];
  float phoHcalIso[MAXPHO];
  float phoTrkIso[MAXPHO];
  float cHadIso[MAXPHO] ;
  float nHadIso[MAXPHO] ;
  float photIso[MAXPHO] ;
  float dR_TrkPho[MAXPHO];
  float pt_TrkPho[MAXPHO];
  float phoHoverE[MAXPHO];
  float sMinPho[MAXPHO];
  float sMajPho[MAXPHO];
  float seedTime[MAXPHO];
  float seedTimeErr[MAXPHO];
  float aveTime[MAXPHO];
  float aveTime1[MAXPHO];
  float aveTimeErr[MAXPHO];
  float aveTimeErr1[MAXPHO];
  float timeChi2[MAXPHO] ;
  float fSpike[MAXPHO] ;
  float maxSwissX[MAXPHO] ;
  float seedSwissX[MAXPHO] ;
  float sigmaEta[MAXPHO] ;
  float sigmaIeta[MAXPHO] ;
  int   nXtals[MAXPHO] ;
  int   nBC[MAXPHO] ;

  float cscRho[MAXPHO];
  float cscdPhi[MAXPHO];
  float cscTime[MAXPHO];
  float dtdEta[MAXPHO];
  float dtdPhi[MAXPHO];

  // Gen Particle information
  int nGen ; 
  int pdgId[MAXGEN] ;
  int momId[MAXGEN] ;
  float genPx[MAXGEN] ; 
  float genPy[MAXGEN] ; 
  float genPz[MAXGEN] ; 
  float genE[MAXGEN] ; 
  float genM[MAXGEN] ; 
  float genVx[MAXGEN] ; 
  float genVy[MAXGEN] ; 
  float genVz[MAXGEN] ; 
  float genT[MAXGEN] ; 

};

// ------------------------------------------------------------------------
//! branch addresses settings
void setBranchAddresses(TTree* chain, Ntuple& treeVars);

//! create branches for a tree
void setBranches(TTree* chain, Ntuple& treeVars);

//! initialize branches
void initializeBranches(TTree* chain, Ntuple& treeVars);



#endif
