# Description

Provides tools to analyze disks on byte level

# Available Tools

- Master Boot Record Examiner
  - Provides information and analysis of MBR

- FAT Examiner
  - Provides information and analysis of:
    -  FAT VBR
    -  FAT FSInfo

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

`python -m disk_detective --path PATH --mode {mbr,structure,fat-vbr,fat-fsinfo} [--offset OFFSET]`

| Option | Short | Type | Default | Description |
|---|---|---|---|---|
|--path | -p | String | - | Path to file (dd, raw) or <br> path to disk (\\.\PhysicalDrive0, /dev/sda, /dev/disk1)|
|--mode | -p | String | - | mbr = Examines the MBR <br> usage = Overview of disk space usage <br> fat-vbr = Examines FAT VBR <br> fat-fsinfo = Examines FAT FSInfo|
|--offset | -o | Int | - | The offset in bytes to start reading |

# Example

**Output for mode == mbr**

`python -m disk_detective -p path/to/example.dd -m mbr`

Please find the result [here](example/example-mbr.txt)

<hr>

**Output for mode == fat-vbr**

`python -m disk_detective -p path/to/example.dd -m fat-vbr -o 1048576`

Please find the result [here](example/example-fat-vbr.txt)

<hr>

**Output for mode == fat-fsinfo**

`python -m disk_detective -p path/to/example.dd -m fat-fsinfo -o 1049088`

Please find the result [here](example/example-fat-fsinfo.txt)


# License

MIT