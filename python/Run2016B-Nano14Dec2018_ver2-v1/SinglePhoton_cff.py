import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016B_ver2/SinglePhoton/NANOAOD/Nano14Dec2018_ver2-v1/90000/04F37576-DCAE-0748-80BE-47312A25CFEA.root',
       '/store/data/Run2016B_ver2/SinglePhoton/NANOAOD/Nano14Dec2018_ver2-v1/90000/0DD7D401-A711-374E-8C8F-C7E383C8122A.root',
       '/store/data/Run2016B_ver2/SinglePhoton/NANOAOD/Nano14Dec2018_ver2-v1/90000/1D6E1F0C-3DE9-C845-A442-5CB2F852F04D.root',
       '/store/data/Run2016B_ver2/SinglePhoton/NANOAOD/Nano14Dec2018_ver2-v1/90000/25EA296D-5A93-B842-8C44-0FD733CD8077.root',
       '/store/data/Run2016B_ver2/SinglePhoton/NANOAOD/Nano14Dec2018_ver2-v1/90000/265B2A10-6D87-1D4A-803B-F26CCFFAC291.root',
       '/store/data/Run2016B_ver2/SinglePhoton/NANOAOD/Nano14Dec2018_ver2-v1/90000/303AB2EE-8425-7F4E-AB36-E8E42E2C85A3.root',
       '/store/data/Run2016B_ver2/SinglePhoton/NANOAOD/Nano14Dec2018_ver2-v1/90000/30EECE6C-FFAC-0E4D-BAB5-4A0A744C81FC.root',
       '/store/data/Run2016B_ver2/SinglePhoton/NANOAOD/Nano14Dec2018_ver2-v1/90000/319AA1F0-4620-0641-A82F-DF3B39A02D63.root',
       '/store/data/Run2016B_ver2/SinglePhoton/NANOAOD/Nano14Dec2018_ver2-v1/90000/31CF6035-5389-D148-9EA6-F084C506EBC9.root',
       '/store/data/Run2016B_ver2/SinglePhoton/NANOAOD/Nano14Dec2018_ver2-v1/90000/42A9127D-2C9A-D14F-B339-6A3EE67D3158.root',
       '/store/data/Run2016B_ver2/SinglePhoton/NANOAOD/Nano14Dec2018_ver2-v1/90000/4488CC50-DCAC-B743-BAB7-5797D649A98C.root',
       '/store/data/Run2016B_ver2/SinglePhoton/NANOAOD/Nano14Dec2018_ver2-v1/90000/45B0F27C-444F-464D-891A-EB4A2460DD75.root',
       '/store/data/Run2016B_ver2/SinglePhoton/NANOAOD/Nano14Dec2018_ver2-v1/90000/490C93A6-FBFF-1F4F-BFAB-6CC18B927912.root',
       '/store/data/Run2016B_ver2/SinglePhoton/NANOAOD/Nano14Dec2018_ver2-v1/90000/4B9F00EF-F011-7944-A553-51D2D4521052.root',
       '/store/data/Run2016B_ver2/SinglePhoton/NANOAOD/Nano14Dec2018_ver2-v1/90000/50C0FC06-201A-DB44-801C-5FAD07103DAC.root',
       '/store/data/Run2016B_ver2/SinglePhoton/NANOAOD/Nano14Dec2018_ver2-v1/90000/6A2D15AA-024D-7B48-8D03-66FF498B0E19.root',
       '/store/data/Run2016B_ver2/SinglePhoton/NANOAOD/Nano14Dec2018_ver2-v1/90000/6B2AA033-0570-5643-9AEB-D87CF6BA9254.root',
       '/store/data/Run2016B_ver2/SinglePhoton/NANOAOD/Nano14Dec2018_ver2-v1/90000/6DF3AF7C-6AF1-744E-9F8A-CCB534C7339A.root',
       '/store/data/Run2016B_ver2/SinglePhoton/NANOAOD/Nano14Dec2018_ver2-v1/90000/71277F5C-76C8-7543-A02A-1D3F06BDBF44.root',
       '/store/data/Run2016B_ver2/SinglePhoton/NANOAOD/Nano14Dec2018_ver2-v1/90000/80957054-A969-874B-9DBD-2039DD6E090C.root',
       '/store/data/Run2016B_ver2/SinglePhoton/NANOAOD/Nano14Dec2018_ver2-v1/90000/8540DE37-E521-9B4B-9A8E-E0CF9A1B9AF9.root',
       '/store/data/Run2016B_ver2/SinglePhoton/NANOAOD/Nano14Dec2018_ver2-v1/90000/9893C99B-CA7C-A340-8578-28AAD248881E.root',
       '/store/data/Run2016B_ver2/SinglePhoton/NANOAOD/Nano14Dec2018_ver2-v1/90000/9E4694B3-EA3A-334F-82BF-0D12FBE7F5A7.root',
       '/store/data/Run2016B_ver2/SinglePhoton/NANOAOD/Nano14Dec2018_ver2-v1/90000/A136C34D-45E9-584E-A9F2-D557C2E58C54.root',
       '/store/data/Run2016B_ver2/SinglePhoton/NANOAOD/Nano14Dec2018_ver2-v1/90000/AB867FAF-DF54-D747-B500-213222872B32.root',
       '/store/data/Run2016B_ver2/SinglePhoton/NANOAOD/Nano14Dec2018_ver2-v1/90000/AC25DEA5-EFD3-5147-9005-4F1DB5056766.root',
       '/store/data/Run2016B_ver2/SinglePhoton/NANOAOD/Nano14Dec2018_ver2-v1/90000/BE5D2443-E259-7B4F-B2A6-B21F65A95E39.root',
       '/store/data/Run2016B_ver2/SinglePhoton/NANOAOD/Nano14Dec2018_ver2-v1/90000/C0066BBE-F6E5-864E-8599-AC1F9314E73A.root',
       '/store/data/Run2016B_ver2/SinglePhoton/NANOAOD/Nano14Dec2018_ver2-v1/90000/C2A13A84-ABE9-934D-B439-B06523E463AD.root',
       '/store/data/Run2016B_ver2/SinglePhoton/NANOAOD/Nano14Dec2018_ver2-v1/90000/C3A5BFAA-6F1D-694D-B273-0CE985E48483.root',
       '/store/data/Run2016B_ver2/SinglePhoton/NANOAOD/Nano14Dec2018_ver2-v1/90000/D06C12C8-5F7B-6A45-A123-9B0C2494CA90.root',
       '/store/data/Run2016B_ver2/SinglePhoton/NANOAOD/Nano14Dec2018_ver2-v1/90000/F557754C-2C0C-3C43-8E84-C123B418332F.root',
       '/store/data/Run2016B_ver2/SinglePhoton/NANOAOD/Nano14Dec2018_ver2-v1/90000/F58AEC54-AF16-3C4C-9828-E32C2E7BDB15.root',
] )
