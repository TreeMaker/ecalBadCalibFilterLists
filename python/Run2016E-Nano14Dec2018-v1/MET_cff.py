import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016E/MET/NANOAOD/Nano14Dec2018-v1/80000/22B28A73-BB26-3C4B-92BC-1DA5A879295B.root',
       '/store/data/Run2016E/MET/NANOAOD/Nano14Dec2018-v1/80000/2743ED75-AA75-714A-837F-D41053DCEABC.root',
       '/store/data/Run2016E/MET/NANOAOD/Nano14Dec2018-v1/80000/3D7E1A9A-3CF4-474E-AE5E-77A2C87ECFAF.root',
       '/store/data/Run2016E/MET/NANOAOD/Nano14Dec2018-v1/80000/8388DD35-3694-684F-A696-E2D08E724F4D.root',
       '/store/data/Run2016E/MET/NANOAOD/Nano14Dec2018-v1/80000/8FF12347-222D-A748-96FE-B926EC13A160.root',
       '/store/data/Run2016E/MET/NANOAOD/Nano14Dec2018-v1/80000/97A4E410-E551-1C46-B61B-B277AD9D5656.root',
       '/store/data/Run2016E/MET/NANOAOD/Nano14Dec2018-v1/80000/9BBD7069-7224-FF4D-B640-EE365A9770DB.root',
       '/store/data/Run2016E/MET/NANOAOD/Nano14Dec2018-v1/80000/9CC8CD87-B4FF-F04A-99B6-2320390092E9.root',
       '/store/data/Run2016E/MET/NANOAOD/Nano14Dec2018-v1/80000/A9243BBA-097D-B040-BDE4-10E0FE6C6175.root',
       '/store/data/Run2016E/MET/NANOAOD/Nano14Dec2018-v1/80000/B100D876-4572-D54A-BE8E-EB925EC65814.root',
       '/store/data/Run2016E/MET/NANOAOD/Nano14Dec2018-v1/80000/E84EB7C2-0333-B141-B297-36D4E57431E3.root',
       '/store/data/Run2016E/MET/NANOAOD/Nano14Dec2018-v1/80000/E9B9EC94-3AEF-2649-99EB-643A0DF779F1.root',
       '/store/data/Run2016E/MET/NANOAOD/Nano14Dec2018-v1/80000/EB2AF06A-70EE-FC4C-AB28-E6EC34A647F3.root',
] )
