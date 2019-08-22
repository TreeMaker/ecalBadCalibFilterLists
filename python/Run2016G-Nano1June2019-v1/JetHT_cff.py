import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/230000/02D07222-7898-E44B-A11A-3E86489197AD.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/230000/0306E682-3F39-7549-91BB-75EE8C14C09D.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/230000/0984ED42-1330-8640-9106-0298B375B62E.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/230000/0EF3617C-B92E-6D46-B35E-948B1C5AD256.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/230000/0F9A9A7A-7DDA-D246-9EC4-6B37FA10B3D0.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/230000/108D6D99-B1BF-5743-A406-732D6F0AB1C2.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/230000/11E94218-C185-DA4D-AF8A-70F766F0864B.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/230000/1B417D6C-4037-9240-92C6-F4E3EAE1B6E3.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/230000/1C1007D1-3058-C94C-A069-D0478A60C95D.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/230000/1E6398C0-5DF0-1E45-858A-ADF1891B5CC7.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/230000/1E796019-8804-4E46-88C5-2EBD3F680252.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/230000/28E31F45-2773-9B48-A286-CC657709C53F.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/230000/2B82E30C-6A70-6944-A698-BC8A3E915FA4.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/230000/2DE05278-6EDB-9644-8D38-EC3B14EDE506.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/230000/30D9457F-C079-1547-B811-DF432EA19C1D.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/230000/32D57447-B70B-9743-9840-B0CCD24FBFA6.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/230000/33B5FD13-0918-A044-ADC1-1EDD2972F153.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/230000/34B0C2BD-9CD4-7D44-8A67-076A943CAB84.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/230000/3516EDEE-DD9F-8744-8801-3DF44199CCA5.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/230000/3C3E37A5-2EB8-2449-9370-0BE42AC95F84.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/230000/4021A883-83FB-2548-8C2C-D945B168AB13.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/230000/412DED4C-3586-F547-A5E5-6F9D41A24AF1.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/230000/4389C52C-4681-F943-96E1-8F56FADB3513.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/230000/4A3D4168-0709-B743-8B4F-9B6220F19D85.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/230000/4E6ECF59-F5CA-9E47-96D4-88369BBE61A4.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/230000/4F59E7C5-B1AF-494B-8FC5-4CE32C9C74EA.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/230000/516FB116-78A6-D042-A37B-98C5CE161220.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/230000/55631898-009C-0E48-9E42-593E0E91C9D7.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/230000/56D9B45B-6B5D-1440-BF16-BEE417F88D63.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/230000/5720E1D3-5C99-2B42-98D6-3C981DAE692C.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/230000/598CA3F7-99D9-0249-915B-B37B4FEC44FE.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/230000/5A600876-8808-B842-A7E1-0560F8E95639.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/230000/5CB91305-B7AF-814B-9607-7B2323B2D117.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/230000/5F9CFF82-6368-2242-918E-E16B277897AF.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/230000/60E85C03-37CD-E84B-8C6F-CBD37310EF10.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/230000/625C0E32-A4A3-A948-A913-D40D9771160A.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/230000/629FB3C2-DA96-534A-BBD3-6E738D935EA4.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/230000/692C5C56-7BCC-F549-8E88-39B8B30DD794.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/230000/6CB7EBDE-BA89-5F41-A393-C45599CD1354.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/230000/72C91BFC-773C-984A-9906-19F8F02361FC.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/230000/74255E65-A9E6-8640-B0D3-4F98EDA7CEA7.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/230000/7ADC3971-6A91-2649-A796-560BE9250A30.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/230000/7E1F4477-7123-9846-AA02-91EF43B5C9A2.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/230000/7E533BAD-42BE-2C41-84D6-9AB1F64BF3E1.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/230000/81A79A92-B956-2C4C-B3D2-CD7584C96FA0.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/230000/81E170DA-D127-6B47-ABB7-DC1A29FF1423.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/230000/897ED5BD-E614-F24D-BDBA-82B26D40DAE4.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/230000/8D8D8A43-D561-F34A-AB61-3BE7760CF73E.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/230000/8DCC55B0-3663-5045-B63F-9C0640CB2563.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/230000/93FAE684-8D2C-574D-8C64-E06B7F762D59.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/230000/951D9095-78EE-4E49-A32A-04D7671CCCA1.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/230000/971156D6-265D-0544-8A5A-B21BEEFB8100.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/230000/9C28D5CF-2307-5440-8BB4-ECF513928F0C.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/230000/9FF7013A-C0AF-4947-9B27-895BAD9C948C.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/230000/A2D9A190-AFF0-D249-94AA-7925FFB378DF.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/230000/A4D54E06-0508-914D-9A61-E7AA1D558810.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/230000/A67EA598-C529-9A4A-B1A4-8999E037F847.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/230000/AA3BC416-577A-B84C-BBC4-35430B8C9E12.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/230000/AF769A1C-70E8-6043-93CA-13FED7B46D5D.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/230000/B96A3458-70A4-B946-9D81-39EE0EB3A450.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/230000/C22EFF00-D9F4-C44E-B5F4-24D0C6E267A8.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/230000/C4063B33-D51B-D34E-B4C2-4F0991E00621.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/230000/C496B06C-F128-244F-BBAD-CBBE1C7DF9F1.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/230000/C8F16894-BBC6-AD40-A1CC-B924B5403521.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/230000/CA874F5C-0F16-3E43-99BA-88CB1C2658AD.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/230000/CE8048CE-C609-264F-84DE-01A3D953334D.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/230000/D5551499-F6F1-BA4D-82FA-386DFBA51B80.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/230000/DA38DE3C-1146-DB47-B9A9-0B0B8C9F24AD.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/230000/DBF35FDE-1801-D644-9CA5-F707C6250703.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/230000/DD343B60-0AA6-6241-9A0E-4B64870567CE.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/230000/E57965FD-E83F-AC40-A420-71B29D08C27D.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/230000/E81D2D93-149C-A245-82BB-72D9A174DCBF.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/230000/EBF42CF3-FC5F-AB4F-B927-6D13D550F9EE.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/230000/EC2BF60F-7987-F54C-AE8E-B733BEABB2F0.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/230000/EE82E7CB-3FB6-964B-B589-5F1DFAEF55F9.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/230000/EE8E300D-9577-6E46-9624-4C2303BE790B.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/230000/F4ECC9A1-8BD0-7943-B108-56E625CF711A.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/230000/F5B9834F-60D0-3A43-ADD8-BA01990F32C0.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/230000/F6A548A4-E390-FF4C-A5C8-CA94AB8557B7.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/230000/F8D1458C-5F05-BA47-A67E-4964745F8DD9.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/230000/FF746120-4BB3-2D44-B0F4-9153A4BF4E19.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/60000/3727A766-FCBF-2441-BB51-5954FD597BC6.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/60000/40E6DA6E-662A-D94F-8141-CF2789E391F6.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/60000/4C276CC5-E45A-4447-9EF0-FE762CE1B90D.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/60000/52C541E3-8C01-BC4D-A5EA-989C60A69A96.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/60000/64DAEA48-56CF-254D-A6AC-196F3963D007.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/60000/65E49D66-BF76-5A4A-9377-E5BE11695A61.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/60000/6D99055D-A5DF-F74B-B0C6-3A3065480140.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/60000/8426BF93-8D99-764B-A873-3780FC21DB2E.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/60000/AB1089F9-8E4B-B145-8ED4-10F27AFE0C98.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/60000/B78C33EA-7530-8542-9030-66C86B441BF6.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/60000/BA099264-5826-7F48-B14D-410F60401729.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/60000/BFD620CC-09E4-7746-9A27-08E8290726FE.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/60000/CE7DED8D-31A8-F849-AC08-440D0A88EEB4.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/60000/DF9A1B1F-50D4-1142-94F2-5B6BAB065C25.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/60000/E17BBB94-8D2D-7940-91D3-6B53F5948804.root',
       '/store/data/Run2016G/JetHT/NANOAOD/Nano1June2019-v1/60000/EC6A82E8-6198-1D46-93A4-3B451A26BEED.root',
] )