---
title: ADFA Linux Dataset
---

- [Overview](#overview)
- [Environment](#environment)
- [Activity](#activity)
- [Contained Data](#contained-data)
- [Papers](#papers)
- [Links](#links)
- [Related Entries](#related-entries)
- [Data Examples](#data-examples)

| <!-- -->                 | <!-- -->                                                                                  |
| ------------------------ | ----------------------------------------------------------------------------------------- |
| **Network Data Source**  | -                                                                                         |
| **Network Data Labeled** | -                                                                                         |
| **Host Data Source**     | Sequences of Syscall Numbers                                                              |
| **Host Data Labeled**    | Yes                                                                                       |
|                          |                                                                                           |
| **Overall Setting**      | Single OS                                                                                 |
| **OS Types**             | Ubuntu 11.04 LTS                                                                          |
| **Number of Machines**   | 1                                                                                         |
| **Total Runtime**        | n/a                                                                                       |
| **Year of Collection**   | 2013                                                                                      |
| **Attack Categories**    | Password Bruteforce <br> Social Engineering <br> Web-Based Attacks <br> Remote Exploits   |
| **Benign Activity**      | Synthetic, unspecified "normal operation"                                                 |
|                          |                                                                                           |
| **Packed Size**          | 2 MB                                                                                      |
| **Unpacked Size**        | 17 MB                                                                                     |
| **Download Link**        | [goto (inofficial)](https://github.com/verazuo/a-labelled-version-of-the-ADFA-LD-dataset) |

***

### Overview

The ADFA (Australian Defence Force Academy) datasets, specifically ADFA-LD (Linux Dataset) and ADFA-WD (Windows
Dataset), are designed for the evaluation of anomaly-based intrusion detection systems (IDS).
These datasets were introduced to address the limitations of older datasets, such as the KDD'99 dataset, which had
become outdated given the evolution of cyber threats.
They specifically focus on detection methods leveraging sequences of system calls.

Note: The storage provider 

### Environment

The environment consisted of a single host running Ubuntu 11.04 LTS, which was configured to emulate a (at the time)
modern Linux local server, equipped with services such as MySQL, FTP, and SSH, while being fully patched.
A specific vulnerable version of TikiWiki introduced a potential attack vector for remote exploitation - the authors
argue that this represents a minor flaw in an otherwise well-configured server, reflecting real-world scenarios.

### Activity

Several attacks were performed on the host during data collection:

- Password bruteforce via FTP
- Password bruteforce via SSH
- Adding new superuser using client-side poisoned executable
- Java-based meterpreter by exploiting TikiWiki vulnerability
- Linux meterpreter payload using client-side poisoned executable
- C100 Webshell using PHP remote file inclusion vulnerability

In addition to this, there is also "normal behavior", which is not further detailed by the authors.

### Contained Data

Data is collected in the form of syscall numbers, originating from the unspecified normal behavior and the listed
attacks.
The collected sequences are organized into Training and Validation traces, which exclusively contain benign traces, and
Attack traces, which exclusively feature traces of the performed attacks.
Attack traces are further grouped by their attack types.

Each individual file is in the `.txt` format, simply containing integers separated by spaces.
Labels are not explicitly given, but can of course be derived from the assigned category, Training, Validation, or
Attack.

### Papers

- [Generation of a new IDS Test Dataset: Time to Retire the KDD Collection (2013)](https://doi.org/10.1109/wcnc.2013.6555301)
- [A Semantic Approach to Host Based Intrusion Detection Systems Using Contiguous and Discontiguous System Call Patterns (2014)](https://doi.org/10.1109/tc.2013.13)

### Links

- [Homepage](https://research.unsw.edu.au/projects/adfa-ids-datasets)
- [ADFA-LD Download (inofficial)](https://github.com/verazuo/a-labelled-version-of-the-ADFA-LD-dataset)

*Note: The original version of this dataset was hosted on ClourStor, which shut down in 2023.
At the time of writing, links on the official homepage have not been updated.*

### Related Entries

- [ADFA-WD](/COMIDDS/content/datasets/adfa_wd)

### Data Examples

Syscall numbers stored in `.txt` files.

```
125 5 3 3 3 3 3 3 3 4 4 3 3 102 5 197 192 3 6 91 102 102 102 6 102 102 6 5 197 192 3 3 6 91 5 197 192 3 3 6 91 240 5 197
192 3 3 6 91 5 197  192 6 33 5 3 197 192 192 6 125 91 5 197 192 6 33 5 3 197 192 192 6 125 91 195 5 197 192 3 3 6 91 102
4 5 142 4 4 13 102 6 142 3 3 13 199 5 140 197 192 140 91 6 5 140 197 192 140 91 6 4 6 142 4 4 13 102 3 3 13 199 5 140
197 192 140 13 102
```