import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
       #'dcache:/pnfs/cms/WAX/11/store/data/Run2012B/SinglePhoton/RECO/PromptReco-v1/000/193/998/10950429-439D-E111-B454-BCAEC5329705.root'
       #'file:/PhotonHad/Run2012B-PromptReco-v1/RECO/file.root'
       #'file:/GMSB_Lambda-180_CTau-2000_TuneZ2star_8TeV-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v2/GEN-SIM-RECO/file.root'
    'dcache:/pnfs/cms/WAX/11/store/mc/Summer12_DR53X/GMSB_Lambda-180_CTau-2000_TuneZ2star_8TeV-pythia6/GEN-SIM-RECO/PU_S10_START53_V7A-v2/00000/4CF5F5B5-EB10-E211-9515-00215E21DCA2.root'
       #'file:/MET/Run2012B-PromptReco-v1/RECO/file.root'

    ),
    # explicitly drop photons resident in AOD/RECO, to make sure only those locally re-made (uncleaned photons) are used
    inputCommands = cms.untracked.vstring('keep *'
                                          #,'drop  *_photonCore_*_RECO' # drop hfRecoEcalCandidate as remade in this process
                                          #, 'drop *_photons_*_RECO' # drop photons as remade in this process
                                          )

)

process.options   = cms.untracked.PSet(
                    wantSummary = cms.untracked.bool(True),  
                    SkipEvent = cms.untracked.vstring('ProductNotFound')
)   

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = cms.untracked.int32(10)

process.ana = cms.EDAnalyzer('DPAnalysis',
    rootFileName     = cms.untracked.string('pat_mc_test.root'),
    #rootFileName     = cms.untracked.string('/uscms_data/d2/sckao/Data2012/run2012_test.root'),
    triggerName      = cms.vstring('HLT_Photon50_CaloIdVL_IsoL','HLT_DisplacedPhoton65_CaloIdVL_IsoL_PFMET25'),
    L1GTSource       = cms.string('L1_SingleEG22'),
    L1Select         = cms.bool( False ),
    isData           = cms.bool( False ),
    cscHaloData      = cms.InputTag("CSCHaloData"),
    staMuons         = cms.InputTag("standAloneMuons"),
    CSCSegmentCollection = cms.InputTag("cscSegments"),
    trigSource = cms.InputTag("TriggerResults","","HLT"),
    jetSource   = cms.InputTag("ak5PFJets"),
    patJetSource = cms.InputTag("selectedPatJetsPFlow"),
    #metSource   = cms.InputTag("pfMet"),
    metSource   = cms.InputTag("pfType1CorrectedMet"),
    muonSource  = cms.InputTag("muons"),
    trackSource = cms.InputTag("generalTracks"),
    electronSource   = cms.InputTag("gsfElectrons"),
    photonSource     = cms.InputTag("myphotons"),
    pvSource         = cms.InputTag("offlinePrimaryVerticesWithBS"),
    beamSpotSource   = cms.InputTag("offlineBeamSpot"),
    EBRecHitCollection = cms.InputTag("reducedEcalRecHitsEB"),
    EERecHitCollection = cms.InputTag("reducedEcalRecHitsEE"),
    tau                = cms.double( 2000 ), 
    genParticles = cms.InputTag("genParticles"),

    # Set up cuts for physics objects
    # vertex cuts                z   ndof   d0 
    vtxCuts       = cms.vdouble( 99,    0,  99 ),
    # photon cuts                pt   eta  sMajMax,  sMinMin, sMinMax,   dR,  Num  leadingPt  
    photonCuts    = cms.vdouble( 45,  2.4,     99.,      -1.,     99.,   0.0,  1,    45  ),
    # photon isolation           trkR,  ecalSumEt, ecalR, hcalSumEt, hcalR 
    photonIso     = cms.vdouble(  1.,       5.0,   1.,       5.0,   1. ),
    # jet cuts                   pt    eta    dR,  nJets
    jetCuts       = cms.vdouble( 30. , 2.4,  0.3,    0 ),
    metCuts       = cms.vdouble( 0. ),
    # electron cuts              pt  eta  EBIso  EEIso nLostHit  
    electronCuts  = cms.vdouble( 25, 2.4,  0.15,   0.1,      2 ),
    # muon cuts                  pt  eta  Iso  dR   
    muonCuts      = cms.vdouble( 25, 2.1, 0.2, 0.3 ),

)

###########  USE UNCLEANED SUPERCLUSTERS  ######################### 
# Global Tag
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
#process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_noesprefer_cff")
#process.GlobalTag.globaltag = 'GR_P_V40::All'
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag( process.GlobalTag, 'GR_R_53_V18::All' )


# to get clustering 
process.load("Configuration.StandardSequences.Geometry_cff")
process.load('Configuration/StandardSequences/GeometryExtended_cff')

# Geometry
process.load("Geometry.CaloEventSetup.CaloTopology_cfi")
process.load("Geometry.CaloEventSetup.CaloGeometry_cff")
process.load("Geometry.CaloEventSetup.CaloGeometry_cfi")
process.load("Geometry.EcalMapping.EcalMapping_cfi")
process.load("Geometry.EcalMapping.EcalMappingRecord_cfi")
process.load("Geometry.MuonNumbering.muonNumberingInitialization_cfi") # gfwork: need this?


process.CaloTowerConstituentsMapBuilder = cms.ESProducer("CaloTowerConstituentsMapBuilder")

process.load("RecoEcal.EgammaClusterProducers.uncleanSCRecovery_cfi")
process.uncleanSCRecovered.cleanScCollection=cms.InputTag ("correctedHybridSuperClusters")

# myPhoton sequence
process.load("RecoEgamma.PhotonIdentification.photonId_cff")
process.load("RecoLocalCalo.EcalRecAlgos.EcalSeverityLevelESProducer_cfi")

import RecoEgamma.EgammaPhotonProducers.photonCore_cfi
import RecoEgamma.EgammaPhotonProducers.photons_cfi

process.myphotonCores=RecoEgamma.EgammaPhotonProducers.photonCore_cfi.photonCore.clone()
process.myphotonCores.scHybridBarrelProducer=cms.InputTag ("uncleanSCRecovered:uncleanHybridSuperClusters")

from RecoEgamma.PhotonIdentification.mipVariable_cfi import *
newMipVariable = mipVariable.clone()
newMipVariable.barrelEcalRecHitCollection = cms.InputTag('reducedEcalRecHitsEB')
newMipVariable.endcapEcalRecHitCollection = cms.InputTag('reducedEcalRecHitsEE')

from RecoEgamma.PhotonIdentification.isolationCalculator_cfi import*
newisolationSumsCalculator = isolationSumsCalculator.clone()
newisolationSumsCalculator.barrelEcalRecHitCollection = cms.InputTag('reducedEcalRecHitsEB')
newisolationSumsCalculator.endcapEcalRecHitCollection = cms.InputTag('reducedEcalRecHitsEE')

process.myphotons=RecoEgamma.EgammaPhotonProducers.photons_cfi.photons.clone()
process.myphotons.barrelEcalHits=cms.InputTag("reducedEcalRecHitsEB")
process.myphotons.endcapEcalHits=cms.InputTag("reducedEcalRecHitsEE")
process.myphotons.isolationSumsCalculatorSet=newisolationSumsCalculator
process.myphotons.mipVariableSet = newMipVariable
process.myphotons.photonCoreProducer=cms.InputTag("myphotonCores")

process.myPhotonSequence = cms.Sequence(process.myphotonCores+
                                        process.myphotons)
# photonID sequence
from RecoEgamma.PhotonIdentification.photonId_cfi import *
process.myPhotonIDSequence = cms.Sequence(PhotonIDProd)
process.PhotonIDProd.photonProducer=cms.string("myphotons")

process.uncleanPhotons = cms.Sequence(
               process.uncleanSCRecovered *
               process.myPhotonSequence *
               process.myPhotonIDSequence
               )

# typeI MET correction 
process.load("JetMETCorrections.Type1MET.pfMETCorrections_cff")

# pat process
# conditions
process.load( "Configuration.Geometry.GeometryIdeal_cff" )
process.load( "Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff" )

# load the PAT config
process.load("PhysicsTools.PatAlgos.patSequences_cff")

#process.patElectrons.addGenMatch  = False
#process.patJets.addGenPartonMatch = False
#process.patJets.addGenJetMatch    = False
#process.patMETs.addGenMET         = False
#process.patMuons.addGenMatch      = False
#process.patPhotons.addGenMatch    = False
#process.patTaus.addGenMatch       = False
#process.patTaus.addGenJetMatch    = False
#process.patJetCorrFactors.levels.append( 'L2L3Residual' )
# this function will modify the PAT sequences.
#removeMCMatchingPF2PAT( process, '' )

process.out = cms.OutputModule("PoolOutputModule"
                , fileName = cms.untracked.string( 'patTuple_data.root' )
                , outputCommands = cms.untracked.vstring(
                        'keep *'
                        #               'keep *_cscSegments_*_*'
                        )
                 )

# this function will modify the PAT sequences.
from PhysicsTools.PatAlgos.tools.pfTools import *

postfix = "PFlow"

usePF2PAT( process
                , runPF2PAT = True
                , jetAlgo   = 'AK5'
                , runOnMC   = True
                , postfix   = postfix
                , jetCorrections=('AK5PFchs', ['L1FastJet','L2Relative','L3Absolute'])
                #, jetCorrections=('AK5PFchs', ['L2L3Residual'])
         )


process.p = cms.Path(
                     process.uncleanPhotons *
        #             process.patPF2PATSequence*
                     getattr(process,"patPF2PATSequence"+postfix) *
                     process.producePFMETCorrections *
                     process.ana
                    )

# top projections in PF2PAT:
getattr(process,"pfNoPileUp"+postfix).enable = True
getattr(process,"pfNoMuon"+postfix).enable = True
getattr(process,"pfNoElectron"+postfix).enable = True
getattr(process,"pfNoTau"+postfix).enable = False
getattr(process,"pfNoJet"+postfix).enable = True
# verbose flags for the PF2PAT modules
getattr(process,"pfNoMuon"+postfix).verbose = False

# enable delta beta correction for muon selection in PF2PAT?
getattr(process,"pfIsolatedMuons"+postfix).doDeltaBetaCorrection = False

process.out.outputCommands.extend( [ 'drop *_*_*_*' ] )


