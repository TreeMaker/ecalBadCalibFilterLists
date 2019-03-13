import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/30000/00152E7A-D414-4040-9146-33F524941D86.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/30000/08209A2F-AFE6-5E41-85EE-C3F0349E6E15.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/30000/0D943F2D-C6D8-4946-AF5A-58EB63578675.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/30000/106907BB-9FEF-D747-B3DA-2682E8254D12.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/30000/150FC9F7-CA39-AA4E-B235-FC65F7F2F0DA.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/30000/183CD968-721F-6542-B314-B978296327BE.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/30000/18AA7F92-9A51-3C48-9A3E-46137575C405.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/30000/19270745-4B25-1440-90F8-96B47A2FA4CE.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/30000/1C3502E3-8066-AC44-A765-6A2144C524B0.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/30000/3C47267D-635A-8D46-8DE7-86420584BFD1.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/30000/3DDB8BDD-CF80-3142-9F06-8602A487FA08.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/30000/4BF92D98-C73E-2544-A1A5-8990707EA7E3.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/30000/57EFC378-EB96-2349-9BB1-99DA821056D2.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/30000/60016101-5033-DF45-80A8-9DF4880378BD.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/30000/6C7AA37D-2087-B74B-8684-DD3A78D406D5.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/30000/73E18089-67FD-5249-BA2D-8519FF7CEADD.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/30000/7453C59B-6C68-4549-920A-4216BB47E370.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/30000/7CAB25E1-7477-AC41-BD2B-F525E99D3223.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/30000/80544D5C-16FA-7544-A71A-552A0124801B.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/30000/86CB90B3-D9A5-5241-B4C0-3B57A54D8D8B.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/30000/A4F7BF07-68DC-A54C-AD58-2B5F3AFE1448.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/30000/BB0D753F-4B2E-874C-A019-5C4DA3A7000D.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/30000/C90DE886-D3DF-4446-AEC0-995A6FC3BB3E.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/30000/CCE2C90F-5B83-0444-B6CB-56B4712C7022.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/30000/D3CA3574-302F-E24E-BC4D-C418FA13E1AF.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/30000/D3EB6A7D-9800-D246-BF8A-ABB4E04801A4.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/30000/DC4F31DA-4509-324E-9101-65877B9B9D26.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/30000/DC974084-48BC-3143-9B9F-CBB6A19686EB.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/30000/DF556286-6C8D-CA45-AE89-27E04724805D.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/30000/DFAB3695-B2C0-8747-9E9F-AB8159B2365C.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/30000/E0C4A7AD-B139-074E-B9C1-B5002CF5A124.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/30000/E19F9F73-DCCF-304B-832A-555071081718.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/30000/E1A89806-5AC9-8447-BF0D-2CB69ED9F02D.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/30000/E8ED23BE-2E48-BD48-B130-FFED7CBCBB90.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/30000/F0CAF010-9844-2845-BA11-1E3BB9AB56E5.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/30000/F9CE8D22-F1DF-8B4A-BA6A-3131F80E2D33.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/30000/FFAB05AB-894D-C749-94AF-5AEAC628C651.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/50000/05CB668C-3E2F-F34B-8278-25A0E4E97008.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/50000/084EC3F5-AF33-DE47-B8A4-B0A4F04377CA.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/50000/0F296D19-9ED1-4542-839E-1D5FDA97EC89.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/50000/177B20FE-BBD3-BF42-852C-B143199DACC6.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/50000/1B0CC167-F630-F144-B32E-CFF5D89793CE.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/50000/27DDCC35-2658-6D4D-A67E-6AFDC04CBFA6.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/50000/2BC493D7-9ACC-E447-B308-B492E33847CF.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/50000/2D138E1E-4FF6-2443-B0A0-F042A2A2C8D5.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/50000/3010ED1F-09A6-B34D-9493-397E4327C6AF.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/50000/31FC36B4-D54A-9B4D-8BA2-1D313D4C57B3.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/50000/3219AADB-810D-9F41-9FD1-868110D49692.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/50000/3C2C6BD3-72CE-DD4A-A1A5-28543D7AE88E.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/50000/4999E714-1630-AB48-A259-B7E11250F088.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/50000/4B50DE4C-BE1A-394E-9F09-C70B817F7700.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/50000/53DDD0D2-FBB1-A549-B523-547FC122400F.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/50000/5C7A6F67-1837-5B40-B478-BB9704267D6D.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/50000/61BEE1EF-EBC9-564C-9353-44465D576362.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/50000/6EDA0EB7-A186-9142-A13D-3FAD2913B44B.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/50000/6FC9B1F5-8E51-BB46-8B6D-88DF5A0C5902.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/50000/72A4C264-E621-E749-881F-609BD4B3912C.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/50000/731C7FB8-E31B-934F-8EAD-6E7D24819923.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/50000/761208D0-A5F9-3D4F-8EC9-81D6094B6144.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/50000/7BAC9971-3EA3-324D-BC74-926C2E733CFE.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/50000/7CC34E72-D20F-C84B-B079-DA00530D7D68.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/50000/8A1FA784-3602-934D-B713-D4644CA0974F.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/50000/8FABDC8F-5483-2146-9075-9796482AFA59.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/50000/9171E778-AF52-F24C-ADA9-0DD5AE116176.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/50000/925E83F1-8E86-8343-9634-DDCBE1BBDB6C.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/50000/943876ED-063A-AE4C-9E89-F1E1BF411B2A.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/50000/94F6CB11-A65F-5342-94A4-58E38F417446.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/50000/A16BE4BC-8959-3A4A-9C89-45EC08332039.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/50000/A47502D8-3D4A-F944-BC97-88AEBDA95C56.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/50000/A984781B-08C8-424D-8115-27C81637E0FB.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/50000/AF5C5A4B-CE88-F04C-B83E-8C285D3569C4.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/50000/BBC82407-AA34-4444-B853-DB96880781D7.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/50000/BCD6293C-6A30-6B45-A9E0-3AC879623758.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/50000/C0586AC8-7A40-1D47-B59C-567EDE4488AE.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/50000/C1B69882-0C08-BB4B-8F6E-E9CB0F8DD725.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/50000/C1D80077-F787-B64A-96F5-5A6006664C2D.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/50000/C60AC93B-D6F2-EC4B-AFED-00D97355606D.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/50000/C7E155AD-9384-214A-96F0-3D2FA973B788.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/50000/CE1DC5C2-4AF2-D245-A7EF-B542E84D127F.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/50000/CFE8DF92-F907-5146-847C-6108177FC81F.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/50000/D13146FD-EC07-D743-94B4-8EA33259E615.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/50000/D4221CD4-AF10-6948-A8CD-B31B726218F3.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/50000/D8D9A974-B460-5F40-8572-FC791C7287E7.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/50000/D9D72461-71AF-9242-8E73-887BFFFFA88E.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/50000/DB372ACF-BC0E-874E-B9DB-93C10AF9A4FB.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/50000/DD4D906C-84F4-E249-AB31-3476BAB2BD37.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/50000/DF78BAD8-3E89-AB48-B7BE-6B4885CDE202.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/50000/E3DB9745-A96D-9C41-90C7-DA832F3E217E.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/50000/E4C9B6E3-5388-9946-A622-2944C17BE571.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/50000/E5A52A05-C696-824F-9E01-B4ECA8B82408.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/50000/E7435056-BC76-BF48-97C9-3865CB75BCE8.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/50000/E7FF1A9E-E2D6-8D42-A0F5-5E09B9744C7D.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/50000/F5D58FC2-3196-7341-86A2-2508C38C26CB.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/50000/FBC9084A-37F3-2E40-B286-EC4112763612.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/90000/05936A38-CB51-0942-BCE4-C2B9AC4BF60F.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/90000/06CE8991-2E61-F645-9D6B-81E903F3764E.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/90000/129F19D1-FAC4-5040-AE03-A2465957E029.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/90000/130CB8F8-0681-7B49-A6F6-150418DE2515.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/90000/1F63EDEA-E7E3-2B4B-8C92-9F5E16D2E8B8.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/90000/372C8DD9-3E73-A448-ACE1-FC16D1D99B1C.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/90000/4A37602C-3C74-C747-8E37-3563CD7D31E7.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/90000/5FB4EB1E-3AE1-1241-80EA-77BC0665C93B.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/90000/675CEBB3-CBA8-6643-BF40-1399ABC02702.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/90000/6C4D633A-6554-7A4C-B4F8-2B41CF02B745.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/90000/70E94218-1DAE-6247-BD88-988536829B9E.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/90000/723281BB-C735-6146-A72A-258F4BECAFB3.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/90000/7845CF05-E363-C540-B007-2BBF25ACBC9D.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/90000/7CC38E63-0E4E-0A41-A463-47A667B1F1C3.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/90000/7F1D5BC3-12C9-FF4E-A321-E8E0AD792F5D.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/90000/8402A45F-24A9-BC47-8EBF-FC83CD113309.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/90000/94DF6032-6742-BB4A-8121-1AA1648B40F8.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/90000/A11C3516-66EE-AB43-A0AC-264B2BFECEE8.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/90000/B5D7B249-65E4-4B43-8F7B-078F451C19E6.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/90000/DA117A86-EDA1-F848-9858-D94D1C7B9C75.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/90000/DB614255-881B-E647-9FC8-43F2043F5030.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/90000/E49B316A-D28B-E64E-B04A-2EC0EE3B572B.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/90000/E6A05F54-7F9D-A543-A0E8-6006D27A0403.root',
       '/store/data/Run2018C/EGamma/NANOAOD/Nano14Dec2018-v1/90000/FBE34E52-5F03-1D41-BD2C-C8A9FFCACF52.root',
] )
