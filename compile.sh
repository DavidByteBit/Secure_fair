#!/bin/bash
rm ../spdz/Programs/Source/fair.mpc
mv secure_fairness.py ../spdz/Programs/Source/fair.mpc
./../spdz/compile -R -64 fair