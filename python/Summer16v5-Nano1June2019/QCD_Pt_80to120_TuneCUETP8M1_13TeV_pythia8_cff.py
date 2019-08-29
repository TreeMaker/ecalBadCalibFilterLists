import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/250000/2C7CC538-B657-CD40-82E6-502C6015B94F.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/250000/3432EE21-3259-8946-9591-50522980C64A.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/250000/7CFD6010-9770-D646-A0F9-766957318AB8.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/250000/95DD540E-02C1-A24F-8D15-4437C2DC4A3C.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/250000/BE4D8848-FE3D-0447-9BA3-3FB28CA71242.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/250000/C5375E2D-3AB7-014A-9B9B-448BD0FCF069.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/250000/E80289B4-3463-7040-A1EF-274E574CE1B5.root',
] )
