import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016B_ver1/SingleMuon/NANOAOD/Nano14Dec2018_ver1-v1/90000/4074F613-50E6-5545-8347-CCF58D02E64C.root',
       '/store/data/Run2016B_ver1/SingleMuon/NANOAOD/Nano14Dec2018_ver1-v1/90000/87B8F064-C966-FD4F-BD32-E1FCB470AC7B.root',
       '/store/data/Run2016B_ver1/SingleMuon/NANOAOD/Nano14Dec2018_ver1-v1/90000/BD130B6E-3ACD-0743-9F08-D0D6BDCD372D.root',
] )
