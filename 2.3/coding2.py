"""
Write an Olympic Judging program that outputs the average scores from 5 different judges. 

Each score is out of 10 points maximum. Half points are allowed (e.g. 7.5)

The program should take 5 inputs and output the final average score.

Example:

Judge 1: 5.5
Judge 2: 10
Judge 3: 7
Judge 4: 8.5
Judge 5: 9
Your Olympic score is 8.0
"""

total_score = 0
# range(5) acts like [0, 1, 2, 3, 4]
for i in range(5):
    total_score += float(input("Judge " + str(i + 1) + ": "))
print("Your O lympic score is: " + str(total_score / 5))
