---
title: KDD Cup 1999
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
| **Year of Collection**   | 1998                                                                               |
| **Attack Categories**    | DoS<br/>Remote to Local<br/>User to Root<br/>Surveillance/Probing                  |
| **Benign Activity**      | Scripts for synthetic traffic generation, real humans for performing complex tasks |
|                          |                                                                                    |
| **Packed Size**          | 18 MB                                                                              |
| **Unpacked Size**        | 743 MB                                                                             |
| **Download Link**        | [goto](http://kdd.ics.uci.edu/databases/kddcup99/kddcup.data.gz)                   |

***

### Overview

This dataset was used in the fifth International Conference on Knowledge Discovery and Data Mining (KDD'99).
It is itself based on data captured in DARPAs '98 IDS evaluation program, which contains data collected from a total of
nine weeks of synthetic network activity, including a small variety of attacks.
The task for participants was to develop a "network intrusion detector", a model capable of distinguishing between bad
and good/normal connections.
Like the dataset it is based on, due to its age and a number of flaws, it should be used with reservations, if at all.

### Environment

Refer to the underlying [DARPA'98 Intrusion Detection Program](darpa98.md).

### Activity

Refer to the underlying [DARPA'98 Intrusion Detection Program](darpa98.md).

### Contained Data

The raw DARPA data, which comes in the form of binary TCP dumps, is divided and processed into seven weeks (~five
million connection records) of training data, and two weeks (~two million connection records) of test data.
A connection record is defined as "a sequence of TCP packets starting and ending at some well-defined times, between
which data flows to and from a source IP address to a target IP address under some well-defined protocol".
Each of these connection records contains 41 features (description linked below), with a 42nd label indicating whether
this event is normal or malicious, which in the latter case also references the specific attack that event belongs to.

The KDD'99 dataset fixes some issues present in its DARPA foundation, which was severely affected by simulation
artifacts (e.g., attack traffic could often easily be distinguished by looking only at the TTL).
However, it introduces some problems of its own, such as the distribution of data being noticeably uneven (hindering
cross-validation), the large number of redundant/duplicate records, or the fact that DoS attacks constitute the vast
majority (71%) of the entire test data set.

### Papers

- [A detailed analysis of the KDD CUP 99 data set (2009)](https://doi.org/10.1109/cisda.2009.5356528)

### Links

- [Homepage](https://kdd.ics.uci.edu/databases/kddcup99/kddcup99.html)
- [Detailed Feature Description](https://kdd.ics.uci.edu/databases/kddcup99/task.html)

### Related Entries

- [NSL KDD](nsl_kdd_dataset.md)
- [DARPA'98 Intrusion Detection Program](darpa98.md)

### Data Examples

Labeled features taken from `kddcup.data`.

```
[...]
1,tcp,smtp,SF,2633,331,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,2,3,0.00,0.00,0.00,0.00,1.00,0.00,0.67,222,168,0.76,0.02,0.00,0.00,0.00,0.00,0.00,0.00,normal.
2,tcp,smtp,SF,974,327,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,1,0.00,0.00,0.00,0.00,1.00,0.00,0.00,223,169,0.76,0.02,0.00,0.00,0.00,0.00,0.00,0.00,normal.
12359,tcp,telnet,SF,3676,23454,0,0,0,2,0,1,2,0,0,4,20,0,0,0,0,0,1,1,0.00,0.00,0.00,0.00,1.00,0.00,0.00,1,3,1.00,0.00,1.00,0.67,0.00,0.00,0.00,0.00,normal.
12345,tcp,telnet,SF,8070,14511,0,0,0,0,0,1,1,0,0,0,35,0,5,0,0,0,1,1,0.00,0.00,0.00,0.00,1.00,0.00,0.00,2,4,1.00,0.00,0.50,0.50,0.00,0.00,0.00,0.00,normal.
0,tcp,http,S0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1.00,1.00,0.00,0.00,1.00,0.00,0.00,3,1,0.33,0.67,0.33,0.00,0.33,1.00,0.00,0.00,neptune.
0,tcp,http,S0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,1.00,1.00,0.00,0.00,1.00,0.00,0.00,4,2,0.50,0.50,0.25,0.00,0.50,1.00,0.00,0.00,neptune.
0,tcp,http,S0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,3,1.00,1.00,0.00,0.00,1.00,0.00,0.00,5,3,0.60,0.40,0.20,0.00,0.60,1.00,0.00,0.00,neptune.
0,tcp,http,S0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,4,1.00,1.00,0.00,0.00,1.00,0.00,0.00,6,4,0.67,0.33,0.17,0.00,0.67,1.00,0.00,0.00,neptune.
[...]
```

List of attack types taken from `training_attack_types`.

```
back dos
buffer_overflow u2r
ftp_write r2l
guess_passwd r2l
imap r2l
ipsweep probe
land dos
loadmodule u2r
multihop r2l
neptune dos
nmap probe
perl u2r
phf r2l
pod dos
portsweep probe
rootkit u2r
satan probe
smurf dos
spy r2l
teardrop dos
warezclient r2l
warezmaster r2l
```