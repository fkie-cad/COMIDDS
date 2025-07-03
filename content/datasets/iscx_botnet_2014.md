---
title: ISCX Botnet Dataset 2014
---

- [Overview](#overview)
- [Environment](#environment)
- [Activity](#activity)
- [Contained Data](#contained-data)
- [Papers](#papers)
- [Links](#links)
- [Related Entries](#related-entries)

| <!-- -->                 | <!-- -->      |
| ------------------------ | ------------- |
| **Network Data Source**  | pcaps         |
| **Network Data Labeled** | Yes           |
| **Host Data Source**     | -             |
| **Host Data Labeled**    | -             |
|                          |               |
| **Overall Setting**      | Enterprise IT |
| **OS Types**             | Undisclosed   |
| **Number of Machines**   | 2000+         |
| **Total Runtime**        | n/a           |
| **Year of Collection**   | 2004-2014     |
| **Attack Categories**    | Botnets       |
| **User Emulation**       | Real Users    |
|                          |               |
| **Packed Size**          | -             |
| **Unpacked Size**        | 13,8 GB       |
| **Download Link**        | n/a           |

***

### Overview
The ISCX Botnet Dataset originated from the need for a modern botnet dataset suitable for evaluation of botnet detection methods;
specifically, how much individual NetFlow features contribute towards detection.
To this end, three overarching shortcomings affecting (at the time) current datasets are laid out:
- Generality (few botnets included)
- Realism (environments are not realistic / long-lasting enough for a botnet to perform all malicious functionality)
- Representativeness (benign behavior does not resemble that of actual networks)
In order to alleviate these flaws, the authors combine traffic from three sources - ISOT Botnet, ISCX IDS 2012, and the Malware Capture Facility Project - with the goal of creating one novel dataset.

*Note: At the time of writing, this dataset has been taken down by the original authors.
Should you find a working download URL, please open a pull request.*

### Environment
For details regarding the respective underlying datasets, refer to the related entries and links below.

### Activity
The final dataset, divided into a training and test set, contains a total of 7 and 16 types of botnets, respectively (the latter containing more to to evaluate novelty detection).
For the training dataset, these are (total of 43.92% malicious):
| Botnet Name       | Type | Total Flows   |
| ----------------- | ---- | ------------- |
| Neris             | IRC  | 21159 (12%)   |
| Rbot              | IRC  | 39316 (22%)   |
| Virut             | HTTP | 1638 (0.94%)  |
| NSIS              | P2P  | 4336 (2.48%)  |
| SMTP Spam         | P2P  | 11296 (6.48%) |
| Zeus              | P2P  | 31 (0.01%)    |
| Zeus Control (C2) | P2P  | 20 (0.01%)    |

For the test dataset, these are (total of 44.97% malicious):
| Botnet Name       | Type | Total Flows   |
| ----------------- | ---- | ------------- |
| Neris             | IRC  | 25967 (5.67%) |
| Rbot              | IRC  | 83 (0.018%)   |
| Menti             | IRC  | 2878 (0.62%)  |
| Sogou             | HTTP | 89 (0.019%)   |
| Murlo             | IRC  | 4881 (1.06%)  |
| Virut             | HTTP | 58576 (12.8%) |
| NSIS              | P2P  | 757 (0.165%)  |
| Zeus              | P2P  | 502 (0.109%)  |
| SMTP Spam         | P2P  | 21633 (4.72%) |
| UDP Storm         | P2P  | 44062 (9.63%) |
| Tbot              | IRC  | 1296 (0.283)  |
| Weasel            | P2P  | 42313 (9.25%) |
| Zero Access       | P2P  | 1011 (0.221%) |
| Smoke Bot         | P2P  | 78 (0.17%)    |
| Zeus Control (C2) | P2P  | 31 (0.006%)   |
| ISCX IRC Bot      | P2P  | 1816 (0.387%) |

The remaining flows are all benign, though their exact nature is not detailed.

### Contained Data
The three sources have been combined using the overlay methodology [2], whereby malicious traffic was assigned to existing IPs outside the main network using the Bit-Twist packet generator.
This combination of malicious and benign traffic was then replayed via TCPReplay and captured by TCPdump, resulting in a single dataset which was then divided into a training and test set with the properties outlined above.
Labels are available in the form of IPs associated with each botnet and can be found in the homepage linked below.

### Papers
- [[1] Towards effective feature selection in machine learning-based botnet detection approaches (2014)](https://doi.org/10.1109/CNS.2014.6997492)
- [[2] Challenges in Experimenting with Botnet Detection Systems (2011)](https://www.semanticscholar.org/paper/Challenges-in-Experimenting-with-Botnet-Detection-Aviv-Haeberlen/324c3d0acd0c21f0d12894536eaa3597576aae56)

### Links
- [Homepage](https://www.unb.ca/cic/datasets/botnet.html)
- [Malware Capture Facility Project](https://www.stratosphereips.org/datasets-malware)
- [Bit-Twist packet generator](https://bittwist.sourceforge.io/)
  
### Related Entries
- [ISOT Botnet](isot_botnet.md)
- [ISCX IDS 2012](iscx_ids_2012.md)
