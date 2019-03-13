import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/01C4FDD5-D94A-044F-8688-ED6034FD480A.root',
       '/store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/02D97225-9454-E742-A14B-EF949297AC55.root',
       '/store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/043A974F-9479-C542-B56E-8D2CB3A511A6.root',
       '/store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/05265503-0C6E-314D-ADF7-D6F985DCF8F2.root',
       '/store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/09AB7F99-687B-3242-9C54-8D5720EC3408.root',
       '/store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/127AA2B9-AEFE-504B-8446-2C3965AA1D40.root',
       '/store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/140CB2AF-3C9B-1342-B177-D927BD119EC0.root',
       '/store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/14D32DFA-54C3-7549-9D80-6B4390F27B4B.root',
       '/store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/15290EC1-F613-F74C-9937-5111450D73E6.root',
       '/store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/159CB9B8-0B90-2044-BD40-C84E8B905971.root',
       '/store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/1DF905F8-B2AB-6D4F-AD62-A854B3B3E2BC.root',
       '/store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/24381BD2-3560-F74F-8C25-97DA15FB8B6D.root',
       '/store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/26AEA0AA-5DA2-434B-854B-316C6045F20D.root',
       '/store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/278EC82B-6D9A-1349-ACC1-8A40450161EB.root',
       '/store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/29EEB780-3B13-B64E-AB52-261B8166C6BD.root',
       '/store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/2B046123-954B-7141-AC95-9CF5CA3D7643.root',
       '/store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/2CD56638-DFE6-0346-8617-FF9BBC811AB4.root',
       '/store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/2EC32E0E-3137-A54E-A376-5DBDD447DD3F.root',
       '/store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/358E311B-096E-1A4A-8CCD-CDD9B1321C70.root',
       '/store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/3650D06E-878E-3841-A9FE-7B6B2BDA648F.root',
       '/store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/3B9B0851-9368-F746-9ED4-D9148D18B609.root',
       '/store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/3D0BE51B-96B3-6F4C-9064-572180E2CE37.root',
       '/store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/3F13C55E-533E-944F-B1F6-691A771DA1D7.root',
       '/store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/410009FF-85BC-C044-8A3F-851D0B59FF29.root',
       '/store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/4376F608-7BA2-874A-9E3B-FB33B75BAF8C.root',
       '/store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/4381A4CD-6DEE-7441-BCFC-087CD6EDDE1C.root',
       '/store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/442B54A5-63A3-8A4F-9CFD-16C0F4ACC94F.root',
       '/store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/444E800D-9955-5B43-A097-CF1DD4C79F8A.root',
       '/store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/4BEB4757-7396-CA43-89F1-6761996EA3CC.root',
       '/store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/4BF7F640-58EE-A148-B7DF-E84816D80861.root',
       '/store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/4F383CBD-AE93-C24D-83BD-5A6724F4879A.root',
       '/store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/518D270C-5FE0-9348-8E4C-139C26C9D02B.root',
       '/store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/51AA6C08-1E76-054C-9DDF-08D13658F98F.root',
       '/store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/54D386ED-0382-0B4F-945B-6B2DC8DC1AF9.root',
       '/store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/57EF84AA-F582-3445-BFBB-28A6C0BD352D.root',
       '/store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/583FC996-F092-4649-876C-E9CC32B36A94.root',
       '/store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/616475FB-3974-6646-A63F-76A49228542F.root',
       '/store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/63512A8E-1D24-8E49-871F-5D339C998F29.root',
       '/store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/6A12424E-D799-2841-BDF8-89BA073A287F.root',
       '/store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/726ABBF4-D4DA-1C4A-A96B-9838288F8DD5.root',
       '/store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/735C1B1E-00DC-1B47-9C81-0F2D5E2310F4.root',
       '/store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/73D5F203-F3B1-8E48-919A-DD7F569FA2F9.root',
       '/store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/77957EFD-143D-1E4F-AFF8-5012BDA8B7B0.root',
       '/store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/79460693-4F20-584B-B604-A6C676215C4F.root',
       '/store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/79B9F080-D3F7-7A4F-8B10-5B64B86A6155.root',
       '/store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/7F90DF96-5E8A-E841-9240-C11812287F6D.root',
       '/store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/8095BE0E-3B18-BC44-BEF6-3ACB6F1DDA48.root',
       '/store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/80C93CA3-F35F-E448-9E3F-7378B5E778C8.root',
       '/store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/8202F938-9BFA-0A4E-83C2-54DE56CFBC3B.root',
       '/store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/82A6B7A5-A61E-5240-BBAD-D0635567858E.root',
       '/store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/8491B9C0-8092-1D48-BAB7-CC6D90694426.root',
       '/store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/8511DEC3-EE31-E64F-AA3D-248195C01BC0.root',
       '/store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/8EF5F9C9-0875-BF4B-999D-999CB095BD1D.root',
       '/store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/8F16DF44-ACDF-FB4D-AE75-C504E47697C1.root',
       '/store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/8F580332-8985-634F-ABC0-A9B1035AD736.root',
       '/store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/92814022-A70F-5C4F-AC58-B06C6199E4C2.root',
       '/store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/959330C0-C942-EE43-8BD3-C60F8B5B1F59.root',
       '/store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/99A94BAC-9130-164C-97BD-3D6F00304333.root',
       '/store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/9AE72BAD-F1E3-0341-8806-33493291A30E.root',
       '/store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/9E036692-52EB-4C46-AA68-7078DA66F347.root',
       '/store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/9F6E0392-F90B-D641-AD61-5E043F9F590C.root',
       '/store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/A066773E-79E6-0B4B-9842-DFF2F4FA39FA.root',
       '/store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/A76B4A49-9AF1-9641-A0C4-B3B454CB484A.root',
       '/store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/A9990249-C6DA-C04B-A8B7-274ED04AB29F.root',
       '/store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/A9BDCD5F-55F5-9B48-8BE5-D3DBFB2A6B14.root',
       '/store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/AB77811C-5791-AB40-8B99-03ED9CEF68C5.root',
       '/store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/AC4BF8AD-3B56-2949-9CF2-E94B47F64E4F.root',
       '/store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/B4B8CF64-5B54-7F4B-B0B6-B72A8586AF59.root',
       '/store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/BAB77E36-AC1A-ED49-B5A1-97E98A3812F2.root',
       '/store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/BBA52555-CD93-6A4B-A603-BF54F476982F.root',
       '/store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/BC0A7E32-1F10-EF4B-83DE-432375D9F8EA.root',
       '/store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/C1A5E354-23FE-D947-90BD-9C8CCBD982C3.root',
       '/store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/C2DA9927-0C84-BD45-9334-423D196D8734.root',
       '/store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/CA2FC983-4286-D344-B68D-28CE523D88A8.root',
       '/store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/CDFDBF69-E753-E841-93B5-6363CF29F31A.root',
       '/store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/D315EBC5-5EC2-CD4D-807D-82C59041D503.root',
       '/store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/DE518177-AE73-0E4F-BB55-851FD523DAB3.root',
       '/store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/E21EB05A-8A76-464B-8E1A-5C3C9DB26EFF.root',
       '/store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/EE0A0788-8BDB-0641-AF10-B2CD449121CA.root',
       '/store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/F171123D-4739-8C40-82B5-3E37FBAFE25A.root',
       '/store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/FB91E08A-B48F-ED4A-8E52-5233FE6B447A.root',
       '/store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/FD252EDA-232C-6A43-AF87-C8ADB06A5DB2.root',
] )
