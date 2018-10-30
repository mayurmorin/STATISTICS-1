
# coding: utf-8

# Task 1.1. Blood glucose levels for obese patients have a mean of 100 with a standard deviation of 15. A
# researcher thinks that a diet high in raw cornstarch will have a positive effect on blood glucose
# levels. A sample of 36 patients who have tried the raw cornstarch diet have a mean glucose
# level of 108. Test the hypothesis that the raw cornstarch had an effect or not.

# Solution:
# 
# Step-1: We need to state the hypotheses. The population mean is 100.
# 
# H0: μ= 100  (Null Hypothesis)
# H1: μ > 100 (Alternate Hypothesis)
# 
# Step-2: We need to Set up the significance level. It is not given in the problem so let’s assume it as 5% (0.05).
# 
# Step-3: We need to compute the random chance probability using z score and z-table.
# 
# For this set of data: z= X-μ/σ*√n = (108-100) / (15/√36) =3.20
# 
# Now by looking at the P- Value probability at z- table and p-value associated with 3.20 is 0.9993.
# The probability of having a value less than 108 is 0.9993.
# The probability of having a value more than or equals to 108 is (1-0.9993)=0.0007.
# 
# Step-4: It is less than 0.05 so Null hypothesis can be rejected stating that there is raw cornstarch effect.
# 
# So, we can conclude that a diet high in raw cornstarch will have a positive effect in blood glucose levels.

# Task 1.2. In one state, 52% of the voters are Republicans, and 48% are Democrats. In a second state,
# 47% of the voters are Republicans, and 53% are Democrats. Suppose a simple random sample
# of 100 voters are surveyed from each state. What is the probability that the survey will show a greater percentage of Republican voters in the second state than in the first state?

# Solution:
# Step 1: We need to assosiate values:
# n1 = 100
# n2 = 100
# 
# P1 (Proportion of Republican voters in first state) = 0.52
# p1 (Proportion of Republican voters in sample form in first state) = 0.52
# P2 (Proportion of Republican voters in second state) = 0.47
# p2 (Proportion of Republican voters in sample form in second state) = 0.53
# 
# Step 2: We need to check that sample is large enough
# n1P1 = 100 * 0.52 = 52                 n1(1 - P1) = 100 * 0.48 = 48
# n2P2 = 100 * 0.47 = 47                 n2(1 - P2) = 100 * 0.53 = 53
# Since the sample size is greater than 10 therefore, sample size is large enough.
# 
# Step 3: We need to find the mean of the difference in sample proportions: 
# E(p1 - p2) = P1 - P2 = 0.52 - 0.47 = 0.05
#             
# Step 4: We need to find the standard deviation of the difference. 
# σd = sqrt{ [ P1(1 - P1) / n1 ] + [ P2(1 - P2) / n2 ] }
# σd = sqrt{ [ (0.52)(0.48) / 100 ] + [ (0.47)(0.53) / 100 ] }
# σd = sqrt (0.002496 + 0.002491) = sqrt(0.004987) = 0.0706
#             
# Step 5: We need to find the probability. 
# This problem requires us to find the probability that p1 < p1
# This is equivalent to finding the probability that (p1 - p2)< 0 and transform the random variable (p1 - p2) into a z-score.
# 
# Putting into the formula:
# Z(p1 - p2) = (x - μ(p1 - p2)) / σd = (0 - 0.05)/0.0706 = -0.7082
# The probability of a z-score being -0.7082 or less is 0.24.
# So, the probability that the survey will show a greater percentage of Republican voters in the second state 
# than in the first state is 0.24.

# Task 1.3. You take the SAT and score 1100. The mean score for the SAT is 1026 and the standard
# deviation is 209. How well did you score on the test compared to the average test taker?

# #Step 1: We need to assosiate values.
# X=1100
# μ=1026
# σ=209
# 
# Step 2: Calculate the answer using a calculator:
# 
# Z = X-μ / σ 
#   = (1100–1026)	/ 209	
#   =	.354	
#   
# It means that your score was .354 standard deviations above	the	mean.
# 
# 
# Step 3: Refer the z-value in the z-table to calculate the percentage of test-takers scored below you. 
# 
# A z-score of 0.354 is 0.1368 which is 13.68%
# Since, z-table shown has scores for the right of the mean. It is required to add .500 ( 50%) for all of the area left of the mean.
# 
# So 0.354 + 0.5000* = .6368 or 63.68%.

# Task 2.1. Is gender independent of education level? A random sample of 395 people were surveyed
# and each person was asked to report the highest education level they obtained. The data that
# resulted from the survey is summarized in the following table:
# High School Bachelors Masters Ph.d. Total
# Female 60 54 46 41 201
# Male 40 44 53 57 194
# Total 100 98 99 98 395
# Question: Are gender and education level dependent at 5% level of significance? In other
# words, given the data collected above, is there a relationship between the gender of an
# individual and the level of education that they have obtained?

# Step 1: We will do Hypothesis for Chi-Sqaure Test statistics:   
# 
# Null Hypothesis: The two categorical variables are independent.
# Alternative Hypothesis: The two categorical variables are dependent.
# 
# The chi-square test statistic is calculated by using the formula:
# χ2 = ∑(O−E)^2/E
# where, 
# O represents the observed frequency
# E represents the expected frequency under the null hypothesis and computed by:
# 
# E = (row total × column total) / sample size
# 
# We will compare the value of the test statistic to the critical value of χ2α with degree of freedom = (r - 1) (c - 1), 
# and reject the null hypothesis if χ2>χ2α.
# 
# Step 2: We will calculate the table of expected counts:
# eg) High School Female = (201*100)/395 = 50.886 (we shall get the table as below for rest of the values once calculated)      
#           High School  Bachelors  Masters   Ph.d.   Total
# Female       50.886     49.868    50.377   49.868    201
# Male         49.114     48.132    48.623   48.132    194
# Total          100        98        99       98      395
# 
# Step 3: We will calculate the Chi-Square value:               
# χ2= (60−50.886)^2/50.886 + (54−49.868)^2/49.868 + (46−50.377)^2/50.377 + (41-49.868)^2/49.868 + (54−49.868)^2/49.868 + (40-49.114)^2/49.114 + (44-48.132)^2/48.132 + (53-48.623)^2/48.623 + (57−48.132)^2/48.132 = 8.006
# χ2= 8.006
#          
# Step 4: Conclusion:
# The critical value of χ2 with 3 degree of freedom is 7.815
# Since 8.006 > 7.815, therefore we reject the null hypothesis
# So, the education level depends on gender at a 5% level of significance.

# Task 2.2. Using the following data, perform a oneway analysis of variance using α=.05. Write up the
# results in APA format.
# 
# [Group1: 51, 45, 33, 45, 67]
# [Group2: 23, 43, 23, 43, 45]
# [Group3: 56, 76, 74, 87, 56]

# Step 1: Calculate Mean, Std Deviations, and Variance of each group.
# 
# Sample means (x¯) for the groups: = 48.2, 35.4, 69.8
# Intermediate steps in calculating the group variances:
# 
# Group1:
#   value mean deviations sq deviations
# 1    51 48.2        2.8          7.84
# 2    45 48.2       -3.2         10.24
# 3    33 48.2      -15.2        231.04
# 4    45 48.2       -3.2         10.24
# 5    67 48.2       18.8        353.44
# 
# Group2:
#   value mean deviations sq deviations
# 1    23 35.4      -12.4        153.76
# 2    43 35.4        7.6         57.76
# 3    23 35.4      -12.4        153.76
# 4    43 35.4        7.6         57.76
# 5    45 35.4        9.6         92.16
# 
# Group3:
#   value mean deviations sq deviations
# 1    56 69.8      -13.8        190.44
# 2    76 69.8        6.2         38.44
# 3    74 69.8        4.2         17.64
# 4    87 69.8       17.2        295.84
# 5    56 69.8      -13.8        190.44
# 
# Sum of squared deviations from the mean (SS) for the groups:
# 612.8 515.2 732.8
# 
# Var1=612.8/5−1=153.2
# Var2=515.2/5−1=128.8
# Var3=732.8/5−1=183.2
# MSerror=(153.2+128.8+183.2)/3=155.07
# 
# Step 2: Calculate the remaining error (or within) terms for the ANOVA table:
# dferror=15−3=12   SSerror=(155.07)(15−3)=1860.8
# Intermediate steps in calculating the variance of the sample means:
# Grand mean (x¯grand) = (48.2+35.4+69.8)/3=51.13
#     group mean grand mean deviations sq deviations
#        48.2      51.13      -2.93          8.58
#        35.4      51.13     -15.73        247.43
#        69.8      51.13      18.67        348.57
# Sum of squares (SSmeans)=604.58
# Varmeans=604.58/3−1=302.29
# MSbetween=(302.29)(5)=1511.45
# 
# Step 3: Calculate the remaining between (or group) terms of the ANOVA table:
# dfgroups=3−1=2   SSgroup=(1511.4/5)(3−1)=3022.9
# 
# Test statistic and critical value
# F=1511.45/155.07=9.75
# Fcritical(2,12)=3.89
# Decision: reject H0 
# 
# ANOVA table
# source	SS	    df	 MS	    F
# group	3022.9	2	1511.45	9.75
# error	1860.8	12	155.07	
# total	4883.7			
# 
# Effect size
# η2=3022.9/4883.7=0.62
# APA writeup
# F(2, 12)=9.75, p <0.05, η2=0.62.

# Task 2.3 Calculate F Test for given 10, 20, 30, 40, 50 and 5,10,15, 20, 25.

# F Test = σ^2m(first Sample Data)/σ^2(Second Sample Data)
# F Test = Variance of first Sample Data/Variance of Second Sample Data.
# 
# Let's calculate Variance of first set for 10, 20, 30, 40, 50:
# 
# Mean (xm)= i=1∑5 (xi)/N = 10+20+30+40+50/5 = 150/5 = 30 
# Means(xm)= 30 
# 
# Variance=(1/(N-1)*(i=1∑5 (xi-xm)2) 
# =1/(5-1)((10-30)2+(20-30)2+(30-30)2+(40-30)2+(50-30)2)) 
# =1/4((-20)2+(-10)2+(0)2+(10)2+(20)2)) 
# =1/4((400)+(100)+(0)+(100)+(400)) 
# =250 
# 
# Let's calculate Variance of first set for 5, 10, 15, 20, 25:
# 
# Mean (xm)= i=1∑5 (xi)/N = 5+10+15+20+25/5 = 75/5 = 15 
# Means(xm)= 15 
# 
# Variance=(1/(N-1)*(i=1∑5 (xi-xm)2) 
# =1/(5-1)((5-15)2+(10-15)2+(15-15)2+(20-15)2+(25-15)2)) 
# =1/4((-10)2+(-5)2+(0)2+(5)2+(10)2)) 
# =1/4((100)+(25)+(0)+(25)+(100)) 
# =62.5 
# 
# Let's calculate F Test: 
# F Test = σ^2m/σ^2
# = 250/62.5 
# = 4
# 
# The F Test value is 4. 
