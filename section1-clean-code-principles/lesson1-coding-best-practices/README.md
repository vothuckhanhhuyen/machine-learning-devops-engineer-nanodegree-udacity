## Key Points

- pep8: https://peps.python.org/pep-0008/#code-lay-out
- set is faster than list: https://stackoverflow.com/questions/8929284/what-makes-sets-faster-than-lists/8929445#8929445
- docstring convention:
    + https://peps.python.org/pep-0257/
    + https://numpydoc.readthedocs.io/en/latest/format.html
- readme:
    + https://www.udacity.com/course/writing-readmes--ud777
    + https://github.com/twbs/bootstrap
    + https://github.com/scikit-learn/scikit-learn
    + https://github.com/jjrunner/stackoverflow

## Key Terms

- Refactoring - the process of writing code that improves its maintainability, speed, and readability without changing its functionality.
- Modular - the logical partition of software into smaller programs for the purpose of improved maintainability, speed, and readability.
- Efficiency - using the resources optimally where resources could be memory, CPU, time, files, connections, databases, etc. [Source]
- Optimization - a way of writing code to be more efficient.
Documentation - written material or illustration that explains computer software.
- Linting - the automated checking of your source code for programmatic, syntactic, or stylistic errors. [Source]
- PEP8 - a document providing guidelines and best practices for writing Python code.

## Two ways to automate clean code are with

- pylint
- autopep8
- pylint script_name.py will provide feedback on updates to make to your code, as well as a score out of 10 that can help you understand which improvements are most important.
- autopep8 --in-place --aggressive --aggressive script_name.py will attempt to automatically clean up your code.