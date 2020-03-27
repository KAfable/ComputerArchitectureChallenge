import sys
from cpu import CPU

cpu = CPU()

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    print("Please make sure you entered a valid filepath.")
    sys.exit(1)

cpu.load(filename)
cpu.run()

# get filename from args
# load program
# run
