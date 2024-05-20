from turtle import Turtle
LOCATION = (0,300)
POSITION = 'center'
FONT_CHAR = ('Courier',18,'bold')
PRINT_XAXIS = 100

class Score_Track(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.guess = []
        self.ht()
        self.penup()
        self.color('white')
        self.goto(LOCATION)
        self.update_score()

        self.text_turtle = Turtle()
        self.text_turtle.ht()
        self.text_turtle.penup()
        self.text_turtle.color('white')
        self.puzzle_display()

        

    def draw_sep(self):
        self.text_turtle.goto(x=0, y= -170)
        self.text_turtle.pendown()
        self.text_turtle.left(90)
        self.text_turtle.fd(350)
        self.text_turtle.penup()
        


    def update_score(self):
        self.write(f"Your Score: {self.score}",align=POSITION,font=FONT_CHAR)



    def score_updater(self):
        self.score += 1
        self.clear()
        self.update_score()



    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!",align=POSITION,font=FONT_CHAR)



    def puzzle_display(self):
        self.draw_sep()
        self.text_turtle.goto(-260,260)
        self.text_turtle.write("PUZZLE",align=POSITION,font=FONT_CHAR)
        self.text_turtle.goto(210,260)
        self.text_turtle.write("WORDS FOUND",align=POSITION,font=FONT_CHAR)



    def word_tracker(self,word):
        self.guess.append(word)



    def already_guessed(self, input_word):
        return self.screen.textinput("Already guessed", prompt=f"You have already guessed '{input_word}'. Guess another word: ").lower()
    
        

    def word_check(self,word):
        if self.guess.count(word)>1:
            sec_word = self.already_guessed(word)
            print(f"The sec word is {sec_word}")
            
            if sec_word in self.guess:
                flag = True
                print(f"If flag {flag}")
                while flag:

                    final_word = self.already_guessed(sec_word)
                    print(f"The final word is {final_word}")
                    if final_word not in self.guess:
                        flag = False
                        self.word_tracker(final_word)
                        self.score_updater()
                        print(self.guess)
            else:
                self.word_tracker(sec_word)
                self.score_updater()
                print(self.guess)
        else:
            self.score_updater()
            self.print_word(word,self.score)
            print(self.guess)


    
    def print_word(self,word,score):
        target_yaxis = PRINT_XAXIS *2
        pointer = 50
        target_yaxis -= pointer * score 

        self.text_turtle.goto(PRINT_XAXIS,target_yaxis)
        self.text_turtle.write(f"{score}. {word}",align=POSITION,font=FONT_CHAR)
      




        
    










    


    
