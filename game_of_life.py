from Grid import Grid, Cell

import pygame

pygame.init()


# game of life rules:
# 1.Any live cell with fewer than two live neighbours dies, as if by underpopulation.
# 2.Any live cell with two or three live neighbours lives on to the next generation.
# 3.Any live cell with more than three live neighbours dies, as if by overpopulation.
# 4.Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.


def getNeighborsCount(neighbors):
    live = 0
    dead = 0
    for cell in neighbors:
        if cell.alive():
            live += 1
        else:
            dead += 1

    return live, dead


def getNextGenCells(cells):
    toLive = []
    toDie = []
    for row in cells:
        for cell in row:
            neighbors = grid.getCellNeighbors(cell)

            live, dead = getNeighborsCount(neighbors)
            if cell.alive():
                # 1.Any live cell with fewer than two live neighbours dies, as if by underpopulation.
                if live < 2:
                    toDie.append(cell)

                # 2.Any live cell with two or three live neighbours lives on to the next generation.
                elif live == 2 or live == 3:
                    toLive.append(cell)

                # 3.Any live cell with more than three live neighbours dies, as if by overpopulation.
                elif live > 3:
                    toDie.append(cell)

            else:
                # 4.Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
                if live == 3:
                    toLive.append(cell)

    return toLive, toDie


def loadStartingPosFromFile(filename):
    with open(filename, "r") as f:
        for r, line in enumerate(f):
            for c, char in enumerate(line):
                if char == "X":
                    grid.birthCellAt(r, c)


ROWS = 50
COLS = 50
CELL_SIZE = 16
SCREEN_WIDTH = ROWS * CELL_SIZE
SCREEN_HEIGHT = COLS * CELL_SIZE
FONT1 = pygame.font.SysFont("ariel", 50)


screen = pygame.display.set_mode((SCREEN_WIDTH + 1, SCREEN_HEIGHT + 1))
pygame.display.set_caption("Snake Game!")
clock = pygame.time.Clock()

grid = Grid(screen, ROWS, COLS, CELL_SIZE)

# CHOOSE PATTERN OR MAKE YOUR OWN
loadStartingPosFromFile("starting_position2.txt")
# SET SIMULATION SPEED (LOWER IS SLOWER)
FPS = 15


def main():
    generations = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        toLive, toDie = getNextGenCells(grid.cells)
        for cell in toLive:
            cell.birthCell()

        for cell in toDie:
            cell.killCell()

        # generation label
        score_lbl = FONT1.render(str(generations) + " Generations", True, (255, 0, 0))

        grid.drawGrid(False)
        screen.blit(score_lbl, (5, 0))
        pygame.display.update()
        clock.tick(FPS)

        generations += 1


if __name__ == "__main__":
    # start with
    main()
