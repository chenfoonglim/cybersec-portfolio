# A28. Implement a security solution of your choice and put it on your GitHub.

I implemented a Python CLI password generator. I made this as many existing built in password generators do not give users control over what type of character types are included. Apple passwords for instance only use “-“ for special characters, and some others include special characters without the option to turn it off, which can be frustrating when a sit has a specific password requirement.

This tool lets the user choose the length, and exactly which character sets to include before generating the password.

The generator uses Python’s secrets module rather than random, as secrets is cryptographically secure and specifically made for generating passwords and tokens. To satisfy the selected criteria, at least one character from each category is chosen, with the remaining characters chosen randomly. The result is then shuffled to prevent predictable character positions.

After generating the password, a checkSecurity function will run and print a breakdown of which of the criterias are met, and produce a verdict if the password is Strong, Moderate, or Weak. This gives the user confidence that the password is suitable to use.