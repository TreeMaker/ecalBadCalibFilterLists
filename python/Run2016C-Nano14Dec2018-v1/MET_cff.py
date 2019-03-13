import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016C/MET/NANOAOD/Nano14Dec2018-v1/10000/11844CDD-28AC-D549-B470-E94D4DA10DA1.root',
       '/store/data/Run2016C/MET/NANOAOD/Nano14Dec2018-v1/10000/2754F055-ABC0-4547-92BC-034E840C9E17.root',
       '/store/data/Run2016C/MET/NANOAOD/Nano14Dec2018-v1/10000/75C4E995-2885-8048-BA07-FD4ACCD3572E.root',
       '/store/data/Run2016C/MET/NANOAOD/Nano14Dec2018-v1/10000/813E60C1-E7E9-C848-8B41-685642060D34.root',
       '/store/data/Run2016C/MET/NANOAOD/Nano14Dec2018-v1/10000/958ED760-E8C9-914E-B6AF-BB0431D78C1B.root',
       '/store/data/Run2016C/MET/NANOAOD/Nano14Dec2018-v1/10000/9ABD1B8D-2552-1347-8713-781C62AEBE6D.root',
       '/store/data/Run2016C/MET/NANOAOD/Nano14Dec2018-v1/10000/AA804D87-467E-6242-9EAA-F3D5A7B27A87.root',
       '/store/data/Run2016C/MET/NANOAOD/Nano14Dec2018-v1/10000/D0387C78-0D46-3246-A8FE-0E4F28877FA1.root',
       '/store/data/Run2016C/MET/NANOAOD/Nano14Dec2018-v1/10000/D93148DE-B4EF-C448-95A9-AD8BB374CD40.root',
       '/store/data/Run2016C/MET/NANOAOD/Nano14Dec2018-v1/10000/EF60B1EB-8515-DF48-80DC-7666FA7D35AA.root',
       '/store/data/Run2016C/MET/NANOAOD/Nano14Dec2018-v1/10000/F215B2C1-EA57-F945-BE71-A941499F0768.root',
       '/store/data/Run2016C/MET/NANOAOD/Nano14Dec2018-v1/10000/F5AFB6FD-0B31-9A4F-8DEC-C4437308F157.root',
] )
