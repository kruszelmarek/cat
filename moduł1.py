import os;

c = input(">>");
ct = [];
ct = c.split(" ");

print("You entered: >>" + c);

if(ct[0] == "cat"):
    print("We will check in: " + os.path.dirname(os.path.abspath(__file__)));
    if(os.path.exists(ct[2])):
        f = open(ct[2], "r");
        l = f.read().split("\n");
        if(len(ct) == 2):
            n = 0;
            for i in l:
                print(i);
                n += 1;
        elif(ct[1] == "-n"):
            n = 0;
            for i in l:
                print(str(n) + " " + i);
                n += 1;
        elif(ct[1] == "-s"):
            n = 0;
            for i in l:
                if(i == ""):
                    continue
                else:
                    print(i);
            n += 1;
        elif(ct[1] == "-E"):
            n = 0;
            for i in l:
                print(i + "$");
            n += 1;
        else:
            print("Enter correct argument");
    else:
        print("File not exist!");
else:
   print("Enter correct command!");
