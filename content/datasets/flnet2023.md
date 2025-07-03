---
title: FLNET2023
---

- [Overview](#overview)
- [Environment](#environment)
- [Activity](#activity)
- [Contained Data](#contained-data)
- [Papers](#papers)
- [Links](#links)
- [Data Examples](#data-examples)

| <!-- -->                 | <!-- -->                                                                                                                          |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------------------- |
| **Network Data Source**  | pcaps, derived features                                                                                                           |
| **Network Data Labeled** | Yes                                                                                                                               |
| **Host Data Source**     | -                                                                                                                                 |
| **Host Data Labeled**    | -                                                                                                                                 |
|                          |                                                                                                                                   |
| **Overall Setting**      | ISP-like                                                                                                                          |
| **OS Types**             | Undisclosed                                                                                                                       |
| **Number of Machines**   | 40 total nodes                                                                                                                    |
| **Total Runtime**        | n/a                                                                                                                               |
| **Year of Collection**   | 2023                                                                                                                              |
| **Attack Categories**    | DDOS & DOS<br>Infiltration<br>Web-based (SQLi, XSS, command injection)                                                            |
| **User Emulation**       | Synthetic, using hping3                                                                                                           |
|                          |                                                                                                                                   |
| **Packed Size**          | -                                                                                                                                 |
| **Unpacked Size**        | 176 GB                                                                                                                            |
| **Download Link**        | [goto](https://eltnmsu-my.sharepoint.com/:f:/g/personal/pratyay_nmsu_edu/ErDns0cRITtEsawkCgfqYTIB7BGJ_YDfp9r-p_80v3GxIQ?e=UimpBG) |

---

### Overview

The "**F**ederated **L**earning for **Net**works" dataset (FLNET2023) is based on the emulation of a large-scale network topology mimicking that of an Internet Service Provider.
Traffic is collected from a subset of routers while a variety of scripted attacks and benign traffic are generated.
As the name suggests, this dataset aims to enable federated learning by providing labeled data on a per-client basis.

### Environment

The dataset originates from a CORE-emulated environment running the GEANT-2012 network topology with 40 interconnected routers, similar to the network infrastructure of an ISP.
Each node represents a "primary router" serving a specific geographic location; a subset of ten of these are chosen as data collection points.
While further details like operating system or services are not specified, CORE typically uses Linux-based containers and standard Linux-based network services
Refer to the [README](https://github.com/nsol-nmsu/FML-Network) for a detailed illustration of the network setup.

### Activity

Benign traffic generation (via hping3) is described as representing multiple protocols and covering a variety of devices and traffic patterns.
Attacks are orchestrated by integrating various open-source tools in the CORE environment to automate the execution of a number of attacks:
- DDoS Bot/Dyn/Stomp/TCP (MHDDoS)
- DoS (Hulk, SlowHTTP)
- Web SQLi (sqlmap)
- Web XSS (xsstrike)
- Web Command Injection (commix)
- Infiltration (MITM) (bettercap)

### Contained Data

Data is collected in the form of pcaps, from which 82 flow-based features are extracted using CICFlowMeter.
These features are labeled either as `Normal`, or after the attack they originate from (e.g., `Infiltration-mitm`).
Both the original pcaps and the labeled features are available, divided by type (normal or type of attack) and by origin (one of the 10 collection points).
The labeling process is not detailed.

### Papers

- [FLNET2023: Realistic Network Intrusion Detection Dataset for Federated Learning](https://doi.org/10.1109/MILCOM58377.2023.10356272)

### Links

- [README](https://github.com/nsol-nmsu/FML-Network)
- [CORE Emulator](https://github.com/coreemu/core)
- [hping3 traffic generator](https://www.kali.org/tools/hping3/)
- [CICFlowMeter](https://github.com/ISCX/CICFlowMeter)

### Data Examples

Snippet of labeled features, taken from `Infiltration/CSV/Dataset-1.csv`

<!--  {% raw %} -->

```
src_ip,dst_ip,src_port,dst_port,protocol,timestamp,flow_duration,flow_byts_s,flow_pkts_s,fwd_pkts_s,bwd_pkts_s,tot_fwd_pkts,tot_bwd_pkts,totlen_fwd_pkts,totlen_bwd_pkts,fwd_pkt_len_max,fwd_pkt_len_min,fwd_pkt_len_mean,fwd_pkt_len_std,bwd_pkt_len_max,bwd_pkt_len_min,bwd_pkt_len_mean,bwd_pkt_len_std,pkt_len_max,pkt_len_min,pkt_len_mean,pkt_len_std,pkt_len_var,fwd_header_len,bwd_header_len,fwd_seg_size_min,fwd_act_data_pkts,flow_iat_mean,flow_iat_max,flow_iat_min,flow_iat_std,fwd_iat_tot,fwd_iat_max,fwd_iat_min,fwd_iat_mean,fwd_iat_std,bwd_iat_tot,bwd_iat_max,bwd_iat_min,bwd_iat_mean,bwd_iat_std,fwd_psh_flags,bwd_psh_flags,fwd_urg_flags,bwd_urg_flags,fin_flag_cnt,syn_flag_cnt,rst_flag_cnt,psh_flag_cnt,ack_flag_cnt,urg_flag_cnt,ece_flag_cnt,down_up_ratio,pkt_size_avg,init_fwd_win_byts,init_bwd_win_byts,active_max,active_min,active_mean,active_std,idle_max,idle_min,idle_mean,idle_std,fwd_byts_b_avg,fwd_pkts_b_avg,bwd_byts_b_avg,bwd_pkts_b_avg,fwd_blk_rate_avg,bwd_blk_rate_avg,fwd_seg_size_avg,bwd_seg_size_avg,cwe_flag_count,subflow_fwd_pkts,subflow_bwd_pkts,subflow_fwd_byts,subflow_bwd_byts,label
10.0.63.20,224.0.0.251,12345,5353,2048,2023-05-04 12:15:19,122035478,12.537337707646,0.139303752307177,0.139303752307177,0,17,0,1530,0,90,90,90,0,0,0,0,0,90,90,90,0,0,136,0,8,17,7627217.375,7635351,7616071,5606.56816683566,122035478,7635351,7616071,7627217.375,5606.56816683566,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,90,0,0,18951,1023,9673,6434.76899352261,7627950,7653,1534144.4,3046903.95756634,0,0,0,0,0,0,90,0,0,17,0,1530,0,Infiltration-mitm
10.0.63.20,239.255.255.250,52209,1900,2048,2023-05-04 12:15:19,0,0,0,0,0,1,0,136,0,136,136,136,0,0,0,0,0,136,136,136,0,0,8,0,8,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,136,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,136,0,0,1,0,136,0,Infiltration-mitm
10.0.63.20,224.0.0.251,55866,5353,2048,2023-05-04 12:15:19,0,0,0,0,0,1,0,83,0,83,83,83,0,0,0,0,0,83,83,83,0,0,8,0,8,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,83,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,83,0,0,1,0,83,0,Infiltration-mitm
10.0.63.20,239.255.255.250,41512,3702,2048,2023-05-04 12:15:19,0,0,0,0,0,1,0,623,0,623,623,623,0,0,0,0,0,623,623,623,0,0,8,0,8,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,623,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,623,0,0,1,0,623,0,Infiltration-mitm
10.0.63.20,10.0.63.1,47228,137,2048,2023-05-04 12:15:19,0,0,0,0,0,1,0,94,0,94,94,94,0,0,0,0,0,94,94,94,0,0,8,0,8,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,94,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,94,0,0,1,0,94,0,Infiltration-mitm
10.0.63.20,224.0.0.251,42646,5353,2048,2023-05-04 12:15:20,0,0,0,0,0,1,0,87,0,87,87,87,0,0,0,0,0,87,87,87,0,0,8,0,8,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,87,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,87,0,0,1,0,87,0,Infiltration-mitm
10.0.63.20,224.0.0.251,58119,5353,2048,2023-05-04 12:15:21,0,0,0,0,0,1,0,87,0,87,87,87,0,0,0,0,0,87,87,87,0,0,8,0,8,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,87,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,87,0,0,1,0,87,0,Infiltration-mitm
10.0.63.20,10.0.63.255,53702,137,2048,2023-05-04 12:15:21,0,0,0,0,0,1,0,94,0,94,94,94,0,0,0,0,0,94,94,94,0,0,8,0,8,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,94,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,94,0,0,1,0,94,0,Infiltration-mitm
10.0.63.20,224.0.0.251,46774,5353,2048,2023-05-04 12:15:22,0,0,0,0,0,1,0,84,0,84,84,84,0,0,0,0,0,84,84,84,0,0,8,0,8,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,84,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,84,0,0,1,0,84,0,Infiltration-mitm
10.0.63.20,224.0.0.251,46215,5353,2048,2023-05-04 12:15:23,0,0,0,0,0,1,0,91,0,91,91,91,0,0,0,0,0,91,91,91,0,0,8,0,8,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,91,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,91,0,0,1,0,91,0,Infiltration-mitm
10.0.63.20,224.0.0.251,55152,5353,2048,2023-05-04 12:15:24,0,0,0,0,0,1,0,94,0,94,94,94,0,0,0,0,0,94,94,94,0,0,8,0,8,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,94,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,94,0,0,1,0,94,0,Infiltration-mitm
10.0.63.20,224.0.0.251,50512,5353,2048,2023-05-04 12:15:25,0,0,0,0,0,1,0,90,0,90,90,90,0,0,0,0,0,90,90,90,0,0,8,0,8,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,90,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,90,0,0,1,0,90,0,Infiltration-mitm
10.0.63.20,224.0.0.251,36693,5353,2048,2023-05-04 12:15:26,0,0,0,0,0,1,0,89,0,89,89,89,0,0,0,0,0,89,89,89,0,0,8,0,8,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,89,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,89,0,0,1,0,89,0,Infiltration-mitm
10.0.63.20,239.255.255.250,44167,1900,2048,2023-05-04 12:15:26,0,0,0,0,0,1,0,136,0,136,136,136,0,0,0,0,0,136,136,136,0,0,8,0,8,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,136,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,136,0,0,1,0,136,0,Infiltration-mitm
10.0.63.20,239.255.255.250,42324,3702,2048,2023-05-04 12:15:26,0,0,0,0,0,1,0,623,0,623,623,623,0,0,0,0,0,623,623,623,0,0,8,0,8,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,623,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,623,0,0,1,0,623,0,Infiltration-mitm
10.0.63.20,10.0.63.1,41705,137,2048,2023-05-04 12:15:26,0,0,0,0,0,1,0,94,0,94,94,94,0,0,0,0,0,94,94,94,0,0,8,0,8,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,94,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,94,0,0,1,0,94,0,Infiltration-mitm
10.0.63.20,224.0.0.251,58734,5353,2048,2023-05-04 12:15:27,0,0,0,0,0,1,0,90,0,90,90,90,0,0,0,0,0,90,90,90,0,0,8,0,8,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,90,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,90,0,0,1,0,90,0,Infiltration-mitm
10.0.63.20,224.0.0.251,43410,5353,2048,2023-05-04 12:15:28,0,0,0,0,0,1,0,73,0,73,73,73,0,0,0,0,0,73,73,73,0,0,8,0,8,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,73,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,73,0,0,1,0,73,0,Infiltration-mitm
10.0.63.20,224.0.0.251,59668,5353,2048,2023-05-04 12:15:29,0,0,0,0,0,1,0,83,0,83,83,83,0,0,0,0,0,83,83,83,0,0,8,0,8,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,83,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,83,0,0,1,0,83,0,Infiltration-mitm

```

<!--  {% endraw %} -->
