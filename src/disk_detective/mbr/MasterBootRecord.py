from disk_detective.mbr.PartitionEntry import PartitionEntry

class MasterBootRecord():
    def __init__(self, data) -> None:            
        self.bootloader = bytearray()            #  440 Bytes
        self.serialNumber = bytearray()          #    4 Bytes
        self.nullBytes = bytearray()             #    2 Bytes
        self.partitionEntries = []               # 4*16 Bytes
        self.identifier = bytearray()            #    2 Bytes
        self.__process(data)

    def __process(self, mbrBytes):
        bootloader = [mbrBytes[i:i + 440] for i in range(0, 440, 440)][0]
        self.bootloader.extend(bootloader)
        
        serialNumber = [mbrBytes[i:i + 4] for i in range(440, 444, 4)][0]
        self.serialNumber.extend(serialNumber)

        nullBytes = [mbrBytes[i:i + 2] for i in range(444, 446, 2)][0]
        self.nullBytes.extend(nullBytes)

        partitionEntries = [mbrBytes[i:i + 64] for i in range(446, 510, 64)][0]
        self.__processPartitionEntries(partitionEntries)
        
        identifier = [mbrBytes[i:i + 2] for i in range(510, 512, 2)][0]
        self.identifier.extend(identifier)

    def __processPartitionEntries(self, partitionBytes):
        splitted = [partitionBytes[i:i + 16] for i in range(0, 64, 16)]
        for entry in splitted:
            self.partitionEntries.append(PartitionEntry(entry))
            
