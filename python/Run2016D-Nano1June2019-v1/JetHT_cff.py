import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016D/JetHT/NANOAOD/Nano1June2019-v1/40000/00F07D63-8E96-FB47-9EDF-8819F425BE86.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano1June2019-v1/40000/02334F73-5F9A-D54E-A821-2B636775D89B.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano1June2019-v1/40000/086B9436-A727-CF45-BD0C-49EC5928DD9C.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano1June2019-v1/40000/09159F21-7908-CC48-A987-B78A511305F1.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano1June2019-v1/40000/0CC8C9A2-2E98-B64E-8189-F502A800088A.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano1June2019-v1/40000/179BEAD1-F69F-F244-9886-B4565EEC2CC2.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano1June2019-v1/40000/1D8D5135-2819-9E43-95C8-50EF69CAE184.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano1June2019-v1/40000/2312C909-D19B-B143-91FE-E4EF470955E9.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano1June2019-v1/40000/260E17F9-4A6A-E640-AB1F-5516DF2536A6.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano1June2019-v1/40000/272E9710-AFA3-AC4D-AACF-65AF8140A1C2.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano1June2019-v1/40000/2901DF83-BC45-1549-879E-81F19942AEAA.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano1June2019-v1/40000/292104AE-CF4F-1E43-A48F-B33F6E1834A3.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano1June2019-v1/40000/29F43C2D-258A-2344-A941-F09EF0DE413B.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano1June2019-v1/40000/354B85DD-ECBA-A542-8149-C96A2BA90A0F.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano1June2019-v1/40000/3AACE41C-C8A2-6849-9253-9C2ABD08BFFB.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano1June2019-v1/40000/3B6969AC-1259-5640-8FEC-92C4A4FFC02E.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano1June2019-v1/40000/3E5C75AF-2B85-A249-901A-BBDD70D9426C.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano1June2019-v1/40000/493056A1-647C-FF4A-BE30-69B9F8F9F7C5.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano1June2019-v1/40000/4F35D3BB-2912-1D4F-ABB3-46368AFE0824.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano1June2019-v1/40000/52C35B7C-D6FF-CB4C-A75C-20540E2051ED.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano1June2019-v1/40000/55A6A1BD-8DED-E646-8917-D1EF46E90287.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano1June2019-v1/40000/588C8ADC-6046-C541-B5EF-185367B44DD5.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano1June2019-v1/40000/5E280EB7-3F65-D84E-A2E4-C0CA91395856.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano1June2019-v1/40000/5ED69B20-420B-D84F-BC7F-32981E8534CF.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano1June2019-v1/40000/600CA917-187F-7F40-AB23-5379F3A55B26.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano1June2019-v1/40000/70DD08AE-7E48-7643-8D62-1CCCD5CC690D.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano1June2019-v1/40000/731BFA96-8C5F-B243-90F4-5AFF64486E3C.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano1June2019-v1/40000/7E8BD82E-1485-6040-A194-AD1D27A1323B.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano1June2019-v1/40000/823362FA-9F14-7046-A0EE-C6F4214F0DAA.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano1June2019-v1/40000/88303D34-DF68-CE42-A6BE-52BBA65BFC7B.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano1June2019-v1/40000/90834E1A-9E1A-E94A-B2A6-B44DF0A5C3BE.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano1June2019-v1/40000/9C86BB02-6B60-8B48-AE56-8243B9B193F3.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano1June2019-v1/40000/9F834747-35D1-6642-9361-F3FE8BEF929E.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano1June2019-v1/40000/A496E275-DB54-5B46-A063-CD836A607C89.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano1June2019-v1/40000/A6CA99C7-C914-9C41-806A-635E70FF3CB5.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano1June2019-v1/40000/A8C9850C-7AAE-A646-AE15-0C93DC9609B5.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano1June2019-v1/40000/AAA8724C-ADA3-9C42-9511-E8AEF4FCBF80.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano1June2019-v1/40000/ACA304CA-87DD-B64C-B445-DB92E491606C.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano1June2019-v1/40000/B508556A-2588-7747-99A6-6DD375EB6624.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano1June2019-v1/40000/B5181A20-B6FA-9041-868E-2BE9572B9C31.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano1June2019-v1/40000/B5E99440-C9F3-9E46-AED9-64EB57E4CC91.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano1June2019-v1/40000/BE7E6ED9-B867-F44B-A4DE-9963F0543D32.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano1June2019-v1/40000/C5D86B19-409E-2440-AC6B-534684712868.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano1June2019-v1/40000/CACB4B5C-1EEF-6844-8ED6-16114EF938D7.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano1June2019-v1/40000/D162628B-DB99-1D48-AEA3-7BB490A5A7FB.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano1June2019-v1/40000/D26D32C3-B5B2-B749-A139-47A4AFE87D56.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano1June2019-v1/40000/D66AB084-8D57-1447-A6F7-99B5791D7448.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano1June2019-v1/40000/D900CCC7-6E13-AC40-A939-4D4250BFA2A6.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano1June2019-v1/40000/D9DB0B7D-F42A-7545-83DC-C7E7631AC4CB.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano1June2019-v1/40000/DCBEF266-333A-9F41-9F7B-8521DFFE3CEC.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano1June2019-v1/40000/E14A2F14-4161-4C44-98DC-0764861380D3.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano1June2019-v1/40000/E44DD392-3A04-3D4D-B3FB-2951C1F4AC71.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano1June2019-v1/40000/E5AFC630-3D6E-D942-A185-DB27DA0CEE8F.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano1June2019-v1/40000/EBE45CE9-A67A-BB43-A9B1-245E900CA1B8.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano1June2019-v1/40000/ECF0DD56-028E-1743-B4AD-A7F0A5DD3C66.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano1June2019-v1/40000/F286758E-ECE2-9742-B974-AFECBBB34D27.root',
       '/store/data/Run2016D/JetHT/NANOAOD/Nano1June2019-v1/40000/F95F76F2-35E8-944E-AAEB-6BFD8B6E0247.root',
] )