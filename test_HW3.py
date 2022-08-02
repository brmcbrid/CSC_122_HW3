# Tests for HW3
# Prime Number Checker

import os.path
import sys
from HW3 import main
from tud_tests import *

def test_HW3():

    try:
        exists = os.path.exists("HW3.py")
        assert exists == True
    except:
        sys.exit()

    # Test 1
    set_keyboard_input([25,"y",101,"Y",10013,"y",1013,"y","red",53,"n"])
    main()
    output = get_display_output()

    assert output == [
        "Prime Number Checker",
        "\nEnter an integer to test: ",
        "25 is a composite number because it is divisible by 5",
        "Do you want to test another integer (y/n): ",
        "\nEnter an integer to test: ",
        "101 is a prime number",
        "Do you want to test another integer (y/n): ",
        "\nEnter an integer to test: ",
        "10013 is a composite number because it is divisible by 17",
        "Do you want to test another integer (y/n): ",
        "\nEnter an integer to test: ",
        "1013 is a prime number",
        "Do you want to test another integer (y/n): ",
        "\nEnter an integer to test: ",
        "Invalid integer value! Try again",
        "\nEnter an integer to test: ",
        "53 is a prime number",
        "Do you want to test another integer (y/n): ",
        "\nBye!"
        ]