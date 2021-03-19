import constants as cs
"""
INTERMITTENCY defaults to no intermittency, this number should range between 0-1, 
0 means a constant source of energy, 0.5 means it outputs (max) energy 50% of the time

MIN/MED/MAX are Energy CO2 emissions, in gCo2 equiv/kWh, data from 2014
https://en.wikipedia.org/wiki/Life-cycle_greenhouse_gas_emissions_of_energy_sources
"""


class EnergySource:
    #  IS_INTERMITTENT = False  # is the energy source intermittent? If it is, then what is the intermittency?
    INTERMITTENCY = 0

    MIN = 0
    MED = 300
    MAX = 600

    """
    If INTERMITTENCY is not 0, return true. 
    """
    def is_intermittent(self):
        return self.INTERMITTENCY != 0


class Coal(EnergySource):
    MIN = 720
    MED = 820
    MAX = 910


class Gas(EnergySource):
    MIN = 410
    MED = 490
    MAX = 650


class Biomass(EnergySource):
    MIN = 130
    MED = 230
    MAX = 420


# Utility Grade Solar
class SolarUtility(EnergySource):
    IS_INTERMITTENT = 0.5
    MIN = 18
    MED = 48
    MAX = 180


class SolarConcentrated(EnergySource):
    INTERMITTENCY = 0.5
    MIN = 8.8
    MED = 27
    MAX = 63


class Nuclear(EnergySource):
    MIN = 3.7
    MED = 12
    MAX = 110


class Hydro(EnergySource):
    MIN = 1.0
    MED = 24
    MAX = 2200  # wild


class WindOnshore(EnergySource):
    INTERMITTENCY = 0.4
    MIN = 7
    MED = 11
    MAX = 56


class WindOffshore(EnergySource):
    INTERMITTENCY = True
    MIN = 8
    MED = 12
    MAX = 35


class Diesel(EnergySource):
    EMISSIONS_PER_MJ = 73.25  # gCO2/MJ
    MIN = MED = MAX = EMISSIONS_PER_MJ / (cs.J_PER_Wh * 1e3)  # We want units of kWh not MWh
