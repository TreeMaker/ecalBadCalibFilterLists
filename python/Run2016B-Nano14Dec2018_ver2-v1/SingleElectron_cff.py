import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/10000/1C9FC6AB-7CFC-8747-B039-F965A26EB92E.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/10000/2FC4C427-76FF-5D45-A140-5C546223ADEC.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/10000/3FAA13B5-D247-3044-9F1B-3E98127D66E8.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/10000/5AD24118-712E-A445-8EEE-FF7B1F6F077A.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/10000/63553D12-7CF8-224C-B426-FC88529F938E.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/10000/69529EEE-00C0-A948-BD3E-6C9DA5F9A0A2.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/10000/C1205B5B-22D4-F44A-B4DA-AE5BAC7E56FC.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/10000/C265B198-124C-AA4D-83B8-CF2C5B2B5220.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/10000/C3CDD9C0-826D-844A-9550-4B942E240A39.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/10000/F717C194-ECC4-E443-B179-046A9B457B5E.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/20000/075272FB-5EC8-A84E-BBDD-EE100F907457.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/20000/084FF076-4EE6-8943-A02B-1F0CB03519B5.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/20000/0B66E5BB-05A1-BF4D-99A4-18469AD94095.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/20000/14DEAA44-11D3-0249-B320-0469536EB5AC.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/20000/18C2D409-729E-4E46-BF29-E75EA0425FFA.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/20000/1B9F274E-BADB-B541-874B-A885E4E0A8C2.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/20000/1CAC60A0-EDB9-1143-85C5-9927E015D8DD.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/20000/1EE058AF-2572-A142-90E0-FCF815935086.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/20000/2AD5E20E-0CB7-CB46-8C8A-6C3CDFCF1DBC.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/20000/2EF1AF99-7B10-D04F-879A-A4C5EA0CCF58.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/20000/34F67284-35C3-A242-BEF6-5963105FADC0.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/20000/49A5918E-F8D4-F746-AB77-A5C25D8D3A28.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/20000/4D396AD7-FBBB-534D-8C7A-0C5B18895F85.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/20000/4DB241B4-9B49-6448-8B3C-8BE922E7D20E.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/20000/4F7D2BC3-42E9-5546-A1C8-376C6F0E5C42.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/20000/5348970A-8F49-F744-BE17-9909B7645176.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/20000/556C397B-16C3-0744-93A9-FD0110386627.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/20000/5F35628C-C09B-0B42-AF57-2D895561FA29.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/20000/601AC215-25E3-7F40-B78A-11200C4790B7.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/20000/704EE79C-D6D4-654C-9727-5B3BDE8D8B80.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/20000/7380B27F-01B8-E144-A414-F478452424BF.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/20000/74D23A93-EC24-CA43-908A-DD815BAA37AA.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/20000/7C9E70D9-34D1-1448-A1A4-96FAE0A77D30.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/20000/8372DDF5-8C2D-C04A-8730-68C1C8833429.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/20000/8AED3666-7353-0B41-A8A2-0B57E221593A.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/20000/99A62EFE-D070-AE46-B0B6-2724FD37517D.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/20000/A30EC3F7-821F-C240-BF94-0D0EA6B2A3F4.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/20000/A3385E37-5087-B54D-84CB-35E9F3F71561.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/20000/A59857FA-57B1-C948-88C4-E55773A6A467.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/20000/AA49EBA8-A92A-C248-999B-31926EBC353E.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/20000/AAAF6D34-830D-DB42-828F-E90B8B436404.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/20000/BB0518A9-36CF-BF4C-ACA9-43AA66208312.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/20000/BDFA9C70-22F5-DC41-94CB-E25F4A9E691C.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/20000/C885DFDF-D524-9846-9569-0FC0582EB20F.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/20000/CB7B75A5-77C0-4F4A-8A10-B7CAD5D7210F.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/20000/CC8AD84A-9ED8-3A40-8CC2-7B6481BB657B.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/20000/D0837AB1-F33D-5B48-874A-A1D998B2330D.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/20000/D11D706F-98D3-B840-B657-2663772F751B.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/20000/D4955EA0-89F7-ED4C-A96C-BBE8DAC2CA67.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/20000/D5CC09BC-1AD3-4F49-A48D-641C717E8340.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/20000/D72D2CAB-5EE2-8B40-A9FE-36683B910521.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/20000/DD0A2D8F-6259-4E4B-AC7A-C7A622C642C6.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/20000/E05E8A15-C218-2D49-AD9F-A3475B07EA33.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/20000/E0920AB0-1E0F-184B-9484-93941B020EEF.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/20000/E0BA6646-2344-404C-A4B5-9D2637EA899C.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/20000/E9214FE0-3248-6A48-8EA6-BBC12006B430.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/20000/E940F322-6374-6D4C-B5E9-24D0D4505ED3.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/20000/ED4CC337-C46F-ED44-964D-3BAA797BA504.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/20000/EE7A776F-0DD0-A14A-967C-4A5C69B4A826.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/20000/F6019548-9A9B-C344-91FC-D7BB370D2DB6.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/280000/0653C8A1-2F09-3F44-A6CA-36E3595C7EFF.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/280000/0F762D80-EFA9-6A42-A87F-3C234327C89F.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/280000/160601CF-BEF9-8442-A19D-DC816F6428D2.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/280000/20D7188A-BA54-164B-BEF0-4F191DBF3F88.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/280000/27631D65-61E1-204E-8301-DAC77BD229BD.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/280000/315059A2-D72E-9F4B-986D-BFBFB242B1F6.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/280000/36AC666C-2093-0F4F-9837-3D84D47B68EF.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/280000/398DAA3E-D780-724A-AAD4-E5CE46FCED5C.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/280000/4A11FD26-FBC7-A94D-8078-6DC9557B5058.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/280000/531BDF22-C724-8C44-A77B-46E56E865DD5.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/280000/57899A95-58DF-2947-BD2D-D95206D4509B.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/280000/5792FA84-C668-6142-A88A-0909580178CD.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/280000/57D83878-A5AB-A447-B52A-D1298643ABE9.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/280000/5BBC1C41-FCEF-CE47-91BF-9CF37D95E2AD.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/280000/5D961F31-29E2-2A48-AF5B-65CF019771A2.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/280000/612FCF6A-247D-4D45-9CFB-68CBD84FD6F2.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/280000/63498164-FEB8-A841-A98F-0D948741225B.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/280000/638ABFC9-3DFA-C34F-8219-2A50B0496858.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/280000/657025C5-82DB-C944-A914-0AB0E7076BBA.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/280000/68ECAB3F-F3B8-2F4E-A7EE-59BE5FE53A0C.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/280000/69BAF2E8-2508-EA4C-9AF8-77B12F35169B.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/280000/6A97820B-ED21-6948-9AE9-BAC943F4DD72.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/280000/7474D6D1-D9A7-584B-BED3-BEE52AA29EED.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/280000/96433182-3981-2949-A5A4-924B52F2A1B8.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/280000/983AEF37-F05A-BE4C-8750-779A29522EE6.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/280000/B434D019-8A98-BC4E-8E8E-FFDCB8D3F330.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/280000/B56AC457-FBE6-3349-A657-04F343B70522.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/280000/B9B5B631-6EDF-7944-A9B3-8A56F2AB6425.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/280000/C6235AC2-80C0-7C41-B4F7-DAEA22905D3B.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/280000/CFF88752-EAC0-6E45-A0DB-4AF4593A38F3.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/280000/D446A1DE-F57C-A047-A827-A13064746980.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/280000/D9FF5078-F920-0349-83C1-5B8CC23EFD5F.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/280000/E2599D97-D797-EC4B-BFAA-E466BCEBAF4B.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/280000/E7BB773C-4A1C-3640-BEAB-115F09E1BE6E.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/280000/EBD46490-0139-6E4E-A945-A98D5A9A5D26.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/90000/09DEB309-EA4C-8341-AD5F-88F8C680D3AE.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/90000/0B2716E4-0507-4645-B8E2-9E7ABDED2946.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/90000/11142772-56F7-8D4A-A4B9-E6B1DFC04DAA.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/90000/121376EB-E96C-FC43-903D-1E6D6F025FC9.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/90000/1FD8E549-3FBD-E74F-BDE0-CA33AF7D4A7F.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/90000/235ED176-2617-C049-A7D9-E31F7EB7C2AB.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/90000/23EE9E06-CD99-CD40-99E2-1813922CA68C.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/90000/28F18AAB-3D22-0D4A-AD2F-EA8ABCAAE7FC.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/90000/296A6537-8574-354E-86D8-558B66FA0995.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/90000/29AB9934-40BA-F342-B561-1DFFD365C19B.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/90000/2F5474E0-9238-DC44-98EA-9ECE5E2BAB1D.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/90000/3059FDE1-E6AA-7347-885A-C7C779DC0E96.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/90000/39BC15F8-CA19-CA46-A138-1E4C6FC9A50D.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/90000/39FCB24F-D882-8A47-8A8B-CAF2051C83D1.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/90000/512B8E26-FD17-534C-9BC9-C318B61F09FA.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/90000/68BD8114-6EBC-0F4E-94C1-A92A19464435.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/90000/71EDA343-FEEE-6447-8D11-4934DB74E840.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/90000/75D800B7-174C-3146-B7F0-2F726CEC59BD.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/90000/76FB3FCA-8772-A545-854C-81A150FCCD15.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/90000/863604FA-AD3E-F645-B328-B44E67995A0D.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/90000/8FF64E2B-9A75-5848-A08E-21450A6A51CB.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/90000/91D65A34-821E-9740-A29B-E50D05E3DD20.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/90000/A324CB42-D59C-C94B-83E4-00F52B3F0F39.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/90000/AE280509-8973-A94C-A262-108F85A3E9CA.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/90000/BAFFD10D-B6CF-8E4F-B435-0A24CBC413F5.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/90000/BCB8C129-E1C5-3F42-BFAD-0B6DA7159B03.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/90000/D811B927-A70B-C446-93E2-7FAA55DC907D.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/90000/D9FF7AAB-A965-7B48-B049-FF560CF2D7EE.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/90000/DC6EECEB-5F3E-4143-AE9C-9421C9261CF9.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/90000/DC899F23-7552-B447-B441-89F91D611E69.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/90000/DCEF7FA6-C1BB-F943-912E-CB2C55208A39.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/90000/DD5637E7-1287-0742-AD26-6ECF2C4CC397.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/90000/E8BB6FC1-3C85-7549-B432-C264360E41C8.root',
       '/store/data/Run2016B_ver2/SingleElectron/NANOAOD/Nano14Dec2018_ver2-v1/90000/F686399B-0F4C-2247-AE99-1E9D28891C9A.root',
] )
