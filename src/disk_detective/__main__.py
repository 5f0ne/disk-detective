import sys

import argparse

from hash_calc.HashCalc import HashCalc

from disk_detective.Controller import Controller

from disk_detective.mbr.MBRPrinter import MBRPrinter
from disk_detective.mbr.MasterBootRecord import MasterBootRecord

from disk_detective.fat.FATPrinter import FATPrinter
from disk_detective.fat.FileAllocationTable import FileAllocationTable

from disk_detective.usage.DiskUsagePrinter import DiskUsagePrinter

def main(args=None):
    """The main routine."""
    if args is None:
        args = sys.argv[1:]

    parser = argparse.ArgumentParser()
    parser.add_argument("--path", "-p", type=str, required=True, help="Path to file")
    parser.add_argument("--mode", "-m", choices=["mbr", "usage", "fat"], required=True, help="The tool to use")
    parser.add_argument("--offset", "-o", type=int, help="The offset to start reading (used in mode=fat)")
    args = parser.parse_args()

    c = Controller()
    hash = HashCalc(args.path)

    c.printHeader(args.path, hash)

    if(args.mode == "mbr"):
        with open(args.path, "rb") as f:
            mbrBytes = f.read(512)
            mbr = MasterBootRecord(mbrBytes)
            mbrPrinter = MBRPrinter()
            mbrPrinter.print(mbr)
    elif(args.mode == "usage"):
        with open(args.path, "rb") as f:
            mbrBytes = f.read(512)
            mbr = MasterBootRecord(mbrBytes)
            usagePrinter = DiskUsagePrinter()
            usagePrinter.print(mbr)
    elif(args.mode == "fat"):
        with open(args.path, "rb") as f:
            f.seek(args.offset, 0)
            fatBytes = f.read(512)
            fat = FileAllocationTable(fatBytes)
            fatPrinter = FATPrinter()
            fatPrinter.print(fat)           
        
    c.printExecutionTime()


if __name__ == "__main__":
    sys.exit(main())


