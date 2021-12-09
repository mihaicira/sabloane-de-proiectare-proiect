class TableOfContents():
    def __init__(self,obj):
        self.page_index = 1;
        self.obj = obj
        self.toc = ""
        self.index = 0;


    def generateTocRecursively(self,obj,prefix_idx=1):
        #verifica tot arborele in mod recursiv si adauga rezultatul la stringul self.toc

        prefix = prefix_idx * "*** "
        try:
            if(obj._children):
                self.toc += f"{prefix} {obj.title} ............... {self.page_index} \n"
                for child in obj._children:
                    self.generateTocRecursively(child,prefix_idx+1)

        except:
            self.toc += f"{prefix} {obj.content} ............... {self.page_index} \n"
            self.page_index += 1


    def getToc(self):
        #trimite obiectul primit ca parametru catre functia recursiva
        self.generateTocRecursively(self.obj)
        return self.toc