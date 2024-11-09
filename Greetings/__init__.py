# %%
import sys

# %%

def main():
    from argparse import ArgumentParser

    parser = ArgumentParser(
        prog=__name__,
        description= 'Greets you, '
                     'so be nice.',
        epilog= 'this is my first module with args '
                'and I hope it works. '
         )

    parser.add_argument(
        'name', # after parser this is stored as args.name
        help='this is your name' # display when user uses -h help flag
    )

    # optional arguments
    parser.add_argument(
        '--hi', # after parser this is stored as args.hi
        help='says hi instead', # display when user uses -h help flag
        action= 'store_true', # store as True if argument is passed in
        required= False # this is not required in the command
    )
    
    parser.add_argument(
        '--hello', 
        help='says hello instead',
        action= 'store_true',
        required= False
    )

    parser.add_argument(
        '--royalty',
        help= 'a greeting worthy of a royal',
        action= 'store_true',
        required= False
    )

    group = parser.add_mutually_exclusive_group(required= False)
    group.add_argument(
        '--castle',
        help= 'we are in a castle',
        action= 'store_true',
        required= False
    )

    group.add_argument(
        '--palace',
        help= 'we are in the palace',
        action= 'store_true',
        required= False
    )
    
    args = parser.parse_args()

    print(args)
    print(type(args)) # simple argparse.Namespace

    # Return the __dict__ attribute for a module, class, instance, 
    # or any other object with a __dict__ attribute.
    print(vars(args))

    args_list = list(vars(args).values())

    print(args_list)

    check_args = args_list[1:4]

    print(check_args)

    if check_args == [False] * len(check_args):
        print(f'Greetings, {args.name}')

    if args.hi:
        print(f'Hi, {args.name}!')
    if args.hello:
        print(f'Hello, {args.name}!')
    if args.royalty:
        print(f'Your Royal Highness, the Great {args.name}, has blessed us with their presence!')
    
    # mutually exclusive flags
    if args.castle:
        print(f'We are in the castle.')
    if args.palace:
        print(f'We are in the palace.')



# %%

if __name__ == '__main__':
   
    rc = 1

    try:
        main()
        rc = 0

    except Exception as e:
        print('Error: %s' % e, file=sys.stderr)
        sys.exit(rc)

# %%
