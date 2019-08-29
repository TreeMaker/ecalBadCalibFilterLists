import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_600to800_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/120000/050AF700-B7BE-E747-89AF-B538CB4D5B1A.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_600to800_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/120000/16B581F4-531F-A944-AF52-C945D8B00E0D.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_600to800_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/120000/220DD391-5440-B14B-AAE9-39BC50DD857E.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_600to800_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/120000/43DD353F-C198-7C48-8688-0F6345D6BB0E.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_600to800_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/120000/4B8ECD00-0227-6F4E-B5A9-6BBC34BF858C.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_600to800_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/120000/7EAE33B8-8724-974F-8D1E-5293141B3A4B.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_600to800_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/120000/8E45BEA9-2A94-D245-AAFF-9323CA79F71F.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_600to800_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/120000/B98F8AB9-E38B-1646-85B7-C5608917CEB1.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_600to800_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/120000/BC30AFAE-8884-6E4E-A547-C51F1A2C7497.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_600to800_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/120000/FB178722-0E5C-D548-8D77-4E8A65D3B385.root',
] )
