import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2017C/JetHT/NANOAOD/Nano14Dec2018-v1/00000/DA05CA1A-3265-EE47-84F9-10CB09D22BDA.root',
       '/store/data/Run2017C/JetHT/NANOAOD/Nano14Dec2018-v1/010000/1C558DED-09A5-5C45-B8BB-D37789B18011.root',
       '/store/data/Run2017C/JetHT/NANOAOD/Nano14Dec2018-v1/80000/0539F033-E39E-5348-B57E-F16A03FE0F79.root',
       '/store/data/Run2017C/JetHT/NANOAOD/Nano14Dec2018-v1/80000/0A3BB255-77BD-BF49-AEBD-53C229B5144C.root',
       '/store/data/Run2017C/JetHT/NANOAOD/Nano14Dec2018-v1/80000/115FDA78-56CC-AA44-BA66-53FACFF3FEDD.root',
       '/store/data/Run2017C/JetHT/NANOAOD/Nano14Dec2018-v1/80000/167601DA-69B0-5E49-9FAE-C8E1723B34FA.root',
       '/store/data/Run2017C/JetHT/NANOAOD/Nano14Dec2018-v1/80000/1EF5002F-E8CF-FD4D-9C86-127D141CA959.root',
       '/store/data/Run2017C/JetHT/NANOAOD/Nano14Dec2018-v1/80000/2295A64C-8B29-834C-903C-1926470528CD.root',
       '/store/data/Run2017C/JetHT/NANOAOD/Nano14Dec2018-v1/80000/244B3400-4E44-8C45-A68E-F10F6BF9E5B8.root',
       '/store/data/Run2017C/JetHT/NANOAOD/Nano14Dec2018-v1/80000/25DF8860-C198-2947-8BCB-60A43CCA34EF.root',
       '/store/data/Run2017C/JetHT/NANOAOD/Nano14Dec2018-v1/80000/2664F82A-B075-E64F-8428-A9DC94216FC6.root',
       '/store/data/Run2017C/JetHT/NANOAOD/Nano14Dec2018-v1/80000/349308C2-A9F7-F347-A1B7-B99E1BC4283E.root',
       '/store/data/Run2017C/JetHT/NANOAOD/Nano14Dec2018-v1/80000/42D77EE5-F1D7-D44F-92C3-B1EDF212BC3F.root',
       '/store/data/Run2017C/JetHT/NANOAOD/Nano14Dec2018-v1/80000/4763EFB1-F876-9C4B-ABC2-F19A4A9BC565.root',
       '/store/data/Run2017C/JetHT/NANOAOD/Nano14Dec2018-v1/80000/4C2D66D8-A6BA-804E-9BC5-5086CD28D2C3.root',
       '/store/data/Run2017C/JetHT/NANOAOD/Nano14Dec2018-v1/80000/504F98C2-68B7-EA4C-A715-613BE3EB479C.root',
       '/store/data/Run2017C/JetHT/NANOAOD/Nano14Dec2018-v1/80000/52F2A914-52CA-1049-9936-7D2BD5E4A336.root',
       '/store/data/Run2017C/JetHT/NANOAOD/Nano14Dec2018-v1/80000/55992F1E-BA6E-D34C-A283-ED2B325C23EE.root',
       '/store/data/Run2017C/JetHT/NANOAOD/Nano14Dec2018-v1/80000/56723BF3-AE94-3340-AF9E-10B12B840926.root',
       '/store/data/Run2017C/JetHT/NANOAOD/Nano14Dec2018-v1/80000/5773DBC7-8AC0-3141-B8DF-9DFC6C5A10C5.root',
       '/store/data/Run2017C/JetHT/NANOAOD/Nano14Dec2018-v1/80000/5905BD39-8D38-9B4C-AA6C-FA1C06032396.root',
       '/store/data/Run2017C/JetHT/NANOAOD/Nano14Dec2018-v1/80000/5A89063E-2C36-5B4A-8D4A-3EB8584A5E85.root',
       '/store/data/Run2017C/JetHT/NANOAOD/Nano14Dec2018-v1/80000/5D96FCEC-92CE-9E43-A71D-F0D9D92E1A36.root',
       '/store/data/Run2017C/JetHT/NANOAOD/Nano14Dec2018-v1/80000/60828D7D-B469-9E49-B781-F133B3EFAD8C.root',
       '/store/data/Run2017C/JetHT/NANOAOD/Nano14Dec2018-v1/80000/61221169-CF4E-CF4F-BA9C-AD167136229F.root',
       '/store/data/Run2017C/JetHT/NANOAOD/Nano14Dec2018-v1/80000/62C4B275-A219-DF4C-8303-FD59C372D6C0.root',
       '/store/data/Run2017C/JetHT/NANOAOD/Nano14Dec2018-v1/80000/67A8ACC8-2720-DD44-8972-F2F741DF236B.root',
       '/store/data/Run2017C/JetHT/NANOAOD/Nano14Dec2018-v1/80000/74BB2B17-59D3-6542-8AAE-D42AEAF8E98F.root',
       '/store/data/Run2017C/JetHT/NANOAOD/Nano14Dec2018-v1/80000/74CE4EB8-5848-C84C-A332-6C78AB9538AE.root',
       '/store/data/Run2017C/JetHT/NANOAOD/Nano14Dec2018-v1/80000/7C2B4812-1BF3-5B44-A8FF-33AAD95DE543.root',
       '/store/data/Run2017C/JetHT/NANOAOD/Nano14Dec2018-v1/80000/860337F6-2D68-3542-854A-D985C009C097.root',
       '/store/data/Run2017C/JetHT/NANOAOD/Nano14Dec2018-v1/80000/9171CC4B-05A5-2A42-9835-91A2F68EFDC2.root',
       '/store/data/Run2017C/JetHT/NANOAOD/Nano14Dec2018-v1/80000/9432DF77-0C08-F249-92D7-4A9F1D7A8306.root',
       '/store/data/Run2017C/JetHT/NANOAOD/Nano14Dec2018-v1/80000/94C9DB11-0D89-A645-83C3-2356C50D4B9E.root',
       '/store/data/Run2017C/JetHT/NANOAOD/Nano14Dec2018-v1/80000/9C9A9F2B-0B76-C248-A921-062D99D741D1.root',
       '/store/data/Run2017C/JetHT/NANOAOD/Nano14Dec2018-v1/80000/9D4C06B9-90C2-F249-A3FA-768F8AED964E.root',
       '/store/data/Run2017C/JetHT/NANOAOD/Nano14Dec2018-v1/80000/9E007CB6-6D5E-A345-A487-5385C8261C8D.root',
       '/store/data/Run2017C/JetHT/NANOAOD/Nano14Dec2018-v1/80000/A5B8F671-846B-DA40-A769-D68421866978.root',
       '/store/data/Run2017C/JetHT/NANOAOD/Nano14Dec2018-v1/80000/B56BFD23-FFDE-9743-8773-62BA19E2F3B0.root',
       '/store/data/Run2017C/JetHT/NANOAOD/Nano14Dec2018-v1/80000/BDEAC375-D3AB-0447-8244-EED7DAC989AC.root',
       '/store/data/Run2017C/JetHT/NANOAOD/Nano14Dec2018-v1/80000/BE63A5EE-9A67-DB4A-B657-6D3760929732.root',
       '/store/data/Run2017C/JetHT/NANOAOD/Nano14Dec2018-v1/80000/C56722CF-69C2-D54A-8725-96EB4D0F4461.root',
       '/store/data/Run2017C/JetHT/NANOAOD/Nano14Dec2018-v1/80000/C6F51AFB-F88E-104F-9A4A-0BDC7519A0FB.root',
       '/store/data/Run2017C/JetHT/NANOAOD/Nano14Dec2018-v1/80000/C75C075C-EA00-4344-913A-1AF3C2719EE3.root',
       '/store/data/Run2017C/JetHT/NANOAOD/Nano14Dec2018-v1/80000/CEC34CA4-6399-D24D-91B5-A21F76E37CF6.root',
       '/store/data/Run2017C/JetHT/NANOAOD/Nano14Dec2018-v1/80000/D670924F-E090-4B47-B5A4-3963DBF26650.root',
       '/store/data/Run2017C/JetHT/NANOAOD/Nano14Dec2018-v1/80000/D7156471-A1B1-5949-A71D-FA474A316E96.root',
       '/store/data/Run2017C/JetHT/NANOAOD/Nano14Dec2018-v1/80000/D80C21C8-6514-C140-BB62-41725BC1B230.root',
       '/store/data/Run2017C/JetHT/NANOAOD/Nano14Dec2018-v1/80000/DBA1FD53-DB12-A549-B7FB-C60CB652483C.root',
       '/store/data/Run2017C/JetHT/NANOAOD/Nano14Dec2018-v1/80000/DD68F730-31AB-B645-828E-A474EBDBEB57.root',
       '/store/data/Run2017C/JetHT/NANOAOD/Nano14Dec2018-v1/80000/E03AF15D-A67D-3640-BB7B-60BA60595C24.root',
       '/store/data/Run2017C/JetHT/NANOAOD/Nano14Dec2018-v1/80000/E3B580E1-1201-614E-8700-FDDA17F3ACAE.root',
       '/store/data/Run2017C/JetHT/NANOAOD/Nano14Dec2018-v1/80000/EC1084E1-7BC7-E349-B58A-3ADB05CC9067.root',
       '/store/data/Run2017C/JetHT/NANOAOD/Nano14Dec2018-v1/80000/EFCD7ED1-4E01-E346-82C7-2DB80C8F016A.root',
       '/store/data/Run2017C/JetHT/NANOAOD/Nano14Dec2018-v1/80000/F4343061-4202-7B4F-91C0-69FA5D10D064.root',
       '/store/data/Run2017C/JetHT/NANOAOD/Nano14Dec2018-v1/80000/F92E3A64-B3A8-5247-9E06-E4CC12AB2C6B.root',
       '/store/data/Run2017C/JetHT/NANOAOD/Nano14Dec2018-v1/80000/FA634BB9-271F-4B4E-8AAD-5DF99571650F.root',
] )
