import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016B_ver1/JetHT/NANOAOD/Nano14Dec2018_ver1-v1/20000/03BB4CEC-86D7-1F4C-B7BA-754F84C62AA4.root',
       '/store/data/Run2016B_ver1/JetHT/NANOAOD/Nano14Dec2018_ver1-v1/20000/19C6B7B9-286E-D046-AF20-5A8F85E83DB3.root',
       '/store/data/Run2016B_ver1/JetHT/NANOAOD/Nano14Dec2018_ver1-v1/20000/506746C1-C061-6F45-93A5-8E8A860224E3.root',
       '/store/data/Run2016B_ver1/JetHT/NANOAOD/Nano14Dec2018_ver1-v1/20000/60C5872D-2AFC-6A45-9C5A-ABE1B2E31E52.root',
       '/store/data/Run2016B_ver1/JetHT/NANOAOD/Nano14Dec2018_ver1-v1/20000/885EA852-A4D4-0841-9F59-CFE0B2D4741A.root',
       '/store/data/Run2016B_ver1/JetHT/NANOAOD/Nano14Dec2018_ver1-v1/20000/9FAD26A1-AA3C-E84D-984B-673829026DDB.root',
       '/store/data/Run2016B_ver1/JetHT/NANOAOD/Nano14Dec2018_ver1-v1/20000/F1EBB247-CA21-E14A-BCD4-7C2B62E88282.root',
] )
