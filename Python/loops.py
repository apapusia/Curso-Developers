#loop en una lista
players = ['Altuve', 'Bregman', 'Correa', 'Gattis']

for player in players:
    print(player)

#en una tupla sería exactamnete igual
books = ('Altuve', 'Bregman', 'Correa', 'Gattis')

for book in books:
    print(book)

#en un diccionario puedo acceder a la clave y al valor de cada ele.

d_players={
    '2b':'Altuve',
    '3b':'Bregman',
    'ss':'Correa',
    'dh':'Gattis'
}

for position,d_player in d_players.items():
    print('Position:', position)
    print('Player name:', d_player)