class Player:
    def __init__(self, window) -> None:
        self.window = window
        self.player_1 = True
        
    def player_status(self):
        if self.player_1:
            # print('self.player_1')
            return True
        else:
            return False
        
    def switch_player(self):
        if self.player_1:
            self.player_1 = False
            print('player_2 play the game:')
        else:
            self.player_1 = True
            print('player_1 player the game:')
