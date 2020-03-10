from ._arguments import parse_arguments
from package_template import increment

def main():
    """Run program as executable.
    """

    args = parse_arguments()
    if args.n != None:
        ans = increment(args.n)
        print(ans)

if __name__ == "__main__":
    main()