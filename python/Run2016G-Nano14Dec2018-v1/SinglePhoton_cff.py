import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016G/SinglePhoton/NANOAOD/Nano14Dec2018-v1/90000/10B444E3-01DC-9244-8894-DBC543FD0722.root',
       '/store/data/Run2016G/SinglePhoton/NANOAOD/Nano14Dec2018-v1/90000/1585038F-60EF-FB42-AD8A-3C2462C2CEA7.root',
       '/store/data/Run2016G/SinglePhoton/NANOAOD/Nano14Dec2018-v1/90000/50FAD883-9933-D042-873C-A719AD2E9422.root',
       '/store/data/Run2016G/SinglePhoton/NANOAOD/Nano14Dec2018-v1/90000/5155E40F-39E3-B24E-A70C-42F3EDB66444.root',
       '/store/data/Run2016G/SinglePhoton/NANOAOD/Nano14Dec2018-v1/90000/5BA5312A-FB3D-7D49-96EA-594C9392C20C.root',
       '/store/data/Run2016G/SinglePhoton/NANOAOD/Nano14Dec2018-v1/90000/65C41156-E23A-7342-879B-13FDC168D821.root',
       '/store/data/Run2016G/SinglePhoton/NANOAOD/Nano14Dec2018-v1/90000/7125DCA2-5785-B048-BE2E-D34FE2BDBEA4.root',
       '/store/data/Run2016G/SinglePhoton/NANOAOD/Nano14Dec2018-v1/90000/91F845B6-8F0E-9444-9AF0-439F3EAE487B.root',
       '/store/data/Run2016G/SinglePhoton/NANOAOD/Nano14Dec2018-v1/90000/92BBD1D1-129A-2F4B-B56D-998E1A3EF905.root',
       '/store/data/Run2016G/SinglePhoton/NANOAOD/Nano14Dec2018-v1/90000/9978543B-0400-8240-A5B6-F03A752427A9.root',
       '/store/data/Run2016G/SinglePhoton/NANOAOD/Nano14Dec2018-v1/90000/9C17C94A-B7D1-1B4D-8DE7-FA4306E5D067.root',
       '/store/data/Run2016G/SinglePhoton/NANOAOD/Nano14Dec2018-v1/90000/9E894B6A-1B7C-EC41-A857-A204D52BC28C.root',
       '/store/data/Run2016G/SinglePhoton/NANOAOD/Nano14Dec2018-v1/90000/BCC08BCE-4788-964D-81BA-D7806F552C1E.root',
       '/store/data/Run2016G/SinglePhoton/NANOAOD/Nano14Dec2018-v1/90000/C111EF2B-9CA6-8D4E-85A8-8DD619B772A4.root',
       '/store/data/Run2016G/SinglePhoton/NANOAOD/Nano14Dec2018-v1/90000/C42608EE-265E-5C4E-A3FF-D708F19F8D70.root',
       '/store/data/Run2016G/SinglePhoton/NANOAOD/Nano14Dec2018-v1/90000/D8F1139C-7BF2-1045-80EA-C16A5975599D.root',
       '/store/data/Run2016G/SinglePhoton/NANOAOD/Nano14Dec2018-v1/90000/F7E7F886-D18A-654D-9011-13F402524163.root',
       '/store/data/Run2016G/SinglePhoton/NANOAOD/Nano14Dec2018-v1/90000/FD267B01-BE5F-424E-BBCD-E1AA88953511.root',
] )
