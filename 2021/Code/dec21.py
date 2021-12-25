# Part 1:
def part1(players):
    points = [0,0]
    dice = 2; turns = 3
    nr = 0; next = {0:1, 1:0}
    no_winner = True
    while no_winner:
        players[nr] += dice*3
        players[nr] = (players[nr]-1)%10 +1
        points[nr] += players[nr]
        if points[nr] >= 1000:
            no_winner = False
        else:
            dice += 3
            turns += 3
            if turns > 100:
                dice -= 100
        nr = next[nr]
    print(turns * points[nr])

# Part 2:
class DiracDice:
    def __init__(self):
        self.possible_wins = {}

    def play(self, players, points, nr):
        # if nr=0: 1-nr=1, if nr=1: 1-nr=0
        if points[1-nr] >= 21:
            return [nr, 1-nr]
        
        elif f'{players}, {points}, {nr}' in self.possible_wins:
            return self.possible_wins[f'{players}, {points}, {nr}']

        total_wins = [0,0]
        for dice1 in [1,2,3]:
            for dice2 in [1,2,3]:
                for dice3 in [1,2,3]:
                    temp_player = (dice1+dice2+dice3+players[nr] - 1)%10 + 1
                    temp_points = points[nr] + temp_player
                    new_players = players.copy()
                    new_players[nr] = temp_player
                    new_points = points.copy()
                    new_points[nr] = temp_points
                    winner = self.play(new_players, new_points, 1-nr)
                    total_wins[0] += winner[0]
                    total_wins[1] += winner[1]
        self.possible_wins[f'{players}, {points}, {nr}'] = total_wins
        return total_wins

    def run(self, player1, player2):
        print(self.play([player1, player2], [0,0], 0))


def part2(players):
    DiracDice().run(*players)


if __name__ == '__main__':
    players_test = [4,8]    # test
    players_real = [6,8]    # real
    part1(players_test)
    part1(players_real)
    part2(players_test)
    part2(players_real)
