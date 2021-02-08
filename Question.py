class Question:
    
    prompt=[]
    choices=[]
    answers=[]
    category =[]
    difficulty=[]

    def __init__(self,prompt=[],choices=[],answers=[],category=[],difficulty=[]):
        self.prompt=prompt
        self.choices = choices
        self.answers=answers
        self.category = category
        self.difficulty = difficulty
        
    
    def _addQuestion(self,category,difficulty):

        statement=input("Your question Please: ")
        self.prompt.append(statement)
        Question.prompt.append(statement)
        self.category.append(category)
        Question.category.append(category)
        self.difficulty.append(difficulty)
        Question.difficulty.append(difficulty)

        l1=[]
        for i in range(4):
            l1.append(input("Enter option no. "+str((i+1))+"  "))
        self.choices.append(l1)
        Question.choices.append(l1)

        ans=input("Which is the correct option (1 0r 2 0r 3 0r 4 ? ")
        self.answers.append(int(ans))
        Question.answers.append(int(ans))
        
        
    def _displayAllQuestions(self):
        
        print("Total number of questions are: ",len(self.prompt))
        print("\n")
        for i in range(len(self.prompt)):
            print("Ques. "+str(i+1)+self.prompt[i])
            for j in range(len(self.choices[i])):
                print(str(j+1)+")"+str(self.choices[i][j]))
            print("\n")
            
            
    def viewTopics(self):
        a=set(Question.category)
        print(a)


    @classmethod
    def run_test(cls):

        score=0

        for statement in range(len(cls.prompt)):
            
            print("Topic: "+cls.category[statement])
            print(cls.prompt[statement])
            
            for i in range(len(cls.choices[statement])):
                print(str(i+1)+")"+str(cls.choices[statement][i]))
                
            print("Question level: ",cls.difficulty[statement])
            
            answer=int(input("Enter option number as answer: "))
            print("\n")

            if answer==cls.answers[statement]:
                score+=1
            print("Correct answer is ",cls.answers[statement])
        print("\n")
        print("You got",str(score),"/",str(len(cls.prompt)),"correct.")

        