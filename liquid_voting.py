#!/usr/bin/env python

import numpy as np
import json
from timeit import default_timer as timer

class LiquidVoting:

    ITERATION = 10000


    def __init__(self, _data):
        self.square = len(data)
        self.num_people = len(data[0])
        self.num_plan = self.square - self.num_people
        self.input = np.matrix(data)
        self.make_voting_matrix()

    def make_voting_matrix(self):
        right_top = np.zeros((self.num_people, self.num_plan))
        right_bottom = np.eye(self.num_plan)
        right = np.vstack((right_top, right_bottom))
        self.V = np.hstack((self.input, right))

    def calc(self):
        A = np.eye(self.square)
        result = []
        wj = np.zeros((self.num_people, 1))
        d = np.zeros((self.num_people, 1))

        for i in range(LiquidVoting.ITERATION):
            A = self.V * A

            for p in range(self.num_people):
                wj[p] += np.sum(A[p, :self.num_people])
                d[p] += A[p, p]

            # print(A)

        result = [np.sum(A[self.num_people + i, :self.num_people]) for i in range(self.num_plan)]

        print(wj)
        print(d)

        influence = [n[0] for n in wj/d]
       
        return result, influence

if __name__ == '__main__':

    json_file = "test.json"

    with open(json_file, 'r') as f:
        data = json.load(f)
        ld = LiquidVoting(data)
        start = timer()
        result, influence = ld.calc()
        end = timer()

        print(result)
        print(influence)
        print('elapsed: {}'.format(end-start))

        with open("result.json", 'w') as wf:
            json.dump([result, influence], wf)
