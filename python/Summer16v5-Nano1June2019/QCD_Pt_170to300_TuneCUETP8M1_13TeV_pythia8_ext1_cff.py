import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/60000/088DB0E1-A7CE-2B47-B1CF-CE3BF4544BBC.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/60000/33F44053-B4B8-A04E-B70C-1E3BFD0BF11D.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/60000/3951FB83-21FE-D24B-B5E3-486338D121FC.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/60000/765CC0B8-EAC7-794B-A33E-3E4C4E800FF6.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/60000/8403EA82-0C00-BA49-90D3-19DF6CED62CA.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/60000/A97E75AE-68F8-2A4B-94F3-8817C4100B4D.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/60000/EFC6BC74-52DA-C942-A890-7234562F8EEB.root',
] )
