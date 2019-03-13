import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016B_ver1/HTMHT/NANOAOD/Nano14Dec2018_ver1-v1/80000/3B2AE446-3952-494A-92D7-3360724D958D.root',
       '/store/data/Run2016B_ver1/HTMHT/NANOAOD/Nano14Dec2018_ver1-v1/80000/4A9FF394-EFD6-6341-A84D-CD7B4CF86D78.root',
] )
