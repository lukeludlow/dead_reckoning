
"use strict";

let CfgINF_Block = require('./CfgINF_Block.js');
let NavDOP = require('./NavDOP.js');
let MonGNSS = require('./MonGNSS.js');
let NavTIMEGPS = require('./NavTIMEGPS.js');
let NavSBAS_SV = require('./NavSBAS_SV.js');
let NavSTATUS = require('./NavSTATUS.js');
let NavDGPS = require('./NavDGPS.js');
let NavCLOCK = require('./NavCLOCK.js');
let NavRELPOSNED = require('./NavRELPOSNED.js');
let CfgMSG = require('./CfgMSG.js');
let UpdSOS = require('./UpdSOS.js');
let CfgNMEA = require('./CfgNMEA.js');
let NavVELECEF = require('./NavVELECEF.js');
let RxmSVSI_SV = require('./RxmSVSI_SV.js');
let TimTM2 = require('./TimTM2.js');
let NavVELNED = require('./NavVELNED.js');
let CfgHNR = require('./CfgHNR.js');
let RxmRAWX = require('./RxmRAWX.js');
let NavSVINFO = require('./NavSVINFO.js');
let AidALM = require('./AidALM.js');
let NavPVT7 = require('./NavPVT7.js');
let CfgUSB = require('./CfgUSB.js');
let Ack = require('./Ack.js');
let RxmSVSI = require('./RxmSVSI.js');
let CfgCFG = require('./CfgCFG.js');
let EsfRAW_Block = require('./EsfRAW_Block.js');
let EsfSTATUS = require('./EsfSTATUS.js');
let NavSOL = require('./NavSOL.js');
let UpdSOS_Ack = require('./UpdSOS_Ack.js');
let CfgTMODE3 = require('./CfgTMODE3.js');
let RxmALM = require('./RxmALM.js');
let HnrPVT = require('./HnrPVT.js');
let CfgANT = require('./CfgANT.js');
let NavSAT = require('./NavSAT.js');
let NavPVT = require('./NavPVT.js');
let CfgGNSS_Block = require('./CfgGNSS_Block.js');
let NavATT = require('./NavATT.js');
let MonVER = require('./MonVER.js');
let CfgNMEA6 = require('./CfgNMEA6.js');
let CfgSBAS = require('./CfgSBAS.js');
let RxmSFRBX = require('./RxmSFRBX.js');
let NavSBAS = require('./NavSBAS.js');
let NavSAT_SV = require('./NavSAT_SV.js');
let EsfINS = require('./EsfINS.js');
let MonHW = require('./MonHW.js');
let MonVER_Extension = require('./MonVER_Extension.js');
let RxmRAW_SV = require('./RxmRAW_SV.js');
let CfgNAVX5 = require('./CfgNAVX5.js');
let NavSVIN = require('./NavSVIN.js');
let RxmRAWX_Meas = require('./RxmRAWX_Meas.js');
let NavSVINFO_SV = require('./NavSVINFO_SV.js');
let CfgDAT = require('./CfgDAT.js');
let RxmRAW = require('./RxmRAW.js');
let MgaGAL = require('./MgaGAL.js');
let NavTIMEUTC = require('./NavTIMEUTC.js');
let AidEPH = require('./AidEPH.js');
let EsfMEAS = require('./EsfMEAS.js');
let NavPOSECEF = require('./NavPOSECEF.js');
let RxmSFRB = require('./RxmSFRB.js');
let AidHUI = require('./AidHUI.js');
let MonHW6 = require('./MonHW6.js');
let CfgNMEA7 = require('./CfgNMEA7.js');
let RxmRTCM = require('./RxmRTCM.js');
let CfgNAV5 = require('./CfgNAV5.js');
let NavPOSLLH = require('./NavPOSLLH.js');
let EsfSTATUS_Sens = require('./EsfSTATUS_Sens.js');
let CfgRATE = require('./CfgRATE.js');
let CfgINF = require('./CfgINF.js');
let EsfRAW = require('./EsfRAW.js');
let CfgPRT = require('./CfgPRT.js');
let CfgDGNSS = require('./CfgDGNSS.js');
let Inf = require('./Inf.js');
let CfgGNSS = require('./CfgGNSS.js');
let RxmEPH = require('./RxmEPH.js');
let NavDGPS_SV = require('./NavDGPS_SV.js');
let CfgRST = require('./CfgRST.js');

module.exports = {
  CfgINF_Block: CfgINF_Block,
  NavDOP: NavDOP,
  MonGNSS: MonGNSS,
  NavTIMEGPS: NavTIMEGPS,
  NavSBAS_SV: NavSBAS_SV,
  NavSTATUS: NavSTATUS,
  NavDGPS: NavDGPS,
  NavCLOCK: NavCLOCK,
  NavRELPOSNED: NavRELPOSNED,
  CfgMSG: CfgMSG,
  UpdSOS: UpdSOS,
  CfgNMEA: CfgNMEA,
  NavVELECEF: NavVELECEF,
  RxmSVSI_SV: RxmSVSI_SV,
  TimTM2: TimTM2,
  NavVELNED: NavVELNED,
  CfgHNR: CfgHNR,
  RxmRAWX: RxmRAWX,
  NavSVINFO: NavSVINFO,
  AidALM: AidALM,
  NavPVT7: NavPVT7,
  CfgUSB: CfgUSB,
  Ack: Ack,
  RxmSVSI: RxmSVSI,
  CfgCFG: CfgCFG,
  EsfRAW_Block: EsfRAW_Block,
  EsfSTATUS: EsfSTATUS,
  NavSOL: NavSOL,
  UpdSOS_Ack: UpdSOS_Ack,
  CfgTMODE3: CfgTMODE3,
  RxmALM: RxmALM,
  HnrPVT: HnrPVT,
  CfgANT: CfgANT,
  NavSAT: NavSAT,
  NavPVT: NavPVT,
  CfgGNSS_Block: CfgGNSS_Block,
  NavATT: NavATT,
  MonVER: MonVER,
  CfgNMEA6: CfgNMEA6,
  CfgSBAS: CfgSBAS,
  RxmSFRBX: RxmSFRBX,
  NavSBAS: NavSBAS,
  NavSAT_SV: NavSAT_SV,
  EsfINS: EsfINS,
  MonHW: MonHW,
  MonVER_Extension: MonVER_Extension,
  RxmRAW_SV: RxmRAW_SV,
  CfgNAVX5: CfgNAVX5,
  NavSVIN: NavSVIN,
  RxmRAWX_Meas: RxmRAWX_Meas,
  NavSVINFO_SV: NavSVINFO_SV,
  CfgDAT: CfgDAT,
  RxmRAW: RxmRAW,
  MgaGAL: MgaGAL,
  NavTIMEUTC: NavTIMEUTC,
  AidEPH: AidEPH,
  EsfMEAS: EsfMEAS,
  NavPOSECEF: NavPOSECEF,
  RxmSFRB: RxmSFRB,
  AidHUI: AidHUI,
  MonHW6: MonHW6,
  CfgNMEA7: CfgNMEA7,
  RxmRTCM: RxmRTCM,
  CfgNAV5: CfgNAV5,
  NavPOSLLH: NavPOSLLH,
  EsfSTATUS_Sens: EsfSTATUS_Sens,
  CfgRATE: CfgRATE,
  CfgINF: CfgINF,
  EsfRAW: EsfRAW,
  CfgPRT: CfgPRT,
  CfgDGNSS: CfgDGNSS,
  Inf: Inf,
  CfgGNSS: CfgGNSS,
  RxmEPH: RxmEPH,
  NavDGPS_SV: NavDGPS_SV,
  CfgRST: CfgRST,
};
