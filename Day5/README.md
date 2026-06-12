# Day 5 – Loops & Password Generator

## Overview
This day focused on mastering iteration in Python using `for` loops and the `range()` function. These concepts were reinforced through programming exercises and a password generator project.

## Concepts Covered

### For Loops
Learned how to execute a block of code repeatedly using Python's `for` loop.

### Range Function
Used the `range()` function to generate sequences of numbers and control loop execution.

### Indentation
Understood the significance of indentation in Python and how it defines code blocks.

## Exercise – FizzBuzz

Implemented the classic FizzBuzz challenge using loops and conditional statements.

### Rules
- Print `"Fizz"` for numbers divisible by 3.
- Print `"Buzz"` for numbers divisible by 5.
- Print `"FizzBuzz"` for numbers divisible by both 3 and 5.
- Otherwise, print the number itself.

### Concepts Applied
- For loops
- Range function
- Conditional statements
- Modulo operator (`%`)

---

## Mini Project – Password Generator

Built a password generator that creates custom passwords based on user preferences.

### User Inputs
- Number of letters
- Number of symbols
- Number of digits

### Level 1 – Easy Password Generator

Generated passwords by:
- Adding all letters first
- Adding all numbers next
- Adding all symbols at the end

Example:

```text
abc123!@
```

Since the character order is predictable, the generated password is relatively weak.

---

### Level 2 – Hard Password Generator

Improved the password generator by introducing randomization.

Enhancements:
- Stored all selected characters in a list
- Used `random.shuffle()` to randomly rearrange the characters
- Combined the shuffled characters into the final password

Example:

```text
3@a!2cb1
```

This approach produces stronger passwords because the placement of letters, numbers, and symbols is completely randomized.

### Concepts Applied
- For loops
- Lists
- Random module
- `shuffle()` function
- String manipulation
- User input handling

## Summary

This day strengthened understanding of loops, iteration, and sequence generation in Python. Through the FizzBuzz exercise and the Password Generator project, concepts such as looping, conditionals, lists, randomization, and user input were applied to solve practical programming problems.