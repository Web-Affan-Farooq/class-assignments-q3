def convert_speed(from_unit,to_unit, value_tobe_converted):
    conversion_rate = {
        "Meter per seconds": 1.0,  # considered as base unit
        "Kilometer per hours":3.6,
        "Miles per hours":2.23694,
        "knot":1.94384,
        "Foot per seconds":3.28084,
    }
    number_value = float(value_tobe_converted)
    result = (number_value * conversion_rate[to_unit] ) / conversion_rate[from_unit]
    return {
            "Result":result,
            "Formula":"(Value to be converted * "+ str(conversion_rate[to_unit])+" ) /"+ str(conversion_rate[from_unit]),
            "Conversion factors":{
                              "From unit":from_unit+"("+str(conversion_rate[from_unit],)+")",
                              "To unit":to_unit+"("+str(conversion_rate[to_unit],)+")"
                      }
    }