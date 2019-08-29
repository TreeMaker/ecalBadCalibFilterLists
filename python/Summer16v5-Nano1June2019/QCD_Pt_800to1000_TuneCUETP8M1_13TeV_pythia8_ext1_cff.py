import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/110000/1FBF796C-B393-2443-B486-9D63A56899CE.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/110000/2632991E-72F8-DB47-8169-D20AC5486FFC.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/110000/26763B07-AE72-0C49-A974-BE9B7250730A.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/110000/29D87800-3032-C44E-9C22-B63D99367FDE.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/110000/41AFE75B-4F4E-2244-9A26-7F7CAF3A11D0.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/110000/47CB2159-DA8C-6449-ABE3-2C71BE9F83F5.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/110000/5FEDC9D8-BC5E-9441-911B-67C4AD9B8772.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/110000/6C571846-9029-304E-A8B1-D68F4FD9A3C1.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/110000/7777834C-9949-1548-BFD7-E2F52C2F99E9.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/110000/8533161D-7493-D64F-ABA8-BCC96AC86736.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/110000/90C39448-3132-6142-A496-31E6B821CDFC.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/110000/9BA852E3-D091-BE41-A01F-8D6BB1BC2C43.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/110000/A6D70DF7-9682-7341-AB10-A08737FA3E2A.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/110000/ABF997B3-FA19-7946-8A87-97E003045F6E.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/110000/AD4CB7C4-0E31-AC4B-A58B-E2CAFA8E44B0.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/110000/C02E09A2-AA6D-704D-983F-1577A23D03E4.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/110000/ECAAFA15-E3A3-334E-A4ED-01C3F2187980.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/110000/F57990EB-9803-4B4C-97BC-2641A6686B1C.root',
] )
