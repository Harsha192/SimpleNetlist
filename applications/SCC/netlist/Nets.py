from .nlUtils import *
from .nlNode import nlNode

@static_vars(inst=0)
class Net(nlNode):
    """
    Generic Wire class
    """
    def __init__(self, parent):
        name = 'NET_%d' % Net.inst
        Net.inst += 1
        super().__init__('NET', name, parent)
        self._drivers = []
        self._loads = []

    def addLoad(self, load):
        self._loads.append(load)

    def addDriver(self, driver):
        self._drivers.append(driver)

    def populateNetGraph(self):
        netGraph = nx.DiGraph()

        for load in self._loads:
            netGraph.add_edge(self, load)

        for driver in self._drivers:
            netGraph.add_edge(driver, self)

        return netGraph
    def listDrivers(self):
        return self._drivers 
    def listLoads(self):
        return self._loads
