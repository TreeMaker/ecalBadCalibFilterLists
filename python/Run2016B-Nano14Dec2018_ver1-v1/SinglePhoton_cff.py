import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016B_ver1/SinglePhoton/NANOAOD/Nano14Dec2018_ver1-v1/280000/13AA003F-E302-8B42-8171-B0DB2DB60D28.root',
       '/store/data/Run2016B_ver1/SinglePhoton/NANOAOD/Nano14Dec2018_ver1-v1/280000/40521ACE-C062-9547-A2BE-03631A79D7FA.root',
       '/store/data/Run2016B_ver1/SinglePhoton/NANOAOD/Nano14Dec2018_ver1-v1/280000/6C3C64DB-2551-044F-8187-8AECEFE780FE.root',
       '/store/data/Run2016B_ver1/SinglePhoton/NANOAOD/Nano14Dec2018_ver1-v1/280000/B7177B9E-0F8E-D749-871D-FBE1E5D0719D.root',
       '/store/data/Run2016B_ver1/SinglePhoton/NANOAOD/Nano14Dec2018_ver1-v1/280000/BD2A2884-7E89-E545-9163-029C25A25C25.root',
       '/store/data/Run2016B_ver1/SinglePhoton/NANOAOD/Nano14Dec2018_ver1-v1/280000/EA03FD1A-882D-444A-AECD-FCBB3A638015.root',
       '/store/data/Run2016B_ver1/SinglePhoton/NANOAOD/Nano14Dec2018_ver1-v1/280000/EEC55443-0D1F-5B43-A42A-A69C170CD32E.root',
] )
