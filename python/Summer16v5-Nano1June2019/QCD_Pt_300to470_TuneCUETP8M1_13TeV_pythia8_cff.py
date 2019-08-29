import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/100000/809119D9-93F2-4742-AAAA-8DD354C2950A.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/100000/8BB4069F-B4D0-794D-8D39-367B913E5689.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/100000/A3758884-D862-3944-8923-1590FB44C2BB.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/100000/B298ED05-1E86-A04E-B184-144ACAE215B1.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/100000/C7632817-29CB-BB41-AD46-090D5EF11597.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/100000/F3253DEE-8013-3549-9A66-9079034A0EBC.root',
] )
