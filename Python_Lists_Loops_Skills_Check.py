# # Name: Sophia Chang
# # Period: AM

# # ============================================================
# # Python Skills Check — LISTS & LOOPS
# # CHALLENGE VERSION — 40 TASKS
# # ============================================================
# # DIRECTIONS:
# # - Create a repository, clone it, and add this file.
# # - Complete each task UNDER its directions.
# # - Do not delete the directions.
# # - Use ONLY concepts learned in class, except for 'in' and 'not in'.
# #   You must research these two new operators independently in Section 5.
# # - Use the EXACT variable and function names provided.
# # - The entire file must run without errors.
# # - Do not hard-code results Python should calculate.
# # - Unless a task says otherwise, do NOT use sum(), min(), max(),
# #   sorted(), sort(), list comprehensions, sets, or dictionaries.
# # - For functions, RETURN values when instructed; do not just print.
# # - Test edge cases and change the starting values to check your logic.
# # - Tasks that ask for input() may be tested individually.

# # ============================================================
# # SECTION 1 — LIST FUNDAMENTALS (TASKS 1–6)
# # ============================================================

# # TASK 1:
# # Create a list named scores containing 85, 92, 78, 96, 88.
# # Print the entire list and its length using len().

# scores = [85,92,78,96,88]
# print("scores:", scores, "length: ", len(scores))


# # TASK 2:
# # Using scores from Task 1, print the FIRST, THIRD, and LAST
# # elements on separate lines. Use indexes, not hard-coded values.

# print(scores[0])
# print(scores[2])
# print(scores[len(scores)-1])


# # TASK 3:
# # Change the third element of scores to 100.
# # Print the updated list. Do not create a replacement list.

# scores.pop(2)
# scores.insert(2, 100)
# print(scores)

# # TASK 4:
# # Create games = ["Minecraft", "Roblox", "Fortnite"].
# # Append "Valorant" and insert "Rocket League" at index 1.
# # Print games. Check the order carefully.

# games = ["Minecraft", "Roblox", "Fortnite"]
# games.append("Valorant")
# games.insert(1, "Rocket League ")
# print(games)

# # TASK 5:
# # Using games from Task 4, remove "Roblox" with remove().
# # Then pop the FIRST item into a variable named removed_game.
# # Print removed_game and the remaining games list.

# games.remove("Roblox")
# removed_game = games.pop(0)
# print(removed_game, games)

# # TASK 6:
# # Create colors = ["red", "blue", "green", "yellow", "purple"].
# # Store the index of "green" in green_index using index().
# # Print green_index. Then replace "yellow" with "orange".
# # Print the new list.

# colors = ["red", "blue", "green", "yellow", "purple"]
# green_index = colors.index("green")
# print(green_index)
# colors.insert(colors.index("yellow"), "orange")
# colors.remove("yellow")
# print(colors)

# # ============================================================
# # SECTION 2 — FOR LOOPS & RANGE (TASKS 7–12)
# # ============================================================

# # TASK 7:
# # Use a for loop with range() to print numbers 1 through 20,
# # INCLUDING 20. Do not manually print the numbers.

# for i in range(1,21):
#     print(i)

# # TASK 8:
# # Use a for loop with range() to print 30, 27, 24, ... 0.
# # IMPORTANT: The zero must be included.

# for i in range(30, -1, -3):
#     print(i)

# # TASK 9:
# # Use a for loop to print all EVEN numbers from 1 to 50.
# # You MUST use an if statement and the % operator inside the loop.

# for i in range(1, 51):
#     if i % 2 == 0:
#         print(i)

# # TASK 10:
# # Create number = 7.
# # Print its multiplication table from 1 through 12 using a for loop.
# # Example line: 7 x 3 = 21
# # Your code must also work if number changes.

# number = 7
# for i in range(13):
#     print(number * i)

# # TASK 11:
# # Create students = ["Alex", "Jordan", "Taylor", "Morgan", "Casey"].
# # Use a for loop to print "Student: " followed by each name.
# # Do NOT write five separate print statements.

# students = ["Alex", "Jordan", "Taylor", "Morgan", "Casey"]
# for i in students:
#     print("Student: ", i)


# # TASK 12:
# # Using students, print a NUMBERED roster:
# # 1. Alex
# # 2. Jordan
# # ...
# # 5. Casey
# # Use range(len(students)) OR enumerate().

# for i in range(len(students)):
#     print(i+1,".",students[i])

# # ============================================================
# # SECTION 3 — WHILE LOOPS & VALIDATION (TASKS 13–18)
# # ============================================================

# # TASK 13:
# # Create countdown = 10.
# # Use a while loop to print from countdown down to 0.
# # Then print "Blast off!". Avoid an infinite loop.

# countdown = 10
# while countdown != -1:
#         print(countdown)
#         countdown -= 1
# print("Blast off!")

# # TASK 14:
# # Create password = "Python123".
# # Keep asking the user for a password until it matches.
# # Print "Access granted" exactly once after a correct entry.

# password = "Python123"
# word = input("Enter the password: ")
# while word != password:
#     print("Incorrect password.")
#     word = input("Enter the password:")
# print("Access granted")

# # TASK 15:
# # Ask the user for an integer between 1 and 10 INCLUSIVE.
# # Keep asking while the value is invalid.
# # After a valid entry, print "Valid number".
# # Test 0, 1, 10, and 11.

# num = int(input("Please type in an integer between 1 and 10 inclusive:"))
# while 1 > num or num > 10:
#     num = int(input("Please type in an integer between 1 and 10 inclusive:"))
# print("Valid number")

# # TASK 16:
# # Create total = 0.
# # Repeatedly ask for an integer. Add each nonzero entry to total.
# # Stop when the user enters 0, then print total.
# # Example inputs: 5, 8, -2, 0 -> Total: 11.

# total = 0
# integer = int(input("Please enter an integer:"))

# while integer != 0:
#     total = total + integer
#     integer = int(input("Please enter an integer:"))
# print(total)

# # TASK 17:
# # Create secret = "robot" and attempts = 3.
# # Ask the user to guess secret, allowing AT MOST 3 guesses.
# # Print "Correct" if guessed in time; otherwise "Out of attempts".
# # Make sure a correct guess does NOT print both messages.

# secret = "robot"
# attempts = 3

# while attempts != 0:
#     guess = input("You have " + str(attempts) + " attempts to guess the secret word:")
#     attempts -= 1
#     if guess == secret and attempts > 0:
#         print("Correct")
#         attempts =0
#     elif attempts == 0:
#         print("Out of attempts")

# # TASK 18:
# # Make a while-loop menu:
# # 1. Say Hello
# # 2. Say Goodbye
# # 3. Exit
# # Repeat until the user enters 3. Handle invalid choices.
# # Print "Goodbye" only when option 2 is selected.


# def menu():
#     print("1. Say Hello")
#     print("2. Say Goodbye")
#     print("3. Exit")
#     num = int(input("Please choose a number from the menu.: "))
#     while num < 1  or num > 3:
#         print("Invalid!")
#         num = int(input("Please choose a number from the menu.: "))
#     return num

# loop = menu()

# while loop != 3:
#     if loop == 1:
#         print("Hello")
#     elif loop == 2:
#         print("Goodbye")
#     loop = menu()


# # ============================================================
# # SECTION 4 — PROCESSING LISTS WITH LOOPS (TASKS 19–24)
# # ============================================================

# # TASK 19:
# # Create numbers = [4, 8, 15, 16, 23, 42].
# # Use a for loop to calculate and print their total.
# # Do NOT use sum().

# numbers = [4, 8, 15, 16, 23, 42]
# total = 0
# for i in range(len(numbers)):
#     total += numbers[i]
# print(total)

# # TASK 20:
# # Create grades = [90, 85, 78, 92, 88].
# # Use a loop and len() to calculate the average.
# # Print the average. Do NOT use sum().

# grades = [90, 85, 78, 92, 88]
# total = 0
# for i in range(len(grades)):
#     total += grades[i]
# average = total / len(grades)
# print(average)


# # TASK 21:
# # Create numbers = [3, 8, 12, 7, 15, 20, 24, 9].
# # Use ONE loop to count even and odd values separately.
# # Print "Even: [count]" and "Odd: [count]".

# numbers = [3, 8, 12, 7, 15, 20, 24, 9]
# even = 0
# odd = 0
# for i in range(len(numbers)):
#     if numbers[i] % 2 == 0:
#         even += 1
#     else:
#         odd += 1
# print("Even: ", even)
# print("Odd: ", odd)


# # TASK 22:
# # Create numbers = [-14, -67, -23, -89, -45].
# # Use a loop to find and print the HIGHEST number.
# # Do NOT use max() or sorting.
# # IMPORTANT: Starting your answer at 0 gives a wrong result.

# numbers = [-14, -67, -23, -89, -45]
# max = numbers[0]
# for i in range(len(numbers)):
#     if numbers[i] > max:
#         max = numbers[i]
# print(max)

# # TASK 23:
# # Create numbers = [14, 67, 23, 89, 45, 12].
# # Use a loop to find and print the LOWEST number.
# # Do NOT use min() or sorting.
# # Your logic must also work with all-negative numbers.

# numbers = [14, 67, 23, 89, 45, 12]
# low = numbers[0]
# for i in range(len(numbers)):
#     if numbers[i] < low:
#         low = numbers[i]
# print(low)

# # TASK 24:
# # Create numbers = [5, 2, 5, 8, 5, 3, 2, 5].
# # Create target = 5.
# # Use a loop to count how often target appears; print the count.
# # Do NOT use count(). It must work if target changes.

# numbers = [5, 2, 5, 8, 5, 3, 2, 5]
# target = 5
# count = 0
# for i in range(len(numbers)):
#     if numbers[i] == target:
#         count += 1

# print(count)

# # ============================================================
# # SECTION 5 — IN / NOT IN (TASKS 25–30)
# # ============================================================
# # INDEPENDENT RESEARCH REQUIRED:
# # We have NOT covered 'in' and 'not in' in class. Before starting
# # Tasks 25–30, research both operators on your own using reliable
# # Python learning resources or the official Python documentation.
# # Learn what each operator does, how it works with lists, and how
# # to use it inside if statements and while loops.
# # Write a short comment in your code explaining the difference
# # between 'in' and 'not in' in your own words.
# # The examples below are starting hints, NOT a substitute for research.
# #
# # NEW CONCEPT:
# # 'in' checks whether a value is in a list.
# # Example: "apple" in ["apple", "banana"] evaluates to True.
# # 'not in' checks whether a value is missing.
# # Example: "grape" not in ["apple", "banana"] evaluates to True.
# # These expressions are useful in if statements and while loops.

# #The difference between 'in' and 'not in' is that 'in' checks if a value is within the list or array, and if it is, then it returns True. Otherwise, it'll return False. 'not in' checks if a value is not in a list or array where if the value isn't found in the list or array, it will evaluate to True. Otherwise, it'll return False.

# # TASK 25:
# # Create foods = ["pizza", "burger", "tacos", "sushi", "pasta"].
# # Ask the user to enter a food.
# # Use 'in' to print "Available" or "Not available".
# # Do NOT use index() to search.

# foods = ["pizza", "burger", "tacos", "sushi", "pasta"]
# food = input("Enter a food: ")
# if food in foods:
#     print("Avaliable")
# else:
#     print("Not Available")

# # TASK 26:
# # Create supplies = ["pencil", "notebook", "eraser", "backpack"].
# # Ask the user for an item.
# # Use 'not in' to print "Need to buy" if it is missing,
# # otherwise print "Already have it".

# supplies = ["pencil", "notebook", "eraser", "backpack"]
# item = input("Enter an item: ")
# if item not in supplies:
#     print("Need to buy")
# else:
#     print("Already have it")

# # TASK 27:
# # Create usernames = ["alex123", "gamer99", "pythonpro"].
# # Ask the user to enter a new username.
# # If it is already in the list, print "Username taken".
# # Otherwise append it and print the updated list.
# # Do not allow duplicates.

# usernames = ["alex123", "gamer99", "pythonpro"]
# username = input("Please enter a new username: ")
# if username in usernames:
#     print("Username taken")
# else:
#     usernames.append(username)
#     print(usernames)

# # TASK 28:
# # Modify the idea from Task 27 using a NEW list named accounts.
# # Start with accounts = ["admin", "guest"].
# # Use a while loop to keep asking until the entered name
# # is NOT in accounts. Append the accepted name and print accounts.
# # REQUIREMENT: Use 'not in' in your solution.

# accounts = ["admin", "guest"]
# name = input("Please enter a name: ")

# while name in accounts:
#     name = input("Please enter a name:")
# accounts.append(name)
# print(accounts)

# # TASK 29:
# # Create secret_words = ["dragon", "robot", "python", "galaxy"].
# # Keep asking the user for a word UNTIL it is in secret_words.
# # Count and print the number of guesses made.
# # A correct first guess should count as 1.

# secret_words = ["dragon", "robot", "python", "galaxy"]
# word = input("Guess the secret word: ")
# guess = 1
# while word not in secret_words:
#     word = input("Guess the secret word: ")
#     guess +=1
# print("You've made ", guess, "guesses and have found the secret word!")

# # TASK 30:
# # Create guests = [].
# # Ask the user to enter EXACTLY FIVE UNIQUE guest names.
# # If a name is already in guests, reject it and ask again.
# # Use a while loop, 'in' or 'not in', and append().
# # Print the finished list and its length.

# guests = []
# guest = input("Please enter a unique guest name:")
# guests.append(guest)
# num_of_guesses = 4
# while num_of_guesses != 0:
#     guest = input("Please enter a unique guest name:")
#     if guest in guests:
#         guest = input("Please enter a different unique guest name:")
#         if guest not in guests:
#             guests.append(guest)
#             num_of_guesses -= 1
#     else:
#         guests.append(guest)
#         num_of_guesses -= 1

# print(guests)
# print(len(guests))

# # ============================================================
# # SECTION 6 — LISTS + FUNCTIONS (TASKS 31–35)
# # ============================================================

# # TASK 31:
# # Create a function named count_positive(numbers).
# # RETURN how many elements are greater than 0.
# # Do NOT use count().
# # Test: count_positive([-2, 0, 4, 9, -1]) -> 2

# def count_positive(numbers):
#     count = 0
#     for i in range(len(numbers)):
#         if numbers[i] > 0:
#             count += 1
#     return count
# cnt = count_positive([-2, 0, 4, 9, -1])
# print(cnt)

# # TASK 32:
# # Create a function named find_item(items, target).
# # RETURN the index of the FIRST matching item, or -1 if missing.
# # Do NOT use index().
# # Test: find_item(["cat", "dog", "cat"], "cat") -> 0
# # Test: find_item(["cat", "dog"], "fish") -> -1

# def find_item(items, target):
#     for i in range(len(items)):
#         if items[i] == target:
#             return i
#         else:
#             return -1

# print(find_item(["cat", "dog", "cat"], "cat")) 
# print(find_item(["cat", "dog"], "fish"))

# # TASK 33:
# # Create a function named unique_items(items).
# # RETURN a NEW list without duplicate values, preserving first
# # appearance order. REQUIREMENT: Use 'not in'.
# # Test: unique_items([1, 2, 2, 3, 1, 4]) -> [1, 2, 3, 4]

# def unique_items(items):
#     new = []
#     for i in range(0, len(items)):
#         if items[i] not in new:
#             new.append(items[i])
#     return new

# print(unique_items([1, 2, 2, 3, 1, 4]))

# # TASK 34:
# # Create a function named common_items(list1, list2).
# # RETURN a NEW list of values found in BOTH lists.
# # Include each matching value only once, in list1's order.
# # REQUIREMENT: Use both 'in' and 'not in'.
# # Test: common_items([1, 2, 3, 3], [3, 4, 1]) -> [1, 3]

# def common_items(list1, list2):
#     new1 = []
#     for i in list1:
#         if i in list2:
#             if i not in new1:
#                 new1.append(i)
#     return new1

# print(common_items([1, 2, 3, 3], [3, 4, 1]))


# # TASK 35:
# # Create a function named reverse_list(items).
# # RETURN a NEW list in reverse order, without changing items.
# # Do NOT use reverse(), reversed(), or [::-1].
# # Test: reverse_list([10, 20, 30]) -> [30, 20, 10]

# def reverse_list(items):
#     new2 = []
#     for i in range(len(items)-1, -1, -1):
#         new2.append(items[i])
#     return new2

# print(reverse_list([10, 20, 30]))

# # ============================================================
# # SECTION 7 — DEBUGGING (TASKS 36–37)
# # ============================================================

# # TASK 36:
# # Fix this code so it prints 1, 2, 3, 4, 5 exactly once each.
# # Explain in a comment what was wrong.
# #
# # number = 1
# # while number <= 5:
# #     print(number)
# #
# # Do NOT replace the while loop with a for loop.

# number = 1
# while number <= 5:
#     print(number)
#     number += 1

# #the original code wouls only continue printing 1 because the number never increments, which means it won't be able to get out of the while loop. 

# # TASK 37:
# # Fix this code so it removes ALL 4s without skipping any.
# # Explain in a comment why the original approach can fail.
# #
# # values = [4, 4, 7, 4, 9]
# # for value in values:
# #     if value == 4:
# #         values.remove(value)
# # print(values)
# #
# # Expected: [7, 9]
# # HINT: A while loop and 'in' can help.

# values = [4, 4, 7, 4, 9]
# while 4 in values:
#     values.remove(4)
# print(values)

# #the original approach failed because the for loop keeps on incrementing even when the list changed. The first time the for loop goes through the list, the remove function takes the first 4 it encounters. Now, values changed to [4, 7, 4, 9]. The for loop is going to check the second element in the list, which is 4. Since the if statement checks for a 4 in the list, the remove function will just remove the first 4 it incounters. Now the values list became [7,4,9]. Then, the for loop will check the third element in the list, 9. Since the if statement checks only if the third elemnt is a 4, the code will just print [7,4,9].

# # ============================================================
# # FINAL BOSS CHALLENGES (TASKS 38–40)
# # ============================================================

# TASK 38 — SHOPPING LIST MANAGER:
# Build a menu-driven program with:
# 1. Add item
# 2. Remove item
# 3. View numbered items
# 4. Search for item
# 5. Exit
# Start with shopping_list = [].
# REQUIREMENTS:
# - Use a while loop for the menu and a for loop to display items.
# - Use 'in' to prevent duplicates and 'not in' to reject missing items.
# - Handle an empty list and invalid menu selections.
# - Keep running until the user chooses Exit.

shopping_list = []
products = []
choice = input("Please choose a number from the list:")
def menu():
    print("1. Add item")
    print("2. Remove item")
    print("3. View numbered items")
    print("4. Search for item")
    print("5. Exit")
menu()

while choice != 5:
    if choice == 1:
        for i in range(len(products)):
            print(f"{i+1}.", products[i])
        num = input("Please choose a number from the list of products that are available")
        while num < 0 or num > len(products)-1:
            for i in range(len(products)):
                print(f"{i+1}.", products[i])
            num = input("Please choose a number from the list of products that are available")
        shopping_list.append(products[num])
   
    elif choice == 2:
        print(shopping_list)
        if shopping_list == 0:
            print("You dont have anything in your cart.")
        else:
            num = input("What item would you like to remove?")
            shopping_list.remove(products[num])

    elif choice == 3:
        for i in range(len(products)):
            print(f"{i+1}.", products[i])

    elif choice == 4:
        item = input("What item do you want to find?")
        if item in products:
            print("The item is available.")
        else:

    

# # TASK 39 — GRADE ANALYZER:
# # Create a function named analyze_grades(grades).
# # RETURN a list containing, IN THIS ORDER:
# # [highest_grade, lowest_grade, average_grade, passing_count, failing_count]
# # Passing means 70 or higher.
# # Do NOT use sum(), min(), max(), or sorting.
# # For an empty list, RETURN [].
# # Test: analyze_grades([95, 82, 67, 74, 58])
# # Expected: [95, 58, 75.2, 3, 2]
# # Test with a single grade and all-negative values too.

# def analyze_grades(grades):
#     if len(grades) > 0:
#         grade = []
#         highest_grade = grades[0]
#         lowest_grade = grades[0]
#         sum = 0
#         pass_count = 0
#         fail_count = 0
#         for i in grades:
#             sum = sum + i
#             if i > highest_grade:
#                 highest_grade = i
#             if i < lowest_grade:
#                 lowest_grade = i
#             if i > 70:
#                 pass_count += 1
#             if i < 70:
#                 fail_count += 1
#         grade.append(highest_grade)
#         grade.append(lowest_grade)   
#         average_grade = sum/len(grades)
#         grade.append(average_grade)
#         grade.append(pass_count)
#         grade.append(fail_count)
#         return grade
#     else:
#         return grades
  
# print(analyze_grades([95, 82, 67, 74, 58]))
# print(analyze_grades([6]))
# print(analyze_grades([-2]))
# print(analyze_grades([]))

# TASK 40 — STUDENT ATTENDANCE SYSTEM:
# Start with:
# students = ["Alex", "Jordan", "Taylor", "Morgan", "Casey"]
# present = []
# absent = []
# For EACH student, ask whether they are Present (P) or Absent (A).
# REQUIREMENTS:
# - Use a for loop to process the student list.
# - Use a while loop to reject anything other than P or A.
# - Prevent duplicate attendance records using 'in' / 'not in'.
# - Print numbered present and absent lists.
# - Print the number present, number absent, and attendance percentage.
# - Print "Perfect Attendance!" if everyone is present.
# - Create attendance_percentage(present, students) that RETURNS
#   the percentage; if students is empty, RETURN 0.
# - Test with all present, all absent, and a mixture.

students = ["Alex", "Jordan", "Taylor", "Morgan", "Casey"]
present = []
absent = []

while 

# ============================================================
# END OF CHECKPOINT — REVIEW YOUR WORK BEFORE PUSHING
# ============================================================
