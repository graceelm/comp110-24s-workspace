"""Evaluating algorithm runtimes."""

__author__ = "730654117"

import matplotlib.pyplot as plt
from exercises.ex07.runtime_analysis_functions import evaluate_runtime
START_SIZE: int = 0
END_SIZE: int = 1000


times = evaluate_runtime("selection_sort", START_SIZE, END_SIZE)
plt.plot(times)
plt.title("Runtime Analysis of Selection Sort - 730654117")
plt.show()