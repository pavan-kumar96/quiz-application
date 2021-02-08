from Question import Question
from zauto import admin_Question, questions,question_prompts


class User:
    
    def __init__(self,name,id):
        self.name=name
        self.id=id


class super_user(User,Question):

    def __init__(self,name,e_id):
        self.name=name
        self.e_id=e_id
        super().__init__(self.name,self.e_id)
        Question.__init__(self)
    
    def __repr__(self):
        return self.name + " " +  str(self.e_id)

    def addQuestion(self,topic_name,difficulty_level):
        Question._addQuestion(self,topic_name,difficulty_level)
        
    def displayAllQuestions(self):
        Question._displayAllQuestions(self)



class Candidate(User):

    def __init__(self,name,s_id):
        self.name=name
        self.s_id=s_id
        super().__init__(name,s_id)

    def __repr__(self):
        return self.name + " " +  str(self.s_id)

    def viewTopics(self):
        Question.viewTopics(self)
        
    def run_test(self):
        Question.run_test()
        
