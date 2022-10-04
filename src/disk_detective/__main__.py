import os
import sys

import argparse

from hash_calc.HashCalc import HashCalc

from disk_detective.Controller import Controller

from disk_detective.mbr.MBRPrinter import MBRPrinter
from disk_detective.mbr.MasterBootRecord import MasterBootRecord

from disk_detective.structure.DiskStructurePrinter import DiskStructurePrinter

def main(args=None):
    """The main routine."""
    if args is None:
        args = sys.argv[1:]

    parser = argparse.ArgumentParser()
    parser.add_argument("--path", "-p", type=str, required=True, help="Path to file")
    parser.add_argument("--mode", "-m", choices=["mbr", "structure"], required=True, help="The tool to use")
    args = parser.parse_args()

    c = Controller()
    hash = HashCalc(args.path)

    c.printHeader(args.path, hash)

    with open(args.path, "rb") as f:
        mbrBytes = f.read(512)
        mbr = MasterBootRecord(mbrBytes)

    if(args.mode == "mbr"):
            mbrPrinter = MBRPrinter()
            mbrPrinter.print(mbr)
    elif(args.mode == "structure"):
            structurePrinter = DiskStructurePrinter()
            structurePrinter.print(mbr)

    c.printExecutionTime()


if __name__ == "__main__":
    sys.exit(main())


