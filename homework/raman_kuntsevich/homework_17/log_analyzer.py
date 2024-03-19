import dependency_manager
import os
import sys
from datetime import datetime
from arg_parser import ArgParser
import re
from colorama import init, Fore, Style


class LogAnalyzer:
    def __init__(self, params):
        self.line_limit = 300
        self.line_limit_by_text = 150
        self.params = params
        self.path = self.params['path']
        self.files = self.get_file_names()
        self.check_file_exists()
        self.file_contents = self.read_files()
        self.parsed_logs = self.parse_logs()
        self.parsed_logs_count = len(self.parsed_logs)
        self.result_logs = self.processing_search_params()
        self.result_logs_count = len(self.result_logs)
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
            print("Error: File must have a .log extension")
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
    def exclude_unwanted(unwanted_params, result_logs):
        result = result_logs
        for text in unwanted_params:
            result = dict(filter(lambda item: text not in item[1], result.items()))
        return result

    def print_result(self):
        date_format = "[%Y-%m-%d %H:%M:%S.%f]"
        init()
        for key, value in self.result_logs.items():
            str_date = Fore.YELLOW + datetime.strftime(key, date_format) + Style.RESET_ALL
            if self.params.get('full'):
                print(str_date, value)
            elif self.params.get('text'):
                text = self.params['text']
                start_text_index = value.find(text)
                end_text_index = start_text_index + len(text)
                start_index = max(start_text_index - self.line_limit_by_text, 0)
                end_index = min(end_text_index + self.line_limit_by_text, len(value))
                print(str_date,
                      value[start_index:start_text_index],
                      Fore.GREEN + value[start_text_index:end_text_index] + Style.RESET_ALL,
                      value[end_text_index:end_index])
            else:
                print(str_date, value[:self.line_limit])
        print(Fore.YELLOW + 'Total logs count:', Fore.BLUE + str(self.parsed_logs_count))
        print(Fore.YELLOW + 'Total results count:', Fore.BLUE + str(self.result_logs_count) + Style.RESET_ALL)


if __name__ == "__main__":
    parser = ArgParser()
    file_processor = LogAnalyzer(parser.params)
