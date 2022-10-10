class DiskUsagePrinter():
    def __init__(self) -> None:
        self.__list = []

    def print(self, mbr):
        print("")
        print("Disk Usage Overview")
        print("-----------------------")
        print("")
        counter = 0
        startSector = 0

        self.__printHeader()

        for i in range(0, len(mbr.partitionEntries)):
            entry = mbr.partitionEntries[i]
            lba = entry.getOffsetLBA()
            noOfSectors = entry.getNoOfSectors()
            partTypes = entry.getPartitionTypes()

            # Check if the first partition table entry starts at 0
            if(i == 0):
                if(lba != 0):
                    # If not insert a empty line with LBA is 0, end LBA is the LBA of the next entry - 1
                    self.__printLine("-/-", "-/-", 0, lba - 1, lba - 1)
                    self.__printLine(counter, partTypes, lba, lba + noOfSectors - 1, noOfSectors)

            
            # Check if a partition entry is empty
            elif(lba == 0 and noOfSectors == 0):
                    # In this case, start lba is the lba of the previous entry
                    # and the end lba is the lba of the next entry - 1
                    prevEndLba = mbr.partitionEntries[i-1].getOffsetLBA() + mbr.partitionEntries[i-1].getNoOfSectors()
                    nextStartingLba = mbr.partitionEntries[i+1].getOffsetLBA()
                    # It also needs to be checked if it is the last entry to avoid problems with i
                    self.__printLine("-/-", "Empty", prevEndLba + 1, nextStartingLba - 1, nextStartingLba - prevEndLba)
            else:
                lba = entry.getOffsetLBA()
                partTypes = entry.getPartitionTypes()
                self.__printLine(counter, partTypes, lba, lba + noOfSectors - 1, noOfSectors)

            counter += 1

    def __printHeader(self):
        formatStr = "| {:12} | {:30} | {:12} | {:12} | {:14} |".format("  Number #", " Possible FS Types",  " Start LBA", "   End LBA", " No. of Sectors")
        print("-"*len(formatStr))
        print(formatStr)
        print("-"*len(formatStr))

    def __printLine(self, counter, partitionTypes, startLba, endLba, noOfSectors):
        if(type(partitionTypes) == list and len(partitionTypes) > 1):
            # Multiline Print
            pType = partitionTypes[0].description[0:28] 
            formatStr1 = "| {:12} | {:30} | {:12} | {:12} | {:14} |".format(str(counter), pType, str(startLba), str(endLba), str(noOfSectors))
            print(formatStr1)
            for i in range(1, len(partitionTypes)):
                pType = partitionTypes[i].description[0:28] 
                formatStrN = "| {:12} | {:30} | {:12} | {:12} | {:14} |".format("", pType, "", "", "")
                print(formatStrN)
            print("-"*len(formatStr1))   
        else:
            # Single Line Print
            if(type(partitionTypes) == str):
                pType = partitionTypes
            else:
                pType = partitionTypes[0].description[0:28]

            formatStr = "| {:12} | {:30} | {:12} | {:12} | {:14} |".format(str(counter), pType, str(startLba), str(endLba), str(noOfSectors))
            print(formatStr)
            print("-"*len(formatStr))
