import re

def is_valid_email(addr):
    #if re.match(r'^(\w{2,10}|\w{2,10}.\w{2,10})\@\w{2,10}.com',addr):
    if re.match(r'^(\w+|\w+.\w+)\@\w+.[a-z]{1,3}$',addr):
        return True
    else:
        return False
    
def name_of_email(addr):
    m=re.match(r'^[<]*([a-zA-Z\s]*?)[>\s]*((\w+)|(\w+.\w+))(\@\w+.[a-z]{1,3})$',addr)
    print(m.group(1))
    print(m.group(2))

def name2_of_email(addr):
    m=re.match(r'^((\w+)|(\w+.\w+))(\@\w+.[a-z]{1,3})$',addr)
    print(m.group(1))
    print(m.group(2))

name_of_email('tom@voyager.org')
name2_of_email('tom@voyager.org')
name_of_email('<Tom Paris> tom@voyager.org')

"""
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert is_valid_email('mr-bob@example.com')
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')"""