---
title: UGR'16
---

- [Overview](#overview)
- [Environment](#environment)
- [Activity](#activity)
- [Contained Data](#contained-data)
- [Papers](#papers)
- [Links](#links)
- [Data Examples](#data-examples)

| <!-- -->                 | <!-- -->                                |
|--------------------------|-----------------------------------------|
| **Network Data Source**  | NetFlows                                |
| **Network Data Labeled** | Yes                                     |
| **Host Data Source**     | -                                       |
| **Host Data Labeled**    | -                                       |
|                          |                                         |
| **Overall Setting**      | Tier 3 ISP network                      |
| **OS Types**             | n/a                                     |
| **Number of Machines**   | 27                                      |
| **Total Runtime**        | ~130 days                               |
| **Year of Collection**   | 2016                                    |
| **Attack Categories**    | DoS<br/>Port Scanning<br/>Botnet        |
| **Benign Activity**      | Real users                              |
|                          |                                         |
| **Packed Size**          | 236 GB                                  |
| **Unpacked Size**        | n/a                                     |
| **Download Link**        | [goto](https://nesg.ugr.es/nesg-ugr16/) |

***

### Overview

The UGR'16 dataset (name taken from the acronym of the University of Granada) is a network dataset collected from a real
cloud network accessed by a variety of clients, with some additional victim machines added.
It consists of anonymized network flows collected over a span of ~130 days, with attack traffic injected during the last
30 days.
All traffic has been labeled, though the authors note that this is a complex task for "real" data, as the number and
kind of attacks contained is unknown.
Notable features of this dataset include the scope, which enables analysis of long-running patters, and the use of
representative network traffic.

### Environment

The environment is an unspecified ISP cloud production network, with two victim subnets and one attacker subnet added to
facilitate red team activity.

### Activity

The total collection period lasted 130 days, with attacks being performed during the last 30.
Attack batches include:

- Low-rate DoS with some variations
- Port scanning
- Botnet traffic

### Contained Data

Flows are collected using Netflow, divided into a "calibration set" containing 100 days of "normal" behavior (though
this does not imply complete absence of attacks), and a "test set" containing one month of normal behavior plus
execution of attack batches.
All IP addresses have been anonymized using `nfanon`.
The authors discuss three different labels:

- Normal: Flows synthetically generated with normal patterns
- Attack: Flows the authors positively know to correspond to an attack
- Background: Flows where "no one really knows"

Since there are no synthetically generated normal patterns, collected flows received either the "attack" or "background"
label.
For injected attacks, signature detection was used to label flows originating from these attacks.
For the remaining (real) flows, which are very likely to contain actual attacks, the authors leveraged anomaly detection
to label unusual occurrences, such as increased requests to certain ports or email campaigns, though they do note that
not necessarily all of these correspond to real attacks.

Netflow data is grouped into one file per week, available as `nfcapd` (which contains all features) and
preprocessed `csv` (containing only some selected features, see section 3.D in paper), and only the latter is labeled.
Additionally, there is a `csv` file denoting the start and stop times of each attack within that week, and
separate `csv` files containing only those flows corresponding to a specific attack.

### Papers

- [UGR'16: A New Dataset for the Evaluation of Cyclostationarity-Based Network IDSs (2018)](https://doi.org/10.1016/j.cose.2017.11.004)

### Links

- [Homepage](https://nesg.ugr.es/nesg-ugr16/)

### Data Examples

Snippet of all preprocessed features taken from `july_week5_csv`

```
[...]
2016-07-27 13:43:30,0.000,42.219.154.107,143.72.8.137,59212,53,UDP,.A....,0,0,1,72,background
2016-07-27 13:43:30,0.000,42.219.154.107,143.72.8.137,59372,53,UDP,.A....,0,0,1,55,background
2016-07-27 13:43:30,0.000,42.219.154.107,143.72.8.137,59576,53,UDP,.A....,0,0,1,67,background
2016-07-27 13:43:30,0.000,42.219.154.107,66.98.48.193,80,53367,TCP,.A....,0,72,1,52,background
2016-07-27 13:43:30,0.000,42.219.154.108,143.72.8.137,38817,53,UDP,.A....,0,0,1,76,background
2016-07-27 13:43:30,0.000,42.219.154.108,143.72.8.137,48279,53,UDP,.A....,0,0,1,76,background
2016-07-27 13:43:30,0.000,42.219.154.108,143.72.8.137,50098,53,UDP,.A....,0,0,1,74,background
2016-07-27 13:43:30,0.000,42.219.154.109,143.72.8.137,43109,53,UDP,.A....,0,0,1,75,background
2016-07-27 13:43:30,0.000,42.219.154.109,143.72.8.137,51872,53,UDP,.A....,0,0,1,69,background
2016-07-27 13:43:30,0.000,42.219.154.109,204.97.72.135,53,41040,UDP,.A....,0,0,1,176,background
2016-07-27 13:43:30,0.000,42.219.154.109,85.194.84.240,53,38814,UDP,.A....,0,0,1,160,background
[...]
```

Attack timestamps taken from `attack_ts_july_week5.csv`

```
,counter(mins),Dos,scan44,scan11,nerisbotnet,blacklist,anomaly-udpscan,anomaly-sshscan,anomaly-spam
2016-07-27 13:38:00,0,0,0,0,0,0,0,0,0
2016-07-27 13:39:00,1,0,0,0,0,0,0,0,0
2016-07-27 13:40:00,2,0,0,0,0,0,0,0,0
2016-07-27 13:41:00,3,0,0,0,0,0,0,0,0
2016-07-27 13:42:00,4,0,0,0,0,0,0,0,0
2016-07-27 13:43:00,5,0,0,0,0,1,0,0,0
2016-07-27 13:44:00,6,0,0,0,0,1,0,0,0
[...]
```

Preprocessed features corresponding to a DoS attack taken from `dos_july_week5_csv`

```
[...]
2016-07-28 13:14:17,0.000,42.219.150.242,42.219.152.20,6487,80,TCP,...RS.,0,0,2,200,dos
2016-07-28 13:14:17,0.000,42.219.152.20,42.219.150.242,80,6487,TCP,.A..S.,0,0,1,40,dos
2016-07-28 13:14:17,0.000,42.219.158.16,42.219.150.247,80,6649,TCP,.A..S.,0,0,1,40,dos
2016-07-28 13:14:17,0.000,42.219.150.241,42.219.154.69,6446,80,TCP,...RS.,0,0,2,200,dos
2016-07-28 13:14:17,0.000,42.219.154.69,42.219.150.241,80,6446,TCP,.A..S.,0,0,1,40,dos
2016-07-28 13:14:17,0.000,42.219.150.247,42.219.158.16,6650,80,TCP,...RS.,0,0,2,200,dos
2016-07-28 13:14:17,0.000,42.219.158.16,42.219.150.247,80,6650,TCP,.A..S.,0,0,1,40,dos
2016-07-28 13:14:17,0.004,42.219.150.242,42.219.152.20,6488,80,TCP,...RS.,0,0,2,200,dos
2016-07-28 13:14:17,0.000,42.219.152.20,42.219.150.242,80,6488,TCP,.A..S.,0,0,1,40,dos
[...]
```