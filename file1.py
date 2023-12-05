import chess
import chess.variant
import chess.engine

class BaroqueChessAgent:
    def __init__(self, color, max_depth=2):
        self.board = chess.Board()
        self.color = color
        self.max_depth = max_depth

    def evaluate_board(self):
        # Implement your evaluation function here
        # This is a simple evaluation function that counts the material difference
        score = 0
        for square in chess.SQUARES:
            piece = self.board.piece_at(square)
            if piece is not None:
                score += (piece.piece_type - 2) * (1 if piece.color == self.color else -1)

        return score

    def minimax(self, depth, alpha, beta, maximizing_player):
        if depth == 0 or self.board.is_game_over():
            return self.evaluate_board()

        legal_moves = list(self.board.legal_moves)
        if maximizing_player:
            max_eval = float('-inf')
            for move in legal_moves:
                self.board.push(move)
                eval = self.minimax(depth - 1, alpha, beta, False)
                self.board.pop()
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = float('inf')
            for move in legal_moves:
                self.board.push(move)
                eval = self.minimax(depth - 1, alpha, beta, True)
                self.board.pop()
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval

    def alpha_beta_pruning(self, depth, maximizing_player):
        best_move = None
        legal_moves = list(self.board.legal_moves)
        if maximizing_player:
            max_eval = float('-inf')
            for move in legal_moves:
                self.board.push(move)
                eval = self.minimax(depth - 1, float('-inf'), float('inf'), False)
                self.board.pop()
                if eval > max_eval:
                    max_eval = eval
                    best_move = move
        else:
            min_eval = float('inf')
            for move in legal_moves:
                self.board.push(move)
                eval = self.minimax(depth - 1, float('-inf'), float('inf'), True)
                self.board.pop()
                if eval < min_eval:
                    min_eval = eval
                    best_move = move

        return best_move

    def make_move(self):
        best_move = self.alpha_beta_pruning(self.max_depth, True)
        if best_move:
            self.board.push(best_move)

    def play(self):
        while not self.board.is_game_over():
            self.make_move()
            print(self.board)

        print("Game Over")
        print("Result:", self.board.result())

def play_tournament(agents, rounds=5):
    results = {}

    for i in range(rounds):
        for agent_name, agent in agents.items():
            print(f"Round {i + 1} - {agent_name}")
            agent.play()
            result = agent.board.result()
            if agent_name not in results:
                results[agent_name] = 0
            if result == "1-0":
                results[agent_name] += 1
            elif result == "0-1":
                results[agent_name] -= 1

    print("\nTournament Results:")
    for agent_name, score in results.items():
        print(f"{agent_name}: {score} points")

if __name__ == "__main__":
    agents = {
        "Srikanth": BaroqueChessAgent(chess.WHITE, max_depth=3),
        "Sridhar": BaroqueChessAgent(chess.BLACK, max_depth=3),
        # Add more agents as needed
    }

    play_tournament(agents)