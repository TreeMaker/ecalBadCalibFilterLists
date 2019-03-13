import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2017D/HTMHT/NANOAOD/Nano14Dec2018-v1/10000/0B5552E9-497B-614C-9BA4-496F55FA736E.root',
       '/store/data/Run2017D/HTMHT/NANOAOD/Nano14Dec2018-v1/10000/7294DB23-4963-E048-886D-C9FC51272F2F.root',
       '/store/data/Run2017D/HTMHT/NANOAOD/Nano14Dec2018-v1/10000/9F389A2A-98C9-114F-9497-2C5F8C5F0E55.root',
] )
