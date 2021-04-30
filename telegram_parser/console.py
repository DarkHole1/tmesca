import os
from main import main    

def start_link():
    n_letters = input('How many letters in the link might be (at least 5): ')
    start_point = 'a' + '1'*(int(n_letters)-1)
    open('last_link', 'w').write(start_point)


def console_start():
    parser_type = input('''What type of content do you want to parse (input several numbers, if you want to parse any combination of the possible content): 
 1 - All (Groups/Channel/Users
 2 - Channels
 3 - Groups
 4 - Users
Your choise: ''')[:2].lower()
    work_mode = input('''What type of parsing you want to use:
 1 - Linear parsing
 2 - Random parsing 
 3 - Mutation parsing 
Your choise: ''')[0].lower()
    turbo_mode = input('Turn on turbo mod(y/n): ')[0].lower()                   # work mode with/out delay
    output = input('''What type of output do you want: 
 1 - All output (not False will be only the content, that was choosed to parse)
 2 - If something found
 3 - No output
Your choise: ''')[0].lower()
    window = False
    mutated_initial_link = None
    if work_mode == '1':
        try:                                    # LINK Checking
            open('last_link').read()
            change_start = input('Do you want to change number of letters in link(y/n): ')[0].lower()
            if change_start == 'y':
                start_link()
        except:
            print('Initial setup!')
            start_link()
            
    if work_mode == '3':
        try:
            os.remove('mutated')
        except:
            pass
        mutated_initial_link =  input('Input initial word to mutate (length of the word is greater than 5 letters): ').lower()
    main(work_mode, parser_type, window, turbo_mode, output, print, mutated_initial_link)
    
console_start()