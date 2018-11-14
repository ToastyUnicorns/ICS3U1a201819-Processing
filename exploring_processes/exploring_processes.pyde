page = 1

ball_pos_x = 100
ball_pos_y = 100
ball_size_x = 200
ball_size_y = 200
ball_speed_x = 10
ball_speed_y = 14


def setup():
    global sat_img, back_img
    sat_img = loadImage("Stalin.jpg")
    back_img = loadImage("Soviet.jpg")
    # back_img.resize(width, height)
    # size(1366, 768)
    fullScreen()
    frameRate(960)


def draw():
    global page
    global sat_img, back_img
    global ball_pos_x, ball_pos_y
    global ball_size_x, ball_size_y, ball_speed_x, ball_speed_y
    if page == 1:
        background(155, 3, 255)
        fill(255, 217, 0)
        ellipse(100, 100, 40, 40)
    elif page == 2:
        background(back_img)
        image(sat_img, 0, 0)
    elif page == 3:
        background(255)
        ellipse(ball_pos_x, ball_pos_y, ball_size_x, ball_size_y)
        ball_pos_x += ball_speed_x
        ball_pos_y += ball_speed_y
        print(ball_pos_x, ball_pos_y)
        if ball_pos_x < ball_size_x/2 or ball_pos_x > width - ball_size_x/2:
            ball_speed_x *= -1
        elif ball_pos_y < ball_size_y/2 or ball_pos_y > height - ball_size_y/2:
            ball_speed_y *= -1

    elif page == 4:
        background(255, 100, 3)
    elif page == 5:
        background(255, 217, 0)


def mousePressed():  # Triggers once per mouse-press
    global page
    page += 1
    if page == 6:
        page = 0
