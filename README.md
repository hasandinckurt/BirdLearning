# BirdLearning

https://grup1.github.io/BirdLearning/

 
## Weekly Progress Summary (18.11.2019) 

• We met 2 times in this week.

-- Hümeyra and Oğuzhan;

• Kept continue about the game.
• Updated the web site and GitHub account
• Started project via PyCharm. (Front-end)



 -- Gökçen, Hasan, Yasin Tarık;
 • Researched and started to learn Q-Learning algorithm.
 • Updated the web site and GitHub account
 • Installed libraries (Pygame and Tensorflow)
 • Added System Requirements Report


## Weekly Progress Summary (25.11.2019) 

• We met 1 times in this week.

-- Hümeyra and Oğuzhan;
• Kept continue about the game.
• Updated the web site and GitHub account.
• Added System Requirements Report.



-- Gökçen, Hasan, Yasin Tarık;
• Kept continue about Q-Learning algorithm.
• Added System Requirements 

## Weekly Progress Summary (09.12.2019) 

• We met 1 times in this week.

-- Hümeyra and Oğuzhan;
• Finished the game
• Stabilization
• Testing


-- Gökçen, Hasan, Yasin Tarık;
• Kept continue about Q-Learning algorithm
• Upload the game
• Updated GitHub account

## Weekly Progress Summary (16.12.2019) 
• We met 3 times in this week.

-- All team members;
• Kept continue about Q-Learning algorithm
• Testing
• Recorded the game
• Updated GitHub account


## Weekly Progress Summary (23.12.2019) 
• We met 2 times in this week.

-- All team members;
• Kept continue about Q-Learning algorithm
• Testing
• Recorded the game with next iteration
• Videos uploaded on GitHub account
• Made documentation about Q-Learning
• Updated GitHub account


## Tasking:

Front-end --> Hümeyra BİLGİ

Back-end --> Oğuzhan SOLAK

Machine Learning --> Gökçen TÜRKÖZ, Hasan DİNÇKURT, Yasin Tarık SUYABATMAZ


## DEEP Q-LEARNING DOCUMENTATION
The Q-Learning algorithm is one of the most well-known algorithms of reinforcement learning. The main purpose of the algorithm is to examine the next movements and to see the prize they will earn according to the movements they will make and to maximize this prize and act accordingly.
 
The Q-Learning algorithm, like other Reinforcement Learning methods, is one of the methods that we often use when we want the artificial intelligence programs that we call “agents plan to plan for the future (see Planning in AI). The working principle of the algorithm is based on the principle of encouragement that we use a lot in our daily lives. Just as incentives lead a person or organization to a particular job, they can also direct a robot - or another artificial intelligence - for a specific purpose.
 

The reward map of the bird, the places we want to go to or not, are determined by us in advance and these values are written to the Reward Table. The experience of the bird will be shaped according to this award table.

The bird uses his experience of each iteration to maximize his choice of destination. He keeps these experiences in a table called Q-Table.
 
 
Since our bird has no experience at the beginning, our Q-Table is full of zeros and therefore our bird will move randomly as it will multiply the zeros in the Q-Table in the first selection. This randomness will last until the bird finds the first prize. When the bird arrives at a place where the prize is awarded, he knows his previous place and writes the value of this place on the Q-Table where he has accumulated his own experience. This write process has a specific algorithm.
 

Each time, the bird predicts and moves forward according to this algorithm and reaches the prize. After reaching the award, the agent starts to move again from a random place and tries to find the prize again. As this process continues, the agent begins to know where to go in what situation.

## References

• https://www.analyticsvidhya.com/blog/2019/04/introduction-deep-q-learning-python/

• https://en.wikipedia.org/wiki/Reinforcement_learning

• https://pathmind.com/wiki/deep-reinforcement-learning

• https://www.geeksforgeeks.org/what-is-reinforcement-learning/
