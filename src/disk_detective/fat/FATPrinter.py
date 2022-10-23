from ntrprtr.printer.Printer import Printer

class FATPrinter():
    def __init__(self) -> None:
        self._printer = Printer()

    def __print(self, header, result):
        print("")
        print(header)
        print("------------")
        self._printer.print(result)

    def printVBR(self, vbr):
        print("")
        print("FAT VBR Examiner")
        print("------------")
        print("--> " + vbr["type"])
        print("------------")
        print("")
        self.__print("FAT General Information (0x0000 - 0x0023 | 36 Byte)", vbr["general"])
        print("")
        self.__print("FAT Type Specific Information (0x0024 - 0x01FF | 476 Byte)", vbr["specific"])
        print("")

    def printFsInfo(self, fsInfo):
        self.__print("FAT FSInfo Examiner", fsInfo)

    def printLFN(self, lfn):
        self.__print("FAT Long Filename Examiner", lfn)

    def printDirEntry(self, dirEntry):
        self.__print("FAT Directory Entry Examiner", dirEntry)