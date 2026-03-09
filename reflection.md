# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
First, the enter button doesnt submit the guess, that feature does not work properly. Second, when i submitted a negative number as a guess, it prompted me to guess lower. Even after 8 negative guesses, the correct answer was 89, which doesnt make sense. It should not allow negative number as guesses since the range is 1 - 100. Lastly, the hint feature is broken. When after my submission of negative numbers, it doesn't seem to map the difference and direction between the submitted guess and the correct number accurately.

Additinally, the new game button doesnt refresh the state of the game.
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  - i used claude code
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  - the AI correctly swapped the output for the check_guess function,
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result). The AI was really good at fixing the bugs in the codebase, since it was not a complex bug

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  - i had the AI generate a set of test cases positive and negative, then i ran pytest
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
    - with the AI i created a test case to check if the hint is working correct, asserting its providing the correct string to the user
- Did AI help you design or understand any tests? How?
  - the AI understood what test needed to be added because i passed the file @app.py as context, and what bugs we fixed

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
  - in the code, the logic changes the type of the secret number from int to str back and forth for every guess. on odd guess the secret was int, on even guess the secret was str
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  - streamnlit refreshes the state on every interaction with the application, so we need to make sure keep the secret number in memory so its persistant across states. If we dont, then the secret number is lost with every interaction
- What change did you make that finally gave the game a stable secret number?
  - i remove the type conversion of the secret number.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
  - i thought my use of AI was well done for this project
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  - is forced me to always git commit so i can always go back to a working state of the codebase
