import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/110000/334CB7CB-BD12-D843-8BA5-8D6599A3A134.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/110000/3948C82D-4595-1447-8528-A7D545DC77B3.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/110000/4F28915B-1BAF-A14A-AB9A-65F5F9B3502C.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/110000/BD7EA22F-407C-8F4C-A4EE-99DCDAF728DD.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/110000/CDADED9C-0D32-4941-BCDC-7AB3025ADD19.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/110000/D684ACA7-4E33-9047-AE3F-643295CA260B.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/110000/DC5617C1-DD46-4C44-8C8A-6E7088E8A544.root',
] )
