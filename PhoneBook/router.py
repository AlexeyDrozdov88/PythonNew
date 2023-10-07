from view import *
from db import *

def main():
    while True:
        ans = select_op()
        if ans == '1':
            write_contact(input_contact())
        if ans == '2':
            find_contact(input_search_key())
        if ans == '6':
            break
        if ans == '3':
            print(show_contacts())
main()