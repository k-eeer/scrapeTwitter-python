import pytest
import sys

#本script用於協助擷取參數，用法：python3 run.py code.py argv2 argv3 argv4 ...

def main():
    # extract your arg here
    print('Extracted arg is ==> %s' % sys.argv[2:])
    pytest.main([sys.argv[1]])

if __name__ == '__main__':
    main()

