---
title: EVTX to MITRE ATT&CK
---

- [Overview](#overview)
- [Environment](#environment)
- [Activity](#activity)
- [Contained Data](#contained-data)
- [Links](#links)
- [Example Data](#example-data)

| <!-- -->                 | <!-- -->                                                                                                                                          |
|--------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| **Network Data Source**  | -                                                                                                                                                 |
| **Network Data Labeled** | -                                                                                                                                                 |
| **Host Data Source**     | Windows evtx files                                                                                                                                |
| **Host Data Labeled**    | Yes, in the sense that everything is malicious                                                                                                    |
|                          |                                                                                                                                                   |
| **Overall Setting**      | Single OS                                                                                                                                         |
| **OS Types**             | Windows 10<br/>Windows Server 2012 R2 and higher                                                                                                  |
| **Number of Machines**   | n/a                                                                                                                                               |
| **Total Runtime**        | n/a                                                                                                                                               |
| **Year of Collection**   | n/a                                                                                                                                               |
| **Attack Categories**    | Execution<br/>Persistence<br/>Privilege Escalation<br/>Defense Evasion<br/>Credential Access<br/>Discovery<br/>Lateral Movement<br/>C2<br/>Impact |
| **Benign Activity**      | n/a                                                                                                                                               |
|                          |                                                                                                                                                   |
| **Packed Size**          | 3,7 MB                                                                                                                                            |
| **Unpacked Size**        | n/a                                                                                                                                               |
| **Download Link**        | [goto](https://github.com/mdecrevoisier/EVTX-to-MITRE-Attack/archive/refs/heads/master.zip)                                                       |

***

### Overview

A SIEM oriented project, providing ~270 Windows IOCs, classified per MITRE tactic and technique.
These are intended to be used with ones SIEM solution to measure stuff like security coverage or identify gaps.
I'm guessing that, ideally, all of these should be caught when thrown at the system.

### Environment

Specific details are not provided, but as this focuses on EVTX, all participating machines will most likely run Windows.

### Activity

Benign behavior is not included, description of individual events/attacks can be found on the linked homepage.

### Contained Data

Each IOC is realized as a Windows `.evtx` file, and all files are grouped by their corresponding tactic/technique.
Additionally, there are some attack chains like PrintNightmare or Eternal Romance, also present as `.evtx` files.
The log sources used can be
found [here](https://github.com/mdecrevoisier/EVTX-to-MITRE-Attack#microsoft-log-sources-used).
These files could either be used as-is, or converted into something like JSON or XML.

### Links

- [Homepage](https://github.com/mdecrevoisier/EVTX-to-MITRE-Attack)

### Example Data

Some events taken
from `TA00004-Privilege Escalation/T1574-DLL side-loading/ID354-808-Mimispool printer installation (PrintNightmare).evtx`,
converted to `.csv`

```
Ebene,Datum und Uhrzeit,Quelle,Ereignis-ID,Aufgabenkategorie
Informationen,27.10.2021 12:28:26,Microsoft-Windows-PrintService,317,Ein Druckertreiber wird gelöscht,Der Druckertreiber Generic / Text Only wurde gelöscht. Es ist keine Benutzeraktion erforderlich.
Informationen,27.10.2021 12:28:26,Microsoft-Windows-PrintService,301,Ein Drucker wird gelöscht,"Der Drucker {BABBC1A0-F75A-44B0-92BC-57E20CEDA1D8} wurde gelöscht, und die Benutzer können diesen Drucker nicht mehr verwenden. Es ist keine Benutzeraktion erforderlich."
Informationen,27.10.2021 12:28:26,Microsoft-Windows-PrintService,302,Ein Drucker wird gelöscht,"Der Drucker {BABBC1A0-F75A-44B0-92BC-57E20CEDA1D8},1 wird gelöscht. Es ist keine Benutzeraktion erforderlich."
Informationen,27.10.2021 12:28:26,Microsoft-Windows-PrintService,302,Ein Drucker wird gelöscht,Der Drucker {BABBC1A0-F75A-44B0-92BC-57E20CEDA1D8} wird gelöscht. Es ist keine Benutzeraktion erforderlich.
Fehler,27.10.2021 12:28:26,Microsoft-Windows-PrintService,808,Initialisierung,"Fehler beim Laden eines Plug-In-Moduls C:\Windows\system32\spool\DRIVERS\x64\3mimispool.dll durch den Druckspooler, Fehlercode 0x7E. Kontextinformationen finden Sie in den Benutzerereignisdaten."
Fehler,27.10.2021 12:28:26,Microsoft-Windows-PrintService,808,Initialisierung,"Fehler beim Laden eines Plug-In-Moduls C:\Windows\system32\spool\DRIVERS\x64\3mimispool.dll durch den Druckspooler, Fehlercode 0x7E. Kontextinformationen finden Sie in den Benutzerereignisdaten."
Informationen,27.10.2021 12:28:26,Microsoft-Windows-PrintService,823,Der Standarddrucker wird geändert,Der Standarddrucker wurde in \\fs03vuln\Kiwi Legit Printer geändert. Kontextinformationen finden Sie in den Benutzerereignisdaten.
Informationen,27.10.2021 12:28:26,Microsoft-Windows-PrintService,306,Druckerkonfiguration wird festgelegt,Die Einstellungen für den Drucker {BABBC1A0-F75A-44B0-92BC-57E20CEDA1D8} wurden geändert. Es ist keine Benutzeraktion erforderlich.
Fehler,27.10.2021 12:28:26,Microsoft-Windows-PrintService,354,Initialisierung,"\\fs03vuln\Kiwi Legit Printer-Initialisierungsfehler bei \\fs03vuln\print$\W32X86\3\mimispool.dll. Fehler: 2. The system cannot find the file specified.
. Dieser Fehler kann auftreten, wenn das System instabil ist oder nicht genug Systemressourcen verfügbar sind."
Informationen,27.10.2021 12:28:26,Microsoft-Windows-PrintService,306,Druckerkonfiguration wird festgelegt,Die Einstellungen für den Drucker {BABBC1A0-F75A-44B0-92BC-57E20CEDA1D8} wurden geändert. Es ist keine Benutzeraktion erforderlich.
Informationen,27.10.2021 12:28:26,Microsoft-Windows-PrintService,306,Druckerkonfiguration wird festgelegt,Die Einstellungen für den Drucker {BABBC1A0-F75A-44B0-92BC-57E20CEDA1D8} wurden geändert. Es ist keine Benutzeraktion erforderlich.
Informationen,27.10.2021 12:28:26,Microsoft-Windows-PrintService,304,Der Betrieb eines Druckers wird fortgesetzt.,Der Betrieb des Druckers {BABBC1A0-F75A-44B0-92BC-57E20CEDA1D8} wurde fortgesetzt. Es ist keine Benutzeraktion erforderlich.
Informationen,27.10.2021 12:28:26,Microsoft-Windows-PrintService,300,Ein Drucker wird hinzugefügt,Der Drucker {BABBC1A0-F75A-44B0-92BC-57E20CEDA1D8} wurde erstellt. Es ist keine Benutzeraktion erforderlich.
Informationen,27.10.2021 12:28:26,Microsoft-Windows-PrintService,316,Ein Druckertreiber wird hinzugefügt,"Der Druckertreiber Generic / Text Only für Windows x64 Version-3 wurde hinzugefügt oder aktualisiert. Dateien:- UNIDRV.DLL, UNIDRVUI.DLL, TTY.GPD, UNIDRV.HLP, TTYRES.DLL, TTY.INI, TTY.DLL, TTYUI.DLL, TTYUI.HLP, UNIRES.DLL, STDNAMES.GPD, STDDTYPE.GDL, STDSCHEM.GDL, STDSCHMX.GDL. Es ist keine Benutzeraktion erforderlich."
[...]
```