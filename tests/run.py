import pytest
import sys

#本檔提供後續script抓取參數，例：python3 run.py test.py <argv>


def main():
    # extract your arg here
    print('Extracted arg is ==> %s' % sys.argv[2])
    pytest.main([sys.argv[1]])

if __name__ == '__main__':
    main()

