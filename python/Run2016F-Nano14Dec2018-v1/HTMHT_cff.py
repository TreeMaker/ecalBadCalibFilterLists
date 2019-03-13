import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016F/HTMHT/NANOAOD/Nano14Dec2018-v1/90000/268C6F89-2230-1B4A-B227-2FB11C15C3CE.root',
       '/store/data/Run2016F/HTMHT/NANOAOD/Nano14Dec2018-v1/90000/2951949F-05CD-2341-8DC8-14C949304743.root',
       '/store/data/Run2016F/HTMHT/NANOAOD/Nano14Dec2018-v1/90000/31C73027-DDDF-DA4B-A824-1233FA6A498A.root',
       '/store/data/Run2016F/HTMHT/NANOAOD/Nano14Dec2018-v1/90000/414321D9-508D-0D42-A352-DA59E34EDD50.root',
       '/store/data/Run2016F/HTMHT/NANOAOD/Nano14Dec2018-v1/90000/47ECC24E-8031-254A-B1D5-28B25C71F2D9.root',
       '/store/data/Run2016F/HTMHT/NANOAOD/Nano14Dec2018-v1/90000/C704D288-86B1-AB45-ABA7-A53E82E8D262.root',
       '/store/data/Run2016F/HTMHT/NANOAOD/Nano14Dec2018-v1/90000/E20B75B1-E4B4-6E4A-9CD0-A2FC11444B20.root',
       '/store/data/Run2016F/HTMHT/NANOAOD/Nano14Dec2018-v1/90000/EDA11A7F-39E9-254F-9F29-376530291AC8.root',
       '/store/data/Run2016F/HTMHT/NANOAOD/Nano14Dec2018-v1/90000/FDFA5CAD-7285-DA4A-AB5F-409097E46830.root',
] )
