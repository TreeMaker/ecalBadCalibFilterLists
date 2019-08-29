import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext2-v1/40000/154F81AD-846C-2643-BA4E-5775E913F551.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext2-v1/40000/18C5C4AA-7E51-A24C-B55A-DCEC456D584B.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext2-v1/40000/328A15AA-1914-FF47-B60E-E6CC49765514.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext2-v1/40000/42737BF0-53BA-9140-B90C-1928E16F75EA.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext2-v1/40000/7BD0BD65-DA1E-DE43-B08D-8D7AD11A6CFD.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext2-v1/40000/AA76A107-18E0-8948-AEB7-2BFE78CA3FA1.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext2-v1/40000/AE21090F-80DB-9F49-AAD6-CC818E9C7E1B.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext2-v1/40000/C57E5E34-2834-7640-9761-07F72FD13724.root',
] )
