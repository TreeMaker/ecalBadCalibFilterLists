import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2017B/HTMHT/NANOAOD/Nano14Dec2018-v1/20000/3BDBC62F-7FEC-3A48-B09D-0E3D9B837F2B.root',
       '/store/data/Run2017B/HTMHT/NANOAOD/Nano14Dec2018-v1/20000/7643D6B1-813A-8E43-910F-5C9C15A7F9E5.root',
       '/store/data/Run2017B/HTMHT/NANOAOD/Nano14Dec2018-v1/20000/94C14A97-7E00-8D45-85B1-ACF04E3BA47D.root',
       '/store/data/Run2017B/HTMHT/NANOAOD/Nano14Dec2018-v1/20000/FA4C59AC-84A5-0D40-8B50-F1E431F5D8BA.root',
] )
