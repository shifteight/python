def create_todo(todos, title, description, level):
    todo = {
        'title': title,
        'description': description,
        'level': level,
    }
    todos.append(todo)



def main_loop():
    user_input = ''
    while 1:
        print run_command(user_input)
        user_input = raw_input('> ')
        if user_input.lower().startswith('quit'):
            print 'Exiting...'
            break


if __name__ == '__main__':
    main_loop()
