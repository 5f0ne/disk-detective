class MBRPrinter():
    def __init__(self) -> None:
        pass

    def print(self, mbr):
        bl = mbr.bootloader.hex(" ").upper().split(" ")
        splitted = [bl[i:i + 16] for i in range(0, 440, 16)]
        print("")
        print("Master Boot Record Examiner")
        print("---------------------------")
        print("")
        print("--> Bootloader (0x0000 - 0x01B7 | 440 Bytes) ")
        self.__printBootloader(splitted)
        print("")
        print("--> Serial Number (0x01B8 - 0x01BB | 4 Bytes) ")
        print("    " + mbr.serialNumber.hex(" ").upper())
        print("")
        print("--> Null Bytes (0x01BC - 0x01BD | 2 Bytes) ")
        print("    " + mbr.nullBytes.hex(" ").upper())
        print("")
        print("--> Partition Entries (0x01BE - 0x01FD | 64 Bytes) ")
        for partitionEntry in mbr.partitionEntries:
            self.__printPartitionEntry(partitionEntry)

        print("--> Identifier (0x01FE - 0x01FF | 2 Bytes) ")
        print("    " + mbr.identifier.hex(" ").upper())

    def __printPartitionEntry(self, entry):
        print("")
        s = entry.status.hex(" ").upper()
        f = entry.fSector.hex(" ").upper()
        p = entry.partType.hex(" ").upper()
        partitionTypes = entry.getPartitionTypes()
        l = entry.lSector.hex(" ").upper()
        o = entry.offset.hex(" ").upper()
        n = entry.noOfSectors.hex(" ").upper()

        print("---------->      Entry: " + s + " " + f + " " + p + " " + l + " " + o + " " + n)
        print("                 -----")
        print("                Status: " + s)
        print("        --------------")
        print("                        " + entry.getStatus())
        print("        --------------")
        print("    First Sector (CHS): " + f)
        print("        --------------")
        print(f"            ---------->                {f} to bin: " + entry.fSectorBin[0:8] + " " + entry.fSectorBin[8:16] + " " + entry.fSectorBin[16:24])
        print("            ---------->         Head   " + entry.chs["start"]["headbin"] + " to dec: " + str(entry.chs["start"]["head"]))
        print("            ---------->       Sector     " + entry.chs["start"]["sectorbin"] + " to dec: " + str(entry.chs["start"]["sector"]))
        print("            ---------->     Cylinder " + entry.chs["start"]["cylinderbin"] + " to dec: " + str(entry.chs["start"]["cylinder"]))
        print("")
        print("                            CHS: " + str(entry.chs["start"]["cylinder"]) + "/" + str(entry.chs["start"]["head"]) + "/" + str(entry.chs["start"]["sector"]))
        print("        --------------")
        print("        Partition Type: " + p)
        print("        --------------")
        print("            Candidates:")
        for t in partitionTypes:
            print("                   ---> ID: " + t.id + "   Type: " + t.description)
        print("        --------------")
    
        print("     Last Sector (CHS): " + l)
        print("        --------------")
        print(f"            ---------->                {l} to bin: " + entry.lSectorBin[0:8] + " " + entry.lSectorBin[8:16] + " " + entry.lSectorBin[16:24])
        print("            ---------->         Head   " + entry.chs["end"]["headbin"] + " to dec: " + str(entry.chs["end"]["head"]))
        print("            ---------->       Sector     " + entry.chs["end"]["sectorbin"] + " to dec: " + str(entry.chs["end"]["sector"]))
        print("            ---------->     Cylinder " + entry.chs["end"]["cylinderbin"] + " to dec: " + str(entry.chs["end"]["cylinder"]))
        print("")
        print("                            CHS: " + str(entry.chs["end"]["cylinder"]) + "/" + str(entry.chs["end"]["head"]) + "/" + str(entry.chs["end"]["sector"]))
        print("        --------------")
        print("Offset to first sector: " + o)
        print("        --------------")
        print("                        " + str(entry.getOffsetLBA()))
        print("        --------------")
        print("        No. of sectors: " + n)
        print("        --------------")
        print("                        " + str(entry.getNoOfSectors()))
        print("                        " + str((entry.getNoOfBytes()/1024)/1024) + " MB")
        print("        --------------")
        print("")

    def __printBootloader(self, splitted):
        for line in splitted:
            print("    ", end="")
            for value in line:
                print(value + " ", end="")
            print("")