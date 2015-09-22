from jacktokenizer import JackTokenizer
from  symboltable import SymbolTable
from compilationengine import CompilationEngine
from vmwriter import VMWriter
 
from os import listdir  #  alleen gebruiker bij directories.
from os.path import isdir

class JackCompiler:

    def __init__(self,path_source):           # Path to source directory or single file
         self.path_source = path_source

    def run(self):

        if isdir(self.path_source):
            directory_file_list  = listdir(self.path_source)
            for f in directory_file_list :
                if f.endswith(".jack") :
                    tok = JackTokenizer(self.path_source + '/' + f)
                    vmw   = VMWriter(self.path_source  + '/' \
                                        + f.partition('.')[0] + '.vm')
                    eng = CompilationEngine(tok,vmw)
                    eng.compile_class()
        else :
            if f.endswith(".jack") :
                tok = JackTokenizer(self.path_source + '/' + f)
                vmw   = VMWriter(self.path_source  + '/' \
                                    + f.partition('.')[0] + '.vm')
                eng = CompilationEngine(tok,vmw)
                eng.compile_class()

    
if __name__ == '__main__':
    # Voor Linux
    progdirpath = "/home/cewijk/synx/P/jackcompiler/11/ComplexArrays"
    # Voor Windows
    # progdirpath = r"D:\synx\P\jackcompiler\11\Seven"
    print( listdir(progdirpath))     # Get all jack files in a list.
    jackcompiler = JackCompiler(progdirpath)
    jackcompiler.run()    
