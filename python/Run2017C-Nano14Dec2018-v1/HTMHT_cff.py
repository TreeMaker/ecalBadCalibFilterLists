import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2017C/HTMHT/NANOAOD/Nano14Dec2018-v1/80000/1BA6BB8B-DD88-4344-8725-5BB7F8E94ABE.root',
       '/store/data/Run2017C/HTMHT/NANOAOD/Nano14Dec2018-v1/80000/29CE5E03-A67E-8040-9377-1070B0BB503C.root',
       '/store/data/Run2017C/HTMHT/NANOAOD/Nano14Dec2018-v1/80000/97DA481E-BB89-CA4A-AA94-90878473D991.root',
       '/store/data/Run2017C/HTMHT/NANOAOD/Nano14Dec2018-v1/80000/A62E19E6-841B-1E48-BB46-338F8DB37FE2.root',
       '/store/data/Run2017C/HTMHT/NANOAOD/Nano14Dec2018-v1/80000/A6A7DF24-1C78-FB4D-930D-4165EECC45A3.root',
       '/store/data/Run2017C/HTMHT/NANOAOD/Nano14Dec2018-v1/80000/D495C954-7645-BC40-B6D3-3E02CFDB459D.root',
       '/store/data/Run2017C/HTMHT/NANOAOD/Nano14Dec2018-v1/80000/FDE7F720-98DB-B944-887C-A6BE211E45DD.root',
] )
