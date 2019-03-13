import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2017E/SinglePhoton/NANOAOD/Nano14Dec2018-v1/00000/09DF97DD-BB56-F742-89FD-3E44A2BA2887.root',
       '/store/data/Run2017E/SinglePhoton/NANOAOD/Nano14Dec2018-v1/00000/0F9AC9E0-028B-2946-94E3-AF8F7620B1CA.root',
       '/store/data/Run2017E/SinglePhoton/NANOAOD/Nano14Dec2018-v1/00000/10C9B6C6-75AD-DF41-82E6-86728FA5BA52.root',
       '/store/data/Run2017E/SinglePhoton/NANOAOD/Nano14Dec2018-v1/00000/128B6841-03AA-FC4C-92DC-6496B02EFE85.root',
       '/store/data/Run2017E/SinglePhoton/NANOAOD/Nano14Dec2018-v1/00000/5459A09C-CFF7-5941-81B7-66D471EB52FA.root',
       '/store/data/Run2017E/SinglePhoton/NANOAOD/Nano14Dec2018-v1/00000/5DB1FFDF-357D-8F45-9028-3772596413BF.root',
       '/store/data/Run2017E/SinglePhoton/NANOAOD/Nano14Dec2018-v1/00000/77AA49B0-B723-3E47-B840-46219E67B34C.root',
       '/store/data/Run2017E/SinglePhoton/NANOAOD/Nano14Dec2018-v1/00000/7D76FACF-D051-0646-BE60-33543F2C2D68.root',
       '/store/data/Run2017E/SinglePhoton/NANOAOD/Nano14Dec2018-v1/00000/88CE6D2F-FCCC-2847-B058-1975965C27B4.root',
       '/store/data/Run2017E/SinglePhoton/NANOAOD/Nano14Dec2018-v1/00000/A20D7400-4DD9-B646-B73A-38C260FA03D8.root',
       '/store/data/Run2017E/SinglePhoton/NANOAOD/Nano14Dec2018-v1/00000/C261896E-D66E-7146-B7C0-EA328C40C655.root',
       '/store/data/Run2017E/SinglePhoton/NANOAOD/Nano14Dec2018-v1/00000/FF5BE1E5-BE27-6244-898B-8D8252A195C9.root',
] )
