
## An output  
A, B, C has highest utility,     
D, E, F has good utility,   
G, H, I has average utility,   
J, K, L has lowest utility,   
but corrupt voters are bribed for L     

rational voters count = 1000   
idiot voters count = 1000  
corrupt voter count = 2000  

scores = [1.25, 1.125, 1, 0]    
{'A': 2465.875, 'B': 2493.0, 'C': 2530.25, 'D': 2437.125, 'E': 2413.375, 'F': 2411.0, 'G': 2354.375, 'H': 2365.625, 'I': 2360.75, 'J': 1725.0, 'K': 1768.375, 'L': 3459.75}

Difference of votes: A - L (A lost by less votes)

-993.875  


scores = [1.5, 1.25, 1, 0]   
{'A': 2807.5, 'B': 2800.75, 'C': 2821.5, 'D': 2680.0, 'E': 2631.75, 'F': 2648.5, 'G': 2523.25, 'H': 2550.5, 'I': 2509.25, 'J': 2002.25, 'K': 1972.25, 'L': 3973.5}   
-1166.0



scores = [3, 2, 1, 0]    
{'A': 4932, 'B': 4932, 'C': 4768, 'D': 4282, 'E': 4452, 'F': 4283, 'G': 3649, 'H': 3683, 'I': 3586, 'J': 3138, 'K': 3166, 'L': 7210}  
-2278  


rational voters count = 37500   
idiot voters count = 37500  
corrupt voter count = 25000   
25% of votes are corrupt

scores = [1.25, 1.125, 1, 0]      
{'A': 79173.125, 'B': 78908.75, 'C': 79223.875, 'D': 76436.125, 'E': 76351.25, 'F': 76503.0, 'G': 73651.5, 'H': 73614.375, 'I': 73637.0, 'J': 51970.375, 'K': 52218.875, 'L': 72718.25}

Difference of votes: A - L: 6454.875    
But Difference of votes between I - L is  + 919, I will win, and utility of I is also greater, I, F,all with greater utility will win. 

scores = [1.5, 1.25, 1, 0]     
{'A': 90465.25, 'B': 90319.75, 'C': 90438.5, 'D': 84837.0, 'E': 84770.5, 'F': 84998.5, 'G': 79785.5, 'H': 79606.25, 'I': 79478.25, 'J': 57574.5, 'K': 57272.0, 'L': 82617.0}   
7848.25 

scores = [3, 2, 1, 0]   
{'A': 157565, 'B': 157484, 'C': 157365, 'D': 135391, 'E': 136498, 'F': 135946, 'G': 114150, 'H': 114377, 'I': 114183, 'J': 92161, 'K': 92520, 'L': 141965}

Difference of votes: A - L (A won by more votes)     
15600    
But Difference of votes between I - L is −27782, So I will loose even if it has greater utility
