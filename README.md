# Assessment #1

Welcome to our first assessment! You will have 50 minutes to complete the assignment at which time you will be asked to submit a pull request.

* Time: 50 minutes
* Open book
* Individual

## Assignment

The goal of this assignment is to fill in each function stub to make the associated test pass.

There are 4 questions over these topics in this order:
* general Python (4 questions)

The repository has the following folder structure:

    assessment-day1
    ├── Makefile
    ├── README.md
    ├── src
    │   ├── __init__.py
    │   ├── assessment.py
    ├── data
    │   ├── alice.txt
    │   ├── markets.sql
    └── test
        ├── __init__.py
        └── unittests.py


* If you need help forking, cloning and pulling with git, look at the instructions in the precourse: [How to Submit](https://github.com/alexseong/dsy_python_programming#how-to-submit-the-assignments)

1. `src/assessment.py` contains function stubs for you to fill in. The goal is to make the tests pass. There are 12 problems in the file.

 * **Running Unit Tests**

 * Needs **Python2.7 or greater**    
     * you can check your python version by running this: `python -V`    

 * This section in the assessment can be tested using the unit tests. You can run the tests with this command from the root directory (assessment-day1/):    

    `make test`

 * If you do not have py.test, you may see Import errors. Run the following commands in case you see such errors:    

    `pip install pytest`     

 * `.` refers to passing test, `E` is an error in the code and `F` is a failure. So something that looks like this: `....EFFFFFF` means 4 tests passed, one has an error and 6-11 fail.
 * It can be helpful to press enter a bunch of times between each time you run the test so that it's easy to find the beginning of your most recent results.    


2. The questions for the math portion of the assessment are in
  `math/math_assessment.pdf`. Put your answers in `math_assessment.txt`.
  There are no automated tests for this portion of the assessment.

* At the end of 120 minutes, submit a pull request.

**Feel free to use any online resources like python documentation and tutorials, your notes, readings and exercises.**

Good luck!
