import unittest
import oxo_dialog_ui
from unittest.mock import patch

menu = ["Start new game",
        "Resume saved game",
        "Display help",
        "Quit"]

game = oxo_dialog_ui.startGame()

class test_unit(unittest.TestCase):
    def test_startGame(self):
        '''Testing startGame function'''
        l = list(" " * 9)
        self.assertEqual(oxo_dialog_ui.startGame(), l)

    def test_resumeGame(self):
        '''Testing startGame function'''
        l = list(" " * 9)
        self.assertEqual(oxo_dialog_ui.resumeGame(), l)

    def test_quit(self):
        '''Testing quitGame'''
        with self.assertRaises(SystemExit):
            oxo_dialog_ui.quit()

    def test_getMenuChoice(self):
        '''Testing getMenuChoice menu input'''
        with self.assertRaises(ValueError):
            oxo_dialog_ui.getMenuChoice(0)

    @patch('oxo_dialog_ui.getMenuChoice', return_value=1)
    def test_getMenuChoice2(self, input):
        '''Testing getMenuChoice choice input 1'''
        self.assertTrue(1 <= oxo_dialog_ui.getMenuChoice(menu) <= len(menu))

    @patch('oxo_dialog_ui.getMenuChoice', return_value=2)
    def test_getMenuChoice3(self, input):
        '''Testing getMenuChoice choice input 2'''
        self.assertTrue(1 <= oxo_dialog_ui.getMenuChoice(menu) <= len(menu))

    @patch('oxo_dialog_ui.getMenuChoice', return_value=3)
    def test_getMenuChoice4(self, input):
        '''Testing getMenuChoice choice input 3'''
        self.assertTrue(1 <= oxo_dialog_ui.getMenuChoice(menu) <= len(menu))

    @patch('oxo_dialog_ui.getMenuChoice', return_value=4)
    def test_getMenuChoice5(self, input):
        '''Testing getMenuChoice choice input 4'''
        self.assertTrue(1 <= oxo_dialog_ui.getMenuChoice(menu) <= len(menu))


if __name__ == '__main__':
    unittest.main(verbosity=2)