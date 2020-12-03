import os,sys
p=os.path.join(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(p)
sys.path.append("C:\\Users\\DONGCHUAN\\AppData\\Roaming\\Python\\Python37\\site-packages")
import yaml
from common.public import filePath,getUrl

class OperationYaml:
    def readYaml(self,fileName):
        with open(filePath('data',fileName),'r',encoding='utf-8') as f:
            result = []
            for i in list(yaml.safe_load_all(f)):
                i["url"] = getUrl() + i["url"]
                result.append(i)
            return result



if __name__ == '__main__':
    obj=OperationYaml()
    for i in obj.readYaml('addTeacher.yaml'):
        print(i)

