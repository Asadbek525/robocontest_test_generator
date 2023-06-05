[![uz](https://img.shields.io/badge/lang-uz-red.svg)](https://github.com/Asadbek525/robocontest_test_generetor/blob/main/README.uz.md)
# robocontest_test_generetor
While adding new problems to robocontest.uz, some new users have problems with generating test cases. This repo might be helpful!

### How to use
clone this project
```sh
git clone https://github.com/Asadbek525/robocontest_test_generetor.git
```
enter working directory
```sh
cd robocontest_test_generetor
```

start generating test cases
```sh
python main.py sample_problem
```

Enter problem directory
```sh
cd sample_problem
```

Choose your prefernces and start editing generate.cpp or generate.py

After this proccess run generate.py or compile and run generate.cpp

This proccess generates input and output files in tests folder

Finaly you can zip folder by running zipper.py
```sh
python zipper.py
```

#### You can publish tests.zip file to [robocontest.uz](https://robocontest.uz/home)
