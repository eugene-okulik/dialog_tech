import argparse
import os
import sys
from datetime import datetime


class ArgParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("path",
                                 help="File name or directory. Only files with the .log extension are processed.")
        self.parser.add_argument("-d", "--date",
                                 help="Datetime for search: less than: \"../2022-01-13 00:00:00.000\", "
                                      "more than: \"2022-01-13 00:00:00.000/..\", "
                                      "from - to \"2022-01-13 00:00:00.000/2022-01-14 00:00:00.000\", "
                                      "exact: \"2022-01-13 00:00:00.000\"")
        self.parser.add_argument("-t", "--text",
                                 help="A text to look for")
        self.parser.add_argument("-n", "--unwanted",
                                 help="A text to filter out logs. "
                                      "Logs with this text will be excluded from the results. "
                                      "Can be a string or a list divided by commas (e.g. \"out of memory, info\"")
        self.parser.add_argument("--full",
                                 help="Return full log entry instead of default symbols Qty",
                                 action="store_true")
        self.params = self.process_args()

    def process_args(self):
        args_dict = vars(self.parser.parse_args())
        params = {}

        for arg_name, arg_value in args_dict.items():
            param = None
            error_str = None

            if arg_value:
                match arg_name:
                    case 'path':
                        param, error_str = (self.process_file_argument(arg_value))
                    case 'date':
                        try:
                            param, error_str = (self.process_date_argument(arg_value))
                        except ValueError:
                            error_str = str(ValueError)
                    case 'text':
                        params['text'] = arg_value
                    case 'unwanted':
                        params['unwanted'] = arg_value.split(', ')
                    case 'full':
                        params['full'] = arg_value

            if error_str:
                print(f"Error: {error_str}")
                sys.exit(1)
            elif param:
                params[arg_name] = param

        return params

    @staticmethod
    def process_file_argument(arg_value):
        if os.path.exists(arg_value):
            return arg_value, None
        else:
            return None, f"No such file or directory '{arg_value}'"

    @staticmethod
    def process_date_argument(arg_value):
        date_format = "%Y-%m-%d %H:%M:%S.%f"
        date_formats = [
            ("less", f"../{date_format}"),
            ("more", f"{date_format}/.."),
            ("from-to", date_format),
            ("exact", date_format)
        ]

        for key, value in date_formats:
            try:
                if key == "from-to":
                    start_date_str, end_date_str = arg_value.split("/")
                    start_date = datetime.strptime(start_date_str, value)
                    end_date = datetime.strptime(end_date_str, value)
                    return {'start': start_date, 'end': end_date}, None
                else:
                    date = datetime.strptime(arg_value, value)
                    return {key: date}, None
            except ValueError:
                pass

        return None, f"Unable to recognize date '{arg_value}'"
