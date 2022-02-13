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
python task_3.py
```
The program will prompt you parameters, for example:
```
Enter mean IAT of RT messages: 7
Enter mean IAT of non-RT messages: 10
Enter mean service time of RT messages: 1
Enter mean service time of non-RT messages: 4
Enter number of batches: 5
Enter batch size: 10
```

# Getting the result
The program will automatically generate the mean of the response time, confidence intervals, and 95-percentile of RT and nonRT message.

For example:
```
> python3 task_3.py
Enter mean IAT of RT messages: 7
Enter mean IAT of non-RT messages: 10
Enter mean service time of RT messages: 1
Enter mean service time of non-RT messages: 4
Enter number of batches: 5
Enter batch size: 10
RT mean response time:  3.877414522767637
nonRT mean response time:  35.23130741276549
RT 95-percentile response time:  10.080066792288283
nonRT 95-percentile response time:  63.38927889834281
RT Confidence intervals response time: (1.8656675302172236, 5.889161515318051)
nonRT Confidence intervals response time: (13.54475516227689, 56.91785966325409)
```