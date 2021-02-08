class admin_Question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer
question_prompts = [
     "What does 'sein' mean?\n(1) 'to be'\n(2)'to have'\n",
     "What does 'haben' mean?\n(1) 'to be'\n(2)'to have'\n",
    "What does 'werden' mean?\n (1) 'to become'\n (2) 'to come'\n",
    "What does 'sagen' mean?\n (1) 'to say'\n (2) 'to hear'\n",
    "What does 'geben' mean?\n (1) 'to take'\n (2) 'to give'\n",
]
# admin_name = input("please enter the examinar name")
# cadidate_name = input("Please enter your name: ").title()
questions = [
     admin_Question(question_prompts[0], "1"),
     admin_Question(question_prompts[1], "2"),
    admin_Question(question_prompts[2], "1"),
    admin_Question(question_prompts[3], "1"),
    admin_Question(question_prompts[4], "2")
              ]
def run_quiz_easy(questions):
     score = 0
     for question in questions:
          answer = input(question.prompt)
          if answer == question.answer:
               score += 1
     print("\n, you scored {0} out of {1}.".format( score, len(questions)))

