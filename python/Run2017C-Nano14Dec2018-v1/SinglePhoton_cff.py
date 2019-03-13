import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2017C/SinglePhoton/NANOAOD/Nano14Dec2018-v1/80000/001E956D-BF4C-E04D-882C-747980C38CD8.root',
       '/store/data/Run2017C/SinglePhoton/NANOAOD/Nano14Dec2018-v1/80000/090A25DD-CA87-EE4A-98ED-18B2FFCAC115.root',
       '/store/data/Run2017C/SinglePhoton/NANOAOD/Nano14Dec2018-v1/80000/0B4EAABB-D9F5-BA4E-96FD-7DAAEFE47372.root',
       '/store/data/Run2017C/SinglePhoton/NANOAOD/Nano14Dec2018-v1/80000/131F3D37-AC3E-7847-BD4F-A96E08A5FB0D.root',
       '/store/data/Run2017C/SinglePhoton/NANOAOD/Nano14Dec2018-v1/80000/16B3898D-E134-394B-816E-4E172BCE46EB.root',
       '/store/data/Run2017C/SinglePhoton/NANOAOD/Nano14Dec2018-v1/80000/1EDB0E86-192A-9E42-B648-9DBB3E547646.root',
       '/store/data/Run2017C/SinglePhoton/NANOAOD/Nano14Dec2018-v1/80000/2FFA1C90-D04B-7F4C-AE42-F545DBC8E900.root',
       '/store/data/Run2017C/SinglePhoton/NANOAOD/Nano14Dec2018-v1/80000/3C4137F4-90D5-7D41-8E45-4FFE4AECC93B.root',
       '/store/data/Run2017C/SinglePhoton/NANOAOD/Nano14Dec2018-v1/80000/631F0EDB-E371-AC4C-932B-94C4A1E0BE4C.root',
       '/store/data/Run2017C/SinglePhoton/NANOAOD/Nano14Dec2018-v1/80000/785C0025-1749-724F-8553-9252A2B0BC8E.root',
       '/store/data/Run2017C/SinglePhoton/NANOAOD/Nano14Dec2018-v1/80000/8B50C461-91F3-A143-9969-041B4ABD3379.root',
       '/store/data/Run2017C/SinglePhoton/NANOAOD/Nano14Dec2018-v1/80000/986F3C2D-2E37-E24E-8A69-8720211EF9F5.root',
       '/store/data/Run2017C/SinglePhoton/NANOAOD/Nano14Dec2018-v1/80000/9C5DC945-9067-C149-B03A-A5843D973B32.root',
       '/store/data/Run2017C/SinglePhoton/NANOAOD/Nano14Dec2018-v1/80000/D21EF7A5-DB49-5647-94CE-A235DB69C16C.root',
       '/store/data/Run2017C/SinglePhoton/NANOAOD/Nano14Dec2018-v1/80000/D5F054F8-1F02-E54D-B4D0-5BB87F1CFEA4.root',
       '/store/data/Run2017C/SinglePhoton/NANOAOD/Nano14Dec2018-v1/80000/DC5D00AE-0629-374B-B0E1-0E96320087E7.root',
       '/store/data/Run2017C/SinglePhoton/NANOAOD/Nano14Dec2018-v1/80000/EB14A1F4-30C5-0243-A2A7-0D0CA0613B7C.root',
       '/store/data/Run2017C/SinglePhoton/NANOAOD/Nano14Dec2018-v1/80000/EB373B9E-C7FD-3A45-835B-187DF31D1582.root',
       '/store/data/Run2017C/SinglePhoton/NANOAOD/Nano14Dec2018-v1/80000/F70F8449-E2F4-E144-903D-3EE8B7565A55.root',
       '/store/data/Run2017C/SinglePhoton/NANOAOD/Nano14Dec2018-v1/80000/FA9AD383-8BF1-FE46-95AA-414BC27FAE74.root',
] )
