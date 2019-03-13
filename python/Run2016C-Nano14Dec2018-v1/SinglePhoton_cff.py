import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016C/SinglePhoton/NANOAOD/Nano14Dec2018-v1/10000/0060244A-DF76-0044-9BE1-EEA4E2F1A84A.root',
       '/store/data/Run2016C/SinglePhoton/NANOAOD/Nano14Dec2018-v1/10000/029E08EE-FDEC-4B44-B626-7C345544DEBF.root',
       '/store/data/Run2016C/SinglePhoton/NANOAOD/Nano14Dec2018-v1/10000/0763E13F-8F4C-CC43-A41D-E567D54AE3A5.root',
       '/store/data/Run2016C/SinglePhoton/NANOAOD/Nano14Dec2018-v1/10000/48D33F9E-3DCA-0449-9E30-DD7E8C67C29F.root',
       '/store/data/Run2016C/SinglePhoton/NANOAOD/Nano14Dec2018-v1/10000/56B8C534-88D7-0346-8E28-40B90ECEA231.root',
       '/store/data/Run2016C/SinglePhoton/NANOAOD/Nano14Dec2018-v1/10000/583AECE0-7287-E84F-B9B6-49CE28AA7E16.root',
       '/store/data/Run2016C/SinglePhoton/NANOAOD/Nano14Dec2018-v1/10000/60E832C1-D2A1-E447-8BD4-88387D93B509.root',
       '/store/data/Run2016C/SinglePhoton/NANOAOD/Nano14Dec2018-v1/10000/66416D00-FD32-BA4B-B90D-B6100FA5B3BF.root',
       '/store/data/Run2016C/SinglePhoton/NANOAOD/Nano14Dec2018-v1/10000/88E1C4D6-9643-6D47-AC2A-BF21FD593B06.root',
       '/store/data/Run2016C/SinglePhoton/NANOAOD/Nano14Dec2018-v1/10000/903EB923-29E1-924B-8C4A-DE1C0F4FF59D.root',
       '/store/data/Run2016C/SinglePhoton/NANOAOD/Nano14Dec2018-v1/10000/90DB77B2-F6EE-9E49-81D8-E98D2E964F7B.root',
       '/store/data/Run2016C/SinglePhoton/NANOAOD/Nano14Dec2018-v1/10000/A5195D65-9C05-7F46-AA80-17A4DA0BF318.root',
       '/store/data/Run2016C/SinglePhoton/NANOAOD/Nano14Dec2018-v1/10000/C477D3B6-835C-474E-99EE-5890F9B00307.root',
       '/store/data/Run2016C/SinglePhoton/NANOAOD/Nano14Dec2018-v1/10000/C8D56AD8-40B2-6744-9AB6-7689AEEA9B39.root',
       '/store/data/Run2016C/SinglePhoton/NANOAOD/Nano14Dec2018-v1/10000/CF46075D-7BFF-5C46-8F97-4141032FCDDF.root',
       '/store/data/Run2016C/SinglePhoton/NANOAOD/Nano14Dec2018-v1/10000/E4BCFB1A-0C27-234F-AFB7-9B123FD3F21C.root',
] )
