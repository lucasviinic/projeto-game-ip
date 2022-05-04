from manager import *
import unittest


class TestManager(unittest.TestCase):

    #Cria tabela teste
    def setUp(self):
        cur.execute("DROP TABLE IF EXISTS players")
        create_table()
        connection.commit()

    def test_insert_player(self):
        self.assertTrue(insert_player('teste', 1))
        self.assertFalse(insert_player('teste', 1))

    def test_update_score(self):
        insert_player('teste', 1)
        self.assertTrue(update_score('teste', 2))

    def test_check_if_player_exists(self):
        insert_player('teste', 1)
        self.assertTrue(check_if_player_exists('teste'))
        self.assertFalse(check_if_player_exists('teste2'))

    def test_get_players_sorted_by_score(self):
        insert_player('teste', 2) #id = 1
        insert_player('teste2', 1) #id = 2
        insert_player('teste3', 3) #id = 3
        self.assertEqual(get_players_sorted_by_score(), [(3, 'teste3', 3), (1, 'teste', 2), (2, 'teste2', 1)])


if __name__ == '__main__':
    unittest.main()