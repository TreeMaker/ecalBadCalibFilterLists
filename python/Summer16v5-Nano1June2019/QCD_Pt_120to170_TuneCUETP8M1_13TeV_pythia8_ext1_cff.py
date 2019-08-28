import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/250000/1A2DA969-0A41-394E-B31A-A024FC938FDE.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/250000/2B6B25FC-CBD6-DF4B-A9B7-10EB1D639401.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/250000/719C3647-6350-9B42-8C4E-A6ACCCB1DE99.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/250000/7AAEA559-4319-DF47-AA7D-D47AE37D6AFF.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/250000/CF0AC599-5EAE-8E48-B022-DC86214DF276.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/250000/E56F181F-E522-DD41-8222-DEEC77C02A5B.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/250000/EEF5DB4E-71A5-DF45-B9B7-9FA7EEC559BD.root',
] )
