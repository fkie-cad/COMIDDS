---
title: Twente 2014 Dataset
---

- [Overview](#overview)
- [Environment](#environment)
- [Activity](#activity)
- [Contained Data](#contained-data)
- [Papers](#papers)
- [Links](#links)
- [Data Examples](#data-examples)

| <!-- -->                 | <!-- -->                                                      |
|--------------------------|---------------------------------------------------------------|
| **Network Data Source**  | NetFlows (ssh auth only)                                      |
| **Network Data Labeled** | Yes                                                           |
| **Host Data Source**     | ssh auth logs                                                 |
| **Host Data Labeled**    | Yes                                                           |
|                          |                                                               |
| **Overall Setting**      | Enterprise OS                                                 |
| **OS Types**             | n/a                                                           |
| **Number of Machines**   | 93                                                            |
| **Total Runtime**        | 2 months                                                      |
| **Year of Collection**   | 2013-2014                                                     |
| **Attack Categories**    | ssh bruteforce                                                |
| **Benign Activity**      | Real users                                                    |
|                          |                                                               |
| **Packed Size**          | 2,42 GB                                                       |
| **Unpacked Size**        | 5,76 GB                                                       |
| **Download Link**        | [goto](https://www.simpleweb.org/wiki/index.php/SSH_datasets) |

***

### Overview

This dataset originated from the desire to detect whether an SSH bruteforce attack was successful on a network level (as
opposed to just detecting that one *happened*).
The authors note that this is of course trivial on a host-level, but argue that doing so on a network-level benefits
scalability of detection methods.
To evaluate their approach, two datasets consisting of host logs and network flows were derived from a production
network.
The approach itself will not be discussed here, refer to the referenced paper for further interest.

### Environment

For dataset 1, the environment consisted of 17 honeypots, while for dataset 2 it was made up of 76 servers and four
workstations.
Further details are not provided.

### Activity

No deliberate red team activity is mentioned, most likely implying that all malicious activity comes from the outside.
Note that anything that is *not* an SSH-bruteforce attack is ignored here.
Data was collected from Nov-Dec 2013 (dataset 1) and Jan-Feb 2014 (dataset 2).

### Contained Data

Generally, collected data consists of network flows originating from SSH connections detected on one of four routers,
and host ssh authentication logs.
The latter is used to verify if an SSH login was successful and subsequently determine the labels of corresponding
network flows.

IP addresses and usernames have been anonymized, though for usernames this was done destructively (all names replaced
by "XXXXX").
Host log data is organized per machine, while network flows are organized by time and day and in the form of Cisco's
netflow, which is a binary format.

The authors simply labeled flows as compromises using the following definition:
All successful authentications after more than 6 login attempts with no idle period longer than 60 minutes and not
coming from an IP address range within the network.
Other flows matching this definition without being successful are considered malicious.

### Papers

- [SSH Compromise Detection Using NetFlow/IPFIX (2014)](https://doi.org/10.1145/2677046.2677050)

### Links

- [Homepage](https://www.simpleweb.org/wiki/index.php/SSH_datasets.html)

### Data Examples

Snippet of host ssh authentication logs taken from `dataset2/161.166.1.36/auth.log.anon`

```
Jan 30 07:56:45 161.166.1.38 sshd[5935]: Failed password for XXXXX from 5.140.143.157 port 4590 ssh2
Jan 30 07:56:45 161.166.1.38 sshd[5935]: Disconnecting: Too many authentication failures for XXXXX [preauth]
Jan 30 07:56:45 161.166.1.38 sshd[5935]: PAM 5 more authentication failures; logname= uid=0 euid=0 tty=ssh ruser= rhost=5.140.143.157  user=XXXXX
Jan 30 07:56:45 161.166.1.38 sshd[5935]: PAM service(sshd) ignoring max retries; 6 > 3
Jan 30 07:56:45 161.166.1.38 sshd[5933]: Failed password for XXXXX from 5.140.143.157 port 1685 ssh2
Jan 30 07:56:45 161.166.1.38 sshd[5933]: Disconnecting: Too many authentication failures for XXXXX [preauth]
Jan 30 07:56:45 161.166.1.38 sshd[5933]: PAM 5 more authentication failures; logname= uid=0 euid=0 tty=ssh ruser= rhost=5.140.143.157  user=XXXXX
Jan 30 07:56:45 161.166.1.38 sshd[5933]: PAM service(sshd) ignoring max retries; 6 > 3
Jan 30 07:56:49 161.166.1.38 sshd[5937]: pam_krb5(sshd:auth): authentication failure; logname=XXXXX uid=0 euid=0 tty=ssh ruser= rhost=5.140.143.157
Jan 30 07:56:49 161.166.1.38 sshd[5937]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=5.140.143.157  user=XXXXX
Jan 30 07:56:49 161.166.1.38 sshd[5937]: pam_ldap: ldap_simple_bind Can't contact LDAP server
Jan 30 07:56:49 161.166.1.38 sshd[5937]: pam_ldap: reconnecting to LDAP server...
```