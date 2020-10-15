import numpy as np
import pandas as pd
import re

class Levenshtein:
    """Calculate levenshtein distance of words"""
    def __init__(self):
        # key locations
        self.key_locs = {'q': (0, 0), 'w': (1, 0), 'e': (2, 0), 'r': (3, 0),
                         't': (4, 0), 'y': (5, 0), 'u': (6, 0), 'i': (7, 0),
                         'o': (8, 0), 'p': (9, 0), 'a': (0, 1), 'z': (0, 2),
                         's': (1, 1), 'x': (1, 2), 'd': (2, 1), 'c': (2, 2),
                         'f': (3, 1), 'b': (4, 2), 'm': (5, 2), 'j': (6, 1),
                         'g': (4, 1), 'h': (5, 1), 'k': (7, 1), 'l': (8, 1),
                         'v': (3, 2), 'n': (5, 2)}
        # keys
        self.keys = list(self.key_locs.keys())
        # manhattan and euclidean key distances matrix
        self.manhattan_dist_matrix = np.zeros((len(self.keys), len(self.keys)))
        self.euclidean_dist_matrix = np.zeros((len(self.keys), len(self.keys)))
        # loop for calculating distances of keys
        for i in range(len(self.keys)):
            for j in range(len(self.keys)):
                dist_x = abs(self.key_locs[self.keys[i]][0] - self.key_locs[self.keys[j]][0])
                dist_y = abs(self.key_locs[self.keys[i]][1] - self.key_locs[self.keys[j]][1])
                # manhattan
                self.manhattan_dist_matrix[i, j] = dist_x + dist_y
                # euclidean
                self.euclidean_dist_matrix[i, j] = (dist_x ** 2 + dist_y ** 2) ** .5
        # max distances
        self.max_manhattan = np.max(self.manhattan_dist_matrix)
        self.max_euclidean = np.max(self.euclidean_dist_matrix)
        # weight coefficients
        # scale coef scales edit sizes to between 0 and scale coef
        self.scale_coef = 2
        self.manhattan_coef = self.scale_coef / self.max_manhattan
        self.euclidean_coef = self.scale_coef / self.max_euclidean
    
    def key_distance(self, x, y, type="manhattan"):
        """Return distance of two keys in qwerty keyboard
        based on manhattan or euclidean distance.

        Parameters
        ----------
        x: first word
        y: second word
        type: keyboard weight in distance calculating
        	euclidean: euclidean distance in keyboard
        	manhattan: manhattan distance in keyboard

        Return
        ------
        distance: distance of two keys in keyboard"""
        if type == "manhattan":
            return self.manhattan_dist_matrix[self.keys.index(x), self.keys.index(y)]
        elif type == "euclidean":
            return self.euclidean_dist_matrix[self.keys.index(x), self.keys.index(y)]
    
    def distance_matrix(self, x, y, keyboard_weight=None):
        """Calculate matrix of number of edits to convert 
        every subset of y to every subset of x

        Parameters
        ----------
        x: first word
        y: second word
        keyboard_weight: keyboard weight in distance calculating
        	None: no keyboard weight
        	euclidean: euclidean distance in keyboard
        	manhattan: manhattan distance in keyboard

        Return
        dist_matrix: distance matrix of two words
        	(len(x), len(y))"""
        # create distance matrix
        size_x = len(x) + 1
        size_y = len(y) + 1
        dist_matrix = np.zeros((size_x, size_y))
        for i in range(size_x):
            dist_matrix[i, 0] = i
        for j in range(size_y):
            dist_matrix[0, j] = j

        ## fill distance matrix
        # no keyboard weight
        if not keyboard_weight:
            for i in range(1, size_x):
                for j in range(1, size_y):
                    # if letters are same
                    if x[i-1] == y[j-1]:
                        dist_matrix[i, j] = dist_matrix[i-1, j-1]
                    # if letters are different
                    else:
                        subs = dist_matrix[i-1, j-1] + 1
                        delete = dist_matrix[i-1, j] + 1
                        insert = dist_matrix[i, j-1] + 1 
                        dist_matrix[i, j] = min(subs, delete, insert)
        # manhattan keyboard weight
        elif keyboard_weight == "manhattan":
            for i in range(1, size_x):
                for j in range(1, size_y):
                    # if letters are same
                    if x[i-1] == y[j-1]:
                        dist_matrix[i, j] = dist_matrix[i-1, j-1]
                    # if letters are different
                    else:
                        dist = self.key_distance(x[i-1], y[j-1], keyboard_weight)
                        subs_weight = dist * self.manhattan_coef
                        subs = dist_matrix[i-1, j-1] + subs_weight
                        delete = dist_matrix[i-1, j] + 1
                        insert = dist_matrix[i, j-1] + 1 
                        dist_matrix[i, j] = min(subs, delete, insert)
        # euclidean keyboard weight
        elif keyboard_weight == "euclidean":
            for i in range(1, size_x):
                for j in range(1, size_y):
                    # if letters are same
                    if x[i-1] == y[j-1]:
                        dist_matrix[i, j] = dist_matrix[i-1, j-1]
                    # if letters are different
                    else:
                        dist = self.key_distance(x[i-1], y[j-1], keyboard_weight)
                        subs_weight = dist * self.euclidean_coef
                        subs = dist_matrix[i-1, j-1] + subs_weight
                        delete = dist_matrix[i-1, j] + 1
                        insert = dist_matrix[i, j-1] + 1 
                        dist_matrix[i, j] = min(subs, delete, insert)
        
        return dist_matrix
    
    def distance(self, x, y, keyboard_weight=None):
        """Calculate number of edits to convert y to x

        Parameters
        ----------
        x: first word
        y: second word
        keyboard_weight: keyboard weight in distance calculating
        	None: no keyboard weight
        	euclidean: euclidean distance in keyboard
        	manhattan: manhattan distance in keyboard

        Returns
        -------
        distance"""
        dist_matrix = self.distance_matrix(x, y, keyboard_weight)
        return dist_matrix[-1, -1]
    
    def distance_dataframe(self, x, y, keyboard_weight=None):
        """Return a dataframe of distance matrix of x and y.
        Indexes are letters of x and columns are letters of y.

        Parameters
        ----------
        x: first word
        y: second word
        keyboard_weight: keyboard weight in distance calculating
        	None: no keyboard weight
        	euclidean: euclidean distance in keyboard
        	manhattan: manhattan distance in keyboard

        Return
        ------
        dist_df: pandas dataframe of distance matrix
        	index: letters of x
        	columns: letters of y"""
        dist_matrix = self.distance_matrix(x, y, keyboard_weight)
        dist_df = pd.DataFrame(dist_matrix, index=["", *list(x)], 
                               columns=["", *list(y)])
        return dist_df
        
    def similarity(self, x, y, keyboard_weight=None):
        """Calculate similarity of two words
        Return a number between 0 and 1
        (1 means same and 0 means fully different)

        Parameters
        ----------
        x: first word
        y: second word
        keyboard_weight: keyboard weight in distance calculating
        	None: no keyboard weight
        	euclidean: euclidean distance in keyboard
        	manhattan: manhattan distance in keyboard

        Return
        ------
        similarity: float between 0 and 1"""
        dist = self.distance(x, y, keyboard_weight)
        max_len = max(len(x), len(y))
        max_dissimilarity = max_len * self.scale_coef
        similarity = 1 - dist / max_dissimilarity
        return similarity