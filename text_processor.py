import sys
import importlib

class TextProcessor:
    #initialize text processor with plugins
    def __init__(self, plugins):
        super().__init__()
        self.plugins = []
        #import all plugins
        for plugin in plugins:
            module = importlib.import_module(plugin)
            #create plugin classes
            plugin_class = getattr(module, plugin)
            self.plugins.append(plugin_class())
            print("Plugin %s loaded." % (self.plugins[-1].name), file=sys.stderr)
            
    def run(self):
        try:
            while True:
                #process each line with all plugins
                line = input()
                for plugin in self.plugins:
                    line = plugin.process(line)
                print(line)
        except EOFError:
            print("Text sucessfully processed.", file=sys.stderr)
            pass
                
#main code               
if __name__ == "__main__":
    processor = TextProcessor(sys.argv[1:])
    processor.run()
    
