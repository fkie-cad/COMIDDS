---
title: CIDD
---

- [Description](#description)
- [Remarks](#remarks)
- [Papers](#papers)
- [Links](#links)

### Description

The Cloud Intrusion Detection Dataset (CIDD) attempts to offer training data for behavior-based detection systems in
cloud environments.
It is based on the DARPA'98 program and generates CIDD by leveraging a tool they call Log Analyzer and Correlator
System (LACS), which, in essence, combines logs from various sources that came from the same user to allow IDSs to
track / train on user behavior distributed over various machines and networks.
This is done to then evaluate detection of masquerade attacks, which can be difficult to recognize using traditional
means.

### Remarks

The authors take binary audit data as well as tcpdumps provided by the source dataset and convert them such that they
can be correlated, i.e., assigned to specific users.

_Not exploring this further, mostly because:_

- _most of the dataset is no longer available (loads of dead links), and without useful docs and data to look at, this
  is honestly really annoying to work with_
- _it is based on DARPA'98, which makes it inherently uninteresting_

For further interest, refer to sections 4.1 and 4.2 of the cited paper.

### Papers

- [CIDD: A Cloud Intrusion Detection Dataset For Cloud Computing and Masquerade Attacks (2012)](https://doi.org/10.1109/itng.2012.97)

### Links

- [Homepage](http://groups.di.unipi.it/~hkholidy/projects/cidd/)
- [Download Page](http://groups.di.unipi.it/~hkholidy/projects/cidd/download.html)
    - some links are dead