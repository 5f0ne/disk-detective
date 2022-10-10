# Description

Provides tools to analyze disks on byte level

# Available Tools

- Master Boot Record Examiner
  - Provides information and analysis of MBR

- FAT Examiner
  - Provides information and analysis of FAT boot sector

# Under Construction

- Disk Usage Information
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

`python -m disk_detective --path PATH --mode {mbr,structure,fat} [--offset OFFSET]`

| Option | Short | Type | Default | Description |
|---|---|---|---|---|
|--path | -p | String | - | Path to file (dd, raw) or <br> path to disk (\\.\PhysicalDrive0, /dev/sda, /dev/disk1)|
|--mode | -p | String | - | mbr = Examines the MBR <br> usage = Overview of disk space usage <br> fat = Examines FAT Boot Record |
|--offset | -o | Int | - | The offset in bytes to start reading |

# Example

**Output for mode == mbr**

`python -m disk_detective -p path/to/example.dd -m mbr`

Please find the [here](example/example-mbr.txt)

**Output for mode == fat**

`python -m disk_detective -p path/to/example.dd -m mbr -o 1048576`

Please find the [here](example/example-fat.txt)

# License

MIT