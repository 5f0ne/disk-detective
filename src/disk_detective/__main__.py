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

def loadFATConfigs():
    fatConfigs = []
    configs = ["fat.json", "fat1216.json", "fat32.json", "fat-type.json", "fat-fs-info.json"]
    p = os.path.join(os.path.dirname(__file__), "fat", "config")
    for config in configs:
        fullPath = os.path.join(p, config)
        f = open(fullPath, encoding="utf8")
        fatConfigs.append((config, json.load(f)))
        f.close()
    return fatConfigs


def main(args=None):
    """The main routine."""
    if args is None:
        args = sys.argv[1:]

    parser = argparse.ArgumentParser()
    parser.add_argument("--path", "-p", type=str, required=True, help="Path to file")
    parser.add_argument("--mode", "-m", choices=["mbr", "usage", "fat-vbr", "fat-fsinfo"], required=True, help="The tool to use")
    parser.add_argument("--offset", "-o", type=int, help="The offset to start reading (used in mode=fat)")
    args = parser.parse_args()

    c = Controller()
    loader = ConfigLoader()
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
        
    c.printExecutionTime()


if __name__ == "__main__":
    sys.exit(main())


