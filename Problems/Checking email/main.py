def check_email(string):
    if ' ' in string or '@' not in string or '@.' in string:
        return False
    d = string.split('@')
    if '.' not in d[1][1:]:
        return False
    return True
