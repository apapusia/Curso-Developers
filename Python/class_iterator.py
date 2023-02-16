astros = [
  'Springer',
  'Bregman',
  'Altuve',
  'Correa',
  'Reddick',
  'Gonzalez',
  'McCann',
  'Davis',
  'Tucker'
]
class Lineup:
    def __init__(self, players):
        self.players=players
        self.last_player_index=(len(self.players)-1)
        
    def __iter__(self):
        self.n=0 #contador
        return self #tiene que dvolver algo
    
    def __next__(self):
        if self.n<self.last_player_index:
            player= self.players[self.n]
            self.n+=1
            return player
        elif self.n==self.last_player_index:#al llegar al final, se resetea el contador
            player= self.players[self.n]
            self.n=0
            return player

astros_lineup=Lineup(astros)
process=iter(astros_lineup)
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
        
        

