from ntrprtr.printer.Printer import Printer

class FATPrinter():
    def __init__(self) -> None:
        self._printer = Printer()

    def printVBR(self, vbr):
        print("")
        print("FAT VBR Examiner")
        print("------------")
        print("--> " + vbr["type"])
        print("------------")
        print("")
        print("")
        print("FAT General Information (0x0000 - 0x0023 | 36 Byte)")
        print("------------")
        self._printer.print(vbr["general"])
        print("")
        print("")
        print("FAT Type Specific Information (0x0024 - 0x01FF | 476 Byte)")
        print("------------")
        self._printer.print(vbr["specific"])
        print("")

    def printFsInfo(self, fsInfo):
        print("")
        print("FAT FSInfo Examiner")
        print("------------")
        self._printer.print(fsInfo)