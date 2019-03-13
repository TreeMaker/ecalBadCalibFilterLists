import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2017F/SinglePhoton/NANOAOD/Nano14Dec2018-v1/80000/0BE48600-F33A-DD49-9E90-32D3E56CC708.root',
       '/store/data/Run2017F/SinglePhoton/NANOAOD/Nano14Dec2018-v1/80000/23248339-67ED-C74F-B109-CCAA59F7D05C.root',
       '/store/data/Run2017F/SinglePhoton/NANOAOD/Nano14Dec2018-v1/80000/3928A6E2-9960-4B4A-B5EF-816553EC2A57.root',
       '/store/data/Run2017F/SinglePhoton/NANOAOD/Nano14Dec2018-v1/80000/4CDB7212-2CBD-B240-968A-11A4F5B6F082.root',
       '/store/data/Run2017F/SinglePhoton/NANOAOD/Nano14Dec2018-v1/80000/4F81516E-29F8-B241-86F9-3A16FF5C1AA0.root',
       '/store/data/Run2017F/SinglePhoton/NANOAOD/Nano14Dec2018-v1/80000/53AA211D-9735-4A44-A535-6C90FEAEA2B3.root',
       '/store/data/Run2017F/SinglePhoton/NANOAOD/Nano14Dec2018-v1/80000/5C71C834-01C4-E64B-92AD-F28D66B165FE.root',
       '/store/data/Run2017F/SinglePhoton/NANOAOD/Nano14Dec2018-v1/80000/64FAF3CB-7027-2F46-B55A-95C01019FA0A.root',
       '/store/data/Run2017F/SinglePhoton/NANOAOD/Nano14Dec2018-v1/80000/8E820F1D-20CA-D148-B6CA-8241A4F58AA9.root',
       '/store/data/Run2017F/SinglePhoton/NANOAOD/Nano14Dec2018-v1/80000/8E90E2E4-42D4-734B-B931-018CE33F64C1.root',
       '/store/data/Run2017F/SinglePhoton/NANOAOD/Nano14Dec2018-v1/80000/8FD9338C-469A-BA4B-AC59-13CAFCDFC114.root',
       '/store/data/Run2017F/SinglePhoton/NANOAOD/Nano14Dec2018-v1/80000/94C05E9D-36F8-4C46-84EF-21F3C71E5D51.root',
       '/store/data/Run2017F/SinglePhoton/NANOAOD/Nano14Dec2018-v1/80000/A203B86B-3AFC-BD46-8FB5-E743AE6E566B.root',
       '/store/data/Run2017F/SinglePhoton/NANOAOD/Nano14Dec2018-v1/80000/B2BBDE22-5E00-2E47-9693-6B5527EEC4D4.root',
       '/store/data/Run2017F/SinglePhoton/NANOAOD/Nano14Dec2018-v1/80000/B4999B2A-25B9-CE44-9B22-E0E84A7DBF6F.root',
       '/store/data/Run2017F/SinglePhoton/NANOAOD/Nano14Dec2018-v1/80000/C0A6DA9F-9B93-0A4C-974B-4966D25FBF9C.root',
       '/store/data/Run2017F/SinglePhoton/NANOAOD/Nano14Dec2018-v1/80000/C285FF7F-6D55-3F45-B478-15EF6B671DF5.root',
       '/store/data/Run2017F/SinglePhoton/NANOAOD/Nano14Dec2018-v1/80000/C41F9028-2054-964A-8EB9-216440B8C420.root',
       '/store/data/Run2017F/SinglePhoton/NANOAOD/Nano14Dec2018-v1/80000/D64F38DB-1D7E-9E4A-BFC8-0A9561FD4EE5.root',
       '/store/data/Run2017F/SinglePhoton/NANOAOD/Nano14Dec2018-v1/80000/E583DD23-354F-9146-A97B-1D3FD25097EC.root',
       '/store/data/Run2017F/SinglePhoton/NANOAOD/Nano14Dec2018-v1/80000/EC248602-4132-3345-A2EF-F1F02639A688.root',
] )
