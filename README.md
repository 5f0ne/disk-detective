# Description

Provides tools to analyze disks on byte level

# Available Tools

- Master Boot Record Examiner
  - Provides information and analysis of MBR


# Under Construction

- Disk Structure Information
  - Overview of disk space usage based on MBR information

# Future Tools

- Extended Partition Analyser
  - Examines extended parititions

- File System Analyser
  - FAT
  - ext
  - NTFS
  

# Installation

`pip install disk_detective`

# Usage

**From command line:**

`python -m disk_detective --path PATH --mode {mbr}`

| Option | Short | Type | Default | Description |
|---|---|---|---|---|
|--path | -p | String | - | Path to file (dd, raw) or <br> path to disk (\\.\PhysicalDrive0, /dev/sda, /dev/disk1)|
|--mode | -p | String | - | mbr = Examines the MBR <br> structure = Overview of disk space|

# Example

**Output for mode == mbr**

`python -m disk_detective -p path/to/example.dd -m mbr`

Please find the [here](example/example-mbr.txt)

# License

MIT