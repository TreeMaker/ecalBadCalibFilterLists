import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2017E/HTMHT/NANOAOD/Nano14Dec2018-v1/80000/170D9E95-1C90-BB40-BD68-6B9AA6A4A1ED.root',
       '/store/data/Run2017E/HTMHT/NANOAOD/Nano14Dec2018-v1/80000/1DA0A2A3-4366-3C4B-B49F-E63715384DBA.root',
       '/store/data/Run2017E/HTMHT/NANOAOD/Nano14Dec2018-v1/80000/7409AD13-F2F7-C141-B49B-8CD20C73235E.root',
       '/store/data/Run2017E/HTMHT/NANOAOD/Nano14Dec2018-v1/80000/82097E8D-37BE-9045-937C-9A60D0E15761.root',
       '/store/data/Run2017E/HTMHT/NANOAOD/Nano14Dec2018-v1/80000/90E8E431-6EA8-304A-B735-EA1174339548.root',
       '/store/data/Run2017E/HTMHT/NANOAOD/Nano14Dec2018-v1/80000/AE7DB65D-F461-074F-B664-C14BAF8F6FB1.root',
       '/store/data/Run2017E/HTMHT/NANOAOD/Nano14Dec2018-v1/80000/BA0C37C5-322D-3141-A176-7E2A8A9E53B9.root',
       '/store/data/Run2017E/HTMHT/NANOAOD/Nano14Dec2018-v1/80000/D1C5FE52-C9B2-A843-86EF-B51044944B7C.root',
] )
