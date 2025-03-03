def convert_length(from_unit, to_unit, value_tobe_converted):
    conversion_rates = {
        "Meter":1,
        "Centimeter":100,
        "Kilometer":0.001,
        "Millimeter":1000,
        "Micrometer":1000000,
        "Nanometer":1000000000,
        "Mile":0.000621371,
        "Yard":1.09361,
        "Foot":3.28084,
        "Inch":39.3701 ,
    }
    number_value = float(value_tobe_converted)
    result = (number_value * conversion_rates[to_unit]) / conversion_rates[from_unit]
    return {
            "Result":result,
            "Formula":"(Value to be converted *"+ str(conversion_rates[to_unit])  + ")" + " /"+ str(conversion_rates[from_unit]),
            "Conversion factors":{
                              "From unit":from_unit+"("+str(conversion_rates[from_unit],)+")",
                              "To unit":to_unit+"("+str(conversion_rates[to_unit],)+")"
                      }
    }