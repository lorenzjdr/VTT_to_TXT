import re
import os

class Filing:
    pattern = r':\s*([a-zA-Z].*)$'
    dialogue = []

    @staticmethod
    def openVTTFile(filename):
        with open(filename, 'r') as file:   
            for line in file:
                match = re.search(Filing.pattern, line)
                if match:
                    Filing.dialogue.append(match.group(1))

    @staticmethod
    def output(filename):
        with open(f"{filename}", 'w') as output_file:
            stack = []
            for line in Filing.dialogue:
                while line:
                    idx = line.find('.')
                    if idx == -1:
                        stack.append(line)
                        break
                    else:
                        stack.append(line[:idx + 1])
                        output_file.write(' '.join(stack) + '\n')
                        stack = []
                        line = line[idx + 1:].lstrip()
    
    @staticmethod 
    def create_file_path(filename):
        cwd = os.getcwd()  
        file_path = os.path.join(cwd, filename)
        return file_path