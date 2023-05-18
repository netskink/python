# This is a demo on usage of subcommand

import subcommand

@subcommand.subcommand()
def hello(options, name='world'):
    """Display hello message.

    Usage: hello [option] [name]

    Options:

    -p [--prefix] prefix     : message prefix (default: hello)
    -n [--repeat] n          : repeat the message n times (type: int) (default: 1)
    """
    for i in range(options.n):
        print(options.prefix + ",", name)

if __name__ == "__main__":
    subcommand.main()


