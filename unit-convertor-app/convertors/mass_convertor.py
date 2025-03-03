def convert_mass(from_unit,to_unit, value_tobe_converted):
    conversion_rates = {
        "Grams":1.0,  # considered as base unit
        "Kilograms":0.001,
        "tonnes":0.000001,
        "Milligrams":1000,
        "Micrograms":1000000,
        "Imperial tons":0.000984207,
        "Stone":0.000157473,
        "Pounds":0.00220462,
        "Ounce":0.035274,
    }
    number_value = float(value_tobe_converted)
    result = (number_value * conversion_rates[to_unit])/ conversion_rates[from_unit]
    return {
            "Result":result,
            "Formula":"Value to be calculated * "+ str(conversion_rates[to_unit])+" /"+ str(conversion_rates[from_unit]),
             "Conversion factors":{
                              "From unit":from_unit+"("+str(conversion_rates[from_unit],)+")",
                              "To unit":to_unit+"("+str(conversion_rates[to_unit],)+")"
                      }
    }