---
title: DARPA TC3
---

- [Overview](#overview)
- [Environment](#environment)
- [Activity](#activity)
- [Contained Data](#contained-data)
- [Links](#links)
- [Related Entries](#related-entries)
- [Data Examples](#data-examples)

| <!-- -->                 | <!-- -->                                                                                  |
|--------------------------|-------------------------------------------------------------------------------------------|
| **Network Data Source**  | -                                                                                         |
| **Network Data Labeled** | -                                                                                         |
| **Host Data Source**     | Custom event logs                                                                         |
| **Host Data Labeled**    | Ground truth provided                                                                     |
|                          |                                                                                           |
| **Overall Setting**      | Undisclosed                                                                               |
| **OS Types**             | Windows?                                                                                  |
| **Number of Machines**   | n/a                                                                                       |
| **Total Runtime**        | 8 days                                                                                    |
| **Year of Collection**   | 2018                                                                                      |
| **Attack Categories**    | Backdoor<br/>Loader Drakon APT<br/>Port Scans<br/>Process Elevation<br/>Process Injection |
| **Benign Activity**      | Present, but not specified                                                                |
|                          |                                                                                           |
| **Packed Size**          | 115 GB                                                                                    |
| **Unpacked Size**        | n/a                                                                                       |
| **Download Link**        | [goto](https://drive.google.com/drive/folders/1QlbUFWAGq3Hpl8wVdzOdIoZLFxkII4EK)          |

***

### Overview

The DARPA Transparent Computing (TC) 3 dataset originated from the third of five what the authors call engagements.
The purpose of these operations was to test and evaluate methods of providing visibility into system interactions, aka
technologies to read and record provenance data between entities (--> "Transparent Computing").
"Technical areas" (TAs) were defined, and each "TA performer" is tasked with fulfilling a certain goal:

- TA1: Tagging and Tracking (aka logging)
- TA2: Detection and Policy Enforcement
- TA3: Architecture
- TA4: Scenario Development
- TA5.1: Adversarial Challenge Team

The data released by DARPA contains only information from TA1 and TA5.1, or in other words, log data and ground truth
about executed attacks.

### Environment

Sadly, no information regarding the underlying architecture is present;
I can only presume that Windows hosts made up the majority of the machines, guessing from the referenced targets in the
ground truth.

### Activity

Unspecified "benign background traffic" was run continuously during the testing period, while attacks were only
performed from 0900 to 1700 on weekdays.
The ground truth suggests a total runtime of 8 days, from 06.04.2018 to 13.04.2018.
Performed attacks are divided into three groups with different capabilities:

- Nation State, focusing on stealing proprietary and personal information
- Common Threat, focusing on stealing personally identifiable information (PII) data for financial gain
- Metasploit, simply consisting of launching a few one-off attacks using metasploit

Details regarding these attacks are available in the provided ground truth file, and the provided information can in
theory be used to label datasets.

### Contained Data

Log collection was done by five different TA1 performers, named after the corresponding project (cadets, clearscope,
fivedirections, theia, and trace).
These projects differ in how they balance tracking detail against the resulting system overhead, though exact details
are not available.
All of them store collected data using a predefined data model, offering information about the event, its parameters,
and its parents, accompanied by IDs to allow for the previously mentioned provenance visibility.
Further specifications of the data model are linked below, but no information regarding the actual collection process is
provided.

Note that not all datasets contain "good data" according to DARPA, i.e., they might be missing records or do not include
any useful activity.
A list of "topics containing good data" is provided on their GitHub page.
As mentioned, labels are not provided, but the provided ground truth could be used to identify IOCs.

### Links

- [GitHub README](https://github.com/darpa-i2o/Transparent-Computing/blob/master/README-E3.md)
- [GDrive](https://drive.google.com/drive/folders/1QlbUFWAGq3Hpl8wVdzOdIoZLFxkII4EK)
- [Ground Truth](https://drive.google.com/file/d/1mrs4LWkGk-3zA7t7v8zrhm0yEDHe57QU/view?usp=drive_link)
- [Data Model Description](https://drive.google.com/file/d/15FGTHmOYcBrJka41SfPEy5-fQaoH1s88/view?usp=drive_link)

### Related Entries

- [DARPA TC5](darpa_tc5.md)

### Data Examples

Snippet of json entries taken from `data/fivedirections/ta1-fivedirections-e3-official-3.json`

```json
{"datum":{"com.bbn.tc.schema.avro.cdm18.Event":{"uuid":"A75339EC-D9A7-4864-A0A2-991EB8C1168C","sequence":{"long":0},"type":"EVENT_OPEN","threadId":{"int":0},"hostId":"47923ED7-29D4-4E65-ABA2-F70A4E74DCCD","subject":{"com.bbn.tc.schema.avro.cdm18.UUID":"185AE3D6-EFB1-49A7-9B65-25E4F0933D13"},"predicateObject":{"com.bbn.tc.schema.avro.cdm18.UUID":"62DA9728-17B0-4A1B-8E42-75920F77D454"},"predicateObjectPath":{"string":"\\Device\\HarddiskVolume2\\Windows\\System32\\taskschd.dll"},"predicateObject2":null,"predicateObject2Path":null,"timestampNanos":1523627150493000000,"name":{"string":"EVENT_OPEN"},"parameters":null,"location":{"long":0},"size":{"long":0},"programPoint":null,"properties":{"map":{"FileAttributes":"0","CreateOptions":"1200000","ShareAccess":"7"}}}},"CDMVersion":"18","source":"SOURCE_WINDOWS_FIVEDIRECTIONS"}
{"datum":{"com.bbn.tc.schema.avro.cdm18.Event":{"uuid":"43E4A983-D6A8-495B-BFDC-B84727AC4BDC","sequence":{"long":0},"type":"EVENT_CHECK_FILE_ATTRIBUTES","threadId":{"int":0},"hostId":"47923ED7-29D4-4E65-ABA2-F70A4E74DCCD","subject":{"com.bbn.tc.schema.avro.cdm18.UUID":"185AE3D6-EFB1-49A7-9B65-25E4F0933D13"},"predicateObject":{"com.bbn.tc.schema.avro.cdm18.UUID":"62DA9728-17B0-4A1B-8E42-75920F77D454"},"predicateObjectPath":{"string":"\\Device\\HarddiskVolume2\\Windows\\System32\\taskschd.dll"},"predicateObject2":null,"predicateObject2Path":null,"timestampNanos":1523627150493000000,"name":{"string":"EVENT_CHECK_FILE_ATTRIBUTES"},"parameters":null,"location":{"long":0},"size":{"long":0},"programPoint":null,"properties":{"map":{"FileKey":"ffff8d82f6c0dbf0","ExtraInfo":"0","FileObject":"ffffc3030f9412b0","InfoClass":"FileBasicInformation"}}}},"CDMVersion":"18","source":"SOURCE_WINDOWS_FIVEDIRECTIONS"}
{"datum":{"com.bbn.tc.schema.avro.cdm18.Event":{"uuid":"112C1E96-FB3D-4153-A419-3AEE04559754","sequence":{"long":0},"type":"EVENT_OPEN","threadId":{"int":0},"hostId":"47923ED7-29D4-4E65-ABA2-F70A4E74DCCD","subject":{"com.bbn.tc.schema.avro.cdm18.UUID":"185AE3D6-EFB1-49A7-9B65-25E4F0933D13"},"predicateObject":{"com.bbn.tc.schema.avro.cdm18.UUID":"62DA9728-17B0-4A1B-8E42-75920F77D454"},"predicateObjectPath":{"string":"\\Device\\HarddiskVolume2\\Windows\\System32\\taskschd.dll"},"predicateObject2":null,"predicateObject2Path":null,"timestampNanos":1523627150493000000,"name":{"string":"EVENT_OPEN"},"parameters":null,"location":{"long":0},"size":{"long":0},"programPoint":null,"properties":{"map":{"FileAttributes":"0","CreateOptions":"1000060","ShareAccess":"5"}}}},"CDMVersion":"18","source":"SOURCE_WINDOWS_FIVEDIRECTIONS"}
{"datum":{"com.bbn.tc.schema.avro.cdm18.Event":{"uuid":"93E553CA-0246-4DA8-BAA2-10FBE55D3B30","sequence":{"long":0},"type":"EVENT_CHECK_FILE_ATTRIBUTES","threadId":{"int":0},"hostId":"47923ED7-29D4-4E65-ABA2-F70A4E74DCCD","subject":{"com.bbn.tc.schema.avro.cdm18.UUID":"185AE3D6-EFB1-49A7-9B65-25E4F0933D13"},"predicateObject":{"com.bbn.tc.schema.avro.cdm18.UUID":"62DA9728-17B0-4A1B-8E42-75920F77D454"},"predicateObjectPath":{"string":"\\Device\\HarddiskVolume2\\Windows\\System32\\taskschd.dll"},"predicateObject2":null,"predicateObject2Path":null,"timestampNanos":1523627150493000000,"name":{"string":"EVENT_CHECK_FILE_ATTRIBUTES"},"parameters":null,"location":{"long":0},"size":{"long":0},"programPoint":null,"properties":{"map":{"FileKey":"ffff8d82f6c0dbf0","ExtraInfo":"0","FileObject":"ffffc3030f9412b0","InfoClass":"FileBasicInformation"}}}},"CDMVersion":"18","source":"SOURCE_WINDOWS_FIVEDIRECTIONS"}
{"datum":{"com.bbn.tc.schema.avro.cdm18.Event":{"uuid":"9EBBD3FD-BE9A-47C9-BE23-6E6C6069DDB7","sequence":{"long":0},"type":"EVENT_CHECK_FILE_ATTRIBUTES","threadId":{"int":0},"hostId":"47923ED7-29D4-4E65-ABA2-F70A4E74DCCD","subject":{"com.bbn.tc.schema.avro.cdm18.UUID":"185AE3D6-EFB1-49A7-9B65-25E4F0933D13"},"predicateObject":{"com.bbn.tc.schema.avro.cdm18.UUID":"62DA9728-17B0-4A1B-8E42-75920F77D454"},"predicateObjectPath":{"string":"\\Device\\HarddiskVolume2\\Windows\\System32\\taskschd.dll"},"predicateObject2":null,"predicateObject2Path":null,"timestampNanos":1523627150493000000,"name":{"string":"EVENT_CHECK_FILE_ATTRIBUTES"},"parameters":null,"location":{"long":0},"size":{"long":0},"programPoint":null,"properties":{"map":{"FileKey":"ffff8d82f6c0dbf0","ExtraInfo":"0","FileObject":"ffffc3030f9412b0","InfoClass":"FileBasicInformation"}}}},"CDMVersion":"18","source":"SOURCE_WINDOWS_FIVEDIRECTIONS"}
{"datum":{"com.bbn.tc.schema.avro.cdm18.Event":{"uuid":"73F1C6FF-2575-4780-B5E1-E7AECD8AC2D4","sequence":{"long":0},"type":"EVENT_CHECK_FILE_ATTRIBUTES","threadId":{"int":0},"hostId":"47923ED7-29D4-4E65-ABA2-F70A4E74DCCD","subject":{"com.bbn.tc.schema.avro.cdm18.UUID":"185AE3D6-EFB1-49A7-9B65-25E4F0933D13"},"predicateObject":{"com.bbn.tc.schema.avro.cdm18.UUID":"62DA9728-17B0-4A1B-8E42-75920F77D454"},"predicateObjectPath":{"string":"\\Device\\HarddiskVolume2\\Windows\\System32\\taskschd.dll"},"predicateObject2":null,"predicateObject2Path":null,"timestampNanos":1523627150493000000,"name":{"string":"EVENT_CHECK_FILE_ATTRIBUTES"},"parameters":null,"location":{"long":0},"size":{"long":0},"programPoint":null,"properties":{"map":{"FileKey":"ffff8d82f6c0dbf0","ExtraInfo":"0","FileObject":"ffffc3030f9412b0","InfoClass":"FileNameInformation"}}}},"CDMVersion":"18","source":"SOURCE_WINDOWS_FIVEDIRECTIONS"}
```

Snippet of json entries taken from `data/cadets/ta1-cadets-e3-official-2.json`

```json
{"datum":{"com.bbn.tc.schema.avro.cdm18.Event":{"uuid":"1B6D9E3A-1879-53DB-939F-62C8530975DB","sequence":{"long":1718664},"type":"EVENT_MMAP","threadId":{"int":100311},"hostId":"83C8ED1F-5045-DBCD-B39F-918F0DF4F851","subject":{"com.bbn.tc.schema.avro.cdm18.UUID":"7F075347-3E16-11E8-A5CB-3FA3753A265A"},"predicateObject":{"com.bbn.tc.schema.avro.cdm18.UUID":"FC2CA9A1-1BCF-8B57-8F1B-A854778B9026"},"predicateObjectPath":null,"predicateObject2":null,"predicateObject2Path":null,"timestampNanos":1523512697617160580,"name":{"string":"aue_mmap"},"parameters":{"array":[]},"location":null,"size":{"long":6598656},"programPoint":null,"properties":{"map":{"host":"83c8ed1f-5045-dbcd-b39f-918f0df4f851","partial_path":"/lib/libdevstat.so.7","fd":"3","exec":"vmstat","arg_mem_flags":"['PROT_READ']","ppid":"1349"}}}},"CDMVersion":"18","source":"SOURCE_FREEBSD_DTRACE_CADETS"}
{"datum":{"com.bbn.tc.schema.avro.cdm18.Event":{"uuid":"88E5A979-B2B3-5BA9-99B0-479EC8C817F8","sequence":{"long":1718665},"type":"EVENT_MMAP","threadId":{"int":100311},"hostId":"83C8ED1F-5045-DBCD-B39F-918F0DF4F851","subject":{"com.bbn.tc.schema.avro.cdm18.UUID":"7F075347-3E16-11E8-A5CB-3FA3753A265A"},"predicateObject":{"com.bbn.tc.schema.avro.cdm18.UUID":"FC2CA9A1-1BCF-8B57-8F1B-A854778B9026"},"predicateObjectPath":null,"predicateObject2":null,"predicateObject2Path":null,"timestampNanos":1523512697617160580,"name":{"string":"aue_mmap"},"parameters":{"array":[]},"location":null,"size":{"long":8572928},"programPoint":null,"properties":{"map":{"host":"83c8ed1f-5045-dbcd-b39f-918f0df4f851","partial_path":"/lib/libdevstat.so.7","fd":"3","exec":"vmstat","arg_mem_flags":"['PROT_READ', 'PROT_EXEC']","ppid":"1349"}}}},"CDMVersion":"18","source":"SOURCE_FREEBSD_DTRACE_CADETS"}
{"datum":{"com.bbn.tc.schema.avro.cdm18.Event":{"uuid":"B701826E-DC87-5A4F-B6B5-A822C65247B4","sequence":{"long":1718666},"type":"EVENT_MMAP","threadId":{"int":100311},"hostId":"83C8ED1F-5045-DBCD-B39F-918F0DF4F851","subject":{"com.bbn.tc.schema.avro.cdm18.UUID":"7F075347-3E16-11E8-A5CB-3FA3753A265A"},"predicateObject":{"com.bbn.tc.schema.avro.cdm18.UUID":"FC2CA9A1-1BCF-8B57-8F1B-A854778B9026"},"predicateObjectPath":null,"predicateObject2":null,"predicateObject2Path":null,"timestampNanos":1523512697617160580,"name":{"string":"aue_mmap"},"parameters":{"array":[]},"location":null,"size":{"long":8572928},"programPoint":null,"properties":{"map":{"host":"83c8ed1f-5045-dbcd-b39f-918f0df4f851","partial_path":"/lib/libdevstat.so.7","fd":"3","exec":"vmstat","arg_mem_flags":"['PROT_READ', 'PROT_EXEC']","ppid":"1349"}}}},"CDMVersion":"18","source":"SOURCE_FREEBSD_DTRACE_CADETS"}
{"datum":{"com.bbn.tc.schema.avro.cdm18.Event":{"uuid":"0E4F5CF7-9082-5DF6-A3E5-F10D5993B499","sequence":{"long":1718667},"type":"EVENT_MMAP","threadId":{"int":100311},"hostId":"83C8ED1F-5045-DBCD-B39F-918F0DF4F851","subject":{"com.bbn.tc.schema.avro.cdm18.UUID":"7F075347-3E16-11E8-A5CB-3FA3753A265A"},"predicateObject":{"com.bbn.tc.schema.avro.cdm18.UUID":"FC2CA9A1-1BCF-8B57-8F1B-A854778B9026"},"predicateObjectPath":null,"predicateObject2":null,"predicateObject2Path":null,"timestampNanos":1523512697617160580,"name":{"string":"aue_mmap"},"parameters":{"array":[]},"location":null,"size":{"long":10690560},"programPoint":null,"properties":{"map":{"host":"83c8ed1f-5045-dbcd-b39f-918f0df4f851","partial_path":"/lib/libdevstat.so.7","fd":"3","exec":"vmstat","arg_mem_flags":"['PROT_READ', 'PROT_WRITE']","ppid":"1349"}}}},"CDMVersion":"18","source":"SOURCE_FREEBSD_DTRACE_CADETS"}
{"datum":{"com.bbn.tc.schema.avro.cdm18.Event":{"uuid":"B009A4A1-FABE-58A8-94D1-3D5A46392D82","sequence":{"long":1718668},"type":"EVENT_MMAP","threadId":{"int":100311},"hostId":"83C8ED1F-5045-DBCD-B39F-918F0DF4F851","subject":{"com.bbn.tc.schema.avro.cdm18.UUID":"7F075347-3E16-11E8-A5CB-3FA3753A265A"},"predicateObject":{"com.bbn.tc.schema.avro.cdm18.UUID":"FC2CA9A1-1BCF-8B57-8F1B-A854778B9026"},"predicateObjectPath":null,"predicateObject2":null,"predicateObject2Path":null,"timestampNanos":1523512697617160580,"name":{"string":"aue_mmap"},"parameters":{"array":[]},"location":null,"size":{"long":10690560},"programPoint":null,"properties":{"map":{"host":"83c8ed1f-5045-dbcd-b39f-918f0df4f851","partial_path":"/lib/libdevstat.so.7","fd":"3","exec":"vmstat","arg_mem_flags":"['PROT_READ', 'PROT_WRITE']","ppid":"1349"}}}},"CDMVersion":"18","source":"SOURCE_FREEBSD_DTRACE_CADETS"}
{"datum":{"com.bbn.tc.schema.avro.cdm18.Event":{"uuid":"A8193F7F-AE4C-5965-8F1E-7EDB0A14CD6E","sequence":{"long":1718669},"type":"EVENT_CLOSE","threadId":{"int":100311},"hostId":"83C8ED1F-5045-DBCD-B39F-918F0DF4F851","subject":{"com.bbn.tc.schema.avro.cdm18.UUID":"7F075347-3E16-11E8-A5CB-3FA3753A265A"},"predicateObject":{"com.bbn.tc.schema.avro.cdm18.UUID":"FC2CA9A1-1BCF-8B57-8F1B-A854778B9026"},"predicateObjectPath":null,"predicateObject2":null,"predicateObject2Path":null,"timestampNanos":1523512697617160580,"name":{"string":"aue_close"},"parameters":{"array":[]},"location":null,"size":null,"programPoint":null,"properties":{"map":{"host":"83c8ed1f-5045-dbcd-b39f-918f0df4f851","return_value":"0","fd":"3","exec":"vmstat","ppid":"1349"}}}},"CDMVersion":"18","source":"SOURCE_FREEBSD_DTRACE_CADETS"}
```