import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/100000/2E0A4EB5-61D1-EC42-B6BB-01EFB317F947.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/100000/5758BEDD-DA8F-2845-8364-6D860F4D974E.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/100000/693388DC-EB65-AC41-A823-97306197B3E3.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/100000/A2CF4372-9FD9-1B48-A966-3F810D45580F.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/100000/ECC5C0D6-2AA7-D144-A105-D7E232610378.root',
] )
