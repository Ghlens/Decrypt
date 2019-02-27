import random
import time
import sys


def main():
    input_string = sys.argv[1]
    decrypt(input_string)


def decrypt(data):
    test_string = list(data)
    output_string = [''] * len(data)

    while test_string != output_string:
        for i in range(len(test_string)):
            if output_string[i] != test_string[i]:
                output_string[i] = chr(random.randint(32, 126))
        sys.stdout.write('\r' + ''.join(output_string))
        time.sleep(0.01)
        sys.stdout.flush()

    sys.stdout.write('\n')
    return output_string


if __name__ == '__main__':
    main()
