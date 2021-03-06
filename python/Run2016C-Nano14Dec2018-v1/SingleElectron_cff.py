import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016C/SingleElectron/NANOAOD/Nano14Dec2018-v1/00000/06DC5B49-0204-954F-998D-02C8D01466F6.root',
       '/store/data/Run2016C/SingleElectron/NANOAOD/Nano14Dec2018-v1/00000/0BAAA253-0C6C-7E44-B661-BAAB6818B63F.root',
       '/store/data/Run2016C/SingleElectron/NANOAOD/Nano14Dec2018-v1/00000/0F727F8A-7471-5046-858B-8D0692CEEC4A.root',
       '/store/data/Run2016C/SingleElectron/NANOAOD/Nano14Dec2018-v1/00000/30A7AB5C-6AAB-FA46-8243-A6DB32AE97C6.root',
       '/store/data/Run2016C/SingleElectron/NANOAOD/Nano14Dec2018-v1/00000/3151B5FF-5149-0442-96F9-B66416B1CA95.root',
       '/store/data/Run2016C/SingleElectron/NANOAOD/Nano14Dec2018-v1/00000/3FDDD40B-8B75-FC4D-BC35-F787C24BE178.root',
       '/store/data/Run2016C/SingleElectron/NANOAOD/Nano14Dec2018-v1/00000/5EB0A0C7-B8B1-6C48-8F7A-21910E7BC729.root',
       '/store/data/Run2016C/SingleElectron/NANOAOD/Nano14Dec2018-v1/00000/6A3D62A0-D8B3-AD4E-AD41-F72F1F77847C.root',
       '/store/data/Run2016C/SingleElectron/NANOAOD/Nano14Dec2018-v1/00000/6AC7BC06-9E6A-D240-96FC-36A45522F14B.root',
       '/store/data/Run2016C/SingleElectron/NANOAOD/Nano14Dec2018-v1/00000/7943DF0E-3344-954A-9614-16A63D4C85AC.root',
       '/store/data/Run2016C/SingleElectron/NANOAOD/Nano14Dec2018-v1/00000/7F39E8D3-5998-FE4F-B12F-34B31DB6F57C.root',
       '/store/data/Run2016C/SingleElectron/NANOAOD/Nano14Dec2018-v1/00000/83A2FCE9-ED68-A34E-9BE7-FBCC46BD0A47.root',
       '/store/data/Run2016C/SingleElectron/NANOAOD/Nano14Dec2018-v1/00000/970BB5C0-6067-BD4A-AE9B-55EC8E43D079.root',
       '/store/data/Run2016C/SingleElectron/NANOAOD/Nano14Dec2018-v1/00000/9AA01692-7A99-5D41-B481-C39F62B32BDE.root',
       '/store/data/Run2016C/SingleElectron/NANOAOD/Nano14Dec2018-v1/00000/9B5BF45D-0DDE-7540-BCB6-6C655A05CD39.root',
       '/store/data/Run2016C/SingleElectron/NANOAOD/Nano14Dec2018-v1/00000/9CEA11D3-A6F7-1B4E-9A37-FD42A4425546.root',
       '/store/data/Run2016C/SingleElectron/NANOAOD/Nano14Dec2018-v1/00000/A6A775B8-ED2B-B24D-8E26-400E47579E97.root',
       '/store/data/Run2016C/SingleElectron/NANOAOD/Nano14Dec2018-v1/00000/B2491BBF-DCBD-6444-808A-32F007C92E9D.root',
       '/store/data/Run2016C/SingleElectron/NANOAOD/Nano14Dec2018-v1/00000/B24BD641-8660-6F4D-828B-F79D2625656C.root',
       '/store/data/Run2016C/SingleElectron/NANOAOD/Nano14Dec2018-v1/00000/BEC83C7F-3E4F-3041-BC2D-BC65183FF382.root',
       '/store/data/Run2016C/SingleElectron/NANOAOD/Nano14Dec2018-v1/00000/BF41CDE3-0F68-DB4F-8B46-CC3D77854F17.root',
       '/store/data/Run2016C/SingleElectron/NANOAOD/Nano14Dec2018-v1/00000/C3A088E8-5D14-324D-ADB1-4854C7037791.root',
       '/store/data/Run2016C/SingleElectron/NANOAOD/Nano14Dec2018-v1/00000/C4BD8A9B-7FF9-0642-A9F5-471A1EA607F7.root',
       '/store/data/Run2016C/SingleElectron/NANOAOD/Nano14Dec2018-v1/00000/E7D8C1D4-3014-F640-B649-9C1FEAF683A0.root',
       '/store/data/Run2016C/SingleElectron/NANOAOD/Nano14Dec2018-v1/00000/ED1A5E29-B59E-6B49-80AB-9055F63841B9.root',
       '/store/data/Run2016C/SingleElectron/NANOAOD/Nano14Dec2018-v1/00000/FE0E842F-5F1D-6D4C-BD94-5AE2C3E93FFE.root',
       '/store/data/Run2016C/SingleElectron/NANOAOD/Nano14Dec2018-v1/90000/0F1417F0-771A-0248-BFA7-56940642272F.root',
       '/store/data/Run2016C/SingleElectron/NANOAOD/Nano14Dec2018-v1/90000/1961B3E9-84DD-DE4B-AB12-F6F95925C463.root',
       '/store/data/Run2016C/SingleElectron/NANOAOD/Nano14Dec2018-v1/90000/1AF7C87D-E8EF-E048-9D61-868711428429.root',
       '/store/data/Run2016C/SingleElectron/NANOAOD/Nano14Dec2018-v1/90000/2C86822A-BF91-A544-862E-429F48241579.root',
       '/store/data/Run2016C/SingleElectron/NANOAOD/Nano14Dec2018-v1/90000/3BC3B162-311F-8449-9CEB-7415631B5301.root',
       '/store/data/Run2016C/SingleElectron/NANOAOD/Nano14Dec2018-v1/90000/3C8993AB-E1D4-6C44-86D3-9D7EA90D7720.root',
       '/store/data/Run2016C/SingleElectron/NANOAOD/Nano14Dec2018-v1/90000/3F143327-3AC5-D849-9855-283A4C4738C5.root',
       '/store/data/Run2016C/SingleElectron/NANOAOD/Nano14Dec2018-v1/90000/6254AEB4-299A-E044-ADB7-77B45AEC9B20.root',
       '/store/data/Run2016C/SingleElectron/NANOAOD/Nano14Dec2018-v1/90000/655892AD-F49F-D249-AD8A-C86260D42D2E.root',
       '/store/data/Run2016C/SingleElectron/NANOAOD/Nano14Dec2018-v1/90000/718AD0F8-F6F6-2744-85BF-46394A8C604A.root',
       '/store/data/Run2016C/SingleElectron/NANOAOD/Nano14Dec2018-v1/90000/818A7503-6954-B947-AC2D-CFA8E52F17FC.root',
       '/store/data/Run2016C/SingleElectron/NANOAOD/Nano14Dec2018-v1/90000/81E7CA12-EDDA-834C-843D-A8DDE114FE92.root',
       '/store/data/Run2016C/SingleElectron/NANOAOD/Nano14Dec2018-v1/90000/898BBEA0-8821-C74F-A688-53D5792FD93A.root',
       '/store/data/Run2016C/SingleElectron/NANOAOD/Nano14Dec2018-v1/90000/9550E150-DE8D-7849-BC7F-905AFC823207.root',
       '/store/data/Run2016C/SingleElectron/NANOAOD/Nano14Dec2018-v1/90000/989D7842-C554-3948-99DC-EC87D413B773.root',
       '/store/data/Run2016C/SingleElectron/NANOAOD/Nano14Dec2018-v1/90000/9BD5C826-1CF3-DC4A-818A-B2F13974F330.root',
       '/store/data/Run2016C/SingleElectron/NANOAOD/Nano14Dec2018-v1/90000/D555DE64-01FA-324B-B898-F9FD72AE046B.root',
       '/store/data/Run2016C/SingleElectron/NANOAOD/Nano14Dec2018-v1/90000/D7283E44-3E37-5D4F-8D43-053A4E93A1C7.root',
       '/store/data/Run2016C/SingleElectron/NANOAOD/Nano14Dec2018-v1/90000/DAB26188-03B8-AF43-9B23-F3D79D9C47F4.root',
       '/store/data/Run2016C/SingleElectron/NANOAOD/Nano14Dec2018-v1/90000/DC7B1468-DBD7-2D4E-AC10-145DD85F1FCF.root',
       '/store/data/Run2016C/SingleElectron/NANOAOD/Nano14Dec2018-v1/90000/EF84010E-5CA1-F444-AA5C-B4FB36E3B5E8.root',
       '/store/data/Run2016C/SingleElectron/NANOAOD/Nano14Dec2018-v1/90000/F6A09F90-5999-554F-8E7D-15B9A132B81B.root',
       '/store/data/Run2016C/SingleElectron/NANOAOD/Nano14Dec2018-v1/90000/F8AFD313-9D2F-BD48-ABB0-4752263F84DD.root',
       '/store/data/Run2016C/SingleElectron/NANOAOD/Nano14Dec2018-v1/90000/FC06511D-DD6C-0444-84F1-DC92ECF89FA1.root',
       '/store/data/Run2016C/SingleElectron/NANOAOD/Nano14Dec2018-v1/90000/FCD7AEFA-0012-D146-8EF6-5742240551D6.root',
] )
