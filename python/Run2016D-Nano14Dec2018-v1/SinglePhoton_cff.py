import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016D/SinglePhoton/NANOAOD/Nano14Dec2018-v1/80000/01CF33E5-409F-914A-ACCD-1D1E678B3EC4.root',
       '/store/data/Run2016D/SinglePhoton/NANOAOD/Nano14Dec2018-v1/80000/2C1B9A50-F960-C942-8782-4898DDE55583.root',
       '/store/data/Run2016D/SinglePhoton/NANOAOD/Nano14Dec2018-v1/80000/38F12E98-9872-9C4E-9204-34FBE513F17B.root',
       '/store/data/Run2016D/SinglePhoton/NANOAOD/Nano14Dec2018-v1/80000/3AE07914-9CC8-D34D-82A8-32D37C579D8D.root',
       '/store/data/Run2016D/SinglePhoton/NANOAOD/Nano14Dec2018-v1/80000/42B63B1F-B23B-0E41-9280-DAC3AA2F07E4.root',
       '/store/data/Run2016D/SinglePhoton/NANOAOD/Nano14Dec2018-v1/80000/49EB0304-1E64-DC48-AF1B-9C7ABD8FF25B.root',
       '/store/data/Run2016D/SinglePhoton/NANOAOD/Nano14Dec2018-v1/80000/4C76BF8C-5237-6849-9F4B-E0FDEE39B2A9.root',
       '/store/data/Run2016D/SinglePhoton/NANOAOD/Nano14Dec2018-v1/80000/4EDDB495-4A8A-D544-BD5D-640A2866F468.root',
       '/store/data/Run2016D/SinglePhoton/NANOAOD/Nano14Dec2018-v1/80000/73B99CD8-1F90-8246-86A8-73246965DA73.root',
       '/store/data/Run2016D/SinglePhoton/NANOAOD/Nano14Dec2018-v1/80000/86524F79-6900-A748-9044-A89167DFEE66.root',
       '/store/data/Run2016D/SinglePhoton/NANOAOD/Nano14Dec2018-v1/80000/9D9777A4-67D2-2C4A-A5C0-3E10AB725361.root',
       '/store/data/Run2016D/SinglePhoton/NANOAOD/Nano14Dec2018-v1/80000/C41C2A11-3B4E-8949-8B30-6F5BA4B7FEDC.root',
       '/store/data/Run2016D/SinglePhoton/NANOAOD/Nano14Dec2018-v1/80000/CCDF0EFE-1115-5A49-842F-0E08D9360DF4.root',
       '/store/data/Run2016D/SinglePhoton/NANOAOD/Nano14Dec2018-v1/80000/D1D71508-D6D3-0A47-9A2C-3BE09B93982E.root',
       '/store/data/Run2016D/SinglePhoton/NANOAOD/Nano14Dec2018-v1/80000/E6CC414C-D24E-5345-823C-884806048033.root',
] )
