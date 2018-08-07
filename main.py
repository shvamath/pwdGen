import sys, getopt

optionsFlags = "i:o:date-range:digitalPwd:addSpecialBeg:addSpecialEnd"
optionsArgs = ["ifile=","ofile=","date-range=","length"]
defaultOutputFile = "output.honk"

def interpretArguments(args, options):
    for el in options:
        if (el[0] == "-o"):
            print "setting output to: " + el[1]
            defaultOutputFile = el[1]
            #Make stream to outputFIle
        if (el[0] == '--date-range'):
            print "outputting all possible variants od dates"
            dateRange = el[1]
            dateObject = new dateGenerator()
            dateObject.printDatesInFormat(dateRange, format, defaultOutputFile)
        if (el[0] == '-digitalPwd'):
            length = int(el[1])
            digitsObject = new digitsObject()
            digitsObject.permutations(length)
            print "printing all digital passwords"
        if (el[0] == "-addSpecialBeg"):

        if (el[0] == "-addSpecialEnd"):

def main(argv):
    try:
      opts, args = getopt.getopt(argv,optionsFlags,optionsArgs)
      print("Passed: " + str(args) + "\n" + str(opts))
    except getopt.GetoptError:
      print 'main.py -i <inputfile> -o <outputfile>'
      sys.exit(2)
    interpretArguments(args, opts)

if __name__ == "__main__":
    main(sys.argv[1:])
