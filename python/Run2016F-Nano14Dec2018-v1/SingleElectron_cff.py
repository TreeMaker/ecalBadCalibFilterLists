import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016F/SingleElectron/NANOAOD/Nano14Dec2018-v1/90000/04669647-35BB-2A42-A759-24A6A1F4C0E0.root',
       '/store/data/Run2016F/SingleElectron/NANOAOD/Nano14Dec2018-v1/90000/0575F72A-4C6D-F842-98FE-DD6F48F25F28.root',
       '/store/data/Run2016F/SingleElectron/NANOAOD/Nano14Dec2018-v1/90000/09706075-12FE-9945-A36F-EDBADDF562EC.root',
       '/store/data/Run2016F/SingleElectron/NANOAOD/Nano14Dec2018-v1/90000/0E3317B1-D9B6-AF40-A447-C60F291F24F8.root',
       '/store/data/Run2016F/SingleElectron/NANOAOD/Nano14Dec2018-v1/90000/1546D0B7-E4AB-9A4B-84DA-6224BE73CB0F.root',
       '/store/data/Run2016F/SingleElectron/NANOAOD/Nano14Dec2018-v1/90000/16522F78-F805-4644-8353-67D7034C8E97.root',
       '/store/data/Run2016F/SingleElectron/NANOAOD/Nano14Dec2018-v1/90000/1B3CA3B9-8DC8-2D4D-A6B9-E7F26B70914E.root',
       '/store/data/Run2016F/SingleElectron/NANOAOD/Nano14Dec2018-v1/90000/23572B6B-1A44-A44D-B67B-47081B52509A.root',
       '/store/data/Run2016F/SingleElectron/NANOAOD/Nano14Dec2018-v1/90000/3770B9DE-A6F9-2B49-A6AC-532A12EB23A0.root',
       '/store/data/Run2016F/SingleElectron/NANOAOD/Nano14Dec2018-v1/90000/39302132-B037-6B4C-8911-E19757FA1448.root',
       '/store/data/Run2016F/SingleElectron/NANOAOD/Nano14Dec2018-v1/90000/3ADCA66A-95D5-A34A-A988-C83C6354F150.root',
       '/store/data/Run2016F/SingleElectron/NANOAOD/Nano14Dec2018-v1/90000/4B95D8F5-370D-E74F-8CF5-E56C800CC143.root',
       '/store/data/Run2016F/SingleElectron/NANOAOD/Nano14Dec2018-v1/90000/5CF9B182-01EA-4A4E-ABAC-69DBA850E774.root',
       '/store/data/Run2016F/SingleElectron/NANOAOD/Nano14Dec2018-v1/90000/7682FB73-4285-934F-9BAA-1A8148A317E4.root',
       '/store/data/Run2016F/SingleElectron/NANOAOD/Nano14Dec2018-v1/90000/874D12F4-41C9-364B-A191-CF9631B867C2.root',
       '/store/data/Run2016F/SingleElectron/NANOAOD/Nano14Dec2018-v1/90000/973A5084-79AD-7344-90A3-F1725F3EB905.root',
       '/store/data/Run2016F/SingleElectron/NANOAOD/Nano14Dec2018-v1/90000/A78C0E41-F7DA-A543-8362-39A9DAB3817D.root',
       '/store/data/Run2016F/SingleElectron/NANOAOD/Nano14Dec2018-v1/90000/B5290F51-1F65-5442-923E-3273AB0D60A0.root',
       '/store/data/Run2016F/SingleElectron/NANOAOD/Nano14Dec2018-v1/90000/B75E8A84-3FFD-9940-A79B-CBC695E299DB.root',
       '/store/data/Run2016F/SingleElectron/NANOAOD/Nano14Dec2018-v1/90000/C00D82B6-F18A-4747-AD67-780F684D1EC6.root',
       '/store/data/Run2016F/SingleElectron/NANOAOD/Nano14Dec2018-v1/90000/D5EAEC51-D9F7-984C-BC0C-0CAC8DC380B6.root',
       '/store/data/Run2016F/SingleElectron/NANOAOD/Nano14Dec2018-v1/90000/D65ECF9B-7903-154E-8CE9-5481E8BABB68.root',
       '/store/data/Run2016F/SingleElectron/NANOAOD/Nano14Dec2018-v1/90000/D776B95C-9FC4-E747-B650-73B66DFFA993.root',
       '/store/data/Run2016F/SingleElectron/NANOAOD/Nano14Dec2018-v1/90000/D7D1A0FD-CF5B-F84C-A175-BF317A40EC7B.root',
       '/store/data/Run2016F/SingleElectron/NANOAOD/Nano14Dec2018-v1/90000/E8DC7E3F-8521-7A4A-84FF-06F4B13E4C2A.root',
       '/store/data/Run2016F/SingleElectron/NANOAOD/Nano14Dec2018-v1/90000/E9718E82-D9B3-4449-A0C7-5C93C0E920B6.root',
       '/store/data/Run2016F/SingleElectron/NANOAOD/Nano14Dec2018-v1/90000/EAAC9C64-08A8-BE4E-B8D5-C2EFED4C6C36.root',
       '/store/data/Run2016F/SingleElectron/NANOAOD/Nano14Dec2018-v1/90000/ED16D01A-4CAF-9A40-B851-F017EACBBABE.root',
       '/store/data/Run2016F/SingleElectron/NANOAOD/Nano14Dec2018-v1/90000/F6A593F6-B1C7-AF4A-8742-63C0DC426D7A.root',
       '/store/data/Run2016F/SingleElectron/NANOAOD/Nano14Dec2018-v1/90000/F81BDE36-4450-B148-B8A9-60CC5153C833.root',
       '/store/data/Run2016F/SingleElectron/NANOAOD/Nano14Dec2018-v1/90000/F93D99DA-9DC0-5442-889E-29906770746B.root',
] )
