# TODO: Identification between FAT12, FAT16 and FAT32
from cnvrtr.Converter import Converter

class FileAllocationTable():
    def __init__(self, data) -> None:
        super().__init__()
        self.bootCodeJmpInst = bytearray()      # 3 Byte
        self.fsOemName = bytearray()            # 8 Bytes
        self.sectorSize = bytearray()           # 2 Bytes
        self.sectorsPerDataUnit = bytearray()   # 1 Byte
        self.sectorsPerReserved = bytearray()   # 2 Bytes
        self.noOfFATs = bytearray()             # 1 Byte
        self.maxFilesInRootDir = bytearray()    # 2 Bytes
        self.noOfSectorsInFS = bytearray()      # 2 Bytes
        self.storageMediaType = bytearray()     # 1 Byte
        self.noOfSectorsInFATs = bytearray()    # 2 Bytes
        self.noOfSectorsPerTrack = bytearray()  # 2 Bytes
        self.noOfHeads = bytearray()            # 2 Bytes
        self.noOfHiddenLS = bytearray()         # 4 Bytes
        self.noOfSectorsInFS_long = bytearray() # 4 Bytes
        self._cnvrtr = Converter()
        self.__process(data)

    def getOEMName(self):
        oemName = ""
        hexValues = self.fsOemName.hex(" ").split(" ")
        for v in hexValues:
            dec = self._cnvrtr.hexToDec(v)
            oemName += self._cnvrtr.decToAscii(dec)
        return oemName

    def getSectorSize(self):
        return self.__hexToLittleEndianToDec(self.sectorSize)

    def getLogicalSectorsPerDataUnit(self):
        return self.__hexToLittleEndianToDec(self.sectorsPerDataUnit)

    def getLogicalSectorsPerReservedArea(self):
        return self.__hexToLittleEndianToDec(self.sectorsPerReserved)

    def getNoOfFATs(self):
        return self.__hexToLittleEndianToDec(self.noOfFATs)

    def getMaxFilesInRootDir(self):
        return self.__hexToLittleEndianToDec(self.maxFilesInRootDir)

    def getNoOfSectorsInFS(self):
        return self.__hexToLittleEndianToDec(self.noOfSectorsInFS)

    def getStorageType(self):
        result = "-/-"
        if(self.storageMediaType.hex(" ") == "f8"):
            result = "Fixed"
        elif(self.storageMediaType.hex(" ") == "f0"):
            result = "Removable"
        return result

    def getNoOfSectorsInFATs(self):
        return self.__hexToLittleEndianToDec(self.noOfSectorsInFATs)

    def getNoOfSectorsPerTrack(self):
        return self.__hexToLittleEndianToDec(self.noOfSectorsPerTrack)

    def getNoOfHeads(self):
        return self.__hexToLittleEndianToDec(self.noOfHeads)

    def getNoOfHiddenSectors(self):
        return self.__hexToLittleEndianToDec(self.noOfHiddenLS)

    def getNoOfSectorsInFS_long(self):
        return self.__hexToLittleEndianToDec(self.noOfSectorsInFS_long)

    def __hexToLittleEndianToDec(self, byteArr):
        le = self._cnvrtr.toLittleEndian(byteArr.hex(" "))
        return str(self._cnvrtr.hexToDec(le))

    def __process(self, fatBytes):
        bootCodeJmpInst = [fatBytes[i:i + 3] for i in range(0, 3, 3)][0]
        self.bootCodeJmpInst.extend(bootCodeJmpInst)

        fsOemName = [fatBytes[i:i + 8] for i in range(3, 11, 8)][0]
        self.fsOemName.extend(fsOemName)

        sectorSize = [fatBytes[i:i + 2] for i in range(11, 13, 2)][0]
        self.sectorSize.extend(sectorSize)

        sectorsPerDataUnit = [fatBytes[i:i + 1] for i in range(13, 14, 1)][0]
        self.sectorsPerDataUnit.extend(sectorsPerDataUnit)

        sectorsPerReserved = [fatBytes[i:i + 2] for i in range(14, 16, 2)][0]
        self.sectorsPerReserved.extend(sectorsPerReserved)

        noOfFATs = [fatBytes[i:i + 1] for i in range(16, 17, 1)][0]
        self.noOfFATs.extend(noOfFATs)

        maxFilesInRootDir = [fatBytes[i:i + 2] for i in range(17, 19, 2)][0]
        self.maxFilesInRootDir.extend(maxFilesInRootDir)

        noOfSectorsInFS = [fatBytes[i:i + 2] for i in range(19, 21, 2)][0]
        self.noOfSectorsInFS.extend(noOfSectorsInFS)

        storageMediaType = [fatBytes[i:i + 1] for i in range(21, 22, 1)][0]
        self.storageMediaType.extend(storageMediaType)

        noOfSectorsInFATs = [fatBytes[i:i + 2] for i in range(22, 24, 2)][0]
        self.noOfSectorsInFATs.extend(noOfSectorsInFATs)

        noOfSectorsPerTrack = [fatBytes[i:i + 2] for i in range(24, 26, 2)][0]
        self.noOfSectorsPerTrack.extend(noOfSectorsPerTrack)

        noOfHeads = [fatBytes[i:i + 2] for i in range(26, 28, 2)][0]
        self.noOfHeads.extend(noOfHeads)

        noOfHiddenLS = [fatBytes[i:i + 4] for i in range(28, 32, 4)][0]
        self.noOfHiddenLS.extend(noOfHiddenLS)

        noOfSectorsInFS_long = [fatBytes[i:i + 4] for i in range(32, 36, 4)][0]
        self.noOfSectorsInFS_long.extend(noOfSectorsInFS_long)