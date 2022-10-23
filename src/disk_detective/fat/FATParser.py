from ntrprtr.ByteInterpreter import ByteInterpreter

class FATParser():
    def __init__(self) -> None:
        pass

    def parseVBR(self, fatBytes, configs):
        # Parse the general section of FAT boot sector
        _ntrprtr = ByteInterpreter(fatBytes, configs[0][1])
        generalResult = _ntrprtr.interpret()
        # Check if FAT12/16 or FAT32
        result = None
        fatType = self.getFATType(fatBytes, configs[3][1])
        if(fatType.lower() == "fat32"):
            fat32Result = ByteInterpreter(fatBytes, configs[2][1]).interpret()
            result = { "type": fatType, "general": generalResult, "specific": fat32Result }
        elif("fat" in fatType.lower()):
            fat1216Result = ByteInterpreter(fatBytes, configs[1][1]).interpret()
            result = { "type": fatType, "general": generalResult, "specific": fat1216Result }
        return result

    def parseFsInfo(self, fsInfoBytes, config):
        _ntrprtr = ByteInterpreter(fsInfoBytes, config)
        result = _ntrprtr.interpret()
        return result

    def getFATType(self, fatBytes, config):
        result = "-/-"
        fatTypes = ByteInterpreter(fatBytes, config).interpret()
        if("fat" in fatTypes[0][4].lower()):
            result = fatTypes[0][4].replace(" ", "")
        elif("fat32" in fatTypes[1][4].lower()):
            result = fatTypes[1][4].replace(" ", "")
        return result