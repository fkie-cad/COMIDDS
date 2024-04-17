---
title: CSV Download
---

## [Download here]({{ site.baseurl }}/assets/data/datasets.csv)

This `.csv` file was created by parsing all currently existing dataset entries.
It does not contain any new information, but is intended to facilitate deriving statistics or similar analysis purposes.
The following fields are present for each dataset (semicolon-delimited):

| Field Name           | Description                                                                                                  |
|----------------------|--------------------------------------------------------------------------------------------------------------|
| Name                 | Name of the dataset                                                                                          |
| Network Focus        | Does this dataset feature network-based attacks and logs (Yes/No)                                            |
| Host Focus           | Does this dataset feature host-based attacks and logs (Yes/No)                                               |
| Start Year           | Year in which log collection started                                                                         |
| End Year             | Year in which log collection ended (usually the same as `Start Year`, but not always)                        |
| Setting              | Setting of the underlying scenario (Single OS/Enterprise IT/Military IT/Subsystem/Miscellaneous/Undisclosed) |
| OS Type              | OS families that were part of the underlying scenario (Windows/Linux/Unix/MacOS/Undisclosed)                 |
| Network Log Source   | Source of network logs (e.g., pcaps or NetFlows)                                                             |
| Network Logs Labeled | If and how labels for network logs are available                                                             |
| Host Log Source      | Source of host logs (e.g., Windows events or ssh auth logs)                                                  |
| Host Logs Labeled    | If and how labels for host logs are available                                                                |
| Attack Categories    | Types of attacks in the underlying scenario                                                                  |
| User Emulation       | How user behavior (aka "normal behavior") was generated in the underlying scenario                           |
| Packed Size in MB    | Size of the entire dataset when packed, in MB                                                                |
| Unpacked Size in MB  | Size of the entire dataset when unpacked, in MB                                                              |
