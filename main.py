from datastructures.HashTable import HashTable


# TOTAL MARKS = 30
def main():  # DO NOT MODIFY THIS FILE! IT MUST WORK LIKE THIS, ONCE YOUR IMPLEMENTATION IS CORRECT
    hashtable: HashTable = None
    hashtable = HashTable()  # Task 1 a) and b)
    hashtable.task_1c_i()  # Task 1 c) i)
    hashtable.display()
    print('')

    while True:
        value = int(input('Input value for task_1c_ii : '))
        print('Done:-{}'.format(hashtable.task_1c_ii(value)))  # Task 1 c) ii)
    pass


if __name__ == '__main__':
    main()
