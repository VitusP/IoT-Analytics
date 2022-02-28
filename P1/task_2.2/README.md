# Installation Guide
This project uses Python and ```Pandas``` to store and convert result as a table.

Make sure you have Python 3 installed in the system. There are some package required such as ```Panda``` that you need to install
using pip command. 

For example:
```
pip install <PACKAGE_NAME>
pip3 install <PACKAGE_NAME>
```

# Run the program
To run the program, you need to run the following command:
```
python task_2pt2.py
```
The program will prompt you the max MC:
```
Do the hand simulation until MC: 200
```

# Getting the result
The program will automatically generate an excel file and print the table in the console. I've also put the table that I generate when running the program

For example:
```
Do the hand simulation until MC: 201
             MC        RTCL     nonRTCL n_RT n_nonRT         SCL    s Pre-empted-service-time
0             0           3           5    0       0           4    2                       0
1           3.0    3.169575         5.0  0.0     1.0    9.421326  1.0                     1.0
2      3.169575    8.138741         5.0  1.0     1.0    9.421326  1.0                     1.0
3           5.0    8.138741    6.485152  1.0     2.0    9.421326  1.0                     1.0
4      6.485152    8.138741    7.408513  1.0     3.0    9.421326  1.0                     1.0
..          ...         ...         ...  ...     ...         ...  ...                     ...
112  192.283805  243.825143  192.905794  0.0     0.0  192.818047  2.0                     0.0
113  192.818047  243.825143  192.905794  0.0     0.0  192.818047  0.0                     0.0
114  192.905794  243.825143  200.818421  0.0     0.0  212.115087  2.0                     0.0
115  200.818421  243.825143  204.971086  0.0     1.0  212.115087  2.0                     0.0
116  204.971086  243.825143  217.923266  0.0     2.0  212.115087  2.0                     0.0
```