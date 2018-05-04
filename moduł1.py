import argparse, os, sys

parser = argparse.ArgumentParser()
parser.add_argument("file", help="name of file")
option = parser.add_mutually_exclusive_group();
option.add_argument('-n', '--numer', action='store_true', help='number all output lines')
option.add_argument('-s', '--squeeze_blank', action='store_true', help='suppress repeated empty output lines')
option.add_argument('-E', '--show_ends', action='store_true', help='display $ at end of each line')
args = parser.parse_args()

print("We will check in: " + os.path.dirname(os.path.abspath(__file__)));

file = args.file

if(os.path.exists(file)):
    try:
        f = open(file, "r");
    except:
        print("Permission denied")
        sys.exit(0)
    l = f.read().split("\n");
    if args.numer:
        n = 0;
        for i in l:
            print(str(n) + " " + i);
            n += 1;
    elif args.squeeze_blank:
        n = 0;
        for i in l:
            if(i == ""):
                continue
            else:
                print(i);
                n += 1;
    elif args.show_ends:
        n = 0;
        for i in l:
            print(i + "$");
            n += 1;
    else:
        n = 0;
        for i in l:
            print(i);
            n += 1;
else:
    print("File not exists")