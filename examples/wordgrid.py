#!/usr/bin/python
# -*- coding: utf-8 -*-
# (C) 2015 Muthiah Annamalai

import copy, random
import tamil

from sys import version
PYTHON3 = version > '3'
        
# Vertical / Horizontal Word Grids

# Put a list of words into a grid
class WordGrid:
    @staticmethod
    def sorter(a,b):
        if len(a) > len(b):
            return 1
        if len(a) == len(b):
            return 0
        return -1
    
    @staticmethod
    def compute(words,fill_letters):
        drv = WordGrid( words, fill_letters )
        drv.precompute()
        drv.display()
        print('###############')
        drv.generate( )
        drv.display()
        return
    
    def __init__(self,words,letters):
        self.words = copy.copy(words)
        self.fill_letters = letters
        self.max_word_len = 0
        self.grid_size = 0
        self.grid = list()
        pass
        
    def __del__(self):
        del self.words
        del self.grid
    
    def display(self):
        for row_idx in range(len(self.grid)):
            row_data = " ".join( self.grid[row_idx][col_idx][0] for col_idx in range( len(self.grid[row_idx]) ) )
            print(row_data)
        print("<= P =>")
        for row_idx in range(len(self.grid)):
            row_data = " ".join( str(self.grid[row_idx][col_idx][1])[0] for col_idx in range( len(self.grid[row_idx]) ) )
            print(row_data)
        return
    
    def precompute(self):
        self.max_word_len = max( list(map(len,self.words)) )
        self.grid_size = 2*self.max_word_len
        # sort words in order
        if PYTHON3:
            self.words = sorted( self.words, key=len )
        else:
            self.words.sort( cmp = WordGrid.sorter )
        # prepare a random grid of dim [#words x #max-word-length]
        for itr_r in range( len(self.words) ):
            self.grid.append( [[random.choice( self.fill_letters ),False] for i in range(self.grid_size)] )
        return

    def generate_vertical(self):
        self.generate_horizontal()
        # transpose the array.
        grid_new = list()
        for itr in range( len(self.grid[0]) ):
            grid_new.append( list(range( len(self.grid))) )
        for itr_r in range( len(self.grid) ):
            for itr_c in range( len(self.grid[0]) ):
                grid_new[itr_c][itr_r] = self.grid[itr_r][itr_c]
        self.grid = grid_new
        return
    
    def generate_horizontal(self):
        for idx,word_i in enumerate(self.words):
            L = len(word_i)
            excess = self.grid_size - L
            start_pos = random.choice( list(range(excess)) )
            for idy,letter in enumerate(word_i):
                self.grid[idx][start_pos+idy] = [letter,True]
            pass
        return
    
    def generate(self):
        self.generate_horizontal()
    

if __name__ == "__main__":
    wordlist = ['food','water','shelter','clothing']
    fill_letters = list(map(chr,[ord('a')+i for i in range(0,26)]))
    WordGrid.compute( wordlist, fill_letters )