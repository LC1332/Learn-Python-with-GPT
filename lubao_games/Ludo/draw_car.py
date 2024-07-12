import pygame
import os

def draw_car(surface):
    # Set up some drawing parameters
    car_color = (0, 0, 0)  # Black color for the car
    wheel_color = (0, 0, 0)  # Black color for the wheels
    line_width = 30  # Thickness of the lines

    # Draw the car body
    pygame.draw.line(surface, car_color, (100, 300), (300, 300), line_width)  # Bottom
    pygame.draw.line(surface, car_color, (100, 300), (100, 200), line_width)  # Left
    pygame.draw.line(surface, car_color, (100, 200), (300, 200), line_width)  # Top
    pygame.draw.line(surface, car_color, (300, 200), (300, 300), line_width)  # Right

    # Draw the car roof
    pygame.draw.line(surface, car_color, (150, 200), (250, 200), line_width)  # Roof

    # Draw the wheels
    pygame.draw.circle(surface, wheel_color, (150, 300), 40, line_width)  # Left wheel
    pygame.draw.circle(surface, wheel_color, (250, 300), 40, line_width)  # Right wheel

def create_car_image():
    # Initialize pygame
    pygame.init()

    # Create a surface with transparency (RGBA)
    car_surface = pygame.Surface((400, 400), pygame.SRCALPHA)

    # Fill the surface with transparent color
    car_surface.fill((0, 0, 0, 0))

    # Draw the car on the surface
    draw_car(car_surface)

    # Save the surface to a PNG file
    pygame.image.save(car_surface, "images/car.png")

def render_car_image():
    # Initialize pygame
    pygame.init()

    # Set up the display
    screen = pygame.display.set_mode((400, 400))
    pygame.display.set_caption('Car Image Render')

    # Load the car image
    car_image = pygame.image.load("images/car.png")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the background with white
        screen.fill((255, 255, 255))

        # Blit the car image onto the screen
        screen.blit(car_image, (0, 0))

        # Update the display
        pygame.display.flip()

    pygame.quit()

# Ensure the images directory exists
if not os.path.exists("images"):
    os.makedirs("images")

# Create the car image and render it
create_car_image()
render_car_image()
