---
title: PWNJUTSU
---

- [Overview](#overview)
- [Environment](#environment)
- [Activity](#activity)
- [Contained Data](#contained-data)
- [Papers](#papers)
- [Links](#links)
- [Data Examples](#data-examples)

| <!-- -->                 | <!-- -->                                                                      |
|--------------------------|-------------------------------------------------------------------------------|
| **Network Data Source**  | pcaps, various logs (DNS, ssh, http, ssl, etc.)                               |
| **Network Data Labeled** | No                                                                            |
| **Host Data Source**     | Sysmon, auditd, Windows events, various logs (auth, Apache)                   |
| **Host Data Labeled**    | No                                                                            |
|                          |                                                                               |
| **Overall Setting**      | Miscellaneous                                                                 |
| **OS Types**             | Windows 2008<br/>Ubuntu 14.04 / 20.04                                         |
| **Number of Machines**   | 3                                                                             |
| **Total Runtime**        | n/a                                                                           |
| **Year of Collection**   | 2022                                                                          |
| **Attack Categories**    | Discovery<br/>Lateral Movement<br/>Credential Access<br/>Privilege Escalation |
| **Benign Activity**      | n/a                                                                           |
|                          |                                                                               |
| **Packed Size**          | 82 GB                                                                         |
| **Unpacked Size**        | n/a                                                                           |
| **Download Link**        | [goto](https://pwnjutsu.irisa.fr/dataset/)                                    |

***

### Overview
The PWNJUTSU dataset originated from the desire to facilitate research of APTs, which requires suitable datasets containing appropriate attacks.
For this purpose, the authors designed a framework to unequivocally describe the model of such an APT campaign, modelling various states of knowledge and control an attacker possesses over a network, and how they may move between these states.
Several red team professionals were individually tasked with exploiting a small network, with their behavior then being matched against this model.
The host and network logs extracted from this process form the PWNJUTSU dataset.
The main drawback, however, is that the resulting logs are not labeled.

### Environment
The entire infrastructure was deployed in a virtualized way on a dedicated server, hosting administrative services as well as several small networks.
Each participant was designated one such network instance within this infrastructure, consisting of one gateway and three machines ("level 1-3"), which the participant had to move through laterally.

Each set of three vulnerable machines runs Ubuntu 14.04, Windows 2008, and Ubuntu 20.04, respectively.
The first two machines are derivations of the Metasploitable 3 project, while the third (Ubuntu 20.04) is "custom", with four distinct vulnerabilities:
- vsftpd (CVE-2011-2523)
- drupal (CVE-2018-7600)
- ssh (weak root password)
- vnc (weak passphrase)

Various logging sources are configured/observed, for Linux systems those are auth, auditd and Apache, for Windows systems these are Sysmon and event logs (System, Application, Security).
Additionally, file watchers are present on all machines to observe the state of certain flag files, but these are negligible with respect to the final dataset.

### Activity
The authors developed a model for precisely describing the progression of an attacker, in the form of a state-machine.
A detailed explanation of this model goes beyond the scope of this summary and can be found in section 4 and 5 of the paper.
There isn't a fixed sequence of attacks, as each of the 22 participants was free to chose their method of intrusion and propagation throughout their individual instance of the network.

The goal for all participants was to find flags on each of the three machines, CTF-style.
In terms of MITRE tactics, which is also what the authors adhered to when describing this, these were achieved through a mix of Lateral Movement, Credential Access, Privilege Escalation, and Discovery.

### Contained Data
For each of the 22 runs, the following log data was collected:
- pcaps
- System logs (all aggregated into a single file)
    - auth, auditd and Apache for Linux
    - Sysmon and event logs (System, Application, Security) for Windows
- Various network logs (DNS, ssh, http, etc.)

Sadly, these logs are *not* labeled.
An additional 23rd run is available, which consists of just the configured network, without any malicious activity.
The authors provide an internal search engine, enabling exploration of the data online (linked below).

### Papers
- [PWNJUTSU: A Dataset and Semantics-Driven Approach to Retrace Attack Campaigns](https://doi.org/10.1109/TNSM.2022.3183476)

### Links
- [Homepage](https://pwnjutsu.irisa.fr/)
- [Data Search Engine](https://pwnjutsu.irisa.fr/search/)
- [Metasploitable 3](https://github.com/rapid7/metasploitable3)

### Data Examples
Snippet of system events taken from `pwnjutsu_dataset-system-json-n12.json`:
```json
{"raw": "node=n12-vm3 type=PROCTITLE msg=audit(1620633468.960:16324): proctitle=2F7573722F6C6F63616C2F7362696E2F73736864002D74", "sourcetype": "linux_audit", "source": "/var/log/audit/audit.log", "time": "2021-05-10 07:57:48.960 UTC", "host": "n12-vm3"}
{"raw": "node=n12-vm3 type=EXECVE msg=audit(1620633468.960:16324): argc=2 a0=\"/usr/local/sbin/sshd\" a1=\"-t\"", "sourcetype": "linux_audit", "source": "/var/log/audit/audit.log", "time": "2021-05-10 07:57:48.960 UTC", "host": "n12-vm3"}
{"raw": "node=n12-vm3 type=SYSCALL msg=audit(1620633468.960:16324): arch=c000003e syscall=59 success=yes exit=0 a0=5585fda1c330 a1=5585fd9883c0 a2=5585fdae78a0 a3=4040 items=2 ppid=1 pid=51782 auid=4294967295 uid=0 gid=0 euid=0 suid=0 fsuid=0 egid=0 sgid=0 fsgid=0 tty=(none) ses=4294967295 comm=\"sshd\" exe=\"/usr/local/sbin/sshd\" key=\"rootcmd\"", "sourcetype": "linux_audit", "source": "/var/log/audit/audit.log", "time": "2021-05-10 07:57:48.960 UTC", "host": "n12-vm3"}
{"raw": "node=n12-vm3 type=SERVICE_STOP msg=audit(1620633468.956:16323): pid=1 uid=0 auid=4294967295 ses=4294967295 msg='unit=ssh comm=\"systemd\" exe=\"/usr/lib/systemd/systemd\" hostname=? addr=? terminal=? res=success'", "sourcetype": "linux_audit", "source": "/var/log/audit/audit.log", "time": "2021-05-10 07:57:48.956 UTC", "host": "n12-vm3"}
{"raw": "node=n12-vm3 type=SERVICE_START msg=audit(1620633468.956:16322): pid=1 uid=0 auid=4294967295 ses=4294967295 msg='unit=ssh comm=\"systemd\" exe=\"/usr/lib/systemd/systemd\" hostname=? addr=? terminal=? res=success'", "sourcetype": "linux_audit", "source": "/var/log/audit/audit.log", "time": "2021-05-10 07:57:48.956 UTC", "host": "n12-vm3"}
{"raw": "node=n12-vm3 type=SERVICE_START msg=audit(1620633468.704:16321): pid=1 uid=0 auid=4294967295 ses=4294967295 msg='unit=ssh comm=\"systemd\" exe=\"/usr/lib/systemd/systemd\" hostname=? addr=? terminal=? res=failed'", "sourcetype": "linux_audit", "source": "/var/log/audit/audit.log", "time": "2021-05-10 07:57:48.704 UTC", "host": "n12-vm3"}
{"raw": "May 10 07:57:48 n12-vm3 snoopy[51783]: [login:(unknown) ssh:((undefined)) sid:51783 tty:(none) ((none)/(none)) uid:root(0)/root(0) cwd:/]: /usr/local/sbin/sshd", "sourcetype": "syslog", "source": "/var/log/auth.log", "time": "2021-05-10 07:57:48.000 UTC", "host": "n12-vm3"}
{"raw": "May 10 07:57:48 n12-vm3 snoopy[51782]: [login:(unknown) ssh:((undefined)) sid:51782 tty:(none) ((none)/(none)) uid:root(0)/root(0) cwd:/]: /usr/local/sbin/sshd -t", "sourcetype": "syslog", "source": "/var/log/auth.log", "time": "2021-05-10 07:57:48.000 UTC", "host": "n12-vm3"}
{"raw": "May 10 07:57:48 n12-vm3 sshd[51728]: Received signal 15; terminating.", "sourcetype": "syslog", "source": "/var/log/auth.log", "time": "2021-05-10 07:57:48.000 UTC", "host": "n12-vm3"}
{"raw": "node=n12-vm3 type=PROCTITLE msg=audit(1620633467.456:16320): proctitle=\"(resolved)\"", "sourcetype": "linux_audit", "source": "/var/log/audit/audit.log", "time": "2021-05-10 07:57:47.456 UTC", "host": "n12-vm3"}
{"raw": "node=n12-vm3 type=SYSCALL msg=audit(1620633467.456:16320): arch=c000003e syscall=42 success=yes exit=0 a0=11 a1=7ffd6ce6d880 a2=10 a3=7ffd6ce6d87c items=0 ppid=1 pid=653 auid=4294967295 uid=101 gid=103 euid=101 suid=101 fsuid=101 egid=103 sgid=103 fsgid=103 tty=(none) ses=4294967295 comm=\"systemd-resolve\" exe=\"/usr/lib/systemd/systemd-resolved\" key=\"network_connect_4\"", "sourcetype": "linux_audit", "source": "/var/log/audit/audit.log", "time": "2021-05-10 07:57:47.456 UTC", "host": "n12-vm3"}
```
Snippet of dns network logs taken from `pwnjutsu_dataset-network-json-player_12/player_12_536871846.pcap_dns.log`:
```json
{"ts":1620614187.474508,"uid":"CWm9gc1lRMpZUgMoi2","id.orig_h":"10.12.1.3","id.orig_p":53393,"id.resp_h":"10.12.1.254","id.resp_p":53,"proto":"udp","trans_id":50312,"query":"ntp.ubuntu.com","qclass":1,"qclass_name":"C_INTERNET","qtype":28,"qtype_name":"AAAA","AA":false,"TC":false,"RD":true,"RA":false,"Z":0,"rejected":false}
{"ts":1620614192.478704,"uid":"CHAmz33N2TmhXripsd","id.orig_h":"10.12.1.3","id.orig_p":33904,"id.resp_h":"10.1.2.2","id.resp_p":53,"proto":"udp","trans_id":50312,"query":"ntp.ubuntu.com","qclass":1,"qclass_name":"C_INTERNET","qtype":28,"qtype_name":"AAAA","AA":false,"TC":false,"RD":true,"RA":false,"Z":0,"rejected":false}
{"ts":1620614197.483901,"uid":"CHAmz33N2TmhXripsd","id.orig_h":"10.12.1.3","id.orig_p":33904,"id.resp_h":"10.1.2.2","id.resp_p":53,"proto":"udp","trans_id":50312,"query":"ntp.ubuntu.com","qclass":1,"qclass_name":"C_INTERNET","qtype":28,"qtype_name":"AAAA","AA":false,"TC":false,"RD":true,"RA":false,"Z":0,"rejected":false}
{"ts":1620614527.720085,"uid":"Ckb6qu1gsFckqpzyl5","id.orig_h":"10.12.1.3","id.orig_p":60500,"id.resp_h":"10.1.2.2","id.resp_p":53,"proto":"udp","trans_id":18348,"query":"ntp.ubuntu.com","qclass":1,"qclass_name":"C_INTERNET","qtype":1,"qtype_name":"A","AA":false,"TC":false,"RD":true,"RA":false,"Z":0,"rejected":false}
{"ts":1620614527.720563,"uid":"C37e5VcXn7ng6sco5","id.orig_h":"10.12.1.3","id.orig_p":36062,"id.resp_h":"10.12.1.254","id.resp_p":53,"proto":"udp","trans_id":31917,"query":"ntp.ubuntu.com","qclass":1,"qclass_name":"C_INTERNET","qtype":28,"qtype_name":"AAAA","AA":false,"TC":false,"RD":true,"RA":false,"Z":0,"rejected":false}
{"ts":1620614532.72124,"uid":"Cv8Y571jaNyRRwW3V8","id.orig_h":"10.12.1.3","id.orig_p":52602,"id.resp_h":"10.1.2.2","id.resp_p":53,"proto":"udp","trans_id":31917,"query":"ntp.ubuntu.com","qclass":1,"qclass_name":"C_INTERNET","qtype":28,"qtype_name":"AAAA","AA":false,"TC":false,"RD":true,"RA":false,"Z":0,"rejected":false}
{"ts":1620614532.721645,"uid":"CxGfZZ1gFrADZSXcM8","id.orig_h":"10.12.1.3","id.orig_p":47505,"id.resp_h":"10.12.1.254","id.resp_p":53,"proto":"udp","trans_id":18348,"query":"ntp.ubuntu.com","qclass":1,"qclass_name":"C_INTERNET","qtype":1,"qtype_name":"A","AA":false,"TC":false,"RD":true,"RA":false,"Z":0,"rejected":false}
{"ts":1620614537.726024,"uid":"C4XyPo1hbULmgnbxD","id.orig_h":"10.12.1.3","id.orig_p":60122,"id.resp_h":"10.1.2.2","id.resp_p":53,"proto":"udp","trans_id":18348,"query":"ntp.ubuntu.com","qclass":1,"qclass_name":"C_INTERNET","qtype":1,"qtype_name":"A","AA":false,"TC":false,"RD":true,"RA":false,"Z":0,"rejected":false}
{"ts":1620614537.72638,"uid":"CcktUY3xK5pS1gfsti","id.orig_h":"10.12.1.3","id.orig_p":37027,"id.resp_h":"10.12.1.254","id.resp_p":53,"proto":"udp","trans_id":31917,"query":"ntp.ubuntu.com","qclass":1,"qclass_name":"C_INTERNET","qtype":28,"qtype_name":"AAAA","AA":false,"TC":false,"RD":true,"RA":false,"Z":0,"rejected":false}
{"ts":1620614542.731036,"uid":"CyPZk74J4nkB4xm1m4","id.orig_h":"10.12.1.3","id.orig_p":49234,"id.resp_h":"10.1.2.2","id.resp_p":53,"proto":"udp","trans_id":31917,"query":"ntp.ubuntu.com","qclass":1,"qclass_name":"C_INTERNET","qtype":28,"qtype_name":"AAAA","AA":false,"TC":false,"RD":true,"RA":false,"Z":0,"rejected":false}
```
Snippet of ssh network logs, taken from `pwnjutsu_dataset-network-json-player_12/player_12_536871846.pcap_ssh.log`:
```json
{"ts":1620591622.348385,"uid":"Cs8DfJ30zPc4Lze92e","id.orig_h":"172.16.128.112","id.orig_p":40988,"id.resp_h":"10.12.1.1","id.resp_p":22,"version":2,"auth_success":false,"auth_attempts":5,"client":"SSH-2.0-libssh_0.9.0","server":"SSH-2.0-OpenSSH_6.2","cipher_alg":"aes256-gcm@openssh.com","mac_alg":"hmac-sha2-256-etm@openssh.com","compression_alg":"none","kex_alg":"ecdh-sha2-nistp256","host_key_alg":"ssh-rsa","host_key":"6d:ca:ee:bf:9e:66:42:b6:af:ac:79:1c:34:eb:0f:7c"}
{"ts":1620591622.34745,"uid":"C0HpGMsDL0dbQpJyb","id.orig_h":"172.16.128.112","id.orig_p":40984,"id.resp_h":"10.12.1.1","id.resp_p":22,"version":2,"auth_success":false,"auth_attempts":5,"client":"SSH-2.0-libssh_0.9.0","server":"SSH-2.0-OpenSSH_6.2","cipher_alg":"aes256-gcm@openssh.com","mac_alg":"hmac-sha2-256-etm@openssh.com","compression_alg":"none","kex_alg":"ecdh-sha2-nistp256","host_key_alg":"ssh-rsa","host_key":"6d:ca:ee:bf:9e:66:42:b6:af:ac:79:1c:34:eb:0f:7c"}
{"ts":1620591622.34747,"uid":"C6eGEkqNuEaxrprGg","id.orig_h":"172.16.128.112","id.orig_p":40986,"id.resp_h":"10.12.1.1","id.resp_p":22,"version":2,"auth_success":false,"auth_attempts":5,"client":"SSH-2.0-libssh_0.9.0","server":"SSH-2.0-OpenSSH_6.2","cipher_alg":"aes256-gcm@openssh.com","mac_alg":"hmac-sha2-256-etm@openssh.com","compression_alg":"none","kex_alg":"ecdh-sha2-nistp256","host_key_alg":"ssh-rsa","host_key":"6d:ca:ee:bf:9e:66:42:b6:af:ac:79:1c:34:eb:0f:7c"}
{"ts":1620591695.343606,"uid":"Ci4GNJ386yGfHTO8D7","id.orig_h":"172.16.128.112","id.orig_p":40990,"id.resp_h":"10.12.1.1","id.resp_p":22,"version":2,"auth_attempts":0,"client":"SSH-2.0-libssh_0.9.0","server":"SSH-2.0-OpenSSH_6.2","cipher_alg":"aes256-gcm@openssh.com","mac_alg":"hmac-sha2-256-etm@openssh.com","compression_alg":"none","kex_alg":"ecdh-sha2-nistp256","host_key_alg":"ssh-rsa","host_key":"6d:ca:ee:bf:9e:66:42:b6:af:ac:79:1c:34:eb:0f:7c"}
{"ts":1620591695.871512,"uid":"CitP9UmoyVfqPWQp2","id.orig_h":"172.16.128.112","id.orig_p":41016,"id.resp_h":"10.12.1.1","id.resp_p":22,"auth_attempts":0,"client":"SSH-2.0-libssh_0.9.0"}
{"ts":1620591696.175454,"uid":"CU8h22oQvJSJ0g9Dd","id.orig_h":"172.16.128.112","id.orig_p":41024,"id.resp_h":"10.12.1.1","id.resp_p":22,"auth_attempts":0,"client":"SSH-2.0-libssh_0.9.0"}
{"ts":1620591695.871427,"uid":"C3Zi7d3vAxwJVidEBf","id.orig_h":"172.16.128.112","id.orig_p":41004,"id.resp_h":"10.12.1.1","id.resp_p":22,"version":2,"auth_success":false,"auth_attempts":5,"client":"SSH-2.0-libssh_0.9.0","server":"SSH-2.0-OpenSSH_6.2","cipher_alg":"aes256-gcm@openssh.com","mac_alg":"hmac-sha2-256-etm@openssh.com","compression_alg":"none","kex_alg":"ecdh-sha2-nistp256","host_key_alg":"ssh-rsa","host_key":"6d:ca:ee:bf:9e:66:42:b6:af:ac:79:1c:34:eb:0f:7c"}
{"ts":1620591695.870423,"uid":"CCINrcTQN3Y94Ig24","id.orig_h":"172.16.128.112","id.orig_p":41006,"id.resp_h":"10.12.1.1","id.resp_p":22,"version":2,"auth_success":false,"auth_attempts":5,"client":"SSH-2.0-libssh_0.9.0","server":"SSH-2.0-OpenSSH_6.2","cipher_alg":"aes256-gcm@openssh.com","mac_alg":"hmac-sha2-256-etm@openssh.com","compression_alg":"none","kex_alg":"ecdh-sha2-nistp256","host_key_alg":"ssh-rsa","host_key":"6d:ca:ee:bf:9e:66:42:b6:af:ac:79:1c:34:eb:0f:7c"}
{"ts":1620591695.870571,"uid":"CAPILk4ZSweQD7G7o7","id.orig_h":"172.16.128.112","id.orig_p":40992,"id.resp_h":"10.12.1.1","id.resp_p":22,"version":2,"auth_success":false,"auth_attempts":5,"client":"SSH-2.0-libssh_0.9.0","server":"SSH-2.0-OpenSSH_6.2","cipher_alg":"aes256-gcm@openssh.com","mac_alg":"hmac-sha2-256-etm@openssh.com","compression_alg":"none","kex_alg":"ecdh-sha2-nistp256","host_key_alg":"ssh-rsa","host_key":"6d:ca:ee:bf:9e:66:42:b6:af:ac:79:1c:34:eb:0f:7c"}
{"ts":1620591695.871449,"uid":"CBHL9g3kWQ8fFuVppc","id.orig_h":"172.16.128.112","id.orig_p":41010,"id.resp_h":"10.12.1.1","id.resp_p":22,"version":2,"auth_success":false,"auth_attempts":5,"client":"SSH-2.0-libssh_0.9.0","server":"SSH-2.0-OpenSSH_6.2","cipher_alg":"aes256-gcm@openssh.com","mac_alg":"hmac-sha2-256-etm@openssh.com","compression_alg":"none","kex_alg":"ecdh-sha2-nistp256","host_key_alg":"ssh-rsa","host_key":"6d:ca:ee:bf:9e:66:42:b6:af:ac:79:1c:34:eb:0f:7c"}
```