import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2018A/MET/NANOAOD/Nano14Dec2018-v1/50000/02CD874E-F40C-C64F-A3F5-1FFD1E36EE9A.root',
       '/store/data/Run2018A/MET/NANOAOD/Nano14Dec2018-v1/50000/06FEBD13-FE98-DA40-8FEF-F81016CDA1EF.root',
       '/store/data/Run2018A/MET/NANOAOD/Nano14Dec2018-v1/50000/11C389F1-3635-E44B-88A2-CD0D7503397C.root',
       '/store/data/Run2018A/MET/NANOAOD/Nano14Dec2018-v1/50000/135E67E0-D0DC-0248-A47D-13363D99DA0F.root',
       '/store/data/Run2018A/MET/NANOAOD/Nano14Dec2018-v1/50000/15B460C0-BE3D-F043-A63C-8FF351107CAC.root',
       '/store/data/Run2018A/MET/NANOAOD/Nano14Dec2018-v1/50000/2538738F-25E1-6643-9D07-EF2A52A145FD.root',
       '/store/data/Run2018A/MET/NANOAOD/Nano14Dec2018-v1/50000/28F55B44-73E3-7E40-BDE8-1A0DBA5D1BD1.root',
       '/store/data/Run2018A/MET/NANOAOD/Nano14Dec2018-v1/50000/2FD53FB3-3D22-B140-8979-F860C4CEF7D0.root',
       '/store/data/Run2018A/MET/NANOAOD/Nano14Dec2018-v1/50000/343C5319-2BCC-9246-A0B7-25FC36F7B00D.root',
       '/store/data/Run2018A/MET/NANOAOD/Nano14Dec2018-v1/50000/3B3A13C7-2AB2-6349-BD31-F0354959006E.root',
       '/store/data/Run2018A/MET/NANOAOD/Nano14Dec2018-v1/50000/50112667-F063-3249-B423-C65A0666A1E4.root',
       '/store/data/Run2018A/MET/NANOAOD/Nano14Dec2018-v1/50000/5703D587-1180-324C-93FD-44EF9BACC276.root',
       '/store/data/Run2018A/MET/NANOAOD/Nano14Dec2018-v1/50000/57DC038C-1D8D-A046-8003-F98802007CF5.root',
       '/store/data/Run2018A/MET/NANOAOD/Nano14Dec2018-v1/50000/63030C9D-F43D-6F46-9729-F07FD58297A1.root',
       '/store/data/Run2018A/MET/NANOAOD/Nano14Dec2018-v1/50000/665CF1BA-2D7D-C748-92D0-60188C9331AC.root',
       '/store/data/Run2018A/MET/NANOAOD/Nano14Dec2018-v1/50000/6B640446-D259-4145-B7C3-823D004686AC.root',
       '/store/data/Run2018A/MET/NANOAOD/Nano14Dec2018-v1/50000/73B9EF56-9F5E-AC46-AEFD-155021931AAB.root',
       '/store/data/Run2018A/MET/NANOAOD/Nano14Dec2018-v1/50000/73C0AF68-4293-5544-A764-156E7FD77245.root',
       '/store/data/Run2018A/MET/NANOAOD/Nano14Dec2018-v1/50000/7F004C70-C5D7-D243-87B9-0DE0C91DA69F.root',
       '/store/data/Run2018A/MET/NANOAOD/Nano14Dec2018-v1/50000/8742D634-071E-8446-B552-3213CCF9D0A7.root',
       '/store/data/Run2018A/MET/NANOAOD/Nano14Dec2018-v1/50000/884DAEBD-77D0-234E-BBEB-61CFD2AFB06C.root',
       '/store/data/Run2018A/MET/NANOAOD/Nano14Dec2018-v1/50000/95FF185D-A683-F049-868F-BECB6FBE56A7.root',
       '/store/data/Run2018A/MET/NANOAOD/Nano14Dec2018-v1/50000/9A436BBF-83A3-AA4E-B7F2-AD12DD7CEFFC.root',
       '/store/data/Run2018A/MET/NANOAOD/Nano14Dec2018-v1/50000/A369DB6E-66BC-4143-A22E-1351AEFA741B.root',
       '/store/data/Run2018A/MET/NANOAOD/Nano14Dec2018-v1/50000/A425F451-3DC6-6D4B-9D38-D8A687B86024.root',
       '/store/data/Run2018A/MET/NANOAOD/Nano14Dec2018-v1/50000/A885C3DF-3F99-CE44-8D55-4D0AF24DB077.root',
       '/store/data/Run2018A/MET/NANOAOD/Nano14Dec2018-v1/50000/B5BBF351-CC7C-2942-9695-87117E7876A7.root',
       '/store/data/Run2018A/MET/NANOAOD/Nano14Dec2018-v1/50000/C309AAF0-CDA8-7741-BFB1-96AD7058D8F3.root',
       '/store/data/Run2018A/MET/NANOAOD/Nano14Dec2018-v1/50000/D11CCB41-B73F-EE48-9AC0-9138494EBF38.root',
       '/store/data/Run2018A/MET/NANOAOD/Nano14Dec2018-v1/50000/D263CCB1-7C70-A543-B401-5FF4B799A812.root',
       '/store/data/Run2018A/MET/NANOAOD/Nano14Dec2018-v1/50000/D3DF95ED-1657-9D47-9A84-6D43D13EFA42.root',
       '/store/data/Run2018A/MET/NANOAOD/Nano14Dec2018-v1/50000/D5C575E9-B658-CB40-AAC2-E4D3D99DCE92.root',
       '/store/data/Run2018A/MET/NANOAOD/Nano14Dec2018-v1/50000/D931C43F-2193-6F45-82DF-2050E21112D3.root',
       '/store/data/Run2018A/MET/NANOAOD/Nano14Dec2018-v1/50000/E8FB06ED-1634-714A-88BE-8A168DDC099A.root',
       '/store/data/Run2018A/MET/NANOAOD/Nano14Dec2018-v1/50000/E94E177F-BE47-A54B-AA80-323EAB83231C.root',
       '/store/data/Run2018A/MET/NANOAOD/Nano14Dec2018-v1/50000/EF22DDDC-41AB-6D41-8082-443A04E30123.root',
       '/store/data/Run2018A/MET/NANOAOD/Nano14Dec2018-v1/50000/F4BD0D92-83D4-9A42-86BF-E715ADE3AAA9.root',
       '/store/data/Run2018A/MET/NANOAOD/Nano14Dec2018-v1/50000/FABD0CFF-17FD-3148-9F98-B847FFD54BBF.root',
] )
