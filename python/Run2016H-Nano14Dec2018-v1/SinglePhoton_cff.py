import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016H/SinglePhoton/NANOAOD/Nano14Dec2018-v1/280000/1132EE38-DC03-D24A-8436-FF652FFBB12E.root',
       '/store/data/Run2016H/SinglePhoton/NANOAOD/Nano14Dec2018-v1/280000/1704C5F0-3BC6-B94A-9A27-31507F9206F4.root',
       '/store/data/Run2016H/SinglePhoton/NANOAOD/Nano14Dec2018-v1/280000/1DC5E5F1-566A-4B4B-B13E-920A9FB483BD.root',
       '/store/data/Run2016H/SinglePhoton/NANOAOD/Nano14Dec2018-v1/280000/2D42148B-CA15-4846-978A-E8C1DDEBDA73.root',
       '/store/data/Run2016H/SinglePhoton/NANOAOD/Nano14Dec2018-v1/280000/2D77CB7D-697F-4440-82FE-04C833885836.root',
       '/store/data/Run2016H/SinglePhoton/NANOAOD/Nano14Dec2018-v1/280000/347E3DD7-8FE3-804D-A7CD-75629859B4C4.root',
       '/store/data/Run2016H/SinglePhoton/NANOAOD/Nano14Dec2018-v1/280000/4D693494-3158-B742-ACFA-CE3C139163B4.root',
       '/store/data/Run2016H/SinglePhoton/NANOAOD/Nano14Dec2018-v1/280000/61C4EF8D-0B4E-674E-A92A-88565897CFC9.root',
       '/store/data/Run2016H/SinglePhoton/NANOAOD/Nano14Dec2018-v1/280000/67039242-3A2A-A148-9D3E-C4C3F43CADE0.root',
       '/store/data/Run2016H/SinglePhoton/NANOAOD/Nano14Dec2018-v1/280000/6C2A04EE-F154-3345-92B4-7A3AF28168CC.root',
       '/store/data/Run2016H/SinglePhoton/NANOAOD/Nano14Dec2018-v1/280000/874FAE40-BE56-B242-8028-2CDB2CB5127E.root',
       '/store/data/Run2016H/SinglePhoton/NANOAOD/Nano14Dec2018-v1/280000/8BC64935-7C06-5943-98C4-DA460A6048A4.root',
       '/store/data/Run2016H/SinglePhoton/NANOAOD/Nano14Dec2018-v1/280000/995ADBCF-2D72-574C-B274-2A726A627504.root',
       '/store/data/Run2016H/SinglePhoton/NANOAOD/Nano14Dec2018-v1/280000/9CEE36E4-1843-8D4E-9FFE-B0369E5D3E43.root',
       '/store/data/Run2016H/SinglePhoton/NANOAOD/Nano14Dec2018-v1/280000/AEEC4C07-BE1C-D445-9F94-180A5D34D218.root',
       '/store/data/Run2016H/SinglePhoton/NANOAOD/Nano14Dec2018-v1/280000/B044C40E-8E02-8949-B36B-1E72DC5706E6.root',
       '/store/data/Run2016H/SinglePhoton/NANOAOD/Nano14Dec2018-v1/280000/B5710233-8DD6-DB4B-9F3A-B3622351D9E7.root',
       '/store/data/Run2016H/SinglePhoton/NANOAOD/Nano14Dec2018-v1/280000/D361645D-71A7-4B44-8936-C184F3F0DE57.root',
       '/store/data/Run2016H/SinglePhoton/NANOAOD/Nano14Dec2018-v1/280000/E7B67E0C-973F-CE46-8D43-881736A203CE.root',
       '/store/data/Run2016H/SinglePhoton/NANOAOD/Nano14Dec2018-v1/280000/E8904984-3647-4F42-8150-F19BE3CFFAFA.root',
       '/store/data/Run2016H/SinglePhoton/NANOAOD/Nano14Dec2018-v1/280000/FBC5727D-FFA3-FE4C-92E8-C4EA08EE80BF.root',
       '/store/data/Run2016H/SinglePhoton/NANOAOD/Nano14Dec2018-v1/280000/FFE66CE8-2B6B-0044-845B-D93AA2D7C876.root',
] )
