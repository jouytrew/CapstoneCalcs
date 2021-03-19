import energy_source as energy
import constants as cs
"""
Creating a mine
"""


class Mine:
    maas_load = 0

    def __init__(self,
                 name,  # for identification purposes
                 base_load,  # in Watts
                 grid_source=energy.Coal,
                 grid_energy_price=cs.COST_PER_kWh / 1e3,  # price is now per Wh
                 maas_source=energy.WindOnshore
                 ):
        self.name = name
        self.base_load = base_load
        self.grid_source = grid_source
        self.grid_energy_price = grid_energy_price
        self.maas_source = maas_source
        # Then run some calcs for how the MaaS is to be set up - probably depends on maas source's intermittency
        self.model_maas_system()

    """
    :return the yearly revenue (probably in terms money saved from generating electricity)
    """
    def get_yr_savings(self):
        pass

    """
    :return the yearly operating costs
    """
    def get_yr_op_costs(self):
        pass

    """
    :returns the Operating Cash Delta = savings - costs
    """
    def get_yr_ocd(self):
        return self.get_yr_savings() - self.get_yr_op_costs()

    """
    :returns the number of Watt-hours needed per year to satisfy operations, from the base_load
    """
    def get_annual_energy_use(self):
        return self.base_load * cs.HOURS_PER_DAY * cs.DAYS_OP_PER_YEAR

    """
    :returns the cost per year to run operations using grid electricity, in $
    """
    def get_annual_energy_cost(self):
        return self.grid_energy_price * self.get_annual_energy_use()

    """
    :returns annual co2 emissions in tons of CO2. Annual energy use is in Wh, grid_source.XYZ is in g/kWh
    we need to divide the product by 1e9 to get tons.
    """
    def get_annual_grid_co2_tonnage(self):
        return self.get_annual_energy_use() * self.grid_source.MED / 1e9  # tons of CO2

    def get_emissions_social_cost(self):
        return self.get_annual_grid_co2_tonnage() * cs.CARBON_OFFSET_SOCIAL_COST

    def model_maas_system(self):
        self.maas_load = (1 - self.maas_source.INTERMITTENCY) * self.base_load

