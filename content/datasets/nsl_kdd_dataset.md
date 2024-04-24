---
title: NSL-KDD
---

- [Overview](#overview)
- [Environment](#environment)
- [Activity](#activity)
- [Contained Data](#contained-data)
- [Papers](#papers)
- [Links](#links)
- [Related Entries](#related-entries)
- [Data Examples](#data-examples)

| <!-- -->                 | <!-- -->                                                                           |
|--------------------------|------------------------------------------------------------------------------------|
| **Network Data Source**  | Connection records                                                                 |
| **Network Data Labeled** | Yes                                                                                |
| **Host Data Source**     | -                                                                                  |
| **Host Data Labeled**    | -                                                                                  |
|                          |                                                                                    |
| **Overall Setting**      | Military IT                                                                        |
| **OS Types**             | Linux 2.0.27<br/>SunOS 4.1.4<br/>Sun Solaris 2.5.1<br/>Windows NT                  |
| **Number of Machines**   | 1000's                                                                             |
| **Total Runtime**        | Nine weeks                                                                         |
| **Year of Collection**   | 1998, updated 2009                                                                 |
| **Attack Categories**    | DoS<br/>Remote to Local<br/>User to Root<br/>Surveillance/Probing                  |
| **Benign Activity**      | Scripts for synthetic traffic generation, real humans for performing complex tasks |
|                          |                                                                                    |
| **Packed Size**          | 6 MB                                                                               |
| **Unpacked Size**        | 19 MB                                                                              |
| **Download Link**        | [goto](https://github.com/HoaNP/NSL-KDD-DataSet)                                   |

***

### Overview

An improvement of the original KDD'99 dataset, aiming to fix some of its statistical problems.
KDD'99 is itself based on data captured in DARPAs '98 IDS evaluation program, which contains data collected from a total
of nine weeks of synthetic network activity, including a small variety of attacks.
Like the dataset it is based on, due to its age and other potential flaws, it should be used with reservations, if at
all.

### Environment

Refer to the underlying [DARPA'98 Intrusion Detection Program](darpa98.md).

### Activity

Refer to the underlying [DARPA'98 Intrusion Detection Program](darpa98.md).

### Contained Data

The original version - the KDD Cup 1999 dataset - contained a large number of redundant/duplicate records, which was problematic for two reasons:

- In the training set, it caused classifiers to be biased towards those more frequent records
- In the test set, it caused evaluation to be biased towards learners having better detection rates on artificially
  frequent records

Thus, this new version attempts to rectify these issues by removing duplicates.
In addition to this, the authors define a "difficulty" for each event; by leveraging 21 classifiers (7 different models,
each trained 3 times), an events difficulty was determined by the number of classifiers which did (not) label a given
event correctly.
This difficulty feature was then used to resample the dataset, such that the number of records from each difficulty
group is inversely proportional to the number of records in the original dataset, which, the authors argue, facilitates
evaluation.
The difficulty is available as a new feature of each event (the last one).

Note that the original download source is now longer accessible, however, an unofficial copy is available via an individuals GitHub repository.

### Papers

- [A detailed analysis of the KDD CUP 99 data set (2009)](https://doi.org/10.1109/cisda.2009.5356528)
- [A Study on NSL-KDD Dataset for Intrusion Detection Systems Based on Classification Algorithms (2013)](https://e-tarjome.com/storage/btn_uploaded/2019-07-13/1563006133_9702-etarjome-English.pdf)

### Links

- [Homepage](https://www.unb.ca/cic/datasets/nsl.html)
- [Unofficial Download Source](https://github.com/HoaNP/NSL-KDD-DataSet)

### Related Entries

- [KDD Cup 1999](kdd_cup_1999.md)
- [DARPA'98 Intrusion Detection Program](darpa98.md)

### Data Examples

Labeled features, including the new difficulty feature, taken from KDDTrain+.txt

```
[...]
0,tcp,http,SF,281,1951,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,30,31,0.00,0.00,0.00,0.00,1.00,0.00,0.06,77,255,1.00,0.00,0.01,0.03,0.00,0.01,0.00,0.00,normal,21
0,tcp,bgp,S0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,138,25,1.00,1.00,0.00,0.00,0.18,0.05,0.00,255,25,0.10,0.05,0.00,0.00,1.00,1.00,0.00,0.00,neptune,18
0,udp,domain_u,SF,42,42,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,6,0.00,0.00,0.00,0.00,1.00,0.00,0.50,255,245,0.96,0.01,0.01,0.00,0.00,0.00,0.00,0.00,normal,21
0,tcp,ftp,S0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,300,7,1.00,1.00,0.00,0.00,0.02,0.06,0.00,255,7,0.03,0.07,0.00,0.00,1.00,1.00,0.00,0.00,neptune,18
0,tcp,time,S0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,199,9,1.00,1.00,0.00,0.00,0.05,0.07,0.00,255,9,0.04,0.07,0.00,0.00,1.00,1.00,0.00,0.00,neptune,18
0,tcp,http,SF,263,453,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,15,15,0.00,0.00,0.00,0.00,1.00,0.00,0.00,255,255,1.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,normal,21
36613,tcp,private,RSTR,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,0.00,0.00,1.00,1.00,1.00,0.00,0.00,255,2,0.01,0.50,1.00,0.00,0.00,0.00,1.00,1.00,portsweep,15
0,tcp,ftp,RSTO,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0.00,0.00,1.00,1.00,1.00,0.00,0.00,212,43,0.20,0.02,0.00,0.00,0.00,0.00,0.06,0.12,normal,13
0,tcp,private,S0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,144,15,1.00,1.00,0.00,0.00,0.10,0.06,0.00,255,30,0.12,0.06,0.00,0.00,1.00,1.00,0.00,0.00,neptune,18
0,tcp,sql_net,S0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,104,4,1.00,1.00,0.00,0.00,0.04,0.07,0.00,255,18,0.07,0.07,0.00,0.00,1.00,1.00,0.00,0.00,neptune,19
0,tcp,http,SF,283,1980,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,18,18,0.00,0.00,0.00,0.00,1.00,0.00,0.00,18,255,1.00,0.00,0.06,0.03,0.00,0.00,0.00,0.00,normal,21
0,tcp,http,SF,161,5530,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,2,2,0.00,0.00,0.00,0.00,1.00,0.00,0.00,2,255,1.00,0.00,0.50,0.05,0.00,0.00,0.00,0.00,normal,21
0,tcp,http,SF,211,321,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,7,11,0.00,0.00,0.00,0.00,1.00,0.00,0.27,211,255,1.00,0.00,0.00,0.01,0.00,0.00,0.00,0.00,normal,21
0,tcp,http,SF,201,1701,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,7,7,0.00,0.00,0.00,0.00,1.00,0.00,0.00,32,255,1.00,0.00,0.03,0.04,0.00,0.00,0.00,0.00,normal,21
[...]
```