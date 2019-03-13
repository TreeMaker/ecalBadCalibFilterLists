import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016F/MET/NANOAOD/Nano14Dec2018-v1/80000/09A8BB26-F9CE-3C4C-A17C-71054B03DC52.root',
       '/store/data/Run2016F/MET/NANOAOD/Nano14Dec2018-v1/80000/3EB197FC-0C15-1647-8AD9-8E0AF43F13E1.root',
       '/store/data/Run2016F/MET/NANOAOD/Nano14Dec2018-v1/80000/43B27166-6671-004F-BFDE-86DA7BE618FE.root',
       '/store/data/Run2016F/MET/NANOAOD/Nano14Dec2018-v1/80000/49A3A902-8251-414D-894D-4D5BFB7BEF38.root',
       '/store/data/Run2016F/MET/NANOAOD/Nano14Dec2018-v1/80000/5382B1E4-CBCA-614B-B83A-3D362A9DA66A.root',
       '/store/data/Run2016F/MET/NANOAOD/Nano14Dec2018-v1/80000/65F77237-C606-704E-B923-96527E2BC3AD.root',
       '/store/data/Run2016F/MET/NANOAOD/Nano14Dec2018-v1/80000/68184DB3-98D0-AD45-A2C8-8E6C1C5698AF.root',
       '/store/data/Run2016F/MET/NANOAOD/Nano14Dec2018-v1/80000/7620D82E-A144-1349-A23B-DB9FEFB0F453.root',
       '/store/data/Run2016F/MET/NANOAOD/Nano14Dec2018-v1/80000/AF6DC1A8-165F-8E4C-B594-592AEB3619AF.root',
       '/store/data/Run2016F/MET/NANOAOD/Nano14Dec2018-v1/80000/F814A7A7-B4BB-254B-84E4-552962EA0EE3.root',
] )
