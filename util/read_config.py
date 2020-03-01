from configparser import ConfigParser


def read_db_config(filename=None):
    parser = ConfigParser()
    parser.read(filename, encoding='UTF8')

    db = {}
    for section in parser.sections():
        if parser.has_section(section):
            items = parser.items(section)
            if items.__len__() > 1 and section == 'table':
                sql = {}
                for key, value in items:
                    sql[key] = "".join(value.splitlines())
                db['sql'] = sql
            for item in items:
                db[item[0]] = "".join(item[1].splitlines())
        else:
            raise Exception('{0} not found in the {1} file'.format(section, filename))
    return db