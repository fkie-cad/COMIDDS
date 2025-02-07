---
title: Biblio-US17
---

- [Overview](#overview)
- [Environment](#environment)
- [Activity](#activity)
- [Contained Data](#contained-data)
- [Papers](#papers)
- [Links](#links)

| <!-- -->                 | <!-- -->                                                                                                                                         |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Network Data Source**  | HTTP requests (selected fields)                                                                                                                  |
| **Network Data Labeled** | Yes                                                                                                                                              |
| **Host Data Source**     | -                                                                                                                                                |
| **Host Data Labeled**    | -                                                                                                                                                |
|                          |                                                                                                                                                  |
| **Overall Setting**      | Enterprise IT                                                                                                                                    |
| **OS Types**             | Undisclosed                                                                                                                                      |
| **Number of Machines**   | 1                                                                                                                                                |
| **Total Runtime**        | 198 days                                                                                                                                         |
| **Year of Collection**   | 2017                                                                                                                                             |
| **Attack Categories**    | Unknown                                                                                                                                          |
| **User Emulation**       | Real users                                                                                                                                       |
|                          |                                                                                                                                                  |
| **Packed Size**          | 1,1 GB                                                                                                                                           |
| **Unpacked Size**        | 6 GB                                                                                                                                             |
| **Download Link**        | [must be requested](https://idus.us.es/items/53034f60-d215-44b0-a198-eb8a5229218e/request-a-copy?bitstream=b1b0c077-6f87-4160-8659-9dc34e269e3d) |

***

### Overview
The Biblio-US17 dataset consists of selected features extracted from ~48 million web requests recorded from a webserver at the University of Seville (Spain).
The recording period spanned 6.5 months and includes benign usage during that time.
Requests are made available in a labeled, but heavily anonymized form.

### Environment
The web server in question is an Apache Web Server v2.2, traffic is scanned by a number of intrusion detection systems (Snort, Nemesida, Modsecurity with paranoia level 1 and 2).
Further details, other than that this server is used in/by a library, are not available.

### Activity
Details, such as the purpose of this server within its environment, are not available.
Data is recorded from 2017-01-01 to 2017-07-17, 2017, for a total of 198 days.

### Contained Data
Requests are grouped by day and each assigned an identifier of the form `[MM-DD-Fxxxxxx]`, with the first four digits representing the corresponding month and day, `F` signifying the protocol (A for HTTP, S for HTTPS) and the remainder being a unique number for that day.
For each request, only the following information is available:
- Method
- URI (anonymized)
- Protocol
- Response code
- Response size

With an example looking like this:
```
[02-18-A001234] GET /2003/padron.html HTTP/1.1″ 200 11800
```
Notably, fine-grained timestamps are *not* available.
Labels are available in a separate file;
for each request a line beginning with the same identifier indicates which IDSs triggered on this request.
The researches then manually determine whether this is a true or false positive, leveraging additional info presented by the intrusion detection alerts.
Furthermore, additional labels inform about features like the confidence level of this attack which range from level 1 to 4, with level 1 being a confirmed attack.
For additional information, refer to the README linked below, which documents all fields in a concise way.

### Papers
- [Biblio-US17: A labeled real URL dataset for anomaly-based intrusion detection systems development (2024)](https://doi.org/10.1145/3655693.3661319)

### Links
- [Homepage](https://idus.us.es/items/53034f60-d215-44b0-a198-eb8a5229218e)
  - [README](https://idus.us.es/server/api/core/bitstreams/2b3d8c75-6d36-47a5-83e7-f1cfc2cbc151/content)
