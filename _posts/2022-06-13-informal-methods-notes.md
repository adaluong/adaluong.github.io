---
layout: post
title: Practical Guide to Thinking about Programming
date:   2022-06-13 16:40:16
description: Notes from UNSW’s COMP6721 course, (In-)Formal Methods the Lost Art
---

***Notes from UNSW’s COMP6721 course, (In-)Formal Methods: the Lost Art.***

I’ll add some more context to these notes soon™️, but here’s a practical summary of some key ideas in the course with details in the lecture notes [here](https://www.cse.unsw.edu.au/~cs6721/2022T2/Web/index.html).

---
## Imperative Programming
--- 

#### Writing Comments

- Writing good comments help you maintain a program and it helps you write them in the first place
- Include a comment about **what the program is supposed to do** at the beginning of your code. That’s how you can check that a segment does what it’s expected to do.
- Comments should not be a summary of what a bit of code does. Instead, it should document “**what’s true here**?” or “what’s known now?” This makes it easier for team members to collaborate because it lets large programs be divided into pieces that can be handled separately
- You should include the **pre-condition** and **post-condition** as part of your commenting. In other word, what’s true before and after a piece of code?

#### Assignments

- Preference **multiple assignments** over sequential assignments. This is because sequential assignments have an implicit condition between assignments, and leads to more complexity in reasoning.

#### Functions

- Avoid **functions with side effects**. This makes it easier to reason about a program (consider a function with side effects used as a test for a condition)

#### Invariants

- An invariant is a statement that you come up with that you know to be true throughout the program - i.e., it doesn’t vary (wow!)
- One way to come up with the invariant is to **split the post-condition into two pieces** at the conjunction to become the invariant and the loop guard

#### Writing Loops

- **While loops** are easier to reason with than for loops: you know when it ends and what values are after the loop terminates. Consider writing your program with while loops, and then using “program algebra” (i.e. local changes that are obviously correct) to transpose them to for loops once you can guarantee that your program works.
- **Loop guard** can be written in a way to provide information about what’s true after a loop ends. We prefer `n != N` because it provides more information about the state of the program after the loop terminates than `n < N`
- An efficient thought process for writing loops:
    1. What is the **invariant** of the loop
    2. What should the **initialisation** be to make the invariant true at the beginning of the loop
    3. What should the **loop guard** be: think about this in terms of what we want to be true at the end of the program
    4. What is the **loop body**: remember, progress must be made for the loop to terminate, and we need to maintain to invariant
    5. Clean-up: here, we can do things like **creating special cases** so we don’t need to test conditions more than once, and changing the while loop to a for loop for style reasons.
- To make sure a program **doesn’t loop forever**: find a variant that is a non-negative integer that strictly decreases at each iteration of the loop

#### Propositional Logic

- Propositional logic is helpful when we are thinking about invariants, particularly **implications**
- Propositions are defined by their **truth tables** - search them up!

#### Will the Loop Terminate?

- To avoid infinite loops, you need a **variant** that is
    1. an integer
    2. never negative, and 
    3. strictly decreases with every iteration of the loop
- This can be a **lexicographic variant**, which is a generalisation of the alphabetical order of dictionary sequences

---
## Data Structures
---

How do you translate the high-level problem solving techniques with its implementation in code?

#### Fast Fibonacci

Here’s an example of how we break up our thinking. In this program, we want to calculate the Fibonacci sequence in `log(N)` time.

- ***What’s the high-level insight / technique?***
    
    We rely on an abstraction inherent to matrix operations: they’re associative, so we make multiplication speedy with ✨[fast exponentiation](https://en.wikipedia.org/wiki/Exponentiation_by_squaring#:~:text=In%20mathematics%20and%20computer%20programming,polynomial%20or%20a%20square%20matrix.)✨. Note: the operation is ***not*** commutative.
    
- ***How do you represent this in a program that uses ordinary scalars?***
    
    We introduce coupling invariants so you can move your abstract variable (like a matrix) to a concrete variable (like a bunch of `int` variables) without violating properties (like how matrix multiplication works)… because the coupling invariant serves as the “definition” you assume to be true throughout the programming
    

#### Mean Calculator

Another example is an implementation of a calculator that evaluates the mean of numbers. It has the operations ‘clear’, ‘enter’, and ‘mean’

- Invariants continue to play a role here: we want to use a **data-type invariant** alongside **coupling invariants** and **auxiliary invariants**
- A **data-type invariant** is an invariant that links to the abstract ‘problem-solving’ part of your problem with its implementation within a data structure
- **Bound variables**: are variables that are only within scope of a particular part of the program - i.e. they can be substituted with other variable names, and it wouldn’t make a difference
- **Encapsulation** is important and bound variables help ensure this

---
## Concurrency
---

#### Introduction to Concurrency

When a processor runs a program, it generally interleaves threads together. This is great, because it means we don’t have to wait for a program to completely finish before moving onto another program (consider a thread that is waiting for a resource).

However, it also makes reasoning about programs more COMPLICATED because it introduces new problems :D 

- **Deadlock**: when two threads are stuck, and neither makes progress
- **Livelock**: kind of like when you try to pass someone you’re walking towards, but you both keep going left and right but none of you make progress
- **Individual Starvation**: when there’s an infinite overtaking for one thread that never gets to run

To tackle concurrency, we need to understand

- **Critical sections**: these are sections of the code where processes access shared resources
- **Mutual exclusion**: this is a property that prevents simultaneous access to a shared resource

#### Peterson’s Algorithm via Misra’s Queue

- Peterson’s algorithm implements mutual exclusion for concurrent programs using only shared memory for communication
- Misra’s queue is one implementation of Peterson’s algorithm. It makes use of abstraction, coupling invariants, data type invariants, and auxiliary/ghost variables
- **The idea**: we add the thread number to the queue, and if the thread is at the head of the queue, we execute the critical section and then remove the element from the head of the queue
- **However**: it isn’t mutual exclusion itself, because adding and removing from the queue itself is not atomic
- This is where **DATA REFINEMENT** comes in - we want to use a data-invariant to transpose the abstract queue to a boolean representation with a coupling invariant in order to make the boolean manipulation atomic
- **Data Refinement process**: data type invariant → coupling invariant → introduce concrete ghost variants → swap abstract and concrete → remove (now) ghost abstracts

#### Atomicity and Single Assignments

- We want to split up multiple assignments into single assignments!
- The insight is that we **strengthen the await condition** so we can reduce interleaving and improve safety - the coupling invariant ***is implied by*** the original variables `t1`/`t2`
- A **“really atomic**” statement refers to at most ONE variable that its thread doesn’t **own**
- **Owning** a variable means that it is only assigned in that thread
- **Stability**: cannot be falsified by the other thread