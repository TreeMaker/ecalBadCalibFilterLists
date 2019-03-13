import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2017B/SingleElectron/NANOAOD/Nano14Dec2018-v1/20000/002E6B07-18B4-3F4B-908F-F308F712E853.root',
       '/store/data/Run2017B/SingleElectron/NANOAOD/Nano14Dec2018-v1/20000/019A5DE7-0A1D-1544-8B53-B1D18339DDD8.root',
       '/store/data/Run2017B/SingleElectron/NANOAOD/Nano14Dec2018-v1/20000/033020AA-CD9D-AE48-8D5E-318EDE7FA44A.root',
       '/store/data/Run2017B/SingleElectron/NANOAOD/Nano14Dec2018-v1/20000/0BC7F255-DB58-984D-B143-8FFC2425FAD9.root',
       '/store/data/Run2017B/SingleElectron/NANOAOD/Nano14Dec2018-v1/20000/1844E5A7-B3D9-4D4A-B278-0577DE012E40.root',
       '/store/data/Run2017B/SingleElectron/NANOAOD/Nano14Dec2018-v1/20000/2852A8EC-4165-8E46-8897-7FCFB97D66F8.root',
       '/store/data/Run2017B/SingleElectron/NANOAOD/Nano14Dec2018-v1/20000/2F692FE7-3162-7A47-8D50-9E40C2E4FE3A.root',
       '/store/data/Run2017B/SingleElectron/NANOAOD/Nano14Dec2018-v1/20000/32C0BC98-1CA3-0A45-8469-4C69D74FB96F.root',
       '/store/data/Run2017B/SingleElectron/NANOAOD/Nano14Dec2018-v1/20000/364D7C3C-8DA7-254B-BC4E-5043EB7513E5.root',
       '/store/data/Run2017B/SingleElectron/NANOAOD/Nano14Dec2018-v1/20000/4B449324-F87F-6D4D-A977-BBF841855E98.root',
       '/store/data/Run2017B/SingleElectron/NANOAOD/Nano14Dec2018-v1/20000/4B5F0E18-E8E3-2346-BBAD-AEA18F04D14D.root',
       '/store/data/Run2017B/SingleElectron/NANOAOD/Nano14Dec2018-v1/20000/54D8E67D-5B5E-6542-94F6-6FBD89A6D66F.root',
       '/store/data/Run2017B/SingleElectron/NANOAOD/Nano14Dec2018-v1/20000/56259908-929E-BA45-9BB6-5456350E3B10.root',
       '/store/data/Run2017B/SingleElectron/NANOAOD/Nano14Dec2018-v1/20000/5A4F4AB0-F3E3-464F-A457-751A52D18E9D.root',
       '/store/data/Run2017B/SingleElectron/NANOAOD/Nano14Dec2018-v1/20000/63FCDD49-6B75-7449-BD61-983FAD8F702A.root',
       '/store/data/Run2017B/SingleElectron/NANOAOD/Nano14Dec2018-v1/20000/729DA8F3-60FA-7B46-922D-B8AC6C62F277.root',
       '/store/data/Run2017B/SingleElectron/NANOAOD/Nano14Dec2018-v1/20000/791430DE-5105-B44D-81DF-8D764210E2C4.root',
       '/store/data/Run2017B/SingleElectron/NANOAOD/Nano14Dec2018-v1/20000/85F9C37F-9805-E246-A04D-C910D7E2F764.root',
       '/store/data/Run2017B/SingleElectron/NANOAOD/Nano14Dec2018-v1/20000/9D19FB14-4049-F34D-9C5C-B94A3E518D19.root',
       '/store/data/Run2017B/SingleElectron/NANOAOD/Nano14Dec2018-v1/20000/A8C9047D-14D5-C445-841B-14C30C6FCDA8.root',
       '/store/data/Run2017B/SingleElectron/NANOAOD/Nano14Dec2018-v1/20000/B317DF48-E7DC-CC41-BACF-001212F6AE45.root',
       '/store/data/Run2017B/SingleElectron/NANOAOD/Nano14Dec2018-v1/20000/C6AE9647-B4DA-AD4A-80B4-CFB86F56C7F4.root',
       '/store/data/Run2017B/SingleElectron/NANOAOD/Nano14Dec2018-v1/20000/C75F0DAB-52E9-1F49-836F-280600C789BC.root',
       '/store/data/Run2017B/SingleElectron/NANOAOD/Nano14Dec2018-v1/20000/D34D7EAC-50D9-134B-A1BD-C5B92A43A90A.root',
       '/store/data/Run2017B/SingleElectron/NANOAOD/Nano14Dec2018-v1/20000/D6BC55CC-0849-3D45-8376-DF514CC23440.root',
       '/store/data/Run2017B/SingleElectron/NANOAOD/Nano14Dec2018-v1/20000/DEBBAF02-FCF6-1A4C-B66F-E33FCBF153C1.root',
       '/store/data/Run2017B/SingleElectron/NANOAOD/Nano14Dec2018-v1/20000/E2655AFE-F9D0-4C4C-9AB4-59A7EB0DB2DE.root',
       '/store/data/Run2017B/SingleElectron/NANOAOD/Nano14Dec2018-v1/20000/F00367C2-7DFC-324D-9073-52E63BF71D17.root',
] )