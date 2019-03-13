import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2017B/SinglePhoton/NANOAOD/Nano14Dec2018-v1/00000/99D4F3AA-9324-404D-9909-BECCCF39C365.root',
       '/store/data/Run2017B/SinglePhoton/NANOAOD/Nano14Dec2018-v1/90000/27CFC290-364D-D144-8CBD-D9BEACC92D8D.root',
       '/store/data/Run2017B/SinglePhoton/NANOAOD/Nano14Dec2018-v1/90000/36E58699-0883-0C4D-9FE0-BE36D7CFD8DB.root',
       '/store/data/Run2017B/SinglePhoton/NANOAOD/Nano14Dec2018-v1/90000/4A3FA998-00AC-5546-8C61-FDFB5B4330F0.root',
       '/store/data/Run2017B/SinglePhoton/NANOAOD/Nano14Dec2018-v1/90000/508001CE-3B7C-7245-9A9A-4C66EABAA203.root',
       '/store/data/Run2017B/SinglePhoton/NANOAOD/Nano14Dec2018-v1/90000/5C0CCC7B-B5A5-D54C-AC3C-CEC5554545CE.root',
       '/store/data/Run2017B/SinglePhoton/NANOAOD/Nano14Dec2018-v1/90000/87F7460D-C2E3-0442-9641-D7295A328718.root',
       '/store/data/Run2017B/SinglePhoton/NANOAOD/Nano14Dec2018-v1/90000/8CF453EF-28F3-B748-85EB-95CFB0275731.root',
       '/store/data/Run2017B/SinglePhoton/NANOAOD/Nano14Dec2018-v1/90000/90D6AA83-8BD0-0A4D-A51E-E61ABDEFBB42.root',
       '/store/data/Run2017B/SinglePhoton/NANOAOD/Nano14Dec2018-v1/90000/A27752D2-076E-5546-9F18-20E07922BE36.root',
       '/store/data/Run2017B/SinglePhoton/NANOAOD/Nano14Dec2018-v1/90000/BAC091F8-B457-1544-BCBA-B725DB3E6DEF.root',
       '/store/data/Run2017B/SinglePhoton/NANOAOD/Nano14Dec2018-v1/90000/CE07E3BC-B3A7-454F-B27F-4378916CF0B0.root',
       '/store/data/Run2017B/SinglePhoton/NANOAOD/Nano14Dec2018-v1/90000/D56686F0-E0B2-5F4B-952B-B2652F276868.root',
       '/store/data/Run2017B/SinglePhoton/NANOAOD/Nano14Dec2018-v1/90000/EE5A8F34-6DD5-C54B-825E-DBD7CF36689E.root',
] )
