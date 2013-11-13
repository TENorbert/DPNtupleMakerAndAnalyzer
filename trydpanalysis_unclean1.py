import FWCore.ParameterSet.Config as cms

process = cms.Process("test")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(50000) )

process.source = cms.Source("PoolSource",

    fileNames = cms.untracked.vstring(
#'file:/mnt/hadoop/store/user/sckao/SinglePhoton/EXO_DisplacedPhoton2ndSKIM/176d86b18a84f276e44dc86f253a35ed/skim_c_247_1_KQl.root'
#'file:/mnt/hadoop/store/data/Run2012D/SinglePhoton/RECO/EXODisplacedPhoton-19Dec2012-v1/10000/A02BEF7A-A365-E211-B2EF-001E67397B25.root'

#'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/PhotonHad/RECO/PromptReco-v1/000/208/329/BA806D5E-E23C-E211-B8FF-003048F0258C.root',
#'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/PhotonHad/RECO/PromptReco-v1/000/208/777/905A2B89-6044-E211-842A-002481E0CC00.root',
#'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/PhotonHad/RECO/PromptReco-v1/000/208/783/AC432020-6644-E211-ABA1-003048CFB40C.root'
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SinglePhoton/RECO/22Jan2013-v1/20000/4E08AD76-6A6E-E211-B0FD-002590596486.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SinglePhoton/RECO/22Jan2013-v1/20000/505C4A0A-7F6E-E211-A97E-00261894396F.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SinglePhoton/RECO/22Jan2013-v1/20000/A681265D-7A6E-E211-8C36-00261894383C.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SinglePhoton/RECO/22Jan2013-v1/20000/36E965F8-7A6E-E211-9746-002618943904.root',
'dcache://pnfs/cms/WAX/11/store/data/Run2012C/SinglePhoton/RECO/22Jan2013-v1/20000/9EF09C37-776E-E211-9AA9-003048678C06.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SinglePhoton/RECO/22Jan2013-v1/20000/F68A2210-4A6E-E211-A92D-002590596484.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SinglePhoton/RECO/22Jan2013-v1/20000/F8AA2E32-776E-E211-A331-002618943924.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SinglePhoton/RECO/22Jan2013-v1/20000/FA8EF33F-7D6E-E211-9FEC-003048FFCB6A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SinglePhoton/RECO/22Jan2013-v1/20000/9E746661-4B6E-E211-AD57-0026189438D6.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SinglePhoton/RECO/22Jan2013-v1/20000/F6E302EF-6D6E-E211-9ADB-0026189437E8.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SinglePhoton/RECO/22Jan2013-v1/20000F461BBD6-6A6E-E211-BC5D-003048678B72.root/',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SinglePhoton/RECO/22Jan2013-v1/20000/9E31CFB8-7D6E-E211-85A9-0026189438AD.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SinglePhoton/RECO/22Jan2013-v1/20000/4610CECE-786E-E211-B822-003048FFD770.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SinglePhoton/RECO/22Jan2013-v1/20000/44915AB7-7F6E-E211-AE9F-002618943831.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SinglePhoton/RECO/22Jan2013-v1/20000/9A2894CB-496E-E211-9755-003048FFCB6A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SinglePhoton/RECO/22Jan2013-v1/20000/3EB75AFB-7A6E-E211-9032-003048679010.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SinglePhoton/RECO/22Jan2013-v1/20000/3ECB8663-4B6E-E211-BE20-003048FFD75C.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SinglePhoton/RECO/22Jan2013-v1/20000/DCB19AAB-6F6E-E211-A3A1-003048678FA0.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SinglePhoton/RECO/22Jan2013-v1/20000/EAC583A9-846E-E211-A422-003048678BE8.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SinglePhoton/RECO/22Jan2013-v1/20000/EA98ABBB-7C6E-E211-B737-003048FFD732.root'
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SinglePhoton/RECO/22Jan2013-v1/20000/4092854D-7B6E-E211-A943-002618943901.root', 
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SinglePhoton/RECO/22Jan2013-v1/20000/9A74F70D-806E-E211-BB7F-003048678B36.root',  
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SinglePhoton/RECO/22Jan2013-v1/20000/EEAD35E8-756E-E211-B3C2-00304867C1BA.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SinglePhoton/RECO/22Jan2013-v1/20000/40AA95E7-6D6E-E211-B2F6-0026189438A7.root',  
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SinglePhoton/RECO/22Jan2013-v1/20000/9A837C9A-5F6E-E211-ABB3-002618943980.root',  
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SinglePhoton/RECO/22Jan2013-v1/20000/EEB3FDA1-846E-E211-BE48-00261894396E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SinglePhoton/RECO/22Jan2013-v1/20000/40C1A7D0-6A6E-E211-AFEB-003048678A78.root',  
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SinglePhoton/RECO/22Jan2013-v1/20000/9AE11D9D-856E-E211-80FE-00304867C1BA.root',  
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SinglePhoton/RECO/22Jan2013-v1/20000/F006F4DB-816E-E211-887F-002618943858.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SinglePhoton/RECO/22Jan2013-v1/20000/40D3E6C5-6A6E-E211-83AF-003048679296.root',  
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SinglePhoton/RECO/22Jan2013-v1/20000/9AFA2988-846E-E211-B481-003048678C26.root',  
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SinglePhoton/RECO/22Jan2013-v1/20000/F0177E2A-7F6E-E211-86D1-003048678AE4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SinglePhoton/RECO/22Jan2013-v1/20000/40E17631-7F6E-E211-BD2B-0025905964B6.root',  
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SinglePhoton/RECO/22Jan2013-v1/20000/9C04EDAD-496E-E211-8669-0026189438DB.root',  
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SinglePhoton/RECO/22Jan2013-v1/20000/F01A0215-5E6E-E211-94BB-003048678B14.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SinglePhoton/RECO/22Jan2013-v1/20000/40E2DA47-4A6E-E211-B2D1-00261894395B.root',  
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SinglePhoton/RECO/22Jan2013-v1/20000/9C07E2AE-826E-E211-B512-002618FDA28E.root',  
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SinglePhoton/RECO/22Jan2013-v1/20000/F020C290-766E-E211-BDB7-00304867908C.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SinglePhoton/RECO/22Jan2013-v1/20000/4222872D-856E-E211-9967-003048FFD7A2.root',  
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SinglePhoton/RECO/22Jan2013-v1/20000/9C1C6A23-806E-E211-AC74-002618943973.root',  
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SinglePhoton/RECO/22Jan2013-v1/20000/F06CCD45-796E-E211-90A2-003048FFCBB0.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SinglePhoton/RECO/22Jan2013-v1/20000/423E2C42-736E-E211-A365-003048678DA2.root',  
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SinglePhoton/RECO/22Jan2013-v1/20000/9C5A8427-796E-E211-B655-002618943979.root',  
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SinglePhoton/RECO/22Jan2013-v1/20000/F06E208D-826E-E211-8D21-002618943954.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SinglePhoton/RECO/22Jan2013-v1/20000/42693B04-6D6E-E211-AAC5-002618943807.root',  
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SinglePhoton/RECO/22Jan2013-v1/20000/9C5F2774-6B6E-E211-845E-003048678B3C.root',  
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SinglePhoton/RECO/22Jan2013-v1/20000/F0BE6351-7B6E-E211-B0DE-0026189438AF.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SinglePhoton/RECO/22Jan2013-v1/20000/4298FE10-7D6E-E211-8ACC-00261894389E.root',  
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SinglePhoton/RECO/22Jan2013-v1/20000/9C717383-496E-E211-A89A-0026189438B3.root',  
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SinglePhoton/RECO/22Jan2013-v1/20000/F0DC7C21-6F6E-E211-B3AF-00261894386A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SinglePhoton/RECO/22Jan2013-v1/20000/42CF51BA-496E-E211-9304-00248C55CC3C.root',  
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SinglePhoton/RECO/22Jan2013-v1/20000/9C890DD5-776E-E211-966D-003048678FD6.root',  
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SinglePhoton/RECO/22Jan2013-v1/20000/F2419238-776E-E211-9C56-002618943886.root'


#'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SinglePhoton/AOD/22Jan2013-v1/20000/52FB3684-C26E-E211-9655-002618943916.root',
#'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SinglePhoton/AOD/22Jan2013-v1/20000/A8A6D4EB-A76E-E211-A4FF-003048678AC0.root',
#'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SinglePhoton/AOD/22Jan2013-v1/20000/FCAFCA3E-896E-E211-9465-003048FFD728.root'
# 'file:input_dataSet.root'
#'file:/local/cms/phedex/store/data/Run2012C/SinglePhoton/RECO/EXODisplacedPhoton-PromptSkim-v3/000/200/190/00000/18BB0794-8CDF-E111-B9B0-0025B31E3D3C.root'
    ),

    # explicitly drop photons resident in AOD/RECO, to make sure only those locally re-made (uncleaned photons) are used
    inputCommands = cms.untracked.vstring('keep *'
                                          #,'drop  *_photonCore_*_RECO' # drop hfRecoEcalCandidate as remade in this process
                                          #, 'drop *_photons_*_RECO' # drop photons as remade in this process
                                          )

)


#import EXO.DPAnalysis.skim2012c as fileList
#process.source.fileNames = fileList.fileNames

process.options   = cms.untracked.PSet(
                    wantSummary = cms.untracked.bool(True),  
                    SkipEvent = cms.untracked.vstring('ProductNotFound')
)   

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = cms.untracked.int32(1000)

process.ana = cms.EDAnalyzer('DPAnalysis',
    rootFileName     = cms.untracked.string('run2012C.root'),
    triggerName      = cms.vstring('HLT_Photon50_CaloIdVL_IsoL','HLT_DisplacedPhoton65_CaloIdVL_IsoL_PFMET25'),
    L1GTSource       = cms.string('L1_SingleEG22'),
    L1Select         = cms.bool( False ),
    isData           = cms.bool( True ),
    cscHaloData      = cms.InputTag("CSCHaloData"),
    staMuons         = cms.InputTag("standAloneMuons"),
    CSCSegmentCollection = cms.InputTag("cscSegments"),
    #DTSegmentCollection = cms.InputTag("dtSegments"),
    DTSegmentCollection = cms.InputTag("dt4DCosmicSegments"),
    muonSource  = cms.InputTag("muonsFromCosmics"),
    trigSource = cms.InputTag("TriggerResults","","HLT"),
    jetSource   = cms.InputTag("ak5PFJets"),
    patJetSource = cms.InputTag("selectedPatJetsPFlow"),
    metSource   = cms.InputTag("pfMet"),
    type1metSource   = cms.InputTag("pfType1CorrectedMet"),
    trackSource = cms.InputTag("generalTracks"),
    electronSource   = cms.InputTag("gsfElectrons"),
    photonSource     = cms.InputTag("myphotons"),
    pvSource         = cms.InputTag("offlinePrimaryVerticesWithBS"),
    beamSpotSource   = cms.InputTag("offlineBeamSpot"),
    EBRecHitCollection = cms.InputTag("reducedEcalRecHitsEB"),
    EERecHitCollection = cms.InputTag("reducedEcalRecHitsEE"),
    
    BarrelSuperClusterCollection = cms.InputTag("correctedHybridSuperClusters",""),
    EndcapSuperClusterCollection = cms.InputTag("correctedMulti5x5SuperClustersWithPreshower",""),
    
    tau                = cms.double( 1000 ), 
    genParticles = cms.InputTag("genParticles"),

    # Set up cuts for physics objects
    # vertex cuts                z   ndof   d0 
    vtxCuts       = cms.vdouble( 99,    0,  99 ),
    # photon cuts                pt   eta  sMajMax,  sMinMin, sMinMax,   dR,  Num  leadingPt  
    photonCuts    = cms.vdouble( 45,  3.5,     99.,      -1.,     99.,   0.0,  1,    45  ),
    # photon isolation           trkR,  ecalSumEt, ecalR, hcalSumEt, hcalR 
    photonIso     = cms.vdouble(  1.,       5.0,   1.,       5.0,   1. ),
    # jet cuts                   pt    eta    dR,  nJets
    jetCuts       = cms.vdouble( 30. , 2.5,  0.3,    0 ),
    metCuts       = cms.vdouble( 0. ),
    # electron cuts              pt  eta  EBIso  EEIso nLostHit  
    electronCuts  = cms.vdouble( 25, 2.5,  0.15,   0.1,      2 ),
    # muon cuts                  pt  eta  Iso  dR   
    muonCuts      = cms.vdouble( 25, 2.1, 0.2, 0.3 ),

)

###########  USE UNCLEANED SUPERCLUSTERS  ######################### 
# Global Tag
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
#process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_noesprefer_cff")
#process.GlobalTag.globaltag = 'GR_R_53_V18::All'
from Configuration.AlCa.GlobalTag import GlobalTag
#process.GlobalTag = GlobalTag( process.GlobalTag, 'GR_R_53_V10::All' )
process.GlobalTag = GlobalTag( process.GlobalTag, 'GR_R_53_V18::All' )


# to get clustering 
process.load("Configuration.Geometry.GeometryIdeal_cff")
#process.load("Configuration.StandardSequences.Geometry_cff")
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

# PFIso 
#from CommonTools.ParticleFlow.Tools.pfIsolation import setupPFElectronIso, setupPFPhotonIso
#process.phoIsoSequence = setupPFPhotonIso(process, 'photons')

# typeI MET correction 
process.load("JetMETCorrections.Type1MET.pfMETCorrections_cff")

# pat process

# conditions
process.load( "Configuration.Geometry.GeometryIdeal_cff" )
process.load( "Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff" )

# load the PAT config
process.load("PhysicsTools.PatAlgos.patSequences_cff")

process.patElectrons.addGenMatch  = False
process.patJets.addGenPartonMatch = False
process.patJets.addGenJetMatch    = False
process.patMETs.addGenMET         = False
process.patMuons.addGenMatch      = False
process.patPhotons.addGenMatch    = False
process.patTaus.addGenMatch       = False
process.patTaus.addGenJetMatch    = False
process.patJetCorrFactors.levels.append( 'L2L3Residual' )

process.out = cms.OutputModule("PoolOutputModule" ,
                fileName = cms.untracked.string( 'patTuple_data.root' ) ,
		outputCommands = cms.untracked.vstring(
			'keep *'
			#               'keep *_cscSegments_*_*'
			#               *patEventContentNoCleaning
			)
																                 )


# this function will modify the PAT sequences.
from PhysicsTools.PatAlgos.tools.pfTools import *

postfix = "PFlow"

usePF2PAT( process
		, runPF2PAT = True
		, jetAlgo   = 'AK5'
		, runOnMC   = False
		, postfix   = postfix
		# for MC
		#, jetCorrections=('AK5PFchs', ['L1FastJet','L2Relative','L3Absolute'])
		# for data
		, jetCorrections=('AK5PFchs', ['L2L3Residual'])
	 )



process.p = cms.Path(
                     process.uncleanPhotons*
		     getattr(process,"patPF2PATSequence"+postfix)*
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

