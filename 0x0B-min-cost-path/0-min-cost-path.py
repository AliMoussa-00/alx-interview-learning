#!/usr/bin/env python3

def get_min_cost_path(matrix: list[list[int]]):
	costs = []

	for i in range(len(matrix)):
		for j in range(len(i)):
			next_path=