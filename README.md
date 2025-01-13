Unit Tests with PyTest for Spark Jobs.

For using PyTest essentially makes it clean by seprating the test variables/dependecies and tests by differentiating them into two folders.
You create a conftest.py declaring the variables such as SparkSession object which can be reused in various tests.
We add a test in the same folder, to keep the code clean and modular you can keep the test logic in different folder (`jobs` in this case).

Just browse to the directory with `tests` folder and run pytest to start the unit test.

<img width="1033" alt="image" src="https://github.com/user-attachments/assets/c859a3df-f716-4e21-9420-1cc2600970fd" />
