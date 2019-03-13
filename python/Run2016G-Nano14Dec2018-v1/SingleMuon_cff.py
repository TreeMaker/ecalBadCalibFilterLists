import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016G/SingleMuon/NANOAOD/Nano14Dec2018-v1/00000/022775E5-F819-E647-A237-5D96FB4B8E8B.root',
       '/store/data/Run2016G/SingleMuon/NANOAOD/Nano14Dec2018-v1/00000/0CCB8217-3CA2-B140-8EE5-9C132E20D5F8.root',
       '/store/data/Run2016G/SingleMuon/NANOAOD/Nano14Dec2018-v1/00000/0F3A4128-BD03-1D40-9704-7148EB5BC097.root',
       '/store/data/Run2016G/SingleMuon/NANOAOD/Nano14Dec2018-v1/00000/19E7BC43-384E-864F-916D-5A01CB58A422.root',
       '/store/data/Run2016G/SingleMuon/NANOAOD/Nano14Dec2018-v1/00000/1EAF5A00-1E50-1645-9471-5ADFA3043AFA.root',
       '/store/data/Run2016G/SingleMuon/NANOAOD/Nano14Dec2018-v1/00000/23D0D8D5-9E35-8F42-86AF-F04E0B47995F.root',
       '/store/data/Run2016G/SingleMuon/NANOAOD/Nano14Dec2018-v1/00000/2715B28C-5627-4C46-9B79-B1824E562C69.root',
       '/store/data/Run2016G/SingleMuon/NANOAOD/Nano14Dec2018-v1/00000/39C12754-693A-1845-BC11-FB1C1B8022FF.root',
       '/store/data/Run2016G/SingleMuon/NANOAOD/Nano14Dec2018-v1/00000/3C200327-E52C-7C4E-858D-A0F7A7672F57.root',
       '/store/data/Run2016G/SingleMuon/NANOAOD/Nano14Dec2018-v1/00000/4C15338D-FB91-9E49-BFB1-C8EB8E00CA71.root',
       '/store/data/Run2016G/SingleMuon/NANOAOD/Nano14Dec2018-v1/00000/57E51EC1-15B2-AC46-9D69-32C4FAC9E94B.root',
       '/store/data/Run2016G/SingleMuon/NANOAOD/Nano14Dec2018-v1/00000/63F88827-1420-A14F-81A0-FC9CB239A1A0.root',
       '/store/data/Run2016G/SingleMuon/NANOAOD/Nano14Dec2018-v1/00000/66FDB3C0-882B-4946-B8BE-8D7740DDEB5F.root',
       '/store/data/Run2016G/SingleMuon/NANOAOD/Nano14Dec2018-v1/00000/81FB4E7C-2807-1C4C-8DE2-00F98FD8827B.root',
       '/store/data/Run2016G/SingleMuon/NANOAOD/Nano14Dec2018-v1/00000/8C6449E5-03B9-D442-9B77-CF1929BB2197.root',
       '/store/data/Run2016G/SingleMuon/NANOAOD/Nano14Dec2018-v1/00000/A3CA3FE9-E970-CA49-8643-3102F500E6A2.root',
       '/store/data/Run2016G/SingleMuon/NANOAOD/Nano14Dec2018-v1/00000/D156E983-511B-1A4E-907E-526EA040B2F6.root',
       '/store/data/Run2016G/SingleMuon/NANOAOD/Nano14Dec2018-v1/00000/E58692D2-D50E-6C43-81E8-C8D5781FCB17.root',
       '/store/data/Run2016G/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/03B52ADC-F35D-C94B-99F6-2192C4D45F6B.root',
       '/store/data/Run2016G/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/0CBD0ECE-30B0-EF4A-8BFA-FF141B256E41.root',
       '/store/data/Run2016G/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/0DA28331-8E1B-054B-AD35-098D3D7CE747.root',
       '/store/data/Run2016G/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/12E1DC03-542C-3A48-8231-D9647B8FD90E.root',
       '/store/data/Run2016G/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/1A1CE981-9464-2743-A855-C6FDC1A2315A.root',
       '/store/data/Run2016G/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/36616A4A-1B97-CC4E-A576-74F9229711B6.root',
       '/store/data/Run2016G/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/3836D8D0-445B-FE42-960C-C8D894D47F95.root',
       '/store/data/Run2016G/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/3ADF6073-C260-F74A-8766-D276B2AA4FD1.root',
       '/store/data/Run2016G/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/4018CC87-8996-334E-8120-A061A4F6C451.root',
       '/store/data/Run2016G/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/42B3E95B-611F-614A-80D4-EC0FB45FD470.root',
       '/store/data/Run2016G/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/43B6533D-9A48-0544-A488-DD4C071AA053.root',
       '/store/data/Run2016G/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/4BB6C0AB-D06C-5649-91C9-A78922FD2834.root',
       '/store/data/Run2016G/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/4BBB9D59-04A9-6241-9A92-C00B53E6D241.root',
       '/store/data/Run2016G/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/51C2A3C5-B693-924A-AD0D-8B3D562908B9.root',
       '/store/data/Run2016G/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/52CA65CE-3832-BE45-857E-145A157A923A.root',
       '/store/data/Run2016G/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/5F225E31-36B7-C442-B3F9-236AAD8EE9DC.root',
       '/store/data/Run2016G/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/64FC2602-22E9-B641-9A82-2FADCC7DCD45.root',
       '/store/data/Run2016G/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/683FF34A-68FD-444A-960A-B36640EF24B8.root',
       '/store/data/Run2016G/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/6D3D621A-6475-514C-AE9C-A5913CCEEC32.root',
       '/store/data/Run2016G/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/6DC751D7-A208-C648-B46A-F72D01EFF1A2.root',
       '/store/data/Run2016G/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/73A777C6-37FF-FD41-AA06-89A2F5C3D906.root',
       '/store/data/Run2016G/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/776B9220-466F-B84A-BCFF-53265E9CE079.root',
       '/store/data/Run2016G/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/78B5ABC0-4F67-BE43-96DD-B9F158127BB0.root',
       '/store/data/Run2016G/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/7A43720D-4589-EA42-B49A-089CF980BE97.root',
       '/store/data/Run2016G/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/98CE7791-5EF7-0143-8870-AF88D7BAF839.root',
       '/store/data/Run2016G/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/99852CAF-90F7-C44A-85B7-9308B60C2C3E.root',
       '/store/data/Run2016G/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/9B3D5F7C-46F2-AA41-8E16-F5A409176DF5.root',
       '/store/data/Run2016G/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/A5BC1BD6-BD30-1940-BCC5-D601C8817F08.root',
       '/store/data/Run2016G/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/A96D9E3A-7F5C-C443-BC95-53F1ECB1FD6B.root',
       '/store/data/Run2016G/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/AAC4466D-0EFC-554B-9889-FFEDCA83A3D0.root',
       '/store/data/Run2016G/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/AC99D058-E037-444D-8C3A-FDDBA67D6679.root',
       '/store/data/Run2016G/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/AEF745EF-F26E-C943-BF52-52C2C9378C84.root',
       '/store/data/Run2016G/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/B29FB28C-7403-1D48-904F-13C7255AF5AC.root',
       '/store/data/Run2016G/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/B9D6D9B0-C7F0-A04F-A350-3185904C7F12.root',
       '/store/data/Run2016G/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/C04FCD5E-5D90-5E45-B4B7-81D7B5F73A5C.root',
       '/store/data/Run2016G/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/C58EA529-71FA-BC4A-9987-164FB163C11F.root',
       '/store/data/Run2016G/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/CA38E49E-21B6-7246-9DE0-A00184677245.root',
       '/store/data/Run2016G/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/DA3E6EDE-7D33-0747-B400-891EF5578380.root',
       '/store/data/Run2016G/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/E5132DF2-2384-2443-991A-0156F397EE72.root',
       '/store/data/Run2016G/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/E70046B1-F06B-FE46-BD8C-827AF85057B9.root',
       '/store/data/Run2016G/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/EB923A65-3C53-FC47-AE37-A314FA57BD5C.root',
       '/store/data/Run2016G/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/EFB6DD81-9E6E-4A4F-9C52-1F49C8C7F2B0.root',
       '/store/data/Run2016G/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/F18A7D96-2E66-C14C-B702-31BF3CAFD266.root',
       '/store/data/Run2016G/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/F53A85B0-774C-8C48-8944-5A03FCEAE241.root',
       '/store/data/Run2016G/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/F9608436-2C37-6542-878F-B55FE764B8D1.root',
       '/store/data/Run2016G/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/FEDCA854-8ED4-C248-9177-6F70F8ED40E2.root',
       '/store/data/Run2016G/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/FFDBDC66-41F1-8048-985F-6C2B1184E0F8.root',
] )
