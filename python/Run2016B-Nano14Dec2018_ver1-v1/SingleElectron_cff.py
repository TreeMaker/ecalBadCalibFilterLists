import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016B_ver1/SingleElectron/NANOAOD/Nano14Dec2018_ver1-v1/00000/ECD4BD44-5DA0-5940-A5F1-120C84703015.root',
] )
