import pygame
import sys
import time

# import tictactoe as ttt
import min_max_alpha_beta as MinMaxTicTacToe


pygame.init()
size = width, height = 800, 400

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

screen = pygame.display.set_mode(size)

mediumFont = pygame.font.Font("OpenSans-Regular.ttf", 28)
largeFont = pygame.font.Font("OpenSans-Regular.ttf", 40)
moveFont = pygame.font.Font("OpenSans-Regular.ttf", 60)

# Initialize flags or states
in_game = False
initial_state_sel = None
user = None
ai_turn = False
machine_vs_machine = False
game_over = False
sel_algorithm = None
sel_initial_player = None 

initial_state = [[None,  None, None],
                [ None,  None, None],
                [ None, None, None]]

aux_board = [[None,  None, None],
                [ None,  None, None],
                [ None, None, None]]

minMaxTicTacToe = MinMaxTicTacToe.TicTacToe(initial_state)
board = minMaxTicTacToe.getInitialState()

n_play = 1

# Button properties
button_width, button_height = 300, 50
button_spacing = 20

againButton = pygame.Rect((width - button_width) / 2, height - 65, button_width, button_height)
again = mediumFont.render("Play Again", True, black)
againRect = again.get_rect()
againRect.center = againButton.center

ssButton = pygame.Rect((width - button_width * 2 - button_spacing) / 2 + button_width + button_spacing, height - 65, button_width, button_height)
state = mediumFont.render("Choose Initial State", True, black)
stateRect = state.get_rect()
stateRect.center = ssButton.center

playGAButton = pygame.Rect((width - button_width * 2 - button_spacing) / 2, height - 65, button_width, button_height)
playGA = mediumFont.render("Change Algorithm", True, black)
playGARect = playGA.get_rect()
playGARect.center = playGAButton.center



resStateButton = pygame.Rect((width - button_width) // 2, 100 + 3 * (button_height + button_spacing), button_width, button_height)
resetState= mediumFont.render("Reset Initial State", True, black)
resetStateRect = resetState.get_rect()
resetStateRect.center = resStateButton.center

playXButton = pygame.Rect((width - button_width) // 2, 100, button_width, button_height)
playX = mediumFont.render("Play as X", True, black)
playXRect = playX.get_rect()
playXRect.center = playXButton.center

playOButton = pygame.Rect((width - button_width) // 2, 100 + button_height + button_spacing, button_width, button_height)
playO = mediumFont.render("Play as O", True, black)
playORect = playO.get_rect()
playORect.center = playOButton.center

playMvMButton = pygame.Rect((width - button_width) // 2, 100 + 2 * (button_height + button_spacing), button_width, button_height)
playM = mediumFont.render("Machine VS Machine", True, black)
playMRect = playM.get_rect()
playMRect.center = playMvMButton.center


pruninAButton = pygame.Rect((width - button_width) // 2, 100, button_width, button_height)
playPru = mediumFont.render("Alpha Beta Pruning", True, black)
playPruRect = playPru.get_rect()
playPruRect.center = pruninAButton.center

playMinMaxButton = pygame.Rect((width - button_width) // 2, 100 + button_height + button_spacing, button_width, button_height)
playMM = mediumFont.render("No Pruning", True, black)
playMMRect = playMM.get_rect()
playMMRect.center = playMinMaxButton.center


changePlayerButton = pygame.Rect((width - button_width) // 2, 100 + 3 * (button_height + button_spacing), button_width, button_height)
changePlayer = mediumFont.render("Change Player", True, black)
changePlayerMRect = changePlayer.get_rect()
changePlayerMRect.center = changePlayerButton.center


# ---------------------------------

playerXFisrt = pygame.Rect((width - button_width) // 2, 100, button_width, button_height)
playerX = mediumFont.render("X Starts", True, black)
playerXRect = playerX.get_rect()
playerXRect.center = playerXFisrt.center

playerOFisrt = pygame.Rect((width - button_width) // 2, 100 + button_height + button_spacing, button_width, button_height)
playerO = mediumFont.render("O Starts", True, black)
playerORect = playerO.get_rect()
playerORect.center = playerOFisrt.center




while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:  # Check for mouse button release
            if event.button == 1:  # Left mouse button
                mouse = pygame.mouse.get_pos()
                
                if(sel_initial_player is None):
                    if playerXFisrt.collidepoint(mouse):
                        sel_initial_player = 'X'
                        minMaxTicTacToe.initial_player = 'X'
                    elif playerOFisrt.collidepoint(mouse):
                        sel_initial_player = 'O'
                        minMaxTicTacToe.initial_player = 'O'
                elif(sel_algorithm is None):
                    if pruninAButton.collidepoint(mouse):
                        sel_algorithm = 'pruning'
                    elif playMinMaxButton.collidepoint(mouse):
                        sel_algorithm = 'minmax'
                    elif changePlayerButton.collidepoint(mouse):
                        sel_initial_player = None
                        initial_state_sel = None
                        board = minMaxTicTacToe.getInitialState()
                elif initial_state_sel is None:
                    if ssButton.collidepoint(mouse):
                        initial_state_sel = True
                        in_game = True
                    elif playGAButton.collidepoint(mouse):
                        sel_algorithm = None
                        initial_state_sel = None
                        board = minMaxTicTacToe.getInitialState()
                elif in_game:
                    # Handle game-specific button clicks here
        
                    if(user is None):
                        if playXButton.collidepoint(mouse):
                            time.sleep(0.2)
                            user = minMaxTicTacToe.X
                            minMaxTicTacToe.playerMode = minMaxTicTacToe.X
                        elif playOButton.collidepoint(mouse):
                            time.sleep(0.2)
                            user = minMaxTicTacToe.O
                            minMaxTicTacToe.playerMode = minMaxTicTacToe.O
                        elif playMvMButton.collidepoint(mouse):
                            time.sleep(0.2)
                            machine_vs_machine = True
                            user = minMaxTicTacToe.X
                        elif resStateButton.collidepoint(mouse):
                            time.sleep(0.2)
                            initial_state_sel = None
                            board = minMaxTicTacToe.getInitialState()
                            #board = aux_board
                    if againButton.collidepoint(mouse) and game_over:
                        user = None
                        #board = minMaxTicTacToe.getInitialState()
                        board = aux_board
                        ai_turn = False
                        machine_vs_machine = False
                        game_over = False
                        n_play = 1
                        minMaxTicTacToe.states_visited = 0
                    # Handle other in-game button clicks here
                else:
                    # Handle other button clicks when not in the game or initial state selection
                    print('ok')

    screen.fill(black)

    if(sel_initial_player == None):
        # Draw title
        title = mediumFont.render("Who goes first", True, white)
        titleRect = title.get_rect()
        titleRect.center = ((width / 2), 50)
        screen.blit(title, titleRect)

        pygame.draw.rect(screen, white, playerXFisrt)
        screen.blit(playerX, playerXRect)

        pygame.draw.rect(screen, white, playerOFisrt)
        screen.blit(playerO, playerORect)    

    elif sel_algorithm == None:
        # Draw title
        title = mediumFont.render("Select the MinMax version", True, white)
        titleRect = title.get_rect()
        titleRect.center = ((width / 2), 50)
        screen.blit(title, titleRect)

        pygame.draw.rect(screen, white, pruninAButton)
        screen.blit(playPru, playPruRect)

        pygame.draw.rect(screen, white, playMinMaxButton)
        screen.blit(playMM, playMMRect)

        pygame.draw.rect(screen, white, changePlayerButton)
        screen.blit(changePlayer, changePlayerMRect)

    elif initial_state_sel is None and sel_algorithm != None and sel_initial_player != None:
        # Draw title
        if(sel_algorithm == 'pruning'):
            title = mediumFont.render("Play Tic-Tac-Toe (MinMax with Alpha-Beta Pruning)", True, white)
        elif sel_algorithm == 'minmax':
            title = mediumFont.render("Play Tic-Tac-Toe (MinMax without Pruning)", True, white)
        titleRect = title.get_rect()
        titleRect.center = ((width / 2), 50)

        pygame.draw.rect(screen, white, ssButton)
        screen.blit(state, stateRect)

        pygame.draw.rect(screen, white, playGAButton)
        screen.blit(playGA, playGARect)

        # Draw game board
        tile_size = 80
        tile_origin = (width / 2 - (1.5 * tile_size),
                    height / 2 - (1.5 * tile_size))
        tiles = []
        for i in range(3):
            row = []
            for j in range(3):
                rect = pygame.Rect(
                    tile_origin[0] + j * tile_size,
                    tile_origin[1] + i * tile_size,
                    tile_size, tile_size
                )
                pygame.draw.rect(screen, white, rect, 3)

                if board[i][j] != minMaxTicTacToe.EMPTY:
                    move = moveFont.render(board[i][j], True, white)
                    moveRect = move.get_rect()
                    moveRect.center = rect.center
                    screen.blit(move, moveRect)
                row.append(rect)
            tiles.append(row)

        # let the user select the state
        click_b, _, _ = pygame.mouse.get_pressed()
        if click_b == 1:
            mouse = pygame.mouse.get_pos()
            for i in range(3):
                for j in range(3):
                    if (board[i][j] == minMaxTicTacToe.EMPTY and tiles[i][j].collidepoint(mouse)):
                        board = minMaxTicTacToe.result(board, (i, j))

        aux_board = board
        screen.blit(title, titleRect)


    elif in_game:
        # Game logic and rendering here
        # Make sure game_over and other game-related flags are correctly updated
        #if(initial_state_sel == True):
        if user is None:

            # Draw title
            if(sel_algorithm == 'pruning'):
                title = mediumFont.render("Play Tic-Tac-Toe (MinMax with Alpha-Beta Pruning)", True, white)
            elif sel_algorithm == 'minmax':
                title = mediumFont.render("Play Tic-Tac-Toe (MinMax without Pruning)", True, white)
            titleRect = title.get_rect()
            titleRect.center = ((width / 2), 50)
            screen.blit(title, titleRect)

            # Draw buttons
            pygame.draw.rect(screen, white, playXButton)
            screen.blit(playX, playXRect)

            pygame.draw.rect(screen, white, playOButton)
            screen.blit(playO, playORect)

            pygame.draw.rect(screen, white, playMvMButton)
            screen.blit(playM, playMRect)

            pygame.draw.rect(screen, white, resStateButton)
            screen.blit(resetState, resetStateRect)

        else:

            # Draw game board
            tile_size = 80
            tile_origin = (width / 2 - (1.5 * tile_size),
                        height / 2 - (1.5 * tile_size))
            tiles = []
            for i in range(3):
                row = []
                for j in range(3):
                    rect = pygame.Rect(
                        tile_origin[0] + j * tile_size,
                        tile_origin[1] + i * tile_size,
                        tile_size, tile_size
                    )
                    pygame.draw.rect(screen, white, rect, 3)

                    if board[i][j] != minMaxTicTacToe.EMPTY:
                        move = moveFont.render(board[i][j], True, white)
                        moveRect = move.get_rect()
                        moveRect.center = rect.center
                        screen.blit(move, moveRect)
                    row.append(rect)
                tiles.append(row)

            game_over = minMaxTicTacToe.terminal(board)
            player = minMaxTicTacToe.player(board)

            if(machine_vs_machine == True):
                
                if game_over:
                    winner = minMaxTicTacToe.winner(board)
                    if winner is None:
                        title = f"Game Over: Tie."
                    else:
                        title = f"Game Over: {winner} wins."
                elif user == player:
                    title = f"Play as {user}"
                else:
                    title = f"Computer thinking..."
                title = mediumFont.render(title, True, white)
                titleRect = title.get_rect()
                titleRect.center = ((width / 2), 30)
                screen.blit(title, titleRect)

                time.sleep(0.8)
                if(sel_algorithm == 'pruning'):
                    move = minMaxTicTacToe.minimax(board)
                elif sel_algorithm == 'minmax':
                    move = minMaxTicTacToe.minimax_nopruning(board)

                nodesText = mediumFont.render(f"Nodes: {minMaxTicTacToe.get_states_visited()}", True, white)
                nodesTextRect = nodesText.get_rect()
                nodesTextRect.topleft = (10, 50)
                screen.blit(nodesText, nodesTextRect)
                #if(n_play < 10 and game_over == False):
                #    print(f'Jogada {n_play} / Número de estados visitados: {minMaxTicTacToe.get_states_visited()}')
                #    n_play = n_play+1
                if(move != None):
                    board = minMaxTicTacToe.result(board, move)
                            
                if(player == minMaxTicTacToe.O):
                    user = minMaxTicTacToe.X
                else:
                    user = minMaxTicTacToe.O

            else:# Show title
                if game_over:
                    winner = minMaxTicTacToe.winner(board)
                    if winner is None:
                        title = f"Game Over: Tie."
                    else:
                        title = f"Game Over: {winner} wins."
                elif user == player:
                    title = f"Play as {user}"
                else:
                    title = f"Computer thinking..."
                title = mediumFont.render(title, True, white)
                titleRect = title.get_rect()
                titleRect.center = ((width / 2), 30)
                screen.blit(title, titleRect)


                # Check for AI move

                if user != player and not game_over:
                    if ai_turn:
                        time.sleep(0.5)
                        if(sel_algorithm == 'pruning'):
                            move = minMaxTicTacToe.minimax(board)
                        elif sel_algorithm == 'minmax':
                            move = minMaxTicTacToe.minimax_nopruning(board)
                        board = minMaxTicTacToe.result(board, move)

                        ai_turn = False
                    else:
                        ai_turn = True


                nodesText = mediumFont.render(f"Nodes: {minMaxTicTacToe.get_states_visited()}", True, white)
                nodesTextRect = nodesText.get_rect()
                nodesTextRect.topleft = (10, 50)
                screen.blit(nodesText, nodesTextRect)

                # Check for a user move
                click, _, _ = pygame.mouse.get_pressed()
                if click == 1 and user == player and not game_over:
                    mouse = pygame.mouse.get_pos()
                    for i in range(3):
                        for j in range(3):
                            if (board[i][j] == minMaxTicTacToe.EMPTY and tiles[i][j].collidepoint(mouse)):
                                board = minMaxTicTacToe.result(board, (i, j))

            if game_over:

                pygame.draw.rect(screen, white, againButton)
                screen.blit(again, againRect)


    pygame.display.flip()