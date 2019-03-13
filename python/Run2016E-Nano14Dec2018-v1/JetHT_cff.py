import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016E/JetHT/NANOAOD/Nano14Dec2018-v1/280000/024322E5-01BF-A142-816E-D30C743293C0.root',
       '/store/data/Run2016E/JetHT/NANOAOD/Nano14Dec2018-v1/280000/02B1867D-E9AA-2F4A-A2E5-FB31E576A876.root',
       '/store/data/Run2016E/JetHT/NANOAOD/Nano14Dec2018-v1/280000/0BABBD38-BA50-0747-90D8-D38886FD30C6.root',
       '/store/data/Run2016E/JetHT/NANOAOD/Nano14Dec2018-v1/280000/0CC1590F-0ECF-C346-850F-E259F3A7ACB4.root',
       '/store/data/Run2016E/JetHT/NANOAOD/Nano14Dec2018-v1/280000/0D73EA38-1747-6E41-AEEE-138587CBD3E0.root',
       '/store/data/Run2016E/JetHT/NANOAOD/Nano14Dec2018-v1/280000/0E1513E7-CEB2-6B42-9A75-6E86C0FB7A59.root',
       '/store/data/Run2016E/JetHT/NANOAOD/Nano14Dec2018-v1/280000/1AED98B0-E526-014F-B62D-7D38418AD96F.root',
       '/store/data/Run2016E/JetHT/NANOAOD/Nano14Dec2018-v1/280000/1D9C3686-BC6E-D341-8AAA-573D149214A0.root',
       '/store/data/Run2016E/JetHT/NANOAOD/Nano14Dec2018-v1/280000/1E4D6D46-FDAE-5349-840B-BC29865DFBC2.root',
       '/store/data/Run2016E/JetHT/NANOAOD/Nano14Dec2018-v1/280000/219AD916-AFC8-3B44-8AC4-EA8F0525E8F5.root',
       '/store/data/Run2016E/JetHT/NANOAOD/Nano14Dec2018-v1/280000/23DD5943-A6AA-F744-ABD3-532D269E4F37.root',
       '/store/data/Run2016E/JetHT/NANOAOD/Nano14Dec2018-v1/280000/26F7D46A-1F87-3E46-9534-CCDA324A38D2.root',
       '/store/data/Run2016E/JetHT/NANOAOD/Nano14Dec2018-v1/280000/27F67F73-C720-E444-B91C-E376AC86025D.root',
       '/store/data/Run2016E/JetHT/NANOAOD/Nano14Dec2018-v1/280000/2B6584D3-7BC8-394E-A18A-1DB8D36187E9.root',
       '/store/data/Run2016E/JetHT/NANOAOD/Nano14Dec2018-v1/280000/31726C81-ED3E-7048-B242-9F1DD9074AE0.root',
       '/store/data/Run2016E/JetHT/NANOAOD/Nano14Dec2018-v1/280000/3580EDA4-35EC-4745-B8D4-57FE70EB199A.root',
       '/store/data/Run2016E/JetHT/NANOAOD/Nano14Dec2018-v1/280000/38B9CA0B-4199-614B-929F-90F82C061EAC.root',
       '/store/data/Run2016E/JetHT/NANOAOD/Nano14Dec2018-v1/280000/4306A0DD-9F55-8340-BF47-5959DF670826.root',
       '/store/data/Run2016E/JetHT/NANOAOD/Nano14Dec2018-v1/280000/47CF3083-8818-AE40-B828-98F5BEFA2BB7.root',
       '/store/data/Run2016E/JetHT/NANOAOD/Nano14Dec2018-v1/280000/4895366B-2702-224C-9A96-7AEE16981AA7.root',
       '/store/data/Run2016E/JetHT/NANOAOD/Nano14Dec2018-v1/280000/48C479D6-A0EB-A342-8974-BF82C46F0959.root',
       '/store/data/Run2016E/JetHT/NANOAOD/Nano14Dec2018-v1/280000/5656D790-DE67-E64A-A528-3F5964BC1F49.root',
       '/store/data/Run2016E/JetHT/NANOAOD/Nano14Dec2018-v1/280000/6D53ED96-04B9-2545-A03E-7AFF04826C49.root',
       '/store/data/Run2016E/JetHT/NANOAOD/Nano14Dec2018-v1/280000/7495F237-D622-B94D-8E29-B9561A6DADE6.root',
       '/store/data/Run2016E/JetHT/NANOAOD/Nano14Dec2018-v1/280000/77DEA9D4-43BD-8F4E-99F5-DD1EF68B341B.root',
       '/store/data/Run2016E/JetHT/NANOAOD/Nano14Dec2018-v1/280000/7A876D95-F3B4-4540-9D79-121E0C5605C8.root',
       '/store/data/Run2016E/JetHT/NANOAOD/Nano14Dec2018-v1/280000/7FE2D130-401B-3148-8C13-D2418F483BB0.root',
       '/store/data/Run2016E/JetHT/NANOAOD/Nano14Dec2018-v1/280000/81673C42-0F4B-2B42-81D8-90856C0D3549.root',
       '/store/data/Run2016E/JetHT/NANOAOD/Nano14Dec2018-v1/280000/8E2C9B8A-AC6E-2C4D-A89D-405E49A03D94.root',
       '/store/data/Run2016E/JetHT/NANOAOD/Nano14Dec2018-v1/280000/8FEFF34A-56C1-BE46-AE8D-0985A9D56713.root',
       '/store/data/Run2016E/JetHT/NANOAOD/Nano14Dec2018-v1/280000/943E532F-2A7E-C349-AD61-41EC5C09C6CA.root',
       '/store/data/Run2016E/JetHT/NANOAOD/Nano14Dec2018-v1/280000/A060D389-EDE7-E646-AAD2-14763E101051.root',
       '/store/data/Run2016E/JetHT/NANOAOD/Nano14Dec2018-v1/280000/AB28C053-9C0C-B745-BCE6-2EAD61C187CD.root',
       '/store/data/Run2016E/JetHT/NANOAOD/Nano14Dec2018-v1/280000/AE9F786C-D55F-974B-B8FD-9D4A84348C54.root',
       '/store/data/Run2016E/JetHT/NANOAOD/Nano14Dec2018-v1/280000/B9D625E1-AAAA-3143-9877-909860DE750D.root',
       '/store/data/Run2016E/JetHT/NANOAOD/Nano14Dec2018-v1/280000/B9E5E9D4-7295-F04E-BD42-0B06B6732098.root',
       '/store/data/Run2016E/JetHT/NANOAOD/Nano14Dec2018-v1/280000/BA4D7610-4473-8940-9FC5-CE3573D0ED5C.root',
       '/store/data/Run2016E/JetHT/NANOAOD/Nano14Dec2018-v1/280000/BB572831-17E5-ED4E-A574-A03A7E293320.root',
       '/store/data/Run2016E/JetHT/NANOAOD/Nano14Dec2018-v1/280000/BDB29D71-2256-EC4E-9F88-7C47ED492265.root',
       '/store/data/Run2016E/JetHT/NANOAOD/Nano14Dec2018-v1/280000/C9D35493-E0E8-584D-9A6B-4F0C0FD33E06.root',
       '/store/data/Run2016E/JetHT/NANOAOD/Nano14Dec2018-v1/280000/CB15E974-1104-A045-8F11-AEFE23C35D3E.root',
       '/store/data/Run2016E/JetHT/NANOAOD/Nano14Dec2018-v1/280000/CF2796C1-BD9C-E142-8DEA-F720195360B1.root',
       '/store/data/Run2016E/JetHT/NANOAOD/Nano14Dec2018-v1/280000/D3E89488-1136-F44F-96AA-7E2F3E56082B.root',
       '/store/data/Run2016E/JetHT/NANOAOD/Nano14Dec2018-v1/280000/D6AC7634-297B-ED4A-A203-07C55B4DEE29.root',
       '/store/data/Run2016E/JetHT/NANOAOD/Nano14Dec2018-v1/280000/EF5FBE0D-DF33-054A-A08F-455183B4BE6B.root',
       '/store/data/Run2016E/JetHT/NANOAOD/Nano14Dec2018-v1/280000/F07057EA-6590-4B47-A9AE-8A59F4FEE71E.root',
       '/store/data/Run2016E/JetHT/NANOAOD/Nano14Dec2018-v1/280000/F0DE104B-E7BB-7E4A-BB31-78D462E6B6FD.root',
       '/store/data/Run2016E/JetHT/NANOAOD/Nano14Dec2018-v1/280000/F74A2A61-2748-C44E-93B8-FAEB9CCD9481.root',
       '/store/data/Run2016E/JetHT/NANOAOD/Nano14Dec2018-v1/280000/FB8D0501-546B-3942-994A-B271049C4B48.root',
       '/store/data/Run2016E/JetHT/NANOAOD/Nano14Dec2018-v1/280000/FE8F15E7-4D6D-5E4E-AB23-08A57A2ABB7E.root',
] )
