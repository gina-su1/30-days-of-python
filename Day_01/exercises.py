#Day 1 - Exercises

print(10 + 5)
print("10" + "5")
print(10 * 3)
print("10" * 3)

# My predictions:
# 10 + 5 -> 15
# "10" + "5" -> 105
# 10 * 3 -> 30
# "10" * 3 -> 30 INCORRECT: with strings, * means repeat the string, so it would be 101010, repeating "10" 3 times

print(type(1+3j))
print(type([1,2,3]))
print(type({"name": "Gina"}))
print(type({9.8, 3.14, 2.7}))

# My predictions
# Function INCORRECT: j represents the imaginary component, this is a complex number
# Set INCORRECT: this is a list, represented by []
# Dictionary 
# Tuple INCORRECT: this is a set, represented by {}

# =========================
# Day 1 Exercises
# =========================

# Exercise 1
# Print your name.
print("Gina")

# Exercise 2
# Print your age.
print("I am 25 years old")

# Exercise 3
# Print the result of 25 + 17.
print(25 + 17)

# Exercise 4
# Print the type of 25.
print(type(25))

# Exercise 5
# Print the type of 25.0.
print(type(25.0))

# Exercise 6
# Print the type of "25".
print(type("25"))

# Exercise 7
# Create a list containing three cybersecurity tools.
# Print its type.
tools = ["metasploit", "wireshark", "nmap"]
print(type(tools))

# Exercise 8
# Create a dictionary containing your name and your career goal.
# Print its type.
goal = {
	"name" : "Gina",
	"careergoal" : "analyst"
}
print(type(goal))
