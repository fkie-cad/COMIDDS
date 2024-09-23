---
title: I-SEC-IDS
---

- [Overview](#overview)
- [Environment](#environment)
- [Activity](#activity)
- [Contained Data](#contained-data)
- [Papers](#papers)
- [Links](#links)
- [Data Examples](#data-examples)

| <!-- -->                 | <!-- -->                                                          |
| ------------------------ | ----------------------------------------------------------------- |
| **Network Data Source**  | NetFlows                                                          |
| **Network Data Labeled** | Yes                                                               |
| **Host Data Source**     | -                                                                 |
| **Host Data Labeled**    | -                                                                 |
|                          |                                                                   |
| **Overall Setting**      | Single OS                                                         |
| **OS Types**             | Windows 10                                                        |
| **Number of Machines**   | 1                                                                 |
| **Total Runtime**        | n/a                                                               |
| **Year of Collection**   | 2021                                                              |
| **Attack Categories**    | DoS, Scanning                                                     |
| **User Emulation**       | n/a                                                               |
|                          |                                                                   |
| **Packed Size**          | 66 MB                                                             |
| **Unpacked Size**        | -                                                                 |
| **Download Link**        | [goto](https://gitlab.unige.ch/Benedetto.Serinelli/i-sec-dataset) |

***

### Overview
The I-SEC-IDS dataset (exact meaning of the acronym unknown) consists of a small amount of network flows collected from a singular VM under attack.
It does not feature user behavior or any other notable properties.

### Environment
The collection environment consists of one host running two virtual machines, victim and attacker, operating on Windows 10 and Kali Linux, respectively.
Network traffic is collected and processed on the host machine.

### Activity
Over an unspecified amount of time, six individual attacks are carried out, three of which are DoS, while the other three are scanning attacks.
DoS attacks are executed using `hping3` with the following parameter (each targeting different TCP flags):
- dos_fin: `hping3 –flood -F -q -d 15000 <victim-ip>`
- dos_sync: `hping3 –flood -S -q -d 15000 <victim-ip>`
- dos_rpau: `hping3 –flood -R -P -A -U -q -d 15000 <victim-ip>`
Similarly, scanning attacks utilize three different `nmap` commands:
- nmap_1: `nmap -sS -O <victim-ip>`
- nmap_2: `nmap -sV <victim-ip>`
- nmap_3: `nmap -iR 100000000 -Pn <victim-ip>`

### Contained Data
Network traffic, collected in the form of pcaps, is processed into NetFlows using CICs [CICFlowMeter](https://www.unb.ca/cic/research/applications.html#CICFlowMeter).
These are then labeled (though this process is not further detailed) and divided into six `.csv` files, one for each of the six mentioned attacks.
Additionally, the author provides a second version of these files with a reduced feature set, removing values strongly correlated to the label (such as the IP address).

### Papers
- [Toward Generating a DoS and Scan Statistical Network Traffic Metrics for Building Intrusion Detection Solution Based on Machine and Deep Learning: I-Sec-IDS Datasets (2022)](https://doi.org/10.5281/zenodo.6657210)

### Links
- [Dataset Repository](https://gitlab.unige.ch/Benedetto.Serinelli/i-sec-dataset)

### Data Examples
Labeled NetFlows taken from `dos_fin.csv`.

<!--  {% raw %} -->
```
"Protocol","Flow.Duration","Tot.Fwd.Pkts","Tot.Bwd.Pkts","TotLen.Fwd.Pkts","TotLen.Bwd.Pkts","Fwd.Pkt.Len.Max","Fwd.Pkt.Len.Min","Fwd.Pkt.Len.Mean","Fwd.Pkt.Len.Std","Bwd.Pkt.Len.Max","Bwd.Pkt.Len.Min","Bwd.Pkt.Len.Mean","Bwd.Pkt.Len.Std","Flow.Byts.s","Flow.Pkts.s","Flow.IAT.Mean","Flow.IAT.Std","Flow.IAT.Max","Flow.IAT.Min","Fwd.IAT.Tot","Fwd.IAT.Mean","Fwd.IAT.Std","Fwd.IAT.Max","Fwd.IAT.Min","Bwd.IAT.Tot","Bwd.IAT.Mean","Bwd.IAT.Std","Bwd.IAT.Max","Bwd.IAT.Min","Fwd.PSH.Flags","Bwd.PSH.Flags","Fwd.URG.Flags","Bwd.URG.Flags","Fwd.Header.Len","Bwd.Header.Len","Fwd.Pkts.s","Bwd.Pkts.s","Pkt.Len.Min","Pkt.Len.Max","Pkt.Len.Mean","Pkt.Len.Std","Pkt.Len.Var","FIN.Flag.Cnt","SYN.Flag.Cnt","RST.Flag.Cnt","PSH.Flag.Cnt","ACK.Flag.Cnt","URG.Flag.Cnt","CWR.Flag.Count","ECE.Flag.Cnt","Down.Up.Ratio","Pkt.Size.Avg","Fwd.Seg.Size.Avg","Bwd.Seg.Size.Avg","Fwd.Byts.b.Avg","Fwd.Pkts.b.Avg","Fwd.Blk.Rate.Avg","Bwd.Byts.b.Avg","Bwd.Pkts.b.Avg","Bwd.Blk.Rate.Avg","Subflow.Fwd.Pkts","Subflow.Fwd.Byts","Subflow.Bwd.Pkts","Subflow.Bwd.Byts","Init.Fwd.Win.Byts","Init.Bwd.Win.Byts","Fwd.Act.Data.Pkts","Fwd.Seg.Size.Min","Active.Mean","Active.Std","Active.Max","Active.Min","Idle.Mean","Idle.Std","Idle.Max","Idle.Min","Label"
6,1486,5,2,935,325,935,0,187,418.1447118,325,0,162.5,229.8097039,847913.8627,4710.632571,247.6666667,282.4554242,694,3,1486,371.5,496.6074909,1068,3,694,694,0,694,694,0,0,0,0,124,40,3364.73755,1345.89502,0,935,157.5,334.1086222,111628.5714,0,0,1,1,0,0,0,1,0,180,187,162.5,0,0,0,0,0,0,5,935,2,325,65535,32768,1,20,0,0,0,0,0,0,0,0,0
6,16518,5,2,935,259,935,0,187,418.1447118,259,0,129.5,183.1406563,72284.78024,423.7801187,2753,6446.971444,15910,7,16518,4129.5,8067.116895,16229,8,15910,15910,0,15910,15910,0,0,0,0,124,40,302.7000848,121.0800339,0,935,149.25,330.1734393,109014.5,0,0,1,1,0,0,0,1,0,170.5714286,187,129.5,0,0,0,0,0,0,5,935,2,259,65535,32768,1,20,0,0,0,0,0,0,0,0,0
6,18809,5,2,935,336,935,0,187,418.1447118,336,0,168,237.5878785,67574.03371,372.1622627,3134.833333,7413.02463,18265,7,18809,4702.25,9225.555679,18540,10,18265,18265,0,18265,18265,0,0,0,0,124,40,265.8301877,106.3320751,0,935,158.875,334.918087,112170.125,0,0,1,1,0,0,0,1,0,181.5714286,187,168,0,0,0,0,0,0,5,935,2,336,65535,32768,1,20,0,0,0,0,0,0,0,0,0
6,1343,5,2,935,247,935,0,187,418.1447118,247,0,123.5,174.655375,880119.1363,5212.211467,223.8333333,287.1873372,743,7,1343,335.75,496.8167838,1062,8,743,743,0,743,743,0,0,0,0,124,40,3723.008191,1489.203276,0,935,147.75,329.6304208,108656.2143,0,0,1,1,0,0,0,1,0,168.8571429,187,123.5,0,0,0,0,0,0,5,935,2,247,65535,32768,1,20,0,0,0,0,0,0,0,0,0
6,1267,5,2,935,267,935,0,187,418.1447118,267,0,133.5,188.7975106,948697.7111,5524.861878,211.1666667,273.7717419,710,6,1267,316.75,474.9802627,1014,6,710,710,0,710,710,0,0,0,0,124,40,3946.329913,1578.531965,0,935,150.25,330.5652086,109273.3571,0,0,1,1,0,0,0,1,0,171.7142857,187,133.5,0,0,0,0,0,0,5,935,2,267,65535,32768,1,20,0,0,0,0,0,0,0,0,0
6,33543,5,2,935,342,935,0,187,418.1447118,342,0,171,241.8305192,38070.53633,208.6873565,5590.5,13383.55728,32908,7,33543,8385.75,16587.19069,33266,7,32908,32908,0,32908,32908,0,0,0,0,124,40,149.0623975,59.62495901,0,935,159.625,335.3777987,112478.2679,0,0,1,1,0,0,0,1,0,182.4285714,187,171,0,0,0,0,0,0,5,935,2,342,65535,32768,1,20,0,0,0,0,0,0,0,0,0
6,1367,5,2,935,309,935,0,187,418.1447118,309,0,154.5,218.4959954,910021.9459,5120.702268,227.8333333,308.4142777,807,7,1367,341.75,522.0059866,1112,7,807,807,0,807,807,0,0,0,0,124,40,3657.644477,1463.057791,0,935,155.5,333.0087944,110894.8571,0,0,1,1,0,0,0,1,0,177.7142857,187,154.5,0,0,0,0,0,0,5,935,2,309,65535,32768,1,20,0,0,0,0,0,0,0,0,0
6,1315,5,2,935,299,935,0,187,418.1447118,299,0,149.5,211.4249276,938403.0418,5323.193916,219.1666667,272.3045476,700,6,1315,328.75,477.5153575,1024,6,700,700,0,700,700,0,0,0,0,124,40,3802.281369,1520.912548,0,935,154.25,332.3684487,110468.7857,0,0,1,1,0,0,0,1,0,176.2857143,187,149.5,0,0,0,0,0,0,5,935,2,299,65535,32768,1,20,0,0,0,0,0,0,0,0,0
6,8190,5,2,935,275,935,0,187,418.1447118,275,0,137.5,194.4543648,147741.1477,854.7008547,1365,3051.575855,7588,7,8190,2047.5,3920.32945,7926,7,7588,7588,0,7588,7588,0,0,0,0,124,40,610.5006105,244.2002442,0,935,151.25,330.9806857,109548.2143,0,0,1,1,0,0,0,1,0,172.8571429,187,137.5,0,0,0,0,0,0,5,935,2,275,65535,32768,1,20,0,0,0,0,0,0,0,0,0
6,14508,5,2,935,341,935,0,187,418.1447118,341,0,170.5,241.1234124,87951.47505,482.492418,2418,5684.793787,14020,6,14508,3627,7105.171544,14284,6,14020,14020,0,14020,14020,0,0,0,0,124,40,344.6374414,137.8549766,0,935,159.5,335.3002918,112426.2857,0,0,1,1,0,0,0,1,0,182.2857143,187,170.5,0,0,0,0,0,0,5,935,2,341,65535,32768,1,20,0,0,0,0,0,0,0,0,0
[...]
```
<!--  {% endraw %} -->