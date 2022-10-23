import binascii

class TestFileCreator():
    def __init__(self) -> None:
       pass

    def createFile(self, inputPath, outputPath):
        with open(inputPath) as inFile, open(outputPath, "wb") as outFile:
            for line in inFile:
                outFile.write(binascii.unhexlify(''.join(line.split())))