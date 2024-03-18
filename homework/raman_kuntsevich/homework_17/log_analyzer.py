import os
import sys
from datetime import datetime
from arg_parser import ArgParser
import re


class LogAnalyzer:
    def __init__(self, params):
        self.params = params
        self.path = self.params['path']
        self.files = self.get_file_names()
        self.check_file_exists()
        self.file_contents = self.read_files()
        self.parsed_logs = self.parse_logs()
        self.result_logs = self.processing_search_params()
        self.print_result()

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

    def processing_search_params(self):
        result_logs = self.parsed_logs
        for key, param in self.params.items():
            match key:
                case 'date':
                    result_logs = self.search_by_date(param, result_logs)
                case 'text':
                    result_logs = self.search_by_text(param, result_logs)
                case 'unwanted':
                    result_logs = self.exclude_unwanted(param, result_logs)
        return result_logs

    @staticmethod
    def search_by_date(param, result_logs):
        for key, date in param.items():
            match key:
                case 'exact':
                    return dict(filter(lambda item: item[0] == date, result_logs.items()))
                case 'less':
                    return dict(filter(lambda item: item[0] < date, result_logs.items()))
                case 'more':
                    return dict(filter(lambda item: item[0] > date, result_logs.items()))
                case 'start':
                    return dict(filter(lambda item: param['start'] < item[0] < param['end'], result_logs.items()))

    @staticmethod
    def search_by_text(text, result_logs):
        return dict(filter(lambda item: text in item[1], result_logs.items()))

    @staticmethod
    def exclude_unwanted(unwanted_text, result_logs):
        return dict(filter(lambda item: unwanted_text not in item[1], result_logs.items()))

    def print_result(self):
        if self.params.get('full'):
            for key, value in self.result_logs.items():
                print(value)
        else:
            for key, value in self.result_logs.items():
                print(value[:30])


if __name__ == "__main__":
    parser = ArgParser()
    file_processor = LogAnalyzer(parser.params)
