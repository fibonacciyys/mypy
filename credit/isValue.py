def turn_list(num):
    num_list = []
    if num != 0:
        num_list = turn_list(num // 10)
        num_list.append(num % 10)
    return num_list


def sanitize(cre_str):
    if '\n' in cre_str:
        (cre, blank) = cre_str.split('\n')
        return cre
    else:
        return cre_str


def get_credit(str_file):
    global credit_list
    try:
        credit_list = []
        with open(str_file, 'r') as data_list:
            for each_credit in data_list:
                credit_list.append(int(sanitize(each_credit)))
    except IOError as err:
        print('IOError' + str(err))
    return credit_list


def isTrue(num_credit):
    new_list = []
    num_list = turn_list(num_credit)
    for x in range(len(num_list)):
        if x % 2 == 0:
            new_list.append(num_list.pop(0))
        else:
            new_list.append(num_list.pop(0) * 2)
    return sum(new_list) % 10 == 0


def select(str_file):
    cre_list = get_credit(str_file)
    with open('true_credit.txt', 'w') as true_file, open('false_credit.txt', 'w') as false_file:
        for each_credit in cre_list:
            if isTrue(each_credit):
                print(each_credit, file=true_file)
            else:
                print(each_credit, file=false_file)
