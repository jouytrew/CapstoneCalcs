"""
All the constants for the calculations
"""

"""
Energy CO2 emissions, in gCo2 equiv/kWh
https://en.wikipedia.org/wiki/Life-cycle_greenhouse_gas_emissions_of_energy_sources
"""

J_PER_Wh = 3.6e3  # 3600 Joules / Watt-hour


class EnergySource:
    MIN = 0
    MED = 300
    MAX = 600


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


"""
Utility Grade Solar
"""
class SolarUtility(EnergySource):
    MIN = 18
    MED = 48
    MAX = 180


class SolarConcentrated(EnergySource):
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
    MIN = 7
    MED = 11
    MAX = 56


class WindOffshore(EnergySource):
    MIN = 8
    MED = 12
    MAX = 35


class Diesel(EnergySource):
    EMISSIONS_PER_MJ = 73.25  # gCO2/MJ
    MIN = MED = MAX = EMISSIONS_PER_MJ / (J_PER_Wh * 1e3)  # We want units of kWh not MWh
