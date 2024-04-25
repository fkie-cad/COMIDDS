---
title: LID-DS 2019
---

- [Overview](#overview)
- [Environment](#environment)
- [Activity](#activity)
- [Contained Data](#contained-data)
- [Papers](#papers)
- [Links](#links)
- [Data Examples](#data-examples)

| <!-- -->                 | <!-- -->                                                                 |
|--------------------------|--------------------------------------------------------------------------|
| **Network Data Source**  | -                                                                        |
| **Network Data Labeled** | -                                                                        |
| **Host Data Source**     | Syscalls with parameter information                                      |
| **Host Data Labeled**    | Ground truth provided                                                    |
|                          |                                                                          |
| **Overall Setting**      | Single OS                                                                |
| **OS Types**             | Ubuntu 18.04                                                             |
| **Number of Machines**   | 1                                                                        |
| **Total Runtime**        | 30 seconds per sim                                                       |
| **Year of Collection**   | 2019                                                                     |
| **Attack Categories**    | Various CVEs                                                             |
| **Benign Activity**      | Synthetic                                                                |
|                          |                                                                          |
| **Packed Size**          | 13 GB                                                                    |
| **Unpacked Size**        | n/a                                                                      |
| **Download Link**        | [goto](https://cloud.scadsai.uni-leipzig.de/index.php/s/HLXiWssriRMt9pp) |

***

### Overview

The Leipzig Intrusion Detection Data Set (LID-DS) aims to provide a dataset that is suitable for evaluating Host Based
Intrusion Detection Systems (HIDSs) targeting Linux systems, based on system calls.
Notable features include integration of thread information and data buffers (instead of just syscall number), as well as
execution of a variety of attacks, based on CVEs/CWEs, within their simulations.
An updated version was released two years later in 2021, which featured different exploits and also collected network
traffic in addition to system call information.

### Environment

The general environment is a single Ubuntu 18.04 host inside a docker container.
Running services and their configurations are set up such that the requirements for a given exploit to work are present.

### Activity

The following CVEs/CWEs were selected for emulation:

- CVE-2014-0160, Heartbleed
- CWE-307, Improper Restriction of Excessive Authentication Attempts
- CWE-89, SQL Injection
- CWE-434, Unrestricted Upload of File with Dangerous Type (PHP)
- CVE-2014-3120, Arbitrary code execution
- CVE-2015-1427, Arbitrary code execution
- CVE-2014-6271, Shellshock
- CVE-2016-6515, Denial-of-service
- CVE-2015-5602, Local Privilege Escalation
- Zip Slip (known under several CVEs)
- CWE-434, Unrestricted Upload of File with Dangerous Type (eps)

For each attack type, 1000 runs were executed with only normal behavior, which was defined individually for each
attack (like normal data requests for SQL-injection), and 100 runs with normal behavior plus the respective attack
executed at a varying point of time.
Each simulation runs for approximately 30 seconds.

### Contained Data

The authors provide a readme (see download links below) detailing content and usage of the dataset.
In a nutshell, each simulation run generates one log file (as `.txt`, see example below), thus for each attack type
there are 1000 files with normal and 100 files with normal and malicious behavior.
These files provide information about system calls, along with relevant parameters.
Additionally, for each attack there is a `run.cvs` file, which contains metadata regarding each simulation.

### Papers

- [A Modern and Sophisticated Host Based Intrusion Detection Data set (2019)](https://dbs.uni-leipzig.de/research/publications/a-modern-and-sophisticated-host-based-intrusion-detection-data-set)
- [Dataset Report: LID-DS 2021](https://doi.org/10.1007/978-3-031-35190-7_6)

### Links

- [LID-DS on GitHub](https://github.com/LID-DS/LID-DS)
- [2019 Version Download](https://cloud.scadsai.uni-leipzig.de/index.php/s/HLXiWssriRMt9pp)
- [2021 Version Download](https://cloud.scadsai.uni-leipzig.de/index.php/s/cRswswLo2QfLNYL)

### Data Examples

Metadata taken from `Bruteforce_CWE-307/run.csv`

```
image_name, scenario_name, is_executing_exploit, warmup_time, recording_time, exploit_start_time
[...]
victim_bruteforce:latest, sweet_greider_4408, False, 10, 50, -1
victim_bruteforce:latest, slimy_bhabha_8709, False, 10, 55, -1
victim_bruteforce:latest, ripe_faraday_5596, True, 10, 35, 24
victim_bruteforce:latest, vast_hawking_7675, True, 10, 40, 27
[...]
```

Behavior data taken from `Bruteforce_CWE-307/ripe_faraday_5596.txt`.
These files follow the
format `event_number event_time cpu user_uid process_name thread_id event_direction event_type event_arguments`.

```
[...]
51153 01:47:31.305890363 3 33 apache2 29915 < writev res=31 data=.....=.....o..OU...~..y.WY...+. 
51154 01:47:31.305897206 3 33 apache2 29915 > shutdown fd=12(<4t>172.17.0.1:41097->172.17.0.3:443) how=1(SHUT_WR) 
51155 01:47:31.305898142 3 33 apache2 29915 < shutdown res=-107(ENOTCONN) 
51156 01:47:31.305899247 3 33 apache2 29915 > close fd=12(<4t>172.17.0.1:41097->172.17.0.3:443) 
51157 01:47:31.305899697 3 33 apache2 29915 < close res=0 
[...]
```