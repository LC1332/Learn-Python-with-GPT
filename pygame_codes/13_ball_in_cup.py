import pymunk
import pymunk.pygame_util
import pygame
import pandas as pd

def setup_space():
    space = pymunk.Space()
    space.gravity = (0, -981)  # Gravity pointing downwards

    # Define the cup with three rigid walls
    walls = [
        pymunk.Segment(space.static_body, (50, 50), (50, 350), 5),
        pymunk.Segment(space.static_body, (50, 350), (150, 350), 5),
        pymunk.Segment(space.static_body, (150, 350), (150, 50), 5)
    ]
    for wall in walls:
        wall.elasticity = 0.5
        wall.friction = 0.5
        space.add(wall)
    
    return space

def add_ball(space, position):
    radius = 8
    mass = 1
    moment = pymunk.moment_for_circle(mass, 0, radius, (0, 0))
    body = pymunk.Body(mass, moment)
    body.position = position
    shape = pymunk.Circle(body, radius)
    shape.elasticity = 0  # 设置为完全非弹性碰撞
    shape.friction = 0.5
    space.add(body, shape)
    return body

def simulate(space, balls, highest_ball):
    for x in range(120):  # short time simulation
        space.step(0.02)
    balls.append(highest_ball)

def main():
    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    draw_options = pymunk.pygame_util.DrawOptions(screen)
    space = setup_space()
    balls = []
    highest_ball = 50  # initial height at the bottom of the cup

    for i in range(50):
        if i > 0:
            highest_ball = max(ball.position.y for ball in balls) + 40  # Update to new position above the highest ball
        ball = add_ball(space, (100, highest_ball))
        simulate(space, balls, ball)

    # Save the final position of each ball to Excel
    df = pd.DataFrame([(i, ball.position.y) for i, ball in enumerate(balls)], columns=['Ball Index', 'Height'])
    df.to_excel("ball_heights.xlsx", index=False)

    # Animation loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill((255, 255, 255))
        space.debug_draw(draw_options)
        pygame.display.flip()
        space.step(0.02)

    pygame.quit()

if __name__ == "__main__":
    main()
