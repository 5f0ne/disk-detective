import os
import sys
import json
import argparse

from hash_calc.HashCalc import HashCalc

from disk_detective.Controller import Controller

from disk_detective.util.ConfigLoader import ConfigLoader

from disk_detective.mbr.MBRPrinter import MBRPrinter
from disk_detective.mbr.MasterBootRecord import MasterBootRecord

from disk_detective.fat.FATPrinter import FATPrinter
from disk_detective.fat.FATParser import FATParser

from disk_detective.usage.DiskUsagePrinter import DiskUsagePrinter

def main(args=None):
    """The main routine."""
    if args is None:
        args = sys.argv[1:]

    parser = argparse.ArgumentParser()
    parser.add_argument("--path", "-p", type=str, required=True, help="Path to file")
    parser.add_argument("--mode", "-m", choices=["mbr", "usage", "fat-vbr", "fat-fsinfo", "fat-lfn", "fat-dir-entry"], required=True, help="The tool to use")
    parser.add_argument("--offset", "-o", type=int, default = 0, help="The offset to start reading (used in mode=fat)")
    args = parser.parse_args()

    c = Controller()
    loader = ConfigLoader()
    hash = HashCalc(args.path)

    c.printHeader(args.path, hash, args.offset)

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
    elif(args.mode == "fat-vbr"):
        with open(args.path, "rb") as f:
            f.seek(args.offset, 0)
            fatBytes = f.read(512)
            parser = FATParser()
            fatConfigs = loader.load(os.path.dirname(__file__), "fat")
            fat = parser.parseVBR(fatBytes, fatConfigs)
            fatPrinter = FATPrinter()
            fatPrinter.printVBR(fat)
    elif(args.mode == "fat-fsinfo"):    
         with open(args.path, "rb") as f:
            f.seek(args.offset, 0)
            fatBytes = f.read(512)
            parser = FATParser()
            fatConfigs = loader.load(os.path.dirname(__file__), "fat")
            fat = parser.parseFsInfo(fatBytes, fatConfigs[4][1])
            fatPrinter = FATPrinter()
            fatPrinter.printFsInfo(fat)    
    elif(args.mode == "fat-lfn"):    
         with open(args.path, "rb") as f:
            f.seek(args.offset, 0)
            fatBytes = f.read(32)
            parser = FATParser()
            fatConfigs = loader.load(os.path.dirname(__file__), "fat")
            fat = parser.parseLFN(fatBytes, fatConfigs[5][1])
            fatPrinter = FATPrinter()
            fatPrinter.printLFN(fat)
    elif(args.mode == "fat-dir-entry"):    
         with open(args.path, "rb") as f:
            f.seek(args.offset, 0)
            fatBytes = f.read(32)
            parser = FATParser()
            fatConfigs = loader.load(os.path.dirname(__file__), "fat")
            fat = parser.parseDirEntry(fatBytes, fatConfigs[6][1])
            fatPrinter = FATPrinter()
            fatPrinter.printDirEntry(fat)  
        
    c.printExecutionTime()


if __name__ == "__main__":
    sys.exit(main())


