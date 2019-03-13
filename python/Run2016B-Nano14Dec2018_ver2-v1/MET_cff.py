import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016B_ver2/MET/NANOAOD/Nano14Dec2018_ver2-v1/80000/08283CB4-A23E-9847-AEC9-61264341D380.root',
       '/store/data/Run2016B_ver2/MET/NANOAOD/Nano14Dec2018_ver2-v1/80000/0AC2FBFE-3114-EA40-B947-76D3C8EC6432.root',
       '/store/data/Run2016B_ver2/MET/NANOAOD/Nano14Dec2018_ver2-v1/80000/1250DFE5-D121-E641-8196-74309CD4292D.root',
       '/store/data/Run2016B_ver2/MET/NANOAOD/Nano14Dec2018_ver2-v1/80000/23832E17-9AD3-4741-A1B6-7614C08B1622.root',
       '/store/data/Run2016B_ver2/MET/NANOAOD/Nano14Dec2018_ver2-v1/80000/3565EAEC-C55B-5447-8D6B-0BFDFFE1BAAA.root',
       '/store/data/Run2016B_ver2/MET/NANOAOD/Nano14Dec2018_ver2-v1/80000/394B0049-38A4-B944-8BA2-D5C5E83B948C.root',
       '/store/data/Run2016B_ver2/MET/NANOAOD/Nano14Dec2018_ver2-v1/80000/39F9BD96-7867-CA46-98EF-691D35AC8234.root',
       '/store/data/Run2016B_ver2/MET/NANOAOD/Nano14Dec2018_ver2-v1/80000/439295DF-8DC9-3E43-8529-03368869B40D.root',
       '/store/data/Run2016B_ver2/MET/NANOAOD/Nano14Dec2018_ver2-v1/80000/43FE334E-60DC-464B-882A-319E4907B9D5.root',
       '/store/data/Run2016B_ver2/MET/NANOAOD/Nano14Dec2018_ver2-v1/80000/4426B37B-DF8C-F149-8E6B-6902777CAA31.root',
       '/store/data/Run2016B_ver2/MET/NANOAOD/Nano14Dec2018_ver2-v1/80000/4A6A7DD5-AB0F-A640-9C11-194ED669387B.root',
       '/store/data/Run2016B_ver2/MET/NANOAOD/Nano14Dec2018_ver2-v1/80000/5389838A-64BE-A647-9F87-051A96F86DD3.root',
       '/store/data/Run2016B_ver2/MET/NANOAOD/Nano14Dec2018_ver2-v1/80000/6A14E727-0286-AF42-8A43-70F9C2EC36C6.root',
       '/store/data/Run2016B_ver2/MET/NANOAOD/Nano14Dec2018_ver2-v1/80000/7F63C1ED-ED27-C84C-BC73-54381B60F62E.root',
       '/store/data/Run2016B_ver2/MET/NANOAOD/Nano14Dec2018_ver2-v1/80000/8410579B-321B-8148-BA66-41A5FBABFE99.root',
       '/store/data/Run2016B_ver2/MET/NANOAOD/Nano14Dec2018_ver2-v1/80000/8E2CE53A-9022-104F-A18E-0CC9E8A66B18.root',
       '/store/data/Run2016B_ver2/MET/NANOAOD/Nano14Dec2018_ver2-v1/80000/935D78BB-5695-1440-BCD7-CC3CB79DF7CC.root',
       '/store/data/Run2016B_ver2/MET/NANOAOD/Nano14Dec2018_ver2-v1/80000/937993F4-8006-3347-AD42-ED3870997A7E.root',
       '/store/data/Run2016B_ver2/MET/NANOAOD/Nano14Dec2018_ver2-v1/80000/9FDB732D-A1F7-0D40-9B32-66C4A9699B61.root',
       '/store/data/Run2016B_ver2/MET/NANOAOD/Nano14Dec2018_ver2-v1/80000/A784C46F-96B6-4C44-A3CC-3EAC0504A653.root',
       '/store/data/Run2016B_ver2/MET/NANOAOD/Nano14Dec2018_ver2-v1/80000/CA8F251D-5669-8146-9FD3-815144D72BF9.root',
       '/store/data/Run2016B_ver2/MET/NANOAOD/Nano14Dec2018_ver2-v1/80000/CD0F76D4-44C6-7742-A060-C75E23889C4A.root',
       '/store/data/Run2016B_ver2/MET/NANOAOD/Nano14Dec2018_ver2-v1/80000/D0F8A5DC-6905-A440-8F28-68B26FA5E82E.root',
] )
