from langchain.text_splitter import RecursiveCharacterTextSplitter,Language


text = '''
class grandparent:
    def __init__(self,property):
        self.property=property

    def skincolour(self,scolour):
        self.scolour=scolour
        print(self.scolour)
    
class parent(grandparent):
    def eyecolor(self,ecolour):
        self.ecolour=ecolour
        print(self.ecolour)
    
class child(parent):
    def haircolour(self,hcolour):
        self.hcolour=hcolour
        print(self.hcolour)

child1=child(500000)
print(child1.property)
child1.skincolour("white")
child1.eyecolor("brown")
child1.haircolour("black")

'''


splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size = 200,
    chunk_overlap=0
)

chunk = splitter.split_text(text)

print('len:',len(chunk))
print(chunk)