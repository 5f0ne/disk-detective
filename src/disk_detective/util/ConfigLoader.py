import os
import json

class ConfigLoader():
    def __init__(self) -> None:
        self.config = {
            "fat": ["fat.json", "fat1216.json", "fat32.json", "fat-type.json", "fat-fs-info.json"],
            "ext": ["ext-file-descriptor-table.json", "ext-inode.json", "ext-super-block.json"],
            "ntfs": [""],
            "mbr": ["mbr.json"]
        }

    def load(self, path, config):
        result = []
        p = os.path.join(path, config, "config")
        for configName in self.config[config]:
            fullPath = os.path.join(p, configName)
            f = open(fullPath, encoding="utf8")
            result.append((configName, json.load(f)))
            f.close()
        return result