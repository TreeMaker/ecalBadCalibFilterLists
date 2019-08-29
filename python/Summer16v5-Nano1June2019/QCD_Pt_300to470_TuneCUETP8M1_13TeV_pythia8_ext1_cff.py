import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/1110000/14201A63-4610-7044-939E-B582789F6322.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/250000/10B665B6-A0F9-9F48-B716-A1FE6E893028.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/250000/1750706F-E453-DB4C-8B9B-C31BCCEEB242.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/250000/19C01A1D-A4AA-5A4D-A8BB-80E49023833D.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/250000/3006702D-E3EA-B441-8165-A39445F96AEA.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/250000/379076F1-231C-844B-8C05-6DB656D0DEAA.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/250000/4F011140-4F5C-2B4F-9507-7CAAA79235DA.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/250000/59519117-6C73-A54D-AD3F-811AA330D46E.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/250000/5AC9DC31-2DB4-B344-9B72-63AFA8034752.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/250000/6101C33B-B995-C14D-925D-3B382BCF996A.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/250000/75AE85EF-F6BE-EC45-9246-BF978330B11E.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/250000/892E16C9-37F3-9249-A09C-A04972DB918E.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/250000/B9EA934E-AFB9-804C-A08E-EAB3A0B17A9A.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/250000/C31C1A00-E3D6-E144-A91F-718F12E1FCD6.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/250000/EB5CC36A-9FA3-A04D-AED9-D16970F59230.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/250000/F3EBDCF0-7BE8-4D43-86CD-DBB0646FD6EB.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/250000/FD1EB254-C618-C646-8258-EFC56279BD01.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/30000/055E6DAB-330E-8448-8AFA-CBD71B2404D5.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/30000/2AAE2C05-1081-9A42-A398-06DBBDBCB0A7.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/30000/5BD39CFD-8F2A-A840-BA4B-76A08A05AB69.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/30000/96718BD3-1169-B749-BE2B-B5A5288C827A.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/30000/A148B7BF-D43F-8B4B-9BF1-DF2F9F8E2069.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/30000/A9B058FE-D0F1-8242-B419-9F9F7014E25A.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/30000/AFBD368D-10FC-264C-9636-336B5B04B9E4.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/30000/B70CEE70-2C9C-B843-BE66-F105DD91B5DE.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/30000/D1C40FF8-12CF-B844-A218-371A9B2FB047.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/30000/D3AE7E2D-818E-FF44-A468-767440EF7892.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/30000/D3BF5C80-B598-0340-9F71-E4A0DD1962EA.root',
] )
