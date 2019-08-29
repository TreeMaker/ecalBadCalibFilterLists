import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/110000/0707AE01-5ADE-1F46-805B-7C9E06EC8BA1.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/110000/0BF8289C-3834-D24F-B67D-4E2362BA0997.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/110000/15AE647E-3B1C-F449-BFBF-CFB9280088B6.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/110000/3CFE8F4D-0069-B543-ADCD-689B3FB99A8B.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/110000/5357D119-0337-AA42-ACE0-5573B3A0542B.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/110000/6415CF73-E915-1A4A-B4C3-170892FD023A.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/110000/717CA315-5EC1-3C42-A173-6B285E403980.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/110000/B7CDD6C0-4005-1948-9746-374E28C6D92C.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/110000/E384D80F-8369-8940-8BD8-7304557352F8.root',
] )
