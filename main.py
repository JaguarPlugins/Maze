import pygame

WIDTH = 800
HEIGHT = 600

mazeNumber = [[0,0,1,1,0,0],
        [1,0,1,0,0,1],
        [1,0,1,0,1,1],
        [1,0,0,0,0,1],
        [1,1,1,1,0,1]]

def genTileList (numberList):

    y = 0
    output = []
    for row in numberList:
        line = []
        x = 0
        for solid in row:
            x += 1
            line.append(Tile(x, y, solid))
        output.append(line)

    return output

class Tile:

    def __init__(self, x, y, solid):
        self.x = x
        self.y = y
        if solid == 1:
            self.solid = True
        elif solid == 0:
            self.solid = False
        elif isinstance(solid, bool):
            self.solid = solid

    def render(self, screen, tileWidth, tileHeight):

        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(self.x * (WIDTH/tileWidth), self.y * (HEIGHT/tileHeight), 20, 20))
        pygame.display.flip()

if __name__ == '__main__':

    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Maze Test")

    maze = genTileList(mazeNumber)

    print(maze)

    for section in maze:
        for tile in section:
            tile.render(screen, 6, 5)

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


