def convert_area(from_unit, to_unit, value_tobe_converted):
    conversion_rates = {
        "Square meter":1, # considered as base unit
        "Square kilometer":0.001,
        "Square mile":0.000621371,
        "Square yard":1.09361,
        "Square foot" : 3.28084,
        "Square inch":39.3701,
        "Hectare":100,
        "Acre":247.105,
    }
    number_value = float(value_tobe_converted)
    result = (number_value * conversion_rates[to_unit]) / conversion_rates[from_unit]
    return {
            "Result":result,
            "Formula":"Value to be converted * "+str(conversion_rates[to_unit])+ " /"+ str(conversion_rates[from_unit]),
            "Conversion factors":{
                              "From unit":from_unit+"("+str(conversion_rates[from_unit],)+")",
                              "To unit":to_unit+"("+str(conversion_rates[to_unit],)+")"
                      }
    }