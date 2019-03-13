import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016D/JetHT/NANOAOD/Nano14Dec2018-v1/280000/0127A170-BF37-2340-8D77-28CAF0069AE3.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano14Dec2018-v1/280000/0752A022-F2B6-CC4D-AEBF-673B94B9AB9B.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano14Dec2018-v1/280000/0DBF0EC4-7145-6242-AC7E-8FAA607B76CE.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano14Dec2018-v1/280000/12EB8834-E199-234B-9A7C-29A57D179D03.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano14Dec2018-v1/280000/255901B2-1E00-E94D-8482-AF39AD6294DE.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano14Dec2018-v1/280000/293A3FCF-07AA-7E41-9957-073B591E45E4.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano14Dec2018-v1/280000/2D817BC3-A484-C641-A732-DCAB6E0DED30.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano14Dec2018-v1/280000/335B7BBC-6A84-0C44-840E-12BE546ADF1D.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano14Dec2018-v1/280000/38A1BF26-1503-1244-898E-A433AE46FC77.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano14Dec2018-v1/280000/3AE72A72-D0F3-924A-80E5-6887E140E33A.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano14Dec2018-v1/280000/3C9609A2-FDF4-3F48-964D-1B077B31B88A.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano14Dec2018-v1/280000/4608DDC4-490F-F344-AC40-FAF711E6EEDF.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano14Dec2018-v1/280000/4A5465E2-C97A-DE4A-AA12-A1D309282C60.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano14Dec2018-v1/280000/50C77CF7-C84A-DE43-88FF-447B923B1FA8.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano14Dec2018-v1/280000/5B2FB6CC-4444-FF48-8C6A-415BCBE8CC52.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano14Dec2018-v1/280000/5D57D1F0-5053-A242-93BE-F88659F5C6A1.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano14Dec2018-v1/280000/66D9591D-5CF6-0747-A37E-1E593614BC4C.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano14Dec2018-v1/280000/6738A807-E1C4-694E-9AF7-9FEA487B8F63.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano14Dec2018-v1/280000/6A967FA2-F1B4-424F-A297-8FC7ECA265A6.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano14Dec2018-v1/280000/6FDF3590-5632-AC4C-98D1-9170DBC9EBD3.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano14Dec2018-v1/280000/78320B37-F952-9A4A-94AE-89F2CC0F3FB9.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano14Dec2018-v1/280000/79EE251B-3196-FB4E-89EB-F4895B522CB7.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano14Dec2018-v1/280000/7C119897-2E6F-1947-9963-25F19B06CAA4.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano14Dec2018-v1/280000/857FCBBF-EE63-0F4A-832B-76C3B7034607.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano14Dec2018-v1/280000/986DBAE4-19BD-314E-A264-F3AFA97DDB6E.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano14Dec2018-v1/280000/996F0FD4-4C56-394E-AF2D-5D975ACB52B7.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano14Dec2018-v1/280000/A064C9DF-53A1-7E49-9C8C-F0C231CBEE31.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano14Dec2018-v1/280000/A305A1DC-1B4E-9244-B179-E8CB9593B057.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano14Dec2018-v1/280000/A49841E4-52BF-9D4C-90EA-6E796B142B8D.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano14Dec2018-v1/280000/A9857B5B-ACB2-674F-A3CF-C1BAC594192B.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano14Dec2018-v1/280000/C8D19FA5-FC9C-3E4A-920A-F8DD8C6E4335.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano14Dec2018-v1/280000/C9312A42-818A-3C47-BF46-47C4D509CB03.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano14Dec2018-v1/280000/CA808E7E-F796-414A-998E-990D9516107B.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano14Dec2018-v1/280000/CB83205B-A1FA-BA49-A44B-0F6AAADCFB98.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano14Dec2018-v1/280000/D0657EC2-5672-0B45-9C2F-93D16A77CB16.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano14Dec2018-v1/280000/D46FE702-C3D8-7D44-9B90-A7FC44730B26.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano14Dec2018-v1/280000/D84041DC-B742-9E4B-A528-7CBDA1D8E858.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano14Dec2018-v1/280000/DBE5EE5E-071B-3F40-88FF-3040898AC406.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano14Dec2018-v1/280000/E2E1F706-07A1-AC4A-8E9E-1E682206A473.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano14Dec2018-v1/280000/E404CD5C-E363-1F49-BAE6-270D67D76A39.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano14Dec2018-v1/280000/E56318C5-C1E6-EC48-A536-E1E4DF733387.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano14Dec2018-v1/280000/E87FB0B8-4C5A-AA45-A965-81D0F3BFCF2A.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano14Dec2018-v1/280000/EF8F49CB-9051-2748-82F5-430F68334690.root',
] )
