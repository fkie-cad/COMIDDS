---
title: CSV Download
---

## [Download here]({{ site.baseurl }}/assets/data/datasets.csv)

This `.csv` file is automatically created by parsing all currently existing dataset entries.
It can be used to sort and filter data in a spreadsheet program or generate statistics and plots.
The following fields are present for each dataset (semicolon-delimited):

| Field Name           | Description                                                                                                  |
|----------------------|--------------------------------------------------------------------------------------------------------------|
| Name                 | Name of the dataset                                                                                          |
| Network Attacks      | Does this dataset feature network-based attacks (Yes/No)                                                     |
| Host Attacks         | Does this dataset feature host-based attacks (Yes/No)                                                        |
| Start Year           | Year in which data collection started                                                                        |
| End Year             | Year in which data collection ended (usually the same as `Start Year`, but not always)                       |
| Setting              | Setting of the underlying scenario (Single OS/Enterprise IT/Military IT/Subsystem/Miscellaneous/Undisclosed) |
| OS Type              | OS families that were part of the underlying scenario (Windows/Linux/Unix/MacOS/Undisclosed)                 |
| Network Data Source  | Source of network data (e.g., pcaps or NetFlows)                                                             |
| Network Data Labeled | If and how labels for network data are available                                                             |
| Host Data Source     | Source of host data (e.g., Windows events or ssh auth logs)                                                  |
| Host Data Labeled    | If and how labels for host data are available                                                                |
| Attack Categories    | Types of attacks in the underlying scenario                                                                  |
| Benign activity      | How benign activity (aka "normal behavior") was generated in the underlying scenario                         |
| Packed Size in MB    | Size of the entire dataset when packed, in MB                                                                |
| Unpacked Size in MB  | Size of the entire dataset when unpacked, in MB                                                              |
