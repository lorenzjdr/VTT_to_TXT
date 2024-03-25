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
        with open(f"{filename}.txt", 'w') as output_file:
            for line in Filing.dialogue:
                output_file.write(line + '\n')

    @staticmethod 
    def create_file_path(filename):
        cwd = os.getcwd()  
        file_path = os.path.join(cwd, filename)
        return file_path

