# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
I tried entering numbers in the range indicated, but numbers outside of the range (negative numbers and numbers greater than 100) are also being accepted. 
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
Two bugs that I immediately saw was the hints were directed in the opposite direction. If the secret is 10, and the player entered 20, the hint would say "Go Higher" instead of lower.
Another bug is that the Normal difficulty has more attempts (7 attempts) compared to the Easy (5 attempts)

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| | |64 | Go Higher              Go Lower
| | |66 | Go Lower               Go Higher
| | |52 | Correct                Correct
| | |-1 | Out of Range / Go Higher           Go Lower
| | 101 | Out of Range / Lower               Go Higher

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used Claude as my AI partner in this project
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
It was able to fix the logical errors in the app.py
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
Testing and running the app
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- More interesting is that Claude create a pytest.ini when the test suites failed due to directory issues. I learned that *.ini files can be used in that way.
- Did AI help you design or understand any tests? How?
- Yes, it helped by explaining the insights behind the suggested edits.
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Streamlit refreshes all variable values during each interaction with the webapp. In order to save the values, a dictionary-like structure is used. This is the session state.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
- Creating pytests early on in the development 
- using Git to create checkpoints during software development
- What is one thing you would do differently next time you work with AI on a coding task?
- Try utilizing AI as a coding partner and not a mere chatbot
- In one or two sentences, describe how this project changed the way you think about AI generated code.
- This project demonstrate the capabilities of AI to "understand" and grasp underlying logic of software, which sometimes can overwhelm developers. But while AI can indeed speed up development, constant review should be done to prevent small, edge case errors from being compounded in later stage of the coding process

