score = 0
lives = 3

class Brick(object):

    def __init__(self, isShown, left, top, brickWidth, brickHeight):
        self.isShown = isShown
        self.left = left
        self.top = top
        self.brickWidth = brickWidth
        self.brickHeight = brickHeight

    def right(self):
        return self.left + self.brickWidth

    def bottom(self):
        return self.top + self.brickHeight

    def create(self):
        rect(self.left,self.top,self.brickWidth,self.brickHeight)

class Ball(object):

    def __init__(self, ballSize, x, y, xSpeed, ySpeed):
        self.ballSize = ballSize
        self.x = x
        self.y = y
        self.xSpeed = xSpeed
        self.ySpeed = ySpeed

    def create(self):
        ellipse(self.x,self.y,self.ballSize,self.ballSize)
        self.x += self.xSpeed
        self.y += self.ySpeed
        
class Game(object):
    
    def __init__(self, bricks, ball):
        self.bricks = bricks
        self.ball = ball
        
    def detectHit(self, ball, brick):
        global lives

        #Check ball on left and right of brick
        if ((ball.x > brick.left - (ball.ballSize/2) and ball.y > brick.top and ball.y < brick.bottom()) and 
        (ball.x < brick.right() - (ball.ballSize/2) and ball.y > brick.top and ball.y < brick.bottom())):
            brick.isShown = False
            ball.xSpeed = -ball.xSpeed
            print("brick left or right")
            
        # #Check ball on top and bottom of brick
        if ((ball.y > brick.top - (ball.ballSize/2) and ball.x > brick.left and ball.x < brick.right()) and 
        (ball.y < brick.bottom() - (ball.ballSize/2) and ball.x > brick.left and ball.y < brick.right())):
            brick.isShown = False
            ball.ySpeed = -ball.ySpeed
            print("brick top or bottom")
            
        # if ball.y < 15 and ball.x > 0 and ball.x < 200:
        #     ball.ySpeed = -ball.ySpeed
        # elif ball.y < 15 and ball.x > 200 and ball.x < 400:
        #     ball.ySpeed = -ball.ySpeed
        # elif ball.y < 15 and ball.x > 400 and ball.x < 600:
        #     ball.ySpeed = -ball.ySpeed
        # elif ball.y < 15 and ball.x > 600 and ball.x < 800:
        #     ball.ySpeed = -ball.ySpeed
        # elif ball.y < 15 and ball.x > 800 and ball.x < 1000:
        #     ball.ySpeed = -ball.ySpeed


        if ball.x > 985:
            ball.xSpeed = -ball.xSpeed
            print("right")
        elif ball.x < 15:
            ball.xSpeed = -ball.xSpeed
            print("left")
        
        if ball.y > 685 and ball.y < 710 and ball.x > mouseX - 75 and ball.x < mouseX + 75:
            ball.ySpeed = -ball.ySpeed
        elif ball.y < 15:
            ball.ySpeed = -ball.ySpeed

        # Score Counter
        if ball.y > 1500:
            if lives > 0:
                lives -= 1
                print(lives)
    
    

    def update(self):
        for brick in self.bricks:
            if brick.isShown == False:
                bricks.remove(brick)
            # print(brick)
        
    def draw(self):
        for brick in self.bricks:
            stroke(0,0,0)
            brick.create()
            self.detectHit(self.ball, brick)
            
        self.ball.create()
        
            

# Update state

# In setup()
# Create all game objects
# Place ball somewhere

def createGame():

    # Paddle
    rect(mouseX - 75, 700, 150, 20)

    stroke(0, 0, 0)
    strokeWeight(1)

    fill(0, 0, 0)

    fill(255, 255, 255)
    textSize(22)
    text("Score: " + str(score), 10, 790)
    text("Lives: " + str(lives), 910, 790)

    noStroke()
    fill(255, 255, 255)

def gameOver(x):
    background(0, 0, 0)
    textSize(100)
    text("G A M E  O V E R", 100, 200)
    textSize(100)
    text(x, 270, 400)
    textSize(40)
    text("Play Again?", 400, 600)

def setup():
    global game
    global bricks
    global ball

    size(1000, 800)
    background(255, 255, 255)
    createGame()

    ball = Ball(30, 500, 350, 10, 10)

    brick1 = Brick(True,0,0,200,50)
    brick2 = Brick(True,200,0,200,50)
    brick3 = Brick(True,400,0,200,50)
    brick4 = Brick(True,600,0,200,50)
    brick5 = Brick(True,800,0,200,50)
    
    brick6 = Brick(True,0,50,200,50)
    brick7 = Brick(True,200,50,200,50)
    brick8 = Brick(True,400,50,200,50)
    brick9 = Brick(True,600,50,200,50)
    brick10 = Brick(True,800,50,200,50)
    
    brick11 = Brick(True,0,100,200,50)
    brick12 = Brick(True,200,100,200,50)
    brick13 = Brick(True,400,100,200,50)
    brick14 = Brick(True,600,100,200,50)
    brick15 = Brick(True,800,100,200,50)
    
    bricks =[brick1, brick2, brick3, brick4, brick5, brick6, brick7, brick8, brick9, brick10, brick11, brick12, brick13, brick14, brick15]
    
    game = Game(bricks, ball)

def draw():
    global score1
    global score2
    global lives
    global bricks
    global ball
    global name

    background(0, 0, 0)
    game.update()
    game.draw()
    createGame()
