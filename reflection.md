# PawPal+ Project Reflection

## 1. System Design

Add user info and pet, perhaps being able to create a profile or different family members under users.
Schedule busy or free times, being able to find walk and feeding schedules that correlate with users
free and busy schedules. Capabilities for users, schedules, and creating schedules for pets.

Main objects needed for system include:
User
Pet
FamilyAccount
UserSchedule (can try for 24hr array or so, 48 to include 30 min intervals?)
CareSchedule (could be "PetSchedule") and has similar format to above, but also lists needs at specific intervals, feeding, walk
Assign

**a. Initial design**

- Briefly describe your initial UML design.
The initial UML design has different classes to handle different use cases. Some example classes were FamilyAccount to hold an account id per account, lists of family members, pets, and functionality to add and remove items from those. The UML also had a user class and a pet class to add new users and pets to the familyaccount class. Classes were also created for user schedules to show free time, and to add pet care tasks to user's schedules.
- What classes did you include, and what responsibilities did you assign to each?
The FamilyAccount class is the account class that has a unique account id in case of shared family names
    Also has lists to keep a list of User class and Pet classes.
The schedule class is for a user, and is to store the CareTasks that a pet needs and the user's availability. The schedule is an array of size 48 to give 30 minute intervals in the schedule as well. This class also has functions to add and remove these tasks, and the tasks themselves have a flag to see if the task is covered or not.
The CareTask class is for each individual task a pet needs, such as a walk at a specific time, or dinner.

**b. Design changes**

- Did your design change during implementation?
Yes, explained below
- If yes, describe at least one change and why you made it.
The AI also suggested changes for adding removal methods to remove tasks, as well as consolidating area's of the code that performed the same thing. There were two lists to keep track of the same schedule, as well as two ways to add tasks to a schedule that were both for the same thing.
---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?
The user has a schedule that is filled as tasks are added to the pets, and when the schedule is generated.

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?
One tradeoff for the scheduler is that it does not create a full calendar schedule, so holidays, events, and other things are not taken into account when using it.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?
The AI was most helpful when moving and linking up the different files. It easily created the imports and linked the classes easily to use in each file. The prompts that were most helpful were when I told it to take stuff from one file and add it to another. It was also very useful in building the UML diagrams.

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?
There was a portion of the pytests that the AI tried to help me with. It was unable to fix my error that I was having and actually applied a "fix" that suppressed the error I was getting, and then printing out the expected message, so there are many times you have to keep a close eye on the AI.

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
I tested for the sorting logic, as well as made sure the filtering and scheduling worked in the app.
- Why were these tests important?
These were the main functions of the scheduler, testing the sorting logic helped ensure that the pet lists were sorted correctly

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
