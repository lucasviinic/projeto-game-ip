import sqlite3


connection = sqlite3.connect('database.db')
cur = connection.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS players (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nick TEXT NOT NULL,
        score INTEGER NOT NULL
    );
''')

def check_if_player_exists(nick: str):
    ''' 
        Retorna True se o nick já existe no banco de dados

        Parâmetros:
            nick: nick do usuário
    '''

    cur.execute("SELECT * FROM players WHERE nick = ?", (nick,))

    player = cur.fetchone()

    if player:
        return True
    else:
        return False

def insert_player(nick: str, score: int):
    '''
        Insere um novo usuário na tabela

        Parâmetros:
            nick: nick do usuário
            score: score do usuário
    '''

    if check_if_player_exists(nick):
        return False
    
    cur.execute("INSERT INTO players (nick, score) VALUES (?, ?)", (nick, score))
    connection.commit()

    return True

def update_score(nick: str, score: int):
    '''
        Atualiza o score de um usuário

        Parâmetros:
            nick: nick do usuário
            score: score do usuário
    '''

    cur.execute('''
        UPDATE players SET score = ? WHERE nick = ?
    ''', (score, nick))

    connection.commit()
    return True

def get_players_sorted_by_score():
    '''
        Retorna todos os usuários ordenados por score

        Retorno:
            Lista de tuplas com os dados dos usuários2
    '''

    cur.execute('''
        SELECT * FROM players ORDER BY score DESC
    ''')

    players = cur.fetchall()
    return players