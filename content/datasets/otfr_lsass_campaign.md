---
title: OTFR LSASS Campaign
---

- [Overview](#overview)
- [Environment](#environment)
- [Activity](#activity)
- [Contained Data](#contained-data)
- [Links](#links)
- [Data Examples](#data-examples)

| <!-- -->                 | <!-- -->                                                                                                                             |
|--------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| **Network Data Source**  | pcaps, Zeek logs                                                                                                                     |
| **Network Data Labeled** | No                                                                                                                                   |
| **Host Data Source**     | Windows events                                                                                                                       |
| **Host Data Labeled**    | No                                                                                                                                   |
|                          |                                                                                                                                      |
| **Overall Setting**      | Single OS                                                                                                                            |
| **OS Types**             | Windows                                                                                                                              |
| **Number of Machines**   | n/a                                                                                                                                  |
| **Total Runtime**        | n/a                                                                                                                                  |
| **Year of Collection**   | 2023                                                                                                                                 |
| **Attack Categories**    | Resource Development<br/>Execution<br/>Discovery<br/>Privilege Escalation<br/>Defense Evasion<br/>Credential Access<br/>Exfiltration |
| **Benign Activity**      | None                                                                                                                                 |
|                          |                                                                                                                                      |
| **Packed Size**          | 423 MB                                                                                                                               |
| **Unpacked Size**        | ~1 GB                                                                                                                                |
| **Download Link**        | [goto](https://github.com/OTRF/Security-Datasets/tree/master/datasets/compound)                                                      |

***

### Overview

This is a subset of the Security Datasets Collection, containing seven distinct datasets, each focusing on exploiting
Windows Local Security Authority Subsystem Service (LSASS), with slight variations between runs.

### Environment

I am simply assuming the scenario here is a single OS, as the attack scenario is kind of suggesting it.
However, this already exhausts the available information - there is no description regarding the victim, and any details
about the attack process are only available in the form of command line I/O produced by the attacker.

### Activity

For each of the seven simulation runs, the overall goal was to steal credential material from the process memory
of `LSASS.exe` leveraging meterpreter combined with mimikatz.
Main differences between individual runs include the methods of initial entry, or how information is exfiltrated later
on.

### Contained Data

For each simulation, there exists a YAML file containing metadata information, including a rough outline of the attack
procedure.
Log data is available in the form of `pcaps` for packet captures, `.json` for Windows events and `.log` for Zeek logs.
Labels are not provided.

### Links

- [Metadata](https://github.com/OTRF/Security-Datasets/tree/master/datasets/compound/_metadata)
- [Datasets](https://github.com/OTRF/Security-Datasets/tree/master/datasets/compound)

### Data Examples

Snippet of Windows events taken from `datasets/compound/lsass_campaign_01/metasploit_procdump_lsass_memory_dump.json`

```
{"SourceName":"Microsoft-Windows-Sysmon","ProviderGuid":"{5770385f-c22a-43e0-bf4c-06f5698ffbd9}","Level":"4","Keywords":"0x8000000000000000","Channel":"Microsoft-Windows-Sysmon/Operational","Hostname":"ACCT01.pandalab.com","TimeCreated":"2023-08-15T05:34:54.574Z","@timestamp":"2023-08-15T05:34:54.574Z","EventID":7,"Message":"Image loaded:\r\nRuleName: -\r\nUtcTime: 2023-08-16 00:34:54.390\r\nProcessGuid: {19de6d3b-1978-64dc-100c-000000000c00}\r\nProcessId: 4196\r\nImage: C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe\r\nImageLoaded: C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\92.0.902.67\\telclient.dll\r\nFileVersion: 92.0.902.67\r\nDescription: Microsoft Edge\r\nProduct: Microsoft Edge\r\nCompany: Microsoft Corporation\r\nOriginalFileName: telclient.dll\r\nHashes: SHA1=9E45CAA88981F4824081B54B091CD7A61779C931,MD5=39FEC6969A1EC6462A7303E533A9F08B,SHA256=54974FBA11E994711CC1D57DD3A73C32D244672EF796985D1D6157ACCA0E6FFC,IMPHASH=D9F56A467B70D54F9E55CE6457BCE171\r\nSigned: true\r\nSignature: Microsoft Corporation\r\nSignatureStatus: Valid\r\nUser: PANDALAB\\nora.quemona","Task":"7","RuleName":"-","UtcTime":"2023-08-16 00:34:54.390","ProcessGuid":"{19de6d3b-1978-64dc-100c-000000000c00}","ProcessId":"4196","Image":"C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe","ImageLoaded":"C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\92.0.902.67\\telclient.dll","FileVersion":"92.0.902.67","Description":"Microsoft Edge","Product":"Microsoft Edge","Company":"Microsoft Corporation","OriginalFileName":"telclient.dll","Hashes":"SHA1=9E45CAA88981F4824081B54B091CD7A61779C931,MD5=39FEC6969A1EC6462A7303E533A9F08B,SHA256=54974FBA11E994711CC1D57DD3A73C32D244672EF796985D1D6157ACCA0E6FFC,IMPHASH=D9F56A467B70D54F9E55CE6457BCE171","Signed":"true","Signature":"Microsoft Corporation","SignatureStatus":"Valid","User":"PANDALAB\\nora.quemona"}
{"SourceName":"Microsoft-Windows-Sysmon","ProviderGuid":"{5770385f-c22a-43e0-bf4c-06f5698ffbd9}","Level":"4","Keywords":"0x8000000000000000","Channel":"Microsoft-Windows-Sysmon/Operational","Hostname":"ACCT01.pandalab.com","TimeCreated":"2023-08-15T05:34:54.574Z","@timestamp":"2023-08-15T05:34:54.574Z","EventID":7,"Message":"Image loaded:\r\nRuleName: -\r\nUtcTime: 2023-08-16 00:34:54.390\r\nProcessGuid: {19de6d3b-19ad-64dc-360c-000000000c00}\r\nProcessId: 6984\r\nImage: C:\\Users\\NORA~1.QUE\\AppData\\Local\\Temp\\RarSFX1\\winx64_payload.exe\r\nImageLoaded: C:\\Windows\\System32\\wininet.dll\r\nFileVersion: 11.00.19041.1566 (WinBuild.160101.0800)\r\nDescription: Internet Extensions for Win32\r\nProduct: Internet Explorer\r\nCompany: Microsoft Corporation\r\nOriginalFileName: wininet.dll\r\nHashes: SHA1=451D8D0470CEDB268619BA1E7AE78ADAE0EBA692,MD5=11F7419009AF2874C4B0E4505D185D79,SHA256=AC24CCE72F82C3EBBE9E7E9B80004163B9EED54D30467ECE6157EE4061BEAC95,IMPHASH=C720594958CDF760C61C102397D71D3B\r\nSigned: true\r\nSignature: Microsoft Windows\r\nSignatureStatus: Valid\r\nUser: PANDALAB\\nora.quemona","Task":"7","RuleName":"-","UtcTime":"2023-08-16 00:34:54.390","ProcessGuid":"{19de6d3b-19ad-64dc-360c-000000000c00}","ProcessId":"6984","Image":"C:\\Users\\NORA~1.QUE\\AppData\\Local\\Temp\\RarSFX1\\winx64_payload.exe","ImageLoaded":"C:\\Windows\\System32\\wininet.dll","FileVersion":"11.00.19041.1566 (WinBuild.160101.0800)","Description":"Internet Extensions for Win32","Product":"Internet Explorer","Company":"Microsoft Corporation","OriginalFileName":"wininet.dll","Hashes":"SHA1=451D8D0470CEDB268619BA1E7AE78ADAE0EBA692,MD5=11F7419009AF2874C4B0E4505D185D79,SHA256=AC24CCE72F82C3EBBE9E7E9B80004163B9EED54D30467ECE6157EE4061BEAC95,IMPHASH=C720594958CDF760C61C102397D71D3B","Signed":"true","Signature":"Microsoft Windows","SignatureStatus":"Valid","User":"PANDALAB\\nora.quemona"}
{"SourceName":"Microsoft-Windows-Sysmon","ProviderGuid":"{5770385f-c22a-43e0-bf4c-06f5698ffbd9}","Level":"4","Keywords":"0x8000000000000000","Channel":"Microsoft-Windows-Sysmon/Operational","Hostname":"ACCT01.pandalab.com","TimeCreated":"2023-08-15T05:34:54.574Z","@timestamp":"2023-08-15T05:34:54.574Z","EventID":7,"Message":"Image loaded:\r\nRuleName: -\r\nUtcTime: 2023-08-16 00:34:54.390\r\nProcessGuid: {19de6d3b-19ad-64dc-360c-000000000c00}\r\nProcessId: 6984\r\nImage: C:\\Users\\NORA~1.QUE\\AppData\\Local\\Temp\\RarSFX1\\winx64_payload.exe\r\nImageLoaded: C:\\Windows\\System32\\msvcrt.dll\r\nFileVersion: 7.0.19041.546 (WinBuild.160101.0800)\r\nDescription: Windows NT CRT DLL\r\nProduct: Microsoft® Windows® Operating System\r\nCompany: Microsoft Corporation\r\nOriginalFileName: msvcrt.dll\r\nHashes: SHA1=5AFF4CFDEE689F127DF3C555281DC629D4D62318,MD5=A4F2D5942FB447CD48A5CEE414983E85,SHA256=DD7C8BC34CDBE30EF921395E874909BBF6BE53803822164F75F7207E9F085650,IMPHASH=1273683626EBBA703979F188A1E64237\r\nSigned: true\r\nSignature: Microsoft Windows\r\nSignatureStatus: Valid\r\nUser: PANDALAB\\nora.quemona","Task":"7","RuleName":"-","UtcTime":"2023-08-16 00:34:54.390","ProcessGuid":"{19de6d3b-19ad-64dc-360c-000000000c00}","ProcessId":"6984","Image":"C:\\Users\\NORA~1.QUE\\AppData\\Local\\Temp\\RarSFX1\\winx64_payload.exe","ImageLoaded":"C:\\Windows\\System32\\msvcrt.dll","FileVersion":"7.0.19041.546 (WinBuild.160101.0800)","Description":"Windows NT CRT DLL","Product":"Microsoft® Windows® Operating System","Company":"Microsoft Corporation","OriginalFileName":"msvcrt.dll","Hashes":"SHA1=5AFF4CFDEE689F127DF3C555281DC629D4D62318,MD5=A4F2D5942FB447CD48A5CEE414983E85,SHA256=DD7C8BC34CDBE30EF921395E874909BBF6BE53803822164F75F7207E9F085650,IMPHASH=1273683626EBBA703979F188A1E64237","Signed":"true","Signature":"Microsoft Windows","SignatureStatus":"Valid","User":"PANDALAB\\nora.quemona"}
{"SourceName":"Microsoft-Windows-Sysmon","ProviderGuid":"{5770385f-c22a-43e0-bf4c-06f5698ffbd9}","Level":"4","Keywords":"0x8000000000000000","Channel":"Microsoft-Windows-Sysmon/Operational","Hostname":"ACCT01.pandalab.com","TimeCreated":"2023-08-15T05:34:54.574Z","@timestamp":"2023-08-15T05:34:54.574Z","EventID":7,"Message":"Image loaded:\r\nRuleName: -\r\nUtcTime: 2023-08-16 00:34:54.390\r\nProcessGuid: {19de6d3b-19ad-64dc-360c-000000000c00}\r\nProcessId: 6984\r\nImage: C:\\Users\\NORA~1.QUE\\AppData\\Local\\Temp\\RarSFX1\\winx64_payload.exe\r\nImageLoaded: C:\\Windows\\System32\\advapi32.dll\r\nFileVersion: 10.0.19041.1682 (WinBuild.160101.0800)\r\nDescription: Advanced Windows 32 Base API\r\nProduct: Microsoft® Windows® Operating System\r\nCompany: Microsoft Corporation\r\nOriginalFileName: advapi32.dll\r\nHashes: SHA1=693D29E59790C281A1D269EC26B9F1ABCEF6A7C0,MD5=7EBC4745686496918EF54660CB9640DE,SHA256=5B3ED19956537019C29AABC9DF6B8669C8EF725090BB76DAE46D5E093AB7ED09,IMPHASH=6AAF6F02EEA8BCA6277AB2AABDA3266D\r\nSigned: true\r\nSignature: Microsoft Windows\r\nSignatureStatus: Valid\r\nUser: PANDALAB\\nora.quemona","Task":"7","RuleName":"-","UtcTime":"2023-08-16 00:34:54.390","ProcessGuid":"{19de6d3b-19ad-64dc-360c-000000000c00}","ProcessId":"6984","Image":"C:\\Users\\NORA~1.QUE\\AppData\\Local\\Temp\\RarSFX1\\winx64_payload.exe","ImageLoaded":"C:\\Windows\\System32\\advapi32.dll","FileVersion":"10.0.19041.1682 (WinBuild.160101.0800)","Description":"Advanced Windows 32 Base API","Product":"Microsoft® Windows® Operating System","Company":"Microsoft Corporation","OriginalFileName":"advapi32.dll","Hashes":"SHA1=693D29E59790C281A1D269EC26B9F1ABCEF6A7C0,MD5=7EBC4745686496918EF54660CB9640DE,SHA256=5B3ED19956537019C29AABC9DF6B8669C8EF725090BB76DAE46D5E093AB7ED09,IMPHASH=6AAF6F02EEA8BCA6277AB2AABDA3266D","Signed":"true","Signature":"Microsoft Windows","SignatureStatus":"Valid","User":"PANDALAB\\nora.quemona"}
```

Snippet of Zeek DNS logs taken from `datasets/compound/lsass_campaign_01/dns.log`

```
#separator \x09
#set_separator	,
#empty_field	(empty)
#unset_field	-
#path	dns
#open	2023-08-16-01-28-55
#fields	ts	uid	id.orig_h	id.orig_p	id.resp_h	id.resp_p	proto	trans_id	rtt	query	qclass	qclass_name	qtype	qtype_name	rcode	rcode_name	AA	TC	RD	RA	Z	answers	TTLs	rejected
#types	time	string	addr	port	addr	port	enum	count	interval	string	count	string	count	string	count	string	bool	bool	bool	bool	count	vector[string]	vector[interval]	bool
1692161622.036086	Cnsu5m395zFmE9ikp4	192.168.1.41	52605	192.168.1.4	53	udp	58519	-	-	-	-	-	-	2	SERVFAIL	F	F	F	F	0	-	-	T
1692161629.312072	CgOrga4zQDw8ry59Qe	192.168.1.41	49556	192.168.1.4	53	udp	28710	-	-	-	-	-	-	2	SERVFAIL	F	F	F	F	0	-	-	T
1692161636.595716	C5ezKH2fe1RCVUrfO6	192.168.1.41	63829	192.168.1.4	53	udp	58824	-	-	-	-	-	-	2	SERVFAIL	F	F	F	F	0	-	-	T
1692161639.326842	C525iO2kFboDzCCLj9	192.168.1.41	49556	192.168.1.4	53	udp	28710	-	-	-	-	-	-	2	SERVFAIL	F	F	F	F	0	-	-	T
1692161641.909849	CFNoQW3Mwdu9LAHzB8	192.168.1.41	65243	192.168.1.4	53	udp	34082	-	-	-	-	-	-	3	NXDOMAIN	F	F	F	F	0	-	-	F
```