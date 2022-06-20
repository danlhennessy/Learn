

question_prompts = [
    "What color are Apples? \n (a) Red/Green \n(b) Purple\n(c) Orange \n\n",
    "What color are Bananas? \n (a) Teal \n(b) Magenta\n(c) Yellow \n\n",
    "What color are Strawberries? \n (a) Yellow \n(b) Red\n(c) Blue \n\n"                   
                    ]

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer
        
questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b")
    
]

questions22 = [
    Question("Test Question 1", "a"),
    Question("Test Question 2", "c"),
    Question("Test Question 3", "b")    
        
]

def test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score +=1
    print(f"Thanks for completeing this Quiz, your score is {score}!")
test(questions22)