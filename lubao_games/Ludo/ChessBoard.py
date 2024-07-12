import pygame

class ChessBoard:
    def __init__(self, screen_width, screen_height, grid_size, grid_num, color_type_num=4):
        if screen_width % grid_size != 0:
            screen_width -= screen_width % grid_size

        if screen_height % grid_size != 0:
            screen_height -= screen_height % grid_size
        
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.grid_size = grid_size
        self.grid_num = grid_num
        self.color_type_num = color_type_num
        self.colors = [(255, 0, 0), (0, 255, 0), (255, 255, 0), (0, 0, 255),
                       (255, 0, 255), (0, 255, 255), (255, 192, 203), (255, 255, 255)]
        self.colors = self.colors[:color_type_num]
        
        self.images = []
        self.generate_images()

        self.grid_centers = []

        self.render()

    def get_center(self, index):
        index = min( max(index, 0) , len(self.grid_centers)-1 )
        return self.grid_centers[index]

    def generate_images(self):
        for i in range(1, self.grid_num + 1):
            color = self.colors[(i - 1) % self.color_type_num]
            image = pygame.Surface((400, 400))
            image.fill(color)
            font = pygame.font.Font(None, 300)
            text = font.render(str(i), True, (0, 0, 0))
            text_rect = text.get_rect(center=(200, 200))
            image.blit(text, text_rect)
            image = pygame.transform.scale(image, (self.grid_size, self.grid_size))
            self.images.append(image)

    def render(self, screen = None):
        grid_count_x = self.screen_width // self.grid_size
        grid_count_y = self.screen_height // self.grid_size
        max_grids = grid_count_x * 2 + grid_count_y * 2 - 4

        grids_to_render = min(self.grid_num, max_grids)
        
        x, y = self.grid_size // 2, self.grid_size // 2
        
        directions = [(self.grid_size, 0), (0, self.grid_size), (-self.grid_size, 0), (0, -self.grid_size)]
        direction_index = 0
        step_count = 1
        steps = 0
        for i in range(grids_to_render):
            if screen:
                screen.blit(self.images[i], (x - self.grid_size // 2, y - self.grid_size // 2))

            self.grid_centers.append((x, y))

            new_x = x + directions[direction_index][0] * step_count
            new_y = y + directions[direction_index][1] * step_count

            if new_x < 0 or new_x >= self.screen_width or new_y < 0 or new_y >= self.screen_height:
                direction_index = (direction_index + 1) % 4
                new_x = x + directions[direction_index][0] * step_count
                new_y = y + directions[direction_index][1] * step_count
            
            x = new_x
            y = new_y
            

            steps += 1


if __name__ == '__main__':
    # Pygame setup
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Chess Board')
    clock = pygame.time.Clock()

    # Create ChessBoard object
    chess_board = ChessBoard(800, 600, 100, 20)
    running = True
    while running:
        screen.fill((0, 0, 0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        chess_board.render(screen)
        
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
