import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016B_ver1/MET/NANOAOD/Nano14Dec2018_ver1-v1/10000/9D962128-DCA6-1145-A58B-A68A7890E7B0.root',
       '/store/data/Run2016B_ver1/MET/NANOAOD/Nano14Dec2018_ver1-v1/10000/F0859469-A366-4C4B-BCC7-6F936F39B486.root',
] )
