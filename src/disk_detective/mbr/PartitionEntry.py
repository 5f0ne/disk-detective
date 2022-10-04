from partitiontypes.PartitionTypes import PartitionTypes

class PartitionEntry():
    partitionTypes = PartitionTypes()
    def __init__(self, partitionBytes) -> None:
        # Boot indicator
        self.status = bytearray()                       #   1 Byte
        # Starting sector in CHS notation
        self.fSector = bytearray()                      #   3 Byte
        # Partition type
        self.partType = bytearray()                     #   1 Byte
        # Ending sector in CHS notation
        self.lSector = bytearray()                      #   3 Byte
        # offset to starting sector in LBA notation
        self.offset = bytearray()                       #   4 Byte
        # Number of sectors / size of partition
        self.noOfSectors = bytearray()                  #   4 Byte
        
        self.fSectorBin = ""
        self.lSectorBin = ""

        self.chs = {
            "start": {
                "head": 0,
                "sector": 0,
                "cylinder": 0,
                "headbin": "",
                "sectorbin": "",
                "cylinderbin": ""
            },
             "end": {
                "head": 0,
                "sector": 0,
                "cylinder": 0,
                "headbin": "",
                "sectorbin": "",
                "cylinderbin": ""
            }
        }

        self.__process(partitionBytes)


    def __process(self, pBytes):
        status = [pBytes[i:i + 1] for i in range(0, 1, 1)][0]
        self.status.extend(status)

        fSector = [pBytes[i:i + 3] for i in range(1, 4, 3)][0]
        self.fSector.extend(fSector)

        partType = [pBytes[i:i + 1] for i in range(4, 5, 1)][0]
        self.partType.extend(partType)

        lSector = [pBytes[i:i + 3] for i in range(5, 8, 3)][0]
        self.lSector.extend(lSector)

        offset = [pBytes[i:i + 4] for i in range(8, 12, 4)][0]
        self.offset.extend(offset)
        
        noOfSectors = [pBytes[i:i + 4] for i in range(12, 16, 4)][0]
        self.noOfSectors.extend(noOfSectors)

        h = self.fSector.hex(" ").replace(" ", "")
        self.fSectorBin = self.__hexToBin(h).rjust(24, "0")
        self.__calculateCHS("start", self.fSectorBin)

        h = self.lSector.hex(" ").replace(" ", "")
        self.lSectorBin = self.__hexToBin(h).rjust(24, "0")
        self.__calculateCHS("end", self.lSectorBin)

    def __toLittleEndian(self, value):
        # example for value = "20 21 00"
        s = value.split(" ")
        h_ = "".join(s[i] for i in range(len(s)-1, -1, -1))
        return h_

    def __hexToBin(self, hex):
        return bin(int(hex, base=16)).replace("0b","")

    def __hexToDec(self, hex_):
        return int(hex_, 16)

    def __binToDec(self, bin):
        # example for bin = "100001"
        return int(bin, 2)

    def __calculateCHS(self, type_, binary):
        if(len(binary) < 24):
            binary = binary.rjust(24, "0")

        self.chs[type_]["headbin"] = "".join(binary[i:i+8] for i in range(0, 8, 8))

        
        firstTwoCylBits = "".join(binary[i:i+2] for i in range(8, 10, 2))

        self.chs[type_]["sectorbin"] = "".join(binary[i:i+6] for i in range(10, 16, 6))

        lastSixCylBits = "".join(binary[i:i+8] for i in range(16, 24, 8))

        self.chs[type_]["cylinderbin"]  = firstTwoCylBits + lastSixCylBits

        self.chs[type_]["head"] = self.__binToDec(self.chs[type_]["headbin"])
        self.chs[type_]["sector"] = self.__binToDec(self.chs[type_]["sectorbin"])
        self.chs[type_]["cylinder"] = self.__binToDec(self.chs[type_]["cylinderbin"])


    def getOffsetLBA(self):
        h = self.offset.hex(" ")
        lEHex = self.__toLittleEndian(h)
        return self.__hexToDec(lEHex)

    def getNoOfSectors(self):
        h = self.noOfSectors.hex(" ")
        lEHex = self.__toLittleEndian(h)
        return self.__hexToDec(lEHex)

    def getNoOfBytes(self):
        return self.getNoOfSectors() * 512

    def getStatus(self):
        result = "Not bootable"
        if(self.status.hex() == "80"):
            result = "Bootable"
        return result

    def getPartitionTypes(self):
        t = self.partType.hex(" ").upper()
        return PartitionEntry.partitionTypes.getIds(t)