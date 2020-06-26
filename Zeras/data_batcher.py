# -*- coding: utf-8 -*-

import math
import random


class DataBatcher(object):
    """
    """
    def __init__(self, data, std_routine, batch_size, sort_key='text_indices', sort=False):
        """
        """
        self.sort = sort
        self.sort_key = sort_key
        self.batches = self.sort_and_standardize(data, batch_size, std_routine)
        self.batch_len = len(self.batches)
        #

    def sort_and_standardize(self, data, batch_size, std_routine):
        """
        """        
        if self.sort:
            sorted_data = sorted(data, key=lambda x: len(x[self.sort_key]))
        else:
            sorted_data = data
        #
        num_batch = int(math.ceil(len(data) / batch_size))
        batches = []
        for i in range(num_batch):
            batches.append( std_routine(sorted_data[i*batch_size : (i+1)*batch_size]) )
        return batches

    def shuffle(self):
        random.shuffle(self.batches)

    def __iter__(self):
        for idx in range(self.batch_len):
            yield self.batches[idx]
        #

#
if __name__ == "__main__":
    """
    """ 

    pass
