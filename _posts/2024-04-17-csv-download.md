---
layout: post
title: News in v1.3.0
subtitle: Dataset info now available in CSV format, one new dataset entry
gh-repo: fkie-cad/intrusion-detection-datasets
gh-badge: [star, fork, follow]
tags: [dataset, features]
comments: true
author: Philipp Bönninghausen
---

This update adds the possibility to download a `.csv` file containing information automatically parsed from all currently existing dataset entries.
It can be used to sort and filter data in a spreadsheet program or generate statistics and plots - access the file via the navbar (or [this link](/COMIDDS/content/csv_download)).
There, you will also find explanation for all contained fields.

New dataset entries:
- [TUIDS](/COMIDDS/content/datasets/tuids)

Other changes:
- Attempted to "normalize" several descriptions (e.g., "Packet captures", "Pcaps" and "pcaps" are now all called "pcaps")
- The parser is available as an automated script in the new `/tools` directory and should be used to add new datasets