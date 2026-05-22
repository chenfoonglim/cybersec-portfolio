# B26. Help another student in this unit struggling to understand/learn a cybersecurity concept.
Overview: I helped another student understand what threat modelling is particularly using attack trees. He had missed the lecture and needed help to understand how attack trees work, especially the difference between AND and OR branches and when to multiply the different probabilities.

I used the lecture slides to explain that attack trees are used to break down an attacker’s main goal into smaller possible attack paths. I also drew a simpler version of an attack tree with the goal being compromising a student account. The lower branches included phishing, password reuse, and session theft.

I also explained that AND branches are used when all steps must happen for the attack to be possible, and that their probabilities are multiplied. I gave the example If the phishing path requires having the user to click a bad link, enter password and approve `MFA`, then all three events must happen for this attach to work. I also explained that OR branches are used when there are alternate paths that can be used to the same goal.

I taught him step by step on how to do the probability calculation. For a single AND path, the probability is multiplied together (0.3 x0.5 x 0.2 = 0.03)  so the phishing path has 3% chance. As for OR branches, I first explained the formula 1 - (1 - p1)(1 - p2)(1 - p3) is used to prevent double counting and that we cannot simply use addition. I also briefly explained risk heat maps.
![1.png](images/1.png)
