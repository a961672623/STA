from node import Node
from link import Link
from path import Path
from od import OD
from network import Network

import sys
import traceback
import utils
import random
import numpy as np

FRANK_WOLFE_STEPSIZE_PRECISION = 1e-7
UE_PRECISION = 10

net = Network("SiouxFalls_net.tntp", "SiouxFalls_trips.tntp")

# for ij in net.link:
#     print(ij)
#     print(net.link[ij].flow)

net.userEquilibriumFW()