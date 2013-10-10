#!/usr/bin/python
'''
Title: RPG Inc
Author: Niklas & Ramkumar
'''
import unittest

class RPG_Game(object):
    def __init__(self):
        pass
        #self.output_file = output_f

    def run(self, input_file):
        players = []
        new_list = ""
        with open(input_file, 'r') as f:
            for line in f:
                new_list = line.strip().split(', ')
                players.append({ \
                    'name':new_list[0],
                    'speed':int(new_list[1]),
                    'health':int(new_list[2]),
                    'weapon':new_list[3],
                    'damage':int(new_list[4]) \
                })
        
        players = [players[1], players[0]]
        ticks = 1
        return "%d,%s,%s,%s,%d,%d,%d" % ( \
                ticks,
                players[0]['name'],
                players[1]['name'],
                players[0]['weapon'],
                players[0]['speed'],
                players[1]['health'] - players[0]['damage'],
                players[0]['health'] \
        )

class TestCombat(unittest.TestCase):
    def test_example_input(self):
        inf = 'infile'
        #outf = open('outfile','r').read()
        #testf = open('testfile', 'r').read()
        game = RPG_Game()
        #game.run(inf)
        self.assertEqual(game.run(inf),"1,'John the Bagger','Mark the Fister','Small Bag',1,7,7")

