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
python task_2pt1.py
```
The program will prompt you the following parameters:
```
Enter IAR of RT messages: 10
Enter IAR of non-RT messages: 5
Enter service time of RT messages: 2
Enter service time of non-RT messages: 4
Do the hand simulation until MC: 51
```

# Getting the result
The program will automatically generate an excel file and print the table in the console. I've also put the table that I generate when running the program with the same parameters as task 1.1 and 1.2

For example:
```
Do the hand simulation until MC: 51
    MC RTCL nonRTCL n_RT n_nonRT SCL  s Pre-empted-service-time
0    0    3       5    0       0   4  2                       0
1    3   13       5    0       1   5  1                       1
2    5   13      10    0       2   5  1                       1
3    5   13      10    0       1   6  2                       0
4    6   13      10    0       0  10  2                       0
5   10   13      15    0       1  10  2                       0
6   10   13      15    0       0  14  2                       0
7   13   23      15    0       1  15  1                       1
8   15   23      20    0       2  15  1                       1
9   15   23      20    0       1  16  2                       0
10  16   23      20    0       0  20  2                       0
11  20   23      25    0       1  20  2                       0
12  20   23      25    0       0  24  2                       0
13  23   33      25    0       1  25  1                       1
14  25   33      30    0       2  25  1                       1
15  25   33      30    0       1  26  2                       0
16  26   33      30    0       0  30  2                       0
17  30   33      35    0       1  30  2                       0
18  30   33      35    0       0  34  2                       0
19  33   43      35    0       1  35  1                       1
20  35   43      40    0       2  35  1                       1
21  35   43      40    0       1  36  2                       0
22  36   43      40    0       0  40  2                       0
23  40   43      45    0       1  40  2                       0
24  40   43      45    0       0  44  2                       0
25  43   53      45    0       1  45  1                       1
26  45   53      50    0       2  45  1                       1
27  45   53      50    0       1  46  2                       0
28  46   53      50    0       0  50  2                       0
29  50   53      55    0       1  50  2                       0
30  50   53      55    0       0  54  2                       0
```
