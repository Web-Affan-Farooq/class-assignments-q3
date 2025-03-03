def convert_volume(from_unit, to_unit, value_tobe_converted):
              conversion_rates = {
    # **Metric System (Base Unit: Liter)**
    "Cubic meter": 1000,  "Cubic decimeter": 1,         # 1 dm³ = 1 L
    "Cubic centimeter": 0.001,    # 1 cm³ = 0.001 L (1 mL)
    "Cubic millimeter": 0.000001, # 1 mm³ = 0.000001 L
    "Liter": 1,                   # Base unit
    "Milliliter": 0.001,          # 1 mL = 0.001 L
    "Hectoliter": 100,            # 1 hL = 100 L
    "Kiloliter": 1000,            # 1 kL = 1000 L
    "Megaliter": 1_000_000,       # 1 ML = 1,000,000 L

    # **Imperial System**
    "Imperial gallon": 4.54609,       # 1 imperial gallon = 4.54609 L
    "Imperial quart": 1.13652,        # 1 imperial quart = 1.13652 L
    "Imperial pint": 0.568261,        # 1 imperial pint = 0.568261 L
    "Imperial cup": 0.284131,         # 1 imperial cup = 0.284131 L
    "Imperial fluid ounce": 0.0284131,# 1 imperial fl oz = 0.0284131 L

    # **US Customary System**
    "US gallon": 3.78541,         # 1 US gallon = 3.78541 L
    "US quart": 0.946353,         # 1 US quart = 0.946353 L
    "US pint": 0.473176,          # 1 US pint = 0.473176 L
    "US cup": 0.24,               # 1 US cup = 0.24 L
    "US fluid ounce": 0.0295735,  # 1 US fl oz = 0.0295735 L

    # **Other Units**
    "Cubic inch": 0.0163871,      # 1 in³ = 0.0163871 L
    "Cubic foot": 28.3168,        # 1 ft³ = 28.3168 L
    "Cubic yard": 764.5549,       # 1 yd³ = 764.5549 L
    "Oil barrel": 158.987,        # 1 oil barrel = 158.987 L
    "Bushel": 35.2391             # 1 bushel = 35.2391 L
}
              number_value = float(value_tobe_converted)
              result = number_value*(conversion_rates[from_unit] / conversion_rates[to_unit])
              return {
                      "Result":result,
                      "Formula":"Value to be converted * ("+ str(conversion_rates[from_unit]) + "/" + str(conversion_rates[to_unit]) + ")",
                      "Conversion factors":{
                              "From unit":from_unit+"("+str(conversion_rates[from_unit],)+")",
                              "To unit":to_unit+"("+str(conversion_rates[to_unit],)+")"
                      }
              }