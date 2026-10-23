นายวรากร โสภา 683380095-8 sec1 week5

Lab 5 : Data Structures: Dictionaries & Sets

etailed Labs
Lab 5.1: Simple Contact Book Manager (Dictionary Focus)
Objective: Create a text-based contact book where you can add, view, update, and delete contacts using a dictionary.
Tasks:Setup: Create a new Python file (lab5_1.py) or a Google Colab code cell.Initialize: Create an empty dictionary: contacts = {}Menu Loop: Implement a while loop that presents the following menu to the user:
1. Add/Update Contact
2. View Contact Details
3. List All Contacts
4. Delete Contact
5. Exit
Add/Update:
If the user enters an existing name, update their info.
If it's a new name, add them to the dictionary.
Key: Contact Name
Value: Dictionary of details (e.g., {"phone": "123-4567", "email": "a@b.com"})
View: Prompt for a contact name, use .get() to retrieve and print details, or display "Contact not found."List All: Iterate through contacts.items() and print each contact's name and details.Delete: Prompt for a contact name, use .pop() or del to remove it. Handle "Contact not found." Challenge: Ensure keys are case-insensitive when searching or deleting (convert user input to .lower() or .title() consistently).
Lab 5.2: Course Enrollment & Collaboration (Set Focus)
Objective: Simulate course enrollments and find common students using set operations.
Tasks:Setup: Create a new Python file (lab5_2.py) or a Google Colab code cell.Initialize Sets:
python_students = {"S001", "S003", "S005", "S007", "S009"}
java_students = {"S002", "S003", "S006", "S007", "S010"}
Find Students in Both Courses: Use the intersection() method or & operator to find students enrolled in both Python and Java. Print the result.Find All Unique Students: Use the union() method or | operator to find all unique students across both courses. Print the result.Find Students Only in Python: Use the difference() method or - operator to find students in Python but not in Java. Print the result.Find Students in Only One Course (Exclusive): Use the symmetric_difference() method or ^ operator to find students enrolled in Python or Java, but not both. Print the result.Remove Duplicates from a List:
Create a list with duplicate student IDs (e.g., all_students_list = ["S001", "S003", "S005", "S001", "S002"]).
Convert it to a set to remove duplicates, then convert it back to a list.
Print both the original list and the unique list.
Detailed Activities

Activity 5.1: Real-World Applications of Dictionaries and Sets
Format: Brainstorming session (Small groups or full class)
Purpose: Solidify understanding of practical applications and encourage critical thinking about data structure choices.
Instructions:
Identify real-world scenarios or problems where Dictionaries and Sets would be the ideal data structures to use, explaining why.
Discussion Prompts:
Where would you use a dictionary in a game? (e.g., player inventory, character stats)
How could a dictionary represent data about a product in an online store? (e.g., product details by ID)
When would a set be useful in managing user permissions or tags? (e.g., unique roles, unique hashtags)
Can you think of a scenario where you'd need to quickly check if an item exists in a large collection without caring about its order? (e.g., blocked IP addresses, unique visitors)
 Activity 5.2: Word Frequency Counter (using Dictionary)
Format: Individual Coding Challenge
Purpose: Apply dictionary operations to a common text processing task, demonstrating efficient counting and retrieval.
Instructions & Steps:Prompt the user to enter a sentence.Convert the sentence to lowercase: sentence.lower()Split the sentence into words: words = sentence.split()Initialize an empty dictionary: word_counts = {}Loop through each word in words.Inside the loop, check if the word is already a key using if word in word_counts::
If yes: Increment its count (word_counts[word] += 1)
If no: Add it to the dictionary with a count of 1 (word_counts[word] = 1)
Print the word_counts dictionary.
Challenge: Handle punctuation (e.g., remove commas and periods before counting words).
Hint: Use word.strip('.,!?"')
