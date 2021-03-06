import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2017F/JetHT/NANOAOD/Nano14Dec2018-v1/20000/0405D153-2F0D-3C47-8BC5-625ED6CB9A21.root',
       '/store/data/Run2017F/JetHT/NANOAOD/Nano14Dec2018-v1/20000/043315F3-CDC4-B74E-86DA-5987B9D12F50.root',
       '/store/data/Run2017F/JetHT/NANOAOD/Nano14Dec2018-v1/20000/08670787-B0F5-844D-9F77-AC4F53EC5E0D.root',
       '/store/data/Run2017F/JetHT/NANOAOD/Nano14Dec2018-v1/20000/0A95BA10-6BB1-B44B-BB25-E44C2AE73B1D.root',
       '/store/data/Run2017F/JetHT/NANOAOD/Nano14Dec2018-v1/20000/0AA963EA-1FDC-8D40-811C-834E77FB1ACB.root',
       '/store/data/Run2017F/JetHT/NANOAOD/Nano14Dec2018-v1/20000/119973EF-8240-C14A-A94E-C7EBC6E071B1.root',
       '/store/data/Run2017F/JetHT/NANOAOD/Nano14Dec2018-v1/20000/17B54B49-9315-3547-BB4B-4859831335A0.root',
       '/store/data/Run2017F/JetHT/NANOAOD/Nano14Dec2018-v1/20000/1D51550D-C55D-D74F-AB8C-7722C4184EB1.root',
       '/store/data/Run2017F/JetHT/NANOAOD/Nano14Dec2018-v1/20000/1EA0FF1F-992C-3644-8AFC-42CBC835F4F7.root',
       '/store/data/Run2017F/JetHT/NANOAOD/Nano14Dec2018-v1/20000/27459FA9-A7F2-284F-8D58-BD219C2C0587.root',
       '/store/data/Run2017F/JetHT/NANOAOD/Nano14Dec2018-v1/20000/286EAB5B-9B97-A74F-B665-01221810AFC9.root',
       '/store/data/Run2017F/JetHT/NANOAOD/Nano14Dec2018-v1/20000/2D4F628C-9790-2F41-B9A4-EBD89C95B128.root',
       '/store/data/Run2017F/JetHT/NANOAOD/Nano14Dec2018-v1/20000/303FFAA9-364C-F341-9C4F-3EF9715735C0.root',
       '/store/data/Run2017F/JetHT/NANOAOD/Nano14Dec2018-v1/20000/30F6B25E-E1DE-1E43-AA0C-5DD4325C9104.root',
       '/store/data/Run2017F/JetHT/NANOAOD/Nano14Dec2018-v1/20000/3249B843-0E97-2B48-9520-597EF7918CFC.root',
       '/store/data/Run2017F/JetHT/NANOAOD/Nano14Dec2018-v1/20000/35C777FB-43F8-E842-A0A8-CAB630278165.root',
       '/store/data/Run2017F/JetHT/NANOAOD/Nano14Dec2018-v1/20000/38C39DFF-C586-FF45-A82E-EB0461A7AFEE.root',
       '/store/data/Run2017F/JetHT/NANOAOD/Nano14Dec2018-v1/20000/3AB5F4EE-342C-7249-A049-FD97ED538644.root',
       '/store/data/Run2017F/JetHT/NANOAOD/Nano14Dec2018-v1/20000/3E6F25E9-E543-1447-BC32-C36767A38455.root',
       '/store/data/Run2017F/JetHT/NANOAOD/Nano14Dec2018-v1/20000/46DE5D2F-DA17-1B40-B7F6-A2FB999DEAFB.root',
       '/store/data/Run2017F/JetHT/NANOAOD/Nano14Dec2018-v1/20000/4734D350-C364-764E-B857-17799FEB6485.root',
       '/store/data/Run2017F/JetHT/NANOAOD/Nano14Dec2018-v1/20000/4DAE828A-5300-354D-A99F-3513BF9E0203.root',
       '/store/data/Run2017F/JetHT/NANOAOD/Nano14Dec2018-v1/20000/57E82AEA-118A-6C4F-9E02-409773404C7E.root',
       '/store/data/Run2017F/JetHT/NANOAOD/Nano14Dec2018-v1/20000/5B1EB63C-22AA-7740-99A6-44661FCC3955.root',
       '/store/data/Run2017F/JetHT/NANOAOD/Nano14Dec2018-v1/20000/6006599C-4367-C24A-A689-D6F075BFBC9D.root',
       '/store/data/Run2017F/JetHT/NANOAOD/Nano14Dec2018-v1/20000/60993999-3A9B-0C4B-A15B-3ADC0605DD1E.root',
       '/store/data/Run2017F/JetHT/NANOAOD/Nano14Dec2018-v1/20000/65252A59-3318-EC41-B312-CAF2B85C0CC0.root',
       '/store/data/Run2017F/JetHT/NANOAOD/Nano14Dec2018-v1/20000/71250298-7BD6-AA48-AD9D-661CAB57D3D5.root',
       '/store/data/Run2017F/JetHT/NANOAOD/Nano14Dec2018-v1/20000/71A86C45-32B2-D846-BDE2-B24D599353CA.root',
       '/store/data/Run2017F/JetHT/NANOAOD/Nano14Dec2018-v1/20000/747D0497-2769-4B4C-BF9A-BF5A2BDA1819.root',
       '/store/data/Run2017F/JetHT/NANOAOD/Nano14Dec2018-v1/20000/7BB5DE84-E001-854E-AEF7-C1B69DAA61FA.root',
       '/store/data/Run2017F/JetHT/NANOAOD/Nano14Dec2018-v1/20000/7EB90233-42C6-A941-B542-94C6E17AFA46.root',
       '/store/data/Run2017F/JetHT/NANOAOD/Nano14Dec2018-v1/20000/82A419E3-3C2B-A14A-ABD6-7BDDE0194388.root',
       '/store/data/Run2017F/JetHT/NANOAOD/Nano14Dec2018-v1/20000/88946975-C011-C148-B85F-61B0DC36CA3C.root',
       '/store/data/Run2017F/JetHT/NANOAOD/Nano14Dec2018-v1/20000/904CC58B-AE4F-1D40-870A-509CE04D6D79.root',
       '/store/data/Run2017F/JetHT/NANOAOD/Nano14Dec2018-v1/20000/91355C16-4CA1-D54A-9997-4F1BD3305597.root',
       '/store/data/Run2017F/JetHT/NANOAOD/Nano14Dec2018-v1/20000/95D27A99-2537-044D-9E80-0AFC9F1C6716.root',
       '/store/data/Run2017F/JetHT/NANOAOD/Nano14Dec2018-v1/20000/9D004A85-4277-C548-9A96-932AD533248F.root',
       '/store/data/Run2017F/JetHT/NANOAOD/Nano14Dec2018-v1/20000/9F30A840-A23D-444E-AEAD-AD8CF92406AF.root',
       '/store/data/Run2017F/JetHT/NANOAOD/Nano14Dec2018-v1/20000/9FCCD563-7990-EF4B-B309-9C1229BB1696.root',
       '/store/data/Run2017F/JetHT/NANOAOD/Nano14Dec2018-v1/20000/A4F76DAC-EA2D-2D41-8F3D-C4DFB404497D.root',
       '/store/data/Run2017F/JetHT/NANOAOD/Nano14Dec2018-v1/20000/A79EB2D4-3D34-1C4B-8F77-9197FC234645.root',
       '/store/data/Run2017F/JetHT/NANOAOD/Nano14Dec2018-v1/20000/AC54E62B-F9CB-1C4F-8356-B0C18E006E09.root',
       '/store/data/Run2017F/JetHT/NANOAOD/Nano14Dec2018-v1/20000/AD634035-7C73-CF4E-A706-86B26E35FC10.root',
       '/store/data/Run2017F/JetHT/NANOAOD/Nano14Dec2018-v1/20000/B02B0971-116D-974C-BBAC-EBF427484ACC.root',
       '/store/data/Run2017F/JetHT/NANOAOD/Nano14Dec2018-v1/20000/BC84C267-4430-AF4A-9CEB-E10A25A6C02E.root',
       '/store/data/Run2017F/JetHT/NANOAOD/Nano14Dec2018-v1/20000/BE833B1B-9C3E-1249-9ABD-77AFC9EA7645.root',
       '/store/data/Run2017F/JetHT/NANOAOD/Nano14Dec2018-v1/20000/C04A9536-6005-354C-A2D8-F564B9FF5177.root',
       '/store/data/Run2017F/JetHT/NANOAOD/Nano14Dec2018-v1/20000/C3500AC4-2AB0-664A-B71F-85360E46D215.root',
       '/store/data/Run2017F/JetHT/NANOAOD/Nano14Dec2018-v1/20000/C415F912-215A-E844-8308-053A9E26A0BA.root',
       '/store/data/Run2017F/JetHT/NANOAOD/Nano14Dec2018-v1/20000/C436709E-92C1-6F4E-A2E0-0E8E06DF6137.root',
       '/store/data/Run2017F/JetHT/NANOAOD/Nano14Dec2018-v1/20000/C8D55500-F6F7-4747-B4E6-E88E083290B5.root',
       '/store/data/Run2017F/JetHT/NANOAOD/Nano14Dec2018-v1/20000/CA873168-E66C-C047-8E8A-B1191A980B11.root',
       '/store/data/Run2017F/JetHT/NANOAOD/Nano14Dec2018-v1/20000/D039A26A-1F1F-7246-878E-7E7EB1D52EEF.root',
       '/store/data/Run2017F/JetHT/NANOAOD/Nano14Dec2018-v1/20000/D4DF0376-86EE-A548-B884-FB50649C7B95.root',
       '/store/data/Run2017F/JetHT/NANOAOD/Nano14Dec2018-v1/20000/D6451299-5578-9942-818D-6C1A0089C9D7.root',
       '/store/data/Run2017F/JetHT/NANOAOD/Nano14Dec2018-v1/20000/DBA28ABE-1EB9-0142-9B7E-59C80FFCC57F.root',
       '/store/data/Run2017F/JetHT/NANOAOD/Nano14Dec2018-v1/20000/DD7977F2-FD03-5F42-8D0B-9ABBE4C09330.root',
       '/store/data/Run2017F/JetHT/NANOAOD/Nano14Dec2018-v1/20000/E83B02E9-CFCC-7041-A959-253C73FB0685.root',
       '/store/data/Run2017F/JetHT/NANOAOD/Nano14Dec2018-v1/20000/E9A5A1AC-BD06-7F4C-BB84-AEBE681AE6AE.root',
       '/store/data/Run2017F/JetHT/NANOAOD/Nano14Dec2018-v1/20000/E9ADD43B-0422-B740-B903-ADE7BE4DBA4E.root',
       '/store/data/Run2017F/JetHT/NANOAOD/Nano14Dec2018-v1/20000/F26FA3EC-BA2C-BB4B-8C9E-610B07AF6260.root',
       '/store/data/Run2017F/JetHT/NANOAOD/Nano14Dec2018-v1/20000/F6C3C953-E832-5B4D-AEED-EA50C8A2DBC4.root',
       '/store/data/Run2017F/JetHT/NANOAOD/Nano14Dec2018-v1/20000/F9C6E7E7-ED21-9244-BAF9-99ACE9F24387.root',
       '/store/data/Run2017F/JetHT/NANOAOD/Nano14Dec2018-v1/20000/FA3076A1-1783-8A48-BE72-E8E671C49CE0.root',
       '/store/data/Run2017F/JetHT/NANOAOD/Nano14Dec2018-v1/20000/FBAACD4D-3223-4B4C-82A8-B7FE2E094F5F.root',
       '/store/data/Run2017F/JetHT/NANOAOD/Nano14Dec2018-v1/20000/FEAE9488-5716-2840-B2C3-3B4FEF6E9B5D.root',
] )
