---
title: gureKDDCup
---

- [Overview](#overview)
- [Environment](#environment)
- [Activity](#activity)
- [Contained Data](#contained-data)
- [Papers](#papers)
- [Links](#links)
- [Related Entries](#related-entries)
- [Data Examples](#data-examples)

| <!-- -->                 | <!-- -->                                                                                                   |
|--------------------------|------------------------------------------------------------------------------------------------------------|
| **Network Data Source**  | Connection records with payload                                                                            |
| **Network Data Labeled** | Yes                                                                                                        |
| **Host Data Source**     | -                                                                                                          |
| **Host Data Labeled**    | -                                                                                                          |
|                          |                                                                                                            |
| **Overall Setting**      | Military IT                                                                                                |
| **OS Types**             | Linux 2.0.27<br/>SunOS 4.1.4<br/>Sun Solaris 2.5.1<br/>Windows NT                                          |
| **Number of Machines**   | 1000's                                                                                                     |
| **Total Runtime**        | Nine weeks                                                                                                 |
| **Year of Collection**   | 1998                                                                                                       |
| **Attack Categories**    | DoS<br/>Remote to Local<br/>User to Root<br/>Surveillance/Probing                                          |
| **Benign Activity**      | Scripts for synthetic traffic generation, real humans for performing complex tasks                         |
|                          |                                                                                                            |
| **Packed Size**          | 10 GB                                                                                                      |
| **Unpacked Size**        | n/a                                                                                                        |
| **Download Link**        | [goto](http://www.sc.ehu.es/acwaldap/gureKddcup/gureKDDCup/gureKddcup/complete_database/gureKddcup.tar.gz) |

***

### Overview
The gureKDDCup dataset is an extension of the well known KDDCup 1999 dataset -- which consists of connection records --, adding additional information regarding payloads.
Consequently, it is also based on the DARPA'98 Intrusion Detection Program;
information about both of these datasets can be found in the [Related Entries](#related-entries) section.
Note that the authors did not directly copy the KDDCup 1999 dataset, but instead recreated it using the same methodology, including additional information in the process.

### Environment
Refer to the underlying [DARPA'98 Intrusion Detection Program](darpa98.md).

### Activity
Refer to the underlying [DARPA'98 Intrusion Detection Program](darpa98.md).

### Contained Data
The raw DARPA data, which comes in the form of binary TCP dumps, is transformed into connection records, mimicking the methodology of the KDDCup 1999 dataset.
This entire process is documented extensively in a separate document, which is linked below.
A connection record is defined as "a sequence of TCP packets starting and ending at some well-defined times, between
which data flows to and from a source IP address to a target IP address under some well-defined protocol".
Just as with the KDDCup dataset, each record contains 41 features (described in section C.2 of the documentation), with a 42nd label indicating whether this event is normal or malicious, which in the latter case also references the specific attack that event belongs to.

As mentioned, the distinguishing factor here is the inclusion of additional payload information.
That is, for each connection record, three additional files are generated:
- `*.a`: sent packets' payloads, sorted by time
- `*.b`: received packets' payloads, sorted by time
- `*.c`: all packet payloads of the connection, sorted by time

The filename before the extension is equal to the number of the associated conneciton record.
Data is divided into seven weeks, which then each contain five folders, one for every workday (MON-FR).
Each of those contains the following data:
- `gureKddcup.list`: Connection records for that day.
  The first 6 attributes are: connection_number, start_time, orig_port, resp_port, orig_ip, resp_ip (information to identify the connection), followed by the cited 41 attributes plus class (see data example below)
- `a-matched`: All sent packets' payloads of that days connections, one file per connection record.
  Each filename matches to a connection_number in the list of connection records.
- `b-matched`: All received packets' payloads of that days connections, one file per connection record.
  Each filename matches to a connection_number in the list of connection records.
- `a-matched`: All packets' payloads of that days connections, one file per connection record.
  Each filename matches to a connection_number in the list of connection records.

The authors also supply a subset of this data called gureKddcup6percent.
It supplies the same information in the same way, but, as the name suggests, only supplies 6% of the original connection records plus associated payloads.
This sample contains all no-flood attacks, and a random selection of normal connections.

### Papers
- [Service-independent payload analysis to improve intrusion detection in network traffic (2008)](https://dl.acm.org/doi/10.5555/2449288.2449315)

### Links
- [Homepage](http://www.sc.ehu.es/acwaldap/gureKddcup/galdetegia_jaso.php) (form does not have to be filled out)
- [Documentation](https://addi.ehu.es/bitstream/handle/10810/20608/20160601_Txostena_gurekddcup_InigoPeronaBalda.pdf?sequence=1)
- [Link Hub](http://www.sc.ehu.es/acwaldap/) (in case homepage link deprecates)

## Related Entries
- [DARPA'98 Intrusion Detection Program](darpa98.md)
- [KDD Cup 1999](kdd_cup_1999.md)

### Data Examples
Connection records taken from `gureKddcup/Week6/Thursday/gureKddcup.list/gureKddcup-matched.list`
```
64558768 899989341.327858 8 0 197.218.177.69 172.16.114.115 0.000000 icmp 8 SH 10 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.000000 0.000000 0.000000 0.000000 0.000000 0.000000 0.000000 0 12 0.000000 0.000000 0.120000 1.000000 0.000000 0.000000 0.000000 0.000000 ipsweep
64558769 899989341.638201 4136 80 172.16.113.84 192.43.70.122 0.039594 tcp 80 SF 160 479 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0.000000 0.000000 0.000000 0.000000 0.000000 0.000000 0.000000 0 9 0.000000 0.000000 0.000000 1.000000 0.000000 0.111111 0.000000 0.000000 
64558771 899989342.617289 1904 161 194.27.251.21 192.168.1.1 0.000000 udp 161 S0 105 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.000000 0.000000 0.000000 0.000000 0.000000 0.000000 0.000000 38 28 0.736842 0.263158 0.000000 0.000000 0.368421 0.500000 0.000000 0.000000 
64558772 899989342.617289 161 1904 192.168.1.1 194.27.251.21 0.045382 udp 161 SF 0 146 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1.000000 1.000000 0.000000 0.000000 1.000000 0.000000 0.000000 39 29 0.743590 0.256410 0.010000 0.000000 0.384615 0.517241 0.000000 0.000000 
64558773 899989343.121947 49724 928 206.48.44.18 172.16.112.50 0.000449 tcp 928 REJ 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.000000 0.000000 0.000000 0.000000 0.000000 0.000000 0.000000 25 0 0.000000 1.000000 0.250000 0.000000 0.000000 0.000000 1.000000 0.000000 portsweep
64558774 899989343.345483 4141 25 172.16.113.84 194.7.248.153 2.057617 tcp 25 SF 3044 325 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0.000000 0.000000 0.000000 0.000000 0.000000 0.000000 0.000000 0 12 0.000000 0.000000 0.000000 1.000000 0.000000 0.166667 0.000000 0.000000 
64558776 899989345.407192 4144 25 172.16.113.84 196.37.75.158 3.208491 tcp 25 SF 3047 331 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 2 0.000000 0.000000 0.000000 0.000000 0.000000 0.000000 1.000000 0 14 0.000000 0.000000 0.000000 1.000000 0.000000 0.142857 0.000000 0.000000 
64558777 899989346.151906 49724 91 206.48.44.18 172.16.112.50 0.000430 tcp 91 REJ 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.000000 0.000000 0.000000 0.000000 0.000000 0.000000 0.000000 26 0 0.000000 1.000000 0.260000 0.000000 0.000000 0.000000 1.000000 0.000000 portsweep
64558778 899989346.203066 26326 25 197.182.91.233 172.16.112.207 0.905250 tcp 25 SF 4536 329 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 2 0.000000 0.000000 0.000000 0.000000 0.000000 0.000000 1.000000 0 13 0.000000 0.000000 0.000000 1.000000 0.000000 0.153846 0.000000 0.000000 
64558779 899989346.716433 8 0 197.218.177.69 172.16.114.116 0.000000 icmp 8 SH 10 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.000000 0.000000 0.000000 0.000000 0.000000 0.000000 0.000000 0 13 0.000000 0.000000 0.130000 1.000000 0.000000 0.000000 0.000000 0.000000 ipsweep
```