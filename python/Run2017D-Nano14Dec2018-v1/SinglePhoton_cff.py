import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2017D/SinglePhoton/NANOAOD/Nano14Dec2018-v1/00000/368E03DF-5978-924C-9CC4-6F559231AEF1.root',
       '/store/data/Run2017D/SinglePhoton/NANOAOD/Nano14Dec2018-v1/00000/45A13E2B-50EE-CA44-856F-CBF9AC296549.root',
       '/store/data/Run2017D/SinglePhoton/NANOAOD/Nano14Dec2018-v1/00000/5275DB87-8A60-4441-AB05-562C5F4BB5CC.root',
       '/store/data/Run2017D/SinglePhoton/NANOAOD/Nano14Dec2018-v1/00000/5D63FD6C-104E-AE4D-B75A-26D62E0678FF.root',
       '/store/data/Run2017D/SinglePhoton/NANOAOD/Nano14Dec2018-v1/00000/9B00DDDE-D440-E847-90D6-0E273A634C73.root',
       '/store/data/Run2017D/SinglePhoton/NANOAOD/Nano14Dec2018-v1/00000/CA616413-4037-2343-ACD8-384F52F0DA5B.root',
       '/store/data/Run2017D/SinglePhoton/NANOAOD/Nano14Dec2018-v1/00000/CFB6B130-2019-1149-BACF-92AF7B56B788.root',
] )
