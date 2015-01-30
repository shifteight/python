# generators to parse Apache log lines, using regular expressions

import os
import re


def log_files(dir_name, file_type):
    if not os.path.exists(dir_name):
        raise ValueError(dir_name + " not found!")
    if not os.path.isdir(dir_name):
        raise ValueError(dir_name + " is not a directory!")
    for path, dirs, files in os.walk(dir_name):
        log_files = [f for f in files
                     if f.endswith(file_type)]
        for each_file in log_files:
            yield os.path.join(path, each_file)


def log_lines(dir_name, file_type):
    for each_file in log_files(dir_name, file_type):
        for each_line in file(each_file).readlines():
            yield (each_file, each_line.strip())


def list_errors(dir_name, file_type):
    return (each_file + ': ' + each_line.strip()
            for each_file, each_line in log_lines(dir_name, file_type)
            if 'error' in each_line.lower())


apache_log_headers = ['host', 'client_id', 'user_id',
                      'datetime', 'method', 'request', 'http_proto',
                      'status', 'size', 'referrer', 'user_agent']

log_format = (r'(\S+) (\S+) (\S+) \[(.*?)\] '
	      r'"(\S+) (\S+) (\S+)" (\S+) (\S+) '
	      r'"(.+)" "(.+)"')

log_regexp = re.compile(log_format)


def parse_apache(line):
    log_split = log_regexp.match(str(line))
    if not log_split:
        print "Line didn't match!", line
        return {}
    log_split = log_split.groups()

    result = dict(zip(apache_log_headers, log_split))
    result['status'] = int(result['status'])
    if result['size'].isdigit():
        result['size'] = int(result['size'])
    else:
        result['size'] = 0
    return result


def apache_lines(dir_name, file_type):  # generator
    return (parse_apache(line)
            for line in log_lines(dir_name, file_type))


if __name__ == '__main__':
    dir_name = '/var/log/apache2'
    file_type = '.log'
    for each_line in log_lines(dir_name, file_type):
        print each_line
        print parse_apache(each_line)

    print sum((each_line['size']
               for each_line in apache_lines(dir_name, file_type)
               if each_line.get('status', 0) == 200))
