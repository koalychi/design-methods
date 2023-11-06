SIZE = 8

class EventBus:
    def __init__(self):
        self.subscribers = {}

    def subscribe(self, event, callback):
        if event not in self.subscribers:
            self.subscribers[event] = []
        self.subscribers[event].append(callback)

    def publish(self, event, data=None):
        if event in self.subscribers:
            for callback in self.subscribers[event]:
                callback(data)


class UI:
    def __init__(self, event_bus, board):
        self.event_bus = event_bus
        self.board = board

    def output(self):
        print("Solution is:")

        for i in range(SIZE):
            for j in range(SIZE):
                print(self.board[i][j], end=" ")
            print()

    def no_solution(self):
        print("No solution found")


class SolveBoard:
    def __init__(self, event_bus, board):
        self.event_bus = event_bus
        self.board = board

    def is_safe_to_place(self, row, col):
        for i in range(col):
            if self.board[row][i] == 1:
                return False

        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False

        for i, j in zip(range(row, SIZE, 1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False

        return True

    def place_queens(self, col):
        if col >= SIZE:
            return True
      
        for i in range(SIZE):
            if self.is_safe_to_place(self.board, i, col):
                self.board[i][col] = 1

                if self.place_queens(self.board, col + 1):
                    return True

                self.board[i][col] = 0

        return False

    def solve(self):
      if self.place_queens(self.board, 0):
          self.event_bus.publish("board_processed")
      else:
          self.event_bus.publish("no_solution")
      

if __name__ == "__main__":
    event_bus = EventBus()
    board = [[0] * SIZE for _ in range(SIZE)]

    ui = UI(event_bus=event_bus, board=board)
    solve_board=SolveBoard(event_bus=event_bus, board=board)

    event_bus.subscribe("board_processed", ui.output)
    event_bus.subscribe("no_solution", ui.no_solution)

    solve_board.solve()

