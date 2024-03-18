import os
import sys
from datetime import datetime
from arg_parser import ArgParser
import re


class LogAnalyzer:
    def __init__(self, params):
        self.params = params
        self.path = self.params['path']
    #    self.date = self.params['date']
    #    self.text = self.params['text']
    #    self.unwanted = self.params['unwanted']
    #    self.full = self.params['full']
        self.files = self.get_file_names()
        self.check_file_exists()
        self.file_contents = self.read_files()
        self.parsed_logs = self.parse_logs()
        print(params)
        print(self.parsed_logs.items())

    def get_file_names(self):
        if os.path.isfile(self.path):
            file_name = os.path.basename(self.path)
            self.path = os.path.dirname(self.path)
            return [file_name] if file_name.endswith('log') else []
        elif os.path.isdir(self.path):
            return list([file for file in os.listdir(self.path) if file.endswith('.log')])

    def check_file_exists(self):
        if self.files:
            pass
        else:
            print(f"Error: File must have a .log extension")
            sys.exit(1)

    def read_files(self):
        file_contents = {}
        file_names = self.files

        for file in file_names:
            file_path = os.path.join(self.path, file)
            with open(file_path) as log_file:
                file_contents[file] = log_file.read()

        return file_contents

    def parse_logs(self):
        parsed_logs = {}
        date_pattern = r'\b\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+\b'

        for file_name, file_content in self.file_contents.items():
            date = None
            lines = file_content.split('\n')

            for line in lines:
                match = re.search(date_pattern, line)

                if match:
                    date = datetime.strptime(match.group(), '%Y-%m-%d %H:%M:%S.%f')
                    parsed_logs[date] = line
                elif date:
                    parsed_logs[date] += '\n' + line

        return parsed_logs

    # def search_by_date(self):

if __name__ == "__main__":
    parser = ArgParser()
    file_processor = LogAnalyzer(parser.params)
