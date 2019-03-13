import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016F/SinglePhoton/NANOAOD/Nano14Dec2018-v1/20000/01F5C47B-E0A2-484A-AD3E-B1617BA0CF6D.root',
       '/store/data/Run2016F/SinglePhoton/NANOAOD/Nano14Dec2018-v1/20000/3CD8EC13-86C5-7744-857F-5B502E09179C.root',
       '/store/data/Run2016F/SinglePhoton/NANOAOD/Nano14Dec2018-v1/20000/704276E3-F5C9-7946-91AF-65CD5107E63C.root',
       '/store/data/Run2016F/SinglePhoton/NANOAOD/Nano14Dec2018-v1/20000/870F24C3-161E-5A4A-9BE9-BCD2A0A168FB.root',
       '/store/data/Run2016F/SinglePhoton/NANOAOD/Nano14Dec2018-v1/20000/C80AC745-CD0D-954A-B09C-B3A0AE3312B5.root',
       '/store/data/Run2016F/SinglePhoton/NANOAOD/Nano14Dec2018-v1/20000/DFF83BEB-91D9-0B40-A6A8-EB55BE7F3B63.root',
       '/store/data/Run2016F/SinglePhoton/NANOAOD/Nano14Dec2018-v1/20000/E0F77A9B-3361-AE4C-9C2B-CA8DE90245FC.root',
       '/store/data/Run2016F/SinglePhoton/NANOAOD/Nano14Dec2018-v1/20000/EFCAB7F2-204A-E845-9BD6-A3282B2BDE1E.root',
       '/store/data/Run2016F/SinglePhoton/NANOAOD/Nano14Dec2018-v1/20000/FED92606-7045-D348-8BF3-8845A9E8F297.root',
] )
