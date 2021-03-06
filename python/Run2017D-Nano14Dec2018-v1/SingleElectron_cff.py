import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2017D/SingleElectron/NANOAOD/Nano14Dec2018-v1/20000/123128F7-CB46-1043-935A-03C2A361E438.root',
       '/store/data/Run2017D/SingleElectron/NANOAOD/Nano14Dec2018-v1/20000/14688269-3032-9C43-8E8F-376CB71A7A1F.root',
       '/store/data/Run2017D/SingleElectron/NANOAOD/Nano14Dec2018-v1/20000/18AA5C36-3291-C441-89C9-3AF8AEA24AA9.root',
       '/store/data/Run2017D/SingleElectron/NANOAOD/Nano14Dec2018-v1/20000/2A8E20C5-6400-A14C-9A5A-8FAB324E2DF7.root',
       '/store/data/Run2017D/SingleElectron/NANOAOD/Nano14Dec2018-v1/20000/2FD2493D-8283-0448-BCE6-892EB60F61ED.root',
       '/store/data/Run2017D/SingleElectron/NANOAOD/Nano14Dec2018-v1/20000/3D94E56E-5600-3E48-8FC6-45CA994784DF.root',
       '/store/data/Run2017D/SingleElectron/NANOAOD/Nano14Dec2018-v1/20000/3FEAEF5E-4963-3241-BF6F-C7581E749A01.root',
       '/store/data/Run2017D/SingleElectron/NANOAOD/Nano14Dec2018-v1/20000/4043B5F3-EF7F-5945-93A1-35130C0B0404.root',
       '/store/data/Run2017D/SingleElectron/NANOAOD/Nano14Dec2018-v1/20000/4FCC7CE5-7FF9-C045-A0F9-C59A895C511F.root',
       '/store/data/Run2017D/SingleElectron/NANOAOD/Nano14Dec2018-v1/20000/514BE637-133D-4B43-A512-F7CAA9495D0E.root',
       '/store/data/Run2017D/SingleElectron/NANOAOD/Nano14Dec2018-v1/20000/5D69B5AE-BB8F-5F40-84CB-AD0371747FC7.root',
       '/store/data/Run2017D/SingleElectron/NANOAOD/Nano14Dec2018-v1/20000/76EE065F-EA3D-5840-A00D-E8BF155A456B.root',
       '/store/data/Run2017D/SingleElectron/NANOAOD/Nano14Dec2018-v1/20000/AA532480-B5C8-804F-9CD5-814A8F2A41D5.root',
       '/store/data/Run2017D/SingleElectron/NANOAOD/Nano14Dec2018-v1/20000/B09E7C13-25F1-6E4A-BA4C-5D91E5161140.root',
       '/store/data/Run2017D/SingleElectron/NANOAOD/Nano14Dec2018-v1/20000/B0B89112-DD82-924E-AFA5-3FA47329B6D8.root',
       '/store/data/Run2017D/SingleElectron/NANOAOD/Nano14Dec2018-v1/20000/D6935D1D-C4BF-C448-B3EC-DCC9119387FC.root',
       '/store/data/Run2017D/SingleElectron/NANOAOD/Nano14Dec2018-v1/20000/D6F747F4-CBB9-2C4D-87BF-9356ED880A4A.root',
       '/store/data/Run2017D/SingleElectron/NANOAOD/Nano14Dec2018-v1/20000/E569EA42-5595-474D-BCB9-BF3AD79B9859.root',
       '/store/data/Run2017D/SingleElectron/NANOAOD/Nano14Dec2018-v1/20000/F29EEAF3-87FD-7447-8F46-CE0C31993B06.root',
       '/store/data/Run2017D/SingleElectron/NANOAOD/Nano14Dec2018-v1/90000/16B6E834-E2C0-F84A-B1F8-285C5E1510A4.root',
       '/store/data/Run2017D/SingleElectron/NANOAOD/Nano14Dec2018-v1/90000/195EF8B0-5CAC-364C-BE3D-90AFEAAEF61E.root',
       '/store/data/Run2017D/SingleElectron/NANOAOD/Nano14Dec2018-v1/90000/38BB4776-B8AF-0447-816F-697072C038E1.root',
       '/store/data/Run2017D/SingleElectron/NANOAOD/Nano14Dec2018-v1/90000/508602E9-34B8-B04C-8BA2-D8B9D61CEE8E.root',
       '/store/data/Run2017D/SingleElectron/NANOAOD/Nano14Dec2018-v1/90000/59B9BA57-1804-6D45-B84C-8D0484B53814.root',
       '/store/data/Run2017D/SingleElectron/NANOAOD/Nano14Dec2018-v1/90000/5D8050E3-F1C8-5C44-BC53-DA47C99372B4.root',
       '/store/data/Run2017D/SingleElectron/NANOAOD/Nano14Dec2018-v1/90000/65D710B3-143D-1E4B-B803-29C90F59B34E.root',
       '/store/data/Run2017D/SingleElectron/NANOAOD/Nano14Dec2018-v1/90000/71F196E7-35E2-9B49-8C03-A8E68D4FFABE.root',
       '/store/data/Run2017D/SingleElectron/NANOAOD/Nano14Dec2018-v1/90000/875E04F5-7635-134D-ADB7-757373CA666A.root',
       '/store/data/Run2017D/SingleElectron/NANOAOD/Nano14Dec2018-v1/90000/97442239-EB10-7440-BB24-C1A0348ABDB9.root',
       '/store/data/Run2017D/SingleElectron/NANOAOD/Nano14Dec2018-v1/90000/A3719293-6AC6-D746-9399-02DEA03438DD.root',
       '/store/data/Run2017D/SingleElectron/NANOAOD/Nano14Dec2018-v1/90000/BFEB5394-B117-C542-8B2A-5BB3D538F377.root',
       '/store/data/Run2017D/SingleElectron/NANOAOD/Nano14Dec2018-v1/90000/F117B086-A8C8-7142-AC41-6C033648C76A.root',
] )
