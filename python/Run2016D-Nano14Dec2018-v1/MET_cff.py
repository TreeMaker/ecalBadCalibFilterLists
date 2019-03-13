import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016D/MET/NANOAOD/Nano14Dec2018-v1/280000/301A484B-5A64-A843-8D4D-D35993026206.root',
       '/store/data/Run2016D/MET/NANOAOD/Nano14Dec2018-v1/280000/3535B0C2-7EB4-4C47-8D7A-40B51FF05F17.root',
       '/store/data/Run2016D/MET/NANOAOD/Nano14Dec2018-v1/280000/55B44E4C-31C7-1C46-A37E-E29E6D9C1256.root',
       '/store/data/Run2016D/MET/NANOAOD/Nano14Dec2018-v1/280000/5617A94A-05FA-8341-AD40-AD204F4D13E2.root',
       '/store/data/Run2016D/MET/NANOAOD/Nano14Dec2018-v1/280000/5972A774-AAF2-D147-9C9C-041380D1B5E5.root',
       '/store/data/Run2016D/MET/NANOAOD/Nano14Dec2018-v1/280000/68005405-8077-BA46-8A60-DBA218B5338A.root',
       '/store/data/Run2016D/MET/NANOAOD/Nano14Dec2018-v1/280000/870EBE59-1C5E-AB47-A978-550C44407A2A.root',
       '/store/data/Run2016D/MET/NANOAOD/Nano14Dec2018-v1/280000/BC5A7E0C-6758-2F4A-8B56-3B15124AFB56.root',
       '/store/data/Run2016D/MET/NANOAOD/Nano14Dec2018-v1/280000/CCAA8A4F-1F8D-AB43-880D-78291DCF87A6.root',
       '/store/data/Run2016D/MET/NANOAOD/Nano14Dec2018-v1/280000/DEF27F0E-D1F7-EF4F-BC3F-6B59638623DF.root',
       '/store/data/Run2016D/MET/NANOAOD/Nano14Dec2018-v1/280000/E0979973-8569-6B44-850E-13C69B14EEBE.root',
       '/store/data/Run2016D/MET/NANOAOD/Nano14Dec2018-v1/280000/F6569AED-E6CE-1541-97CE-15AAD9593C8E.root',
] )
