import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016C/JetHT/NANOAOD/Nano1June2019-v1/60000/0832C225-C38C-704D-BA7B-283AC99875AD.root',
       '/store/data/Run2016C/JetHT/NANOAOD/Nano1June2019-v1/60000/0B9C3954-40DE-0742-9D36-9680C74255F8.root',
       '/store/data/Run2016C/JetHT/NANOAOD/Nano1June2019-v1/60000/0CE62FF6-D166-A442-A228-77F48E38BCC1.root',
       '/store/data/Run2016C/JetHT/NANOAOD/Nano1June2019-v1/60000/0E0EDEF4-BFE8-154A-A80D-7356DCD45169.root',
       '/store/data/Run2016C/JetHT/NANOAOD/Nano1June2019-v1/60000/120E79B0-6654-E347-8C51-B74C4A882CD7.root',
       '/store/data/Run2016C/JetHT/NANOAOD/Nano1June2019-v1/60000/282C052F-D7C9-0940-9C8E-187677F74EC0.root',
       '/store/data/Run2016C/JetHT/NANOAOD/Nano1June2019-v1/60000/2F399013-4DD0-1C4D-B222-C61BBACA2295.root',
       '/store/data/Run2016C/JetHT/NANOAOD/Nano1June2019-v1/60000/34E9E699-D975-FB43-A16F-A83AFF0A2CA2.root',
       '/store/data/Run2016C/JetHT/NANOAOD/Nano1June2019-v1/60000/3F97EC51-9DA3-174A-9118-FB48CB43BB04.root',
       '/store/data/Run2016C/JetHT/NANOAOD/Nano1June2019-v1/60000/4A006FAE-A867-2948-84E7-D22528D6EA58.root',
       '/store/data/Run2016C/JetHT/NANOAOD/Nano1June2019-v1/60000/5AD87A54-17C2-7E43-84B0-09EA80BF3BDD.root',
       '/store/data/Run2016C/JetHT/NANOAOD/Nano1June2019-v1/60000/5DAD5969-9288-6A40-B83A-2CF9B4E56306.root',
       '/store/data/Run2016C/JetHT/NANOAOD/Nano1June2019-v1/60000/5E12247F-D874-094A-86BE-1916A2A25158.root',
       '/store/data/Run2016C/JetHT/NANOAOD/Nano1June2019-v1/60000/6AB17256-8DD4-444C-B736-A604EA756B65.root',
       '/store/data/Run2016C/JetHT/NANOAOD/Nano1June2019-v1/60000/74B8D51B-A378-5048-92FB-67459B6110BC.root',
       '/store/data/Run2016C/JetHT/NANOAOD/Nano1June2019-v1/60000/82CE7EB9-2ED9-A441-8FF9-B99B1815E041.root',
       '/store/data/Run2016C/JetHT/NANOAOD/Nano1June2019-v1/60000/8654C528-3479-B44B-A8AA-E7624414D213.root',
       '/store/data/Run2016C/JetHT/NANOAOD/Nano1June2019-v1/60000/910727BA-1093-0343-B569-CD480F6CCC7F.root',
       '/store/data/Run2016C/JetHT/NANOAOD/Nano1June2019-v1/60000/99F4B09B-CB84-CD47-BAF3-F5CDC8E93740.root',
       '/store/data/Run2016C/JetHT/NANOAOD/Nano1June2019-v1/60000/9B4C2476-EC47-454D-BAB5-84BCAADDE435.root',
       '/store/data/Run2016C/JetHT/NANOAOD/Nano1June2019-v1/60000/A35713B4-4844-D54D-9787-CA34149BE339.root',
       '/store/data/Run2016C/JetHT/NANOAOD/Nano1June2019-v1/60000/A610A19B-7F42-854A-A5D2-4D00F4858E06.root',
       '/store/data/Run2016C/JetHT/NANOAOD/Nano1June2019-v1/60000/ACD40092-DBD0-8C45-9DCC-25D8AB720031.root',
       '/store/data/Run2016C/JetHT/NANOAOD/Nano1June2019-v1/60000/AD9CF2E8-FD46-2A45-A244-478A526E25D0.root',
       '/store/data/Run2016C/JetHT/NANOAOD/Nano1June2019-v1/60000/B25180FC-67A7-6348-B026-AB5F7933C9A7.root',
       '/store/data/Run2016C/JetHT/NANOAOD/Nano1June2019-v1/60000/B859C21A-D9BF-D142-8443-C66FEF560634.root',
       '/store/data/Run2016C/JetHT/NANOAOD/Nano1June2019-v1/60000/CE1CF1E8-7F3E-3A41-BA68-92C80FCE9D21.root',
       '/store/data/Run2016C/JetHT/NANOAOD/Nano1June2019-v1/60000/CE5D127D-BA22-C348-A82D-305D0A4C6C6D.root',
       '/store/data/Run2016C/JetHT/NANOAOD/Nano1June2019-v1/60000/D362FDE6-ADB8-FF41-BEF8-461D232ADEB3.root',
       '/store/data/Run2016C/JetHT/NANOAOD/Nano1June2019-v1/60000/D90D900F-F5CF-1244-BAA0-A9F6293D5E1A.root',
       '/store/data/Run2016C/JetHT/NANOAOD/Nano1June2019-v1/60000/DA04FD18-3C61-4443-A91B-D376D6582283.root',
       '/store/data/Run2016C/JetHT/NANOAOD/Nano1June2019-v1/60000/E24AC031-9256-EC46-B3AF-585AA4AEAC35.root',
       '/store/data/Run2016C/JetHT/NANOAOD/Nano1June2019-v1/60000/F4A4C397-E75A-C442-92D2-171271A3E46C.root',
       '/store/data/Run2016C/JetHT/NANOAOD/Nano1June2019-v1/60000/FCBD268E-F25A-8A45-AB52-503587A37EAC.root',
       '/store/data/Run2016C/JetHT/NANOAOD/Nano1June2019-v1/60000/FF003FB6-34DA-9244-AC59-4647FDA1672E.root',
] )
