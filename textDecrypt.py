import random
import time
import sys

inputString = sys.argv[1]
testString = list(inputString)
outputString = [''] * len(inputString)

while testString != outputString:
    for i in range(len(testString)):
        if outputString[i] != testString[i]:
            outputString[i] = chr(random.randint(32, 126))
    sys.stdout.write('\r' + ''.join(outputString))
    time.sleep(0.01)
    sys.stdout.flush()

sys.stdout.write('\n')
