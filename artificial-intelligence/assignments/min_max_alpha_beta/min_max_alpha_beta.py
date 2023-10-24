"""
Tic Tac Toe Player using Min-Max Alpha Beta pruning
"""

import math
import json

class TicTacToe:
    
    def __init__(self, initial_state):
        self.X = "X"
        self.O = "O"
        self.playerMode = None
        self.EMPTY = None
        self.states_visited = 0
        self.initial_player = None
        self.all_states = []

        if(initial_state == None):
           self.initial_state = [[self.EMPTY, self.EMPTY, self.EMPTY],
                                [self.EMPTY, self.EMPTY, self.EMPTY],
                                [self.EMPTY, self.EMPTY, self.EMPTY]]
        
        else:
            self.initial_state = initial_state

    def get_states_visited(self):
            return self.states_visited
    
    def getInitialState(self):
        """
        Returns the initial state of the tic tac toe board
        """

        return self.initial_state


    def player(self, board):
        """
        Returns player who has the next turn on a board.
        """
        cnt_X = 0
        cnt_o = 0
        # Count X and O's on the game board
        for i in range(3):
            for j in range(3): 
                if board[i][j] == self.X:
                    cnt_X += 1
                elif board[i][j] == self.O:
                    cnt_o += 1

        if(self.initial_player == self.X):
            if cnt_X == cnt_o:
                return self.X
            elif cnt_X > cnt_o:
                return self.O
            else:
                return self.X
        elif(self.initial_player == self.O):
            if cnt_X == cnt_o:
                return self.O
            elif cnt_o > cnt_X:
                return self.X
            else:
                return self.O



    def actions(self, board):

        actions = []
        for i in range(3):
            for j in range(3):
                if board[i][j] == None:
                    actions.append((i, j))
        return actions


    def result(self, board, action):

        if action not in self.actions(board):
            raise Exception("Invalid Action")
        
        new_board = [row[:] for row in board]

        new_board[action[0]][action[1]] = self.player(board)

        return new_board


    def winner(self, board):
        """
        Retorna o vencedor do jogo, se houver.
        """
        # Return tictactoe winner if there is one
        for i in range(3):
            # Check rows
            if board[i][0] == board[i][1] == board[i][2]:
                if board[i][0] != None:
                    return board[i][0]
            
            # Check columns
            if board[0][i] == board[1][i] == board[2][i]:
                if board[0][i] != None:
                    return board[0][i]

        # Check Diagonals
        if board[0][0] == board[1][1] == board[2][2]:
            if board[0][0] != None:
                return board[0][0]
        if board[0][2] == board[1][1] == board[2][0]:
            if board[0][2] != None:
                return board[0][2]
        
        return None


    def terminal(self, board):
        """
        Retorna True se o jogo terminar, False caso contrário.
        """

        if self.winner(board) != None:
            return True
        else:
            # Check if the board is full
            for i in range(3):
                for j in range(3):
                    if board[i][j] == None:
                        return False
            return True

    def utility(self, board):
        """
        Retorna 1 se X ganhou o jogo, -1 se O ganhou, 0 caso contrário.
        """
        if self.winner(board) == self.X:
            return 1
        elif self.winner(board) == self.O:
            return -1
        else:
            return 0


    def max_value(self, board, alpha, beta):
        """
         Retorna o valor máximo para o jogador atual no tabuleiro
         usando poda alfa-beta.
        """
        if(self.initial_player == 'X'):
            self.states_visited += 1 

        if self.terminal(board):
            return self.utility(board)
        v = -math.inf

        actions =  self.actions(board)

        for action in actions:

            v = max(v, self.min_value(self.result(board, action), alpha, beta))

            if v >= beta:
                break

            alpha = max(alpha, v)
        return v

    def min_value(self, board, alpha, beta):
        """
         Retorna o valor mínimo do jogador atual no tabuleiro
         usando poda alfa-beta.
        """
        if(self.initial_player == 'O'):
            self.states_visited += 1 

        if self.terminal(board):
            return self.utility(board)
        v = math.inf
        
        actions =  self.actions(board)

        for action in actions:

            v = min(v, self.max_value(self.result(board, action), alpha, beta))

            if v <= alpha:
                break

            beta = min(beta, v)
        return v

    def minimax(self, board):
        """
        Retorna a ação ideal para o jogador atual no tabuleiro
        usando o algoritmo minimax com poda alfa-beta.
        """
        if self.terminal(board):
            return None
   
        if self.player(board) == self.X:
            v = -math.inf
            opt_action = None
            actions =  self.actions(board)
            for action in actions:
                new_value = self.min_value(self.result(board, action), -math.inf, math.inf)
                if new_value > v:
                    v = new_value
                    opt_action = action
                if(self.utility(self.result(board, action)) == 1) :
                     return action
            return opt_action
        
        elif self.player(board) == self.O:
            v = math.inf
            opt_action = None
            for action in self.actions(board):
                new_value = self.max_value(self.result(board, action), -math.inf, math.inf)
                if new_value < v:
                    v = new_value
                    opt_action = action
                if(self.utility(self.result(board, action)) == -1) :
                     return action
            return opt_action
        



    def max_value_nopruning(self, board):
        """
        Retorna o valor máximo para o jogador atual no tabuleiro
        """
        if(self.initial_player == 'X'):
            self.states_visited += 1 
  
        if self.terminal(board):
            return self.utility(board)
        
        v = -math.inf

        for action in self.actions(board):

            v = max(v, self.min_value_nopruning(self.result(board, action)))
            #if(self.terminal(self.result(board, action)) == False):
            #    self.states.append(self.result(board, action))
        return v

    def min_value_nopruning(self, board):
        """
        Retorna o valor mínimo para o jogador atual no tabuleiro
        """
        if(self.initial_player == 'O'):
            self.states_visited += 1 

        if self.terminal(board):
            return self.utility(board)
        
        v = math.inf

        for action in self.actions(board):
        
            v = min(v, self.max_value_nopruning(self.result(board, action)))
            #if(self.terminal(self.result(board, action)) == False):
            #    self.states.append(self.result(board, action))
        return v

    def minimax_nopruning(self, board):
        """
        Returns the optimal action for the current player on the board 
        using the minimax algorithm with alpha-beta pruning.
        """
        if self.terminal(board):
            return None
   
        if self.player(board) == self.X:
            v = -math.inf
            opt_action = None
            #count_max = 1
            for action in self.actions(board):
   
                new_value = self.min_value_nopruning(self.result(board, action))
                if new_value > v:
                    v = new_value
                    opt_action = action
                if(self.utility(self.result(board, action)) == 1) :
                    return action
            return opt_action
        
        elif self.player(board) == self.O:
            v = math.inf
            opt_action = None
            #count_min = 1
            for action in self.actions(board):

                new_value = self.max_value_nopruning(self.result(board, action))
                if new_value < v:
                    v = new_value
                    opt_action = action
                if(self.utility(self.result(board, action)) == -1) :
                    return action               
            return opt_action
        

   