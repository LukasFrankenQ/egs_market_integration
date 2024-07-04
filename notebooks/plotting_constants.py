colors = {
    "dh": "#ec0000",
    "chp": "#ffccab",
    "elec": "#b3c1e6",
}

xaxis_mapper = {
    "2020": "1.0",
    "2025": "1.4",
    "2030": "1.8",
    "2035": "2.5",
    "2040": "3.5",
    "2045": "4.4",
    "2050": "5.0",
}


coarse_regions = {
    "Southern-Central\nGermany": ["DE1 6", "DE1 2", "DE1 4", "DE1 1", "DE1 7", "DE1 9", "DE1 8"],
    "Northern Germany": ["DE1 5", "DE1 0", "DE1 3"],
    "Northern Italy,\nSlovenia": ["IT1 1", "IT1 3", "IT1 0", "SI1 0"],
    "Southern Italy": ["IT1 2", "IT1 4", "IT3 0", "IT1 5"],
    # "Norway": ["NO2 0", "NO2 1"],
    "Western Poland": ["PL1 0"],
    "Eastern Poland": ["PL1 1"],
    # "Sweden": ["SE2 0", "SE2 1"],
    "Scandinavia (w/o DK)": ["SE2 0", "SE2 1", "NO2 0", "NO2 1", "FI2 0"],
    "Denmark": ["DK1 0", "DK2 0"],
    "Ireland": ["IE5 0", "GB5 0"],
    # "Scotland": ["GB0 4"],
    # "Wales and Cornwall": ["GB0 3"],
    "Baltic States": ["LT6 0", "LV6 0", "EE6 0"],
    "Great Britain": ["GB0 1", "GB0 0", "GB0 5", "GB0 2", "GB0 4", "GB0 3"],
    # "England": ["GB0 1", "GB0 0", "GB0 5", "GB0 2"],
    "Northern France": ["FR1 9", "FR1 7", "FR1 2", "FR1 6"],
    "Southern France": ["FR1 3", "FR1 8", "FR1 5", "FR1 1"],
    "Eastern France": ["FR1 0", "FR1 4"],
    # "Netherlands": ["NL1 0", "NL1 1"],
    "Benelux": ["NL1 0", "NL1 1", "LU1 0", "BE1 0"],
    # "Northern Spain": ["ES1 3", "ES1 2"],
    # "Southern Spain": ["ES1 1", "ES1 0", "ES4 0"],
    "Iberia": ["ES1 3", "ES1 2", "ES1 1", "ES1 0", "ES4 0", "PT1 0"],
    "Austria": ["AT1 0"],
    "Switzerland": ["CH1 0"],
    "Czech Republic,\nSlovakia": ["CZ1 0", "SK1 0"],
    "Romania, Bulgaria,\nSerbia, Hungary": ["RO1 0", "BG1 0", "RS1 0", "HU1 0"],
    "Bosnia, Montenegro,\nAlbania, Croatia": ["BA1 0", "ME1 0", "AL1 0", "HR1 0"],
    "Mazedonia, Greece": ["MK1 0", "GR1 0"],
}

reverse_coarse_regions = {
    b: a for a, bs in coarse_regions.items() for b in bs
}

min_cost_acceleration_factor = 0 # years