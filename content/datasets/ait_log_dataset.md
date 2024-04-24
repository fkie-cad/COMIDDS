---
title: AIT Log Data Set
---

- [Overview](#overview)
- [Environment](#environment)
- [Activity](#activity)
- [Contained Data](#contained-data)
- [Papers](#papers)
- [Links](#links)
- [Related Entries](#related-entries)
- [Example Data](#example-data)

| <!-- -->                 | <!-- -->                                                                                                      |
|--------------------------|---------------------------------------------------------------------------------------------------------------|
| **Network Data Source**  | VPN, DNS, pcaps, Suricata                                                                                     |
| **Network Data Labeled** | Yes                                                                                                           |
| **Host Data Source**     | Apache, auth, audit, syslogs, and more                                                                        |
| **Host Data Labeled**    | Yes                                                                                                           |
|                          |                                                                                                               |
| **Overall Setting**      | Enterprise OS                                                                                                 |
| **OS Types**             | Ubuntu 20.04                                                                                                  |
| **Number of Machines**   | 9-27                                                                                                          |
| **Total Runtime**        | 4-6 days per sim, 8 simulations total                                                                         |
| **Year of Collection**   | 2022                                                                                                          |
| **Attack Categories**    | Reconnaissance<br>Privilege Escalation<br>Data Exfiltration<br>Web-based Attacks<br/>Remote Command Execution |
| **Benign Activity**      | Synthetic, models complex behavior                                                                            |
|                          |                                                                                                               |
| **Packed Size**          | 130 GB                                                                                                        |
| **Unpacked Size**        | 206 GB                                                                                                        |
| **Download Link**        | [goto](https://zenodo.org/record/5789064)                                                                     |

***

### Overview

A collection of synthetic log data intended for IDS evaluation, federated learning and alert aggregation.
Logs were collected from eight testbeds built at the Austrian Institute of Technology (AIT).
Each testbed represents a small company network, including simulation of normal user behavior to generate background
noise.
Each of the testbed runs for 4-6 days, and at some point a sequence of attacks is launched against the network.
Differences between attacks include the runtime, the specific execution of attacks and the number of servers, employees,
users, etc.
This dataset, assigned version 2.0, is a continuation of previous efforts by the same authors, improving upon network
complexity, log collection and user simulation.

### Environment

The authors leverage what they call model-driven testbed generation, divided into four layers (L1-L4), each representing
a different level of abstraction.

- L4: Testbed-independent models for attacker, user and technical infrastructure in the form of templates as well as
  labeling rules (e.g., traffic from attacker IP is malicious)
- L3: Testbed-specific models, using those from L4 and filling out available parameters given some objective
- L2: Collection of logs from various sources, in addition to machine facts like IP addresses or OS information
- L1: Filling out available labeling rules with collected facts (e.g. the attacker IP), then processing and labeling
  collected logs

The target use case for the present dataset was the simulation of a small company network, with the number of hosts and
IP ranges differing between each of the eight simulation runs.
The simulated network is divided into three zones:

- Intranet, containing several Ubuntu 20.04 hosts and an intranet server running WordPress and Samba file share
- DMZ, hosting servers for VPN, proxy, mail, and cloud share
- Internet, running "global" DNS and hosting remote and external company resources

More details, such as version numbers etc., are available in section 3.2.1 of the dataset paper.

### Activity

User behavior has been modeled to fit this infrastructure by introducing state machines for available services, again
with some parameters varying between runs.
More details regarding the user behavior can be found in section 3.2.2 of the dataset paper.

For the attack scenarios, it is assumed that the attacker illegitimately obtained VPN credentials, for example via a
successful phishing campaign, allowing them to access the network.
This is part is deliberately not included in the simulation, as it is argued to occur outside the enterprise network and
thus does not leave traces.
The full details of an attack campaign are laid out in section 3.2.3 of the paper.
Attacks include:

- Scans (nmap, WPScan, dirb)
- Webshell upload (CVE-2020-24186)
- Password Cracking (John the Ripper)
- Privilege Escalation
- Remote Command Execution
- Data Exfiltration

### Contained Data

The collected, processes and labeled logs for each simulation run are organized as follows:

- `gather` directory, contains all logs per user
- `labels` directory, mirrors the `gather` directory and file names, wherein each line contains the attack name as well
  as the line number of the respective log in the corresponding log file
- `processsing` directory, contains source code for label generation
- `rules` directory, contains labeling rules
- `environment` directory, contains source code for simulation
- `dataset.yml` file, contains start and end time of simulation

Any unlabeled log is implicitly labeled "normal".
The types of logs collected from each host varies, a summary can be found in the table below.
A circled checkmark indicates that labels exists for that file.

![AIT Log Sources]({{ "/assets/img/ait_log_sources.png" | relative_url }})

### Papers

- [Introducing a New Alert Data Set for Multi-Step Attack Analysis (2023)](https://doi.org/10.48550/arXiv.2308.12627)
- [Maintainable Log Datasets for Evaluation of Intrusion Detection Systems (2023)](https://doi.org/10.1109/TDSC.2022.3201582)

### Links

- [Homepage](https://zenodo.org/record/5789064)
- [Alert dataset generated using this log dataset](https://zenodo.org/record/8263181)
- [Prior v1.1 of this dataset](https://zenodo.org/records/4264796)

### Related entries

- [AIT Alert Dataset](ait_alert_dataset.md)

### Example Data

Suricata alerts stored in `suricata/eve.jsonl` (if available).
The full `.pcap` files can be found in the same directory,
as well as a file called `fast.log` containing only alerts in a short and readable form.

```json
[
  ...
]
{
  "timestamp": "2022-01-24T03:57:01.688371+0000",
  "flow_id": 993095819560297,
  "in_iface": "ens3",
  "event_type": "alert",
  "src_ip": "172.19.131.174",
  "src_port": 38710,
  "dest_ip": "10.143.2.4",
  "dest_port": 80,
  "proto": "TCP",
  "tx_id": 0,
  "alert": {
    "action": "allowed",
    "gid": 1,
    "signature_id": 2024364,
    "rev": 4,
    "signature": "ET SCAN Possible Nmap User-Agent Observed",
    "category": "Web Application Attack",
    "severity": 1,
    "metadata": {
      "affected_product": [
        "Any"
      ],
      "attack_target": [
        "Client_and_Server"
      ],
      "created_at": [
        "2017_06_08"
      ],
      "deployment": [
        "Perimeter"
      ],
      "former_category": [
        "SCAN"
      ],
      "performance_impact": [
        "Low"
      ],
      "signature_severity": [
        "Informational"
      ],
      "updated_at": [
        "2020_08_06"
      ]
    }
  },
  "http": {
    "hostname": "intranet.smith.russellmitchell.com",
    "url": "/sdk",
    "http_user_agent": "Mozilla/5.0 (compatible; Nmap Scripting Engine; https://nmap.org/book/nse.html)",
    "http_content_type": "text/html",
    "http_method": "POST",
    "protocol": "HTTP/1.1",
    "status": 404,
    "length": 196
  },
  "files": [
    {
      "filename": "/sdk",
      "sid": [],
      "gaps": false,
      "state": "CLOSED",
      "stored": false,
      "size": 441,
      "tx_id": 0
    }
  ],
  "app_proto": "http",
  "flow": {
    "pkts_toserver": 4,
    "pkts_toclient": 4,
    "bytes_toserver": 910,
    "bytes_toclient": 632,
    "start": "2022-01-24T03:57:01.623977+0000"
  }
}
[
  ...
]
```

Apache access logs stored in `apache2/*access.log.*` (if available).
Error logs can be found in `apache2/error.log.*`

```
[...]
172.19.131.174 - - [23/Jan/2022:07:59:29 +0000] "GET /wp-content/plugins/wpdiscuz/assets/js/wpdiscuz-combo.min.js?ver=7.0.4 HTTP/1.1" 200 71266 "https://intranet.smith.russellmitchell.com/?p=5" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/97.0.4692.71 Safari/537.36"
::1 - - [23/Jan/2022:07:59:37 +0000] "OPTIONS * HTTP/1.0" 200 110 "-" "Apache/2.4.29 (Ubuntu) OpenSSL/1.1.1 (internal dummy connection)"
172.19.131.174 - - [23/Jan/2022:08:03:03 +0000] "GET /wp-content/plugins/wpdiscuz/assets/img/loading.gif HTTP/1.1" 200 4069 "https://intranet.smith.russellmitchell.com/wp-content/plugins/wpdiscuz/themes/default/style.css?ver=7.0.4" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/97.0.4692.71 Safari/537.36"
172.19.131.174 - - [23/Jan/2022:08:03:03 +0000] "POST /wp-admin/admin-ajax.php HTTP/1.1" 200 5667 "https://intranet.smith.russellmitchell.com/?p=5" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/97.0.4692.71 Safari/537.36"
[...]
```

Auth logs stored in `auth.log.*` (if available).

```
[...]
Jan 24 04:17:01 intranet-server CRON[27933]: pam_unix(cron:session): session opened for user root by (uid=0)
Jan 24 04:17:01 intranet-server CRON[27933]: pam_unix(cron:session): session closed for user root
Jan 24 04:37:40 intranet-server su[27950]: Successful su for jhall by www-data
Jan 24 04:37:40 intranet-server su[27950]: + /dev/pts/1 www-data:jhall
Jan 24 04:37:40 intranet-server su[27950]: pam_unix(su:session): session opened for user jhall by (uid=33)
Jan 24 04:37:40 intranet-server systemd-logind[957]: New session c1 of user jhall.
Jan 24 04:37:58 intranet-server sudo:    jhall : TTY=pts/1 ; PWD=/var/www/intranet.smith.russellmitchell.com/wp-content/uploads/2022/01 ; USER=root ; COMMAND=list
Jan 24 04:38:06 intranet-server sudo:    jhall : TTY=pts/1 ; PWD=/var/www/intranet.smith.russellmitchell.com/wp-content/uploads/2022/01 ; USER=root ; COMMAND=/bin/cat /etc/shadow
Jan 24 04:38:06 intranet-server sudo: pam_unix(sudo:session): session opened for user root by (uid=0)
Jan 24 04:38:06 intranet-server sudo: pam_unix(sudo:session): session closed for user root
[...]
```

Syslogs stored in `syslog.*` (if available).

```
[...]
Jan 23 16:30:47 intranet-server systemd[25186]: Reached target Sockets.
Jan 23 16:30:47 intranet-server systemd[25186]: Reached target Basic System.
Jan 23 16:30:47 intranet-server systemd[1]: Started User Manager for UID 1002.
Jan 23 16:30:47 intranet-server systemd[25186]: Reached target Default.
Jan 23 16:30:47 intranet-server systemd[25186]: Startup finished in 59ms.
Jan 23 16:39:01 intranet-server CRON[25325]: (root) CMD (  [ -x /usr/lib/php/sessionclean ] && if [ ! -d /run/systemd/system ]; then /usr/lib/php/sessionclean; fi)
Jan 23 16:39:12 intranet-server systemd[1]: Starting Clean php session files...
Jan 23 16:39:12 intranet-server systemd[1]: Started Clean php session files.
Jan 23 17:09:01 intranet-server CRON[25400]: (root) CMD (  [ -x /usr/lib/php/sessionclean ] && if [ ! -d /run/systemd/system ]; then /usr/lib/php/sessionclean; fi)
[...]
```

Audit logs stored in `audit/audit.log` (if available).

```
[...]
type=SERVICE_START msg=audit(1642732752.634:441): pid=1 uid=0 auid=4294967295 ses=4294967295 msg='unit=phpsessionclean comm="systemd" exe="/lib/systemd/systemd" hostname=? addr=? terminal=? res=success'
type=SERVICE_STOP msg=audit(1642732752.634:442): pid=1 uid=0 auid=4294967295 ses=4294967295 msg='unit=phpsessionclean comm="systemd" exe="/lib/systemd/systemd" hostname=? addr=? terminal=? res=success'
type=USER_ACCT msg=audit(1642734541.366:443): pid=10653 uid=0 auid=4294967295 ses=4294967295 msg='op=PAM:accounting acct="root" exe="/usr/sbin/cron" hostname=? addr=? terminal=cron res=success'
type=CRED_ACQ msg=audit(1642734541.370:444): pid=10653 uid=0 auid=4294967295 ses=4294967295 msg='op=PAM:setcred acct="root" exe="/usr/sbin/cron" hostname=? addr=? terminal=cron res=success'
type=LOGIN msg=audit(1642734541.370:445): pid=10653 uid=0 old-auid=4294967295 auid=0 tty=(none) old-ses=4294967295 ses=74 res=1
type=USER_START msg=audit(1642734541.374:446): pid=10653 uid=0 auid=0 ses=74 msg='op=PAM:session_open acct="root" exe="/usr/sbin/cron" hostname=? addr=? terminal=cron res=success'
type=CRED_DISP msg=audit(1642734541.378:447): pid=10653 uid=0 auid=0 ses=74 msg='op=PAM:setcred acct="root" exe="/usr/sbin/cron" hostname=? addr=? terminal=cron res=success'
type=USER_END msg=audit(1642734541.378:448): pid=10653 uid=0 auid=0 ses=74 msg='op=PAM:session_close acct="root" exe="/usr/sbin/cron" hostname=? addr=? terminal=cron res=success'
type=SERVICE_START msg=audit(1642734552.622:449): pid=1 uid=0 auid=4294967295 ses=4294967295 msg='unit=phpsessionclean comm="systemd" exe="/lib/systemd/systemd" hostname=? addr=? terminal=? res=success'
[...]
```