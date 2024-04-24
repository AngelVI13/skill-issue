You are given a data file with traffic light information. 

EXAMPLE:

Red,Yellow,Green,TimeActive,Time
1,0,0,7,0:00:07
0,1,0,7,0:00:14
0,0,1,9,0:00:23
0,1,0,1,0:00:24
1,0,0,1,0:00:25

The first row indicates what information is in each column. Columns are separated by a comma.

For example the first line: 1,0,0,7,0:00:07 means that
Red: 1
Yellow: 0
Green: 0
TimeActive: 7
Time: 0:00:07

or in other words, the red light was ON for 7 seconds at 0:00:07 o'clock.

Complete atleast two of the following tasks:
1. Find the number of red, yellow & green occurances.
From the example above: Red=2, Yellow=2, Green=1
2. Find how long each colour was active for.
From the example above: Red=8 seconds, Yellow=8 seconds, Green=9 seconds
3. Find all times when Green was active (by time)
From the example above: [0:00:23]
4. Find the number of complete cycles Red-Yellow-Green-Yellow-Red in the data
From the example above: 1
5. Find number of lines with mistakes (multiple colours active at the same time or no colours active)
From the example above: 0
