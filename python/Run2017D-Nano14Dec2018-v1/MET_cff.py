import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2017D/MET/NANOAOD/Nano14Dec2018-v1/10000/2536594C-ABC3-2A48-87DF-4FF2EDE55069.root',
       '/store/data/Run2017D/MET/NANOAOD/Nano14Dec2018-v1/10000/316C43AD-A1EF-B040-9CCE-04B3C5FF0C88.root',
       '/store/data/Run2017D/MET/NANOAOD/Nano14Dec2018-v1/10000/358501F1-CB0C-E04B-8830-C339A1638A11.root',
       '/store/data/Run2017D/MET/NANOAOD/Nano14Dec2018-v1/10000/40413AEC-F596-FF44-A270-E29201CE8546.root',
       '/store/data/Run2017D/MET/NANOAOD/Nano14Dec2018-v1/10000/4A1EFB1F-6C34-8D41-B930-EDA0F9B6B94B.root',
       '/store/data/Run2017D/MET/NANOAOD/Nano14Dec2018-v1/10000/60A7D2DB-3CB3-7741-AED1-E12690BB0B65.root',
       '/store/data/Run2017D/MET/NANOAOD/Nano14Dec2018-v1/10000/6909466D-ACEA-FA43-8621-CD1369E9030F.root',
       '/store/data/Run2017D/MET/NANOAOD/Nano14Dec2018-v1/10000/7A98CAAF-2F39-C84C-A764-704D37575E74.root',
       '/store/data/Run2017D/MET/NANOAOD/Nano14Dec2018-v1/10000/7B60BFD1-B7A7-244C-826B-C874C060CD29.root',
       '/store/data/Run2017D/MET/NANOAOD/Nano14Dec2018-v1/10000/8934B794-91BE-BE44-9FEF-84F66CCD2872.root',
       '/store/data/Run2017D/MET/NANOAOD/Nano14Dec2018-v1/10000/A40E2AA5-EA8E-0F4F-8A54-60462C2A8756.root',
       '/store/data/Run2017D/MET/NANOAOD/Nano14Dec2018-v1/10000/B8CB3D8A-F169-784E-856F-196120DF52E5.root',
       '/store/data/Run2017D/MET/NANOAOD/Nano14Dec2018-v1/10000/CDA7D9F0-7B55-864D-8D91-8B345555F94E.root',
       '/store/data/Run2017D/MET/NANOAOD/Nano14Dec2018-v1/10000/ECCE2C14-E3CE-454F-9753-F3A206D9641D.root',
] )
