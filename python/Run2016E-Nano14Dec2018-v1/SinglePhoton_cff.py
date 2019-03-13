import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016E/SinglePhoton/NANOAOD/Nano14Dec2018-v1/10000/0880A7BE-037D-D64E-B98D-275D2A0A6DD2.root',
       '/store/data/Run2016E/SinglePhoton/NANOAOD/Nano14Dec2018-v1/10000/0C4DE5E4-A23B-9F46-BBCC-EDA0DF31E8D0.root',
       '/store/data/Run2016E/SinglePhoton/NANOAOD/Nano14Dec2018-v1/10000/1E8B76C5-4AAC-A848-8F45-781A82894551.root',
       '/store/data/Run2016E/SinglePhoton/NANOAOD/Nano14Dec2018-v1/10000/301817F2-BCD0-924B-B9A1-5A8DEA85DD8C.root',
       '/store/data/Run2016E/SinglePhoton/NANOAOD/Nano14Dec2018-v1/10000/419FC83C-D662-8A4E-8736-1BFFABD961AD.root',
       '/store/data/Run2016E/SinglePhoton/NANOAOD/Nano14Dec2018-v1/10000/4A085DF2-D012-AE45-9517-082C2422D1E0.root',
       '/store/data/Run2016E/SinglePhoton/NANOAOD/Nano14Dec2018-v1/10000/9594E745-BDC6-754D-ACE0-8B9E89788A3B.root',
       '/store/data/Run2016E/SinglePhoton/NANOAOD/Nano14Dec2018-v1/10000/E60BCB45-7159-A046-92C1-E961343859F2.root',
       '/store/data/Run2016E/SinglePhoton/NANOAOD/Nano14Dec2018-v1/90000/02D7CB8F-CB72-4841-8ABB-D0DA1609E843.root',
       '/store/data/Run2016E/SinglePhoton/NANOAOD/Nano14Dec2018-v1/90000/0847A992-761E-4441-A5FB-0102D3959CB3.root',
       '/store/data/Run2016E/SinglePhoton/NANOAOD/Nano14Dec2018-v1/90000/52753040-9036-224D-9A8B-050F2DB8AB45.root',
       '/store/data/Run2016E/SinglePhoton/NANOAOD/Nano14Dec2018-v1/90000/7FC4ACA4-A275-694A-835F-CC93BFAD2B69.root',
       '/store/data/Run2016E/SinglePhoton/NANOAOD/Nano14Dec2018-v1/90000/8E483086-9AF5-5841-BEAF-846888ED15A4.root',
       '/store/data/Run2016E/SinglePhoton/NANOAOD/Nano14Dec2018-v1/90000/AF7F3B72-078B-7243-B61C-B69D741A1A16.root',
       '/store/data/Run2016E/SinglePhoton/NANOAOD/Nano14Dec2018-v1/90000/B21F693D-A1B8-F64A-B33E-AA2DDA9FADB9.root',
       '/store/data/Run2016E/SinglePhoton/NANOAOD/Nano14Dec2018-v1/90000/BA1FABBC-3849-1F4D-BC46-F263656475FB.root',
       '/store/data/Run2016E/SinglePhoton/NANOAOD/Nano14Dec2018-v1/90000/DEA17978-1E84-BC45-8823-0163D0B9A37A.root',
       '/store/data/Run2016E/SinglePhoton/NANOAOD/Nano14Dec2018-v1/90000/E9C14023-843D-314A-9EF4-EAEB7B558552.root',
] )
