import pygame


class Cell:
    def __init__(self, row, col, value, CELL_SIZE):
        self.CELL_SIZE = CELL_SIZE

        # coords
        self.row = row
        self.col = col

        coords = self.getCellCoords()
        self.x = coords["x"]
        self.y = coords["y"]
        self.value = value

    def alive(self):
        return self.value == 1

    def killCell(self):
        self.value = 0

    def birthCell(self):
        self.value = 1

    def getCellCoords(self):
        return {"y": self.row * self.CELL_SIZE, "x": self.col * self.CELL_SIZE}


# grid class
class Grid:
    def __init__(self, screen, ROWS, COLS, CELL_SIZE):
        self.new_screen_height = ROWS * CELL_SIZE
        self.new_screen_width = COLS * CELL_SIZE
        self.screen = screen
        self.ROWS = ROWS
        self.COLS = COLS
        self.CELL_SIZE = CELL_SIZE

        # init cell 2D array
        self.cells = [[None for _ in range(self.ROWS)] for _ in range(self.COLS)]
        for r, row in enumerate(self.cells):
            for c, cell in enumerate(row):
                self.cells[r][c] = Cell(r, c, 0, self.CELL_SIZE)

    def drawGrid(self, includeGridLines=True):
        # draw cells first
        for row in self.cells:
            for cell in row:
                # draw black if cell dead, white if alive
                pygame.draw.rect(
                    self.screen,
                    (255, 255, 255) if cell.alive() else (0, 0, 0),
                    (cell.x, cell.y, self.CELL_SIZE, self.CELL_SIZE),
                )

        # draw grid lines
        # horizontal lines
        if includeGridLines:
            for y in range(self.ROWS + 1):
                pygame.draw.line(
                    self.screen,
                    (255, 255, 255),
                    (0, y * self.CELL_SIZE),
                    (self.new_screen_width, y * self.CELL_SIZE),
                    1,
                )

            # vertical lines
            for x in range(self.COLS + 1):
                pygame.draw.line(
                    self.screen,
                    (255, 255, 255),
                    (x * self.CELL_SIZE, 0),
                    (x * self.CELL_SIZE, self.new_screen_height),
                    1,
                )

    def birthCellAt(self, row, col):
        self.cells[row][col].birthCell()

    def killCellAt(self, row, col):
        self.cells[row][col].killCell()

    def getCellNeighbors(self, cell):
        # get all 8 neighbors
        r = cell.row
        c = cell.col
        neighbors = []
        try:
            neighbors.append(self.cells[r - 1][c - 1])
            neighbors.append(self.cells[r - 1][c])
            neighbors.append(self.cells[r - 1][c + 1])
            neighbors.append(self.cells[r][c - 1])
            neighbors.append(self.cells[r][c + 1])
            neighbors.append(self.cells[r + 1][c - 1])
            neighbors.append(self.cells[r + 1][c])
            neighbors.append(self.cells[r + 1][c + 1])
        except:
            return neighbors

        return neighbors


# # #
# # #
# # #
