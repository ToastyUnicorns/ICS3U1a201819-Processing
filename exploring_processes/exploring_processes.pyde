page = 0
mousepage = 0

ball_pos_x = 100
ball_pos_y = 100
ball_size_x = 200
ball_size_y = 200
ball_speed_x = 10
ball_speed_y = 14

x = 0 

text_size = 36
rotation = 0
rotation_speed = 0.01
text_size_speed = .1
animate = False

def setup():
    global sat_img, back_img
    global tennis_img
    sat_img = loadImage("Stalin.jpg")
    back_img = loadImage("Soviet.jpg")
    tennis_img = loadImage("Tennis.jpg")
    tennis_img.resize(width, height)
    back_img.resize(width, height)
    fullScreen()
    frameRate(960)


def draw():
    global page
    global sat_img, back_img 
    global tennis_img
    global ball_pos_x, ball_pos_y
    global ball_size_x, ball_size_y, ball_speed_x, ball_speed_y

    global text_size 
    global rotation
    global text_size_speed
    global rotation_speed
    
    if page == 0:
        background(back_img)
        textAlign(CENTER, CENTER)
        translate(width/2, height/2)
        textSize(text_size)
        fill(255, 255, 255, 255-text_size/2)
        text("Communism Is Free", 0, 0)

    elif page == 1:
        if animate:
            rotation_speed += 0.01
        text_size_speed += 0.1
        text_size += text_size_speed
        rotation += rotation_speed
    
    
        textAlign(CENTER, CENTER)
        translate(width/2, height/2)
        rotate(rotation)
        textSize(text_size)
        fill(255, 255, 255, 255-text_size/2)
        text("Communism Is Free", 0, 0)

    elif page == 2:
        background(back_img)
        fill(255, 217, 0)
        image(sat_img, 0, 0)
    elif page == 3:
     background(tennis_img)
     ellipse(ball_pos_x, ball_pos_y, ball_size_x, ball_size_y)
    ball_pos_x += ball_speed_x
    ball_pos_y += ball_speed_y
    print(ball_pos_x, ball_pos_y)
    if ball_pos_x < ball_size_x/2 or ball_pos_x > width - ball_size_x/2:
        ball_speed_x *= -1
    elif ball_pos_y < ball_size_y/2 or ball_pos_y > height - ball_size_y/2:
            ball_speed_y *= -1

    elif page == 4:
        global x
    
        if x >= 1920:
            x = 0
        x += 5
    
        background(135, 206, 250)  # sky blue
    
        # cloud
        fill(193, 190, 186)
        noStroke()
        ellipse(x, height/2, 50, 50)
        ellipse(x+30, height/2, 50, 50)
        ellipse(x+10, height/2-20, 50, 50)
        # sun
        fill(253, 184, 19)
        ellipse(900, 50, 300, 300)
        
    elif page == 5:
        background(255, 217, 0)


def keyPressed():  # Triggers once per mouse-press
    global page
    page += 1
    if page == 6:
        page = 1
    global animate
    animate = not animate
