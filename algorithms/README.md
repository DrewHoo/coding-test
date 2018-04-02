## Run the code
Note: This code was developed with Python 3.6 on Mac OS
0) Follow the instructions in the README at the root of the project.
1) To run the code, type `python algorithms/string_permutations.py` `path/to/your/input/file`
## Run the tests
Note: The tests might not run on a Windows machine due to the way Windows deals with a file being opened simultaneously more than once
0) After installing, just type `pytest` in the shell
## Notes
This implementation is not the best possible time complexity; the best possible time complexity is O(n!), and this algorithm is O(n!n), where n is the length of the input string. I found O(n!n) to be acceptable, because n can't get very big in the first place before you need some serious storage, which I'd think is outside the scope of the assignment. I think the output from a 13 character string barely fits on a modern hard drive.

Also my algorithm calculates permutations with repetition, so the string `'aa'` has two permutations, for instance.