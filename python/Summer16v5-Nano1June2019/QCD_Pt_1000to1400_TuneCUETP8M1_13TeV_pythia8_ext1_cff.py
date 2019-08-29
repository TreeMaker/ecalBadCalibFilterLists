import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/70000/47923BEC-E711-334E-B82B-8BDEE26E5279.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/70000/5FD52FB3-2EAA-8144-B3B6-C8463504DEB8.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/70000/859FE89C-6835-994A-A3A9-556C61D01CC5.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/70000/8929253A-186D-FB49-8B99-1F4D5D04EE67.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/70000/9C031F5D-C5D2-C14A-8783-FA8AA9B89B38.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/70000/BE548774-47E2-2A42-8D5D-462FC0AC0292.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/70000/EE8CE715-EDC1-D446-AB55-C11043EDBF18.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/70000/F306838E-A762-3043-8A22-CAE69D68D71D.root',
] )
