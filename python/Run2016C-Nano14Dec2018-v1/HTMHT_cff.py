import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016C/HTMHT/NANOAOD/Nano14Dec2018-v1/10000/00337A2D-90A7-F042-8F95-F6563CCEDD50.root',
       '/store/data/Run2016C/HTMHT/NANOAOD/Nano14Dec2018-v1/10000/2B4430D4-2667-F349-921C-9176F4B1456B.root',
       '/store/data/Run2016C/HTMHT/NANOAOD/Nano14Dec2018-v1/10000/2F76B519-D50B-5546-B26F-444A1A344FA0.root',
       '/store/data/Run2016C/HTMHT/NANOAOD/Nano14Dec2018-v1/10000/39B1B097-E92F-BA41-B049-76EE932BFFBC.root',
       '/store/data/Run2016C/HTMHT/NANOAOD/Nano14Dec2018-v1/10000/3B8BEDE4-DE84-7240-8F8D-F64D46336F02.root',
       '/store/data/Run2016C/HTMHT/NANOAOD/Nano14Dec2018-v1/10000/43E263A4-96EE-CB49-A322-EAF5F0624186.root',
       '/store/data/Run2016C/HTMHT/NANOAOD/Nano14Dec2018-v1/10000/570906FE-D095-DB49-B381-8943D7FA49DF.root',
       '/store/data/Run2016C/HTMHT/NANOAOD/Nano14Dec2018-v1/10000/6E4F85A6-0B0D-1B41-960E-1CAB12C61AD4.root',
       '/store/data/Run2016C/HTMHT/NANOAOD/Nano14Dec2018-v1/10000/74E7BB5E-2F65-9547-BC33-437916FB4528.root',
       '/store/data/Run2016C/HTMHT/NANOAOD/Nano14Dec2018-v1/10000/7749FE49-C23C-4048-8ECC-4D24A0C98DA3.root',
       '/store/data/Run2016C/HTMHT/NANOAOD/Nano14Dec2018-v1/10000/81331C09-EEDE-DD4A-B772-EF65F2CD5FA0.root',
       '/store/data/Run2016C/HTMHT/NANOAOD/Nano14Dec2018-v1/10000/980FFC64-265A-1747-8E36-F032B4E75106.root',
       '/store/data/Run2016C/HTMHT/NANOAOD/Nano14Dec2018-v1/10000/A0F91C36-067B-E444-A496-8D2E238B6351.root',
       '/store/data/Run2016C/HTMHT/NANOAOD/Nano14Dec2018-v1/10000/BE3DB6F8-F7B0-ED41-AD30-FF146AA0C1CE.root',
       '/store/data/Run2016C/HTMHT/NANOAOD/Nano14Dec2018-v1/10000/E218C074-641F-9743-A663-70B789852601.root',
       '/store/data/Run2016C/HTMHT/NANOAOD/Nano14Dec2018-v1/10000/F4551B17-9B22-5B47-BE23-215806A1688B.root',
       '/store/data/Run2016C/HTMHT/NANOAOD/Nano14Dec2018-v1/80000/27E9B5FB-7356-4945-ACDD-D2B62CD7BE70.root',
       '/store/data/Run2016C/HTMHT/NANOAOD/Nano14Dec2018-v1/80000/5937E1D7-BE23-CD4F-8D1A-8962DA2ACE0B.root',
       '/store/data/Run2016C/HTMHT/NANOAOD/Nano14Dec2018-v1/80000/BA71525C-64F3-8E46-B217-33064EEBF55B.root',
] )
