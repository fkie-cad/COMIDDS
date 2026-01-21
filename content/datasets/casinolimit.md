---
title: CasinoLimit
---

- [Overview](#overview)
- [Environment](#environment)
- [Activity](#activity)
- [Contained Data](#contained-data)
- [Papers](#papers)
- [Links](#links)
- [Data Examples](#data-examples)

| <!-- -->                 | <!-- -->                                        |
| ------------------------ | ----------------------------------------------- |
| **Network Data Source**  | NetFlows                                        |
| **Network Data Labeled** | Yes                                             |
| **Host Data Source**     | Syslog, auditd                                  |
| **Host Data Labeled**    | Yes                                             |
|                          |                                                 |
| **Overall Setting**      | Enterprise IT                                   |
| **OS Types**             | Linux                                           |
| **Number of Machines**   | 4 (+ Attacker)                                  |
| **Total Runtime**        | 11 hours                                        |
| **Year of Collection**   | 2024                                            |
| **Attack Categories**    | Most ATT&CK tactics                             |
| **User Emulation**       | None                                            |
|                          |                                                 |
| **Packed Size**          | 3,6 GB                                          |
| **Unpacked Size**        | 54,4 GB                                         |
| **Download Link**        | [goto](https://doi.org/10.5281/zenodo.15278062) |

***

### Overview
The CasinoLimit dataset is a set of labeled logs collected from 114 individual attack campaigns, all performed against (copies of) the same target during the Breizh CTF 2024.
Notably, labels are not binary, but instead describe the associated MITRE ATT&CK technique of the associated log.
The dataset is aimed at providing a basis for kill-chain analysis and attacker identification via command inspection, though it does not feature any benign behavior.

### Environment
Each team was provided with an isolated environment that featured 4 Linux hosts distributed across two networks.
Players are given SSH credentials for the first machine and are then meant to move laterally and horizontally through the environment, finding various vulnerabilities as well as clues leading them to these vulnerabilities.
The authors used the [URSID](https://gitlab.inria.fr/pirat-public/ursid) tool for automated and repeatable deployment.
All interactions from players are purely command-line based.

### Activity
Players were tasked with deleting a specific entry in a database, followed by reading a flag found in an email sent to an admin account.
The "minimal" path to achieve this goal contained the following techniques:
- T1021: Remote Services
- T1125: Video Capture
- T1021: Remote Services
- T1068: Exploitation for Privilege Escalation
- T1190: Exploit Public-Facing Application
- T1485: Data Destruction
- T1114: Email Collection

Refer to Section 3c of the paper for a detailed description of the attack path.
Since players naturally didn't strictly adhere to this path, the  final labels contain techniques from all MITRE ATT&CK tactics, except for Initial Access and Execution.

### Contained Data
All hosts and their network traffic were monitored to collect kernel and user-space events as well as network flows.
The authors further filtered these to contain only logs related to terminal interaction, arguing that only those are related to attacker actions.
System logs are automatically labeled based on the command they originated from, followed by a manual review using the Manatee labeling tool.
Created labels were then propagated to the network flows originating from the respective system events, resulting in the following six files:
- ``labelled_flows.zip``: The network flows in unidirectional format with corresponding labels.
- ``flows_zeek.zip``: The network flows in bidirectional format, extracted with Zeek.
- ``syslogs.zip``: The linux system logs, including auditd logs.
- ``syslogs_labels.zip``: The system logs labels for auditd events.
- ``cache.zip``: The preprocessed data used by the Manatee labeling tool.
- ``output.zip``: The output of the Manatee labeling tool, including system labels, relations, and validation data.

Within each directory, data is structured by instance.
The labels in `syslogs_labels` refer to entries in `syslog`.
The authors also provide a [Datasheet](https://gitlab.inria.fr/pirat-public/datasets/casinolimit/-/blob/main/datasheet_casinolimit.pdf) and a [README](https://gitlab.inria.fr/pirat-public/datasets/casinolimit/-/blob/main/README.md?ref_type=heads), supplying further details.

### Papers
- [CasinoLimit: An Offensive Dataset Labeled with MITRE ATT&CK Techniques](https://hal.science/hal-05224264)

### Links
- [Homepage](https://casinolimit.inria.fr/)
- [CasinoLimit Repo](https://gitlab.inria.fr/pirat-public/casinolimit)
- [Dataset Datasheet](https://gitlab.inria.fr/pirat-public/datasets/casinolimit/-/blob/main/datasheet_casinolimit.pdf)

### Data Examples
Snippet of entries from `syslog_labels/system_labels/aeriella.json`

<!--  {% raw %} -->
```
{
    "dfb6882f73d14be9a79882c50002658c": {         # Label UID as key
        "id": "dfb6882f73d14be9a79882c50002658c", # Label UID
        "auditd_events": {                        # Auditd events related to the label
            "start": [                            # Machine name as key
                "94050",                          # List of auditd event IDs
                "94052"
            ]
        },
        "technique": "T1069: Permission Groups Discovery" # MITRE ATT&CK technique (format: <id>: <name>)
    }
}

```
<!--  {% endraw %} -->

Snippet of entries from `syslogs/syslogs/aerliella/start-56/audit.log` (labeled by the entry above)
<!--  {% raw %} -->
```
type=PATH msg=audit(1715994529.336:94050): item=0 name="/etc/shadow" inode=4842 dev=08:01 mode=0100640 ouid=0 ogid=42 rdev=00:00 nametype=NORMAL cap_fp=0 cap_fi=0 cap_fe=0 cap_fver=0 cap_frootid=0 OUID="root" OGID="shadow"
type=SYSCALL msg=audit(1715994529.336:94050): arch=c000003e syscall=257 success=yes exit=7 a0=ffffff9c a1=7fcff4efbbf9 a2=80000 a3=0 items=1 ppid=24962 pid=24968 auid=1001 uid=1001 gid=1001 euid=0 suid=0 fsuid=0 egid=1001 sgid=1001 fsgid=1001 tty=pts0 ses=59 comm="sudo" exe="/usr/bin/sudo" subj=unconfined key="etcpasswd" ARCH=x86_64 SYSCALL=openat AUID="tbenedict" UID="tbenedict" GID="tbenedict" EUID="root" SUID="root" FSUID="root" EGID="tbenedict" SGID="tbenedict" FSGID="tbenedict"
type=PROCTITLE msg=audit(1715994529.336:94050): proctitle=7375646F002D6C
type=PATH msg=audit(1715994529.336:94052): item=0 name="/etc/shadow" inode=4842 dev=08:01 mode=0100640 ouid=0 ogid=42 rdev=00:00 nametype=NORMAL cap_fp=0 cap_fi=0 cap_fe=0 cap_fver=0 cap_frootid=0 OUID="root" OGID="shadow"
type=SYSCALL msg=audit(1715994529.336:94052): arch=c000003e syscall=257 success=yes exit=7 a0=ffffff9c a1=7fcff4efbbf9 a2=80000 a3=0 items=1 ppid=24962 pid=24968 auid=1001 uid=1001 gid=1001 euid=0 suid=0 fsuid=0 egid=1001 sgid=1001 fsgid=1001 tty=pts0 ses=59 comm="sudo" exe="/usr/bin/sudo" subj=unconfined key="etcpasswd" ARCH=x86_64 SYSCALL=openat AUID="tbenedict" UID="tbenedict" GID="tbenedict" EUID="root" SUID="root" FSUID="root" EGID="tbenedict" SGID="tbenedict" FSGID="tbenedict"
type=PROCTITLE msg=audit(1715994529.336:94052): proctitle=7375646F002D6C
```
<!--  {% endraw %} -->

