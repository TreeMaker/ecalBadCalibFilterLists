import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016G/MET/NANOAOD/Nano14Dec2018-v1/80000/259999CE-35DF-FC40-94F3-AF083D3D615B.root',
       '/store/data/Run2016G/MET/NANOAOD/Nano14Dec2018-v1/80000/2FFD045A-0E81-494D-A1C5-5D05A7D261F9.root',
       '/store/data/Run2016G/MET/NANOAOD/Nano14Dec2018-v1/80000/36B5871A-2642-C645-B678-000A44EEA080.root',
       '/store/data/Run2016G/MET/NANOAOD/Nano14Dec2018-v1/80000/3E28CDD2-923E-7B4B-8347-B2A3A77D9295.root',
       '/store/data/Run2016G/MET/NANOAOD/Nano14Dec2018-v1/80000/3EAE39E3-9984-3347-B36D-F780D8D9EE42.root',
       '/store/data/Run2016G/MET/NANOAOD/Nano14Dec2018-v1/80000/5CB2D2AB-E077-3F44-A856-56382B8D37FE.root',
       '/store/data/Run2016G/MET/NANOAOD/Nano14Dec2018-v1/80000/66DE259F-79E4-3E4A-B321-EAE3541F4E63.root',
       '/store/data/Run2016G/MET/NANOAOD/Nano14Dec2018-v1/80000/69885CC9-D601-5D4D-94BA-A89F4A523567.root',
       '/store/data/Run2016G/MET/NANOAOD/Nano14Dec2018-v1/80000/783BB280-F41E-9245-9789-0E2D4D917A4C.root',
       '/store/data/Run2016G/MET/NANOAOD/Nano14Dec2018-v1/80000/8461E89F-62D0-F343-83A2-46966D193DD2.root',
       '/store/data/Run2016G/MET/NANOAOD/Nano14Dec2018-v1/80000/A442A143-884E-0148-BB51-9BBCF5FD6BA5.root',
       '/store/data/Run2016G/MET/NANOAOD/Nano14Dec2018-v1/80000/AA1B8977-17ED-864B-8F4E-0777D0FAD48C.root',
       '/store/data/Run2016G/MET/NANOAOD/Nano14Dec2018-v1/80000/B5830E7A-9B91-3C40-A94B-2E277526DA74.root',
       '/store/data/Run2016G/MET/NANOAOD/Nano14Dec2018-v1/80000/DB06E5F5-DF77-DE4D-A57B-61AC72A034CE.root',
       '/store/data/Run2016G/MET/NANOAOD/Nano14Dec2018-v1/80000/E635B26B-BBF9-9346-A1D5-C68388711262.root',
] )
