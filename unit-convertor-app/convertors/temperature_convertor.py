def convert_temperature(from_unit, to_unit, value_tobe_converted):
        conversion_rates = {
                "Celcius":0,
                "Farenheit":32,
                "Kelvin":273.15
        }
        number_value = float(value_tobe_converted)
        if(from_unit == "Celcius" and to_unit == "Farenheit"):
                result = (number_value*9/5) + 32 
                # return result
                return {
                "Result":result,
                "Formula": "Value to be converted * 9/5 then add 32",
                "Conversion factors":{
                              "From unit":from_unit+"("+str(conversion_rates[from_unit],)+")",
                              "To unit":to_unit+"("+str(conversion_rates[to_unit],)+")"
                      }
                }
        elif(from_unit == "Celcius" and to_unit == "Kelvin"):
                result = number_value + 273.15
                # return result
                return {
                "Result":result,
                "Formula": "Value to be converted + 273.15",
                "Conversion factors":{
                              "From unit":from_unit+"("+str(conversion_rates[from_unit],)+")",
                              "To unit":to_unit+"("+str(conversion_rates[to_unit],)+")"
                      }
                }
        elif(from_unit == "Farenheit" and to_unit == "Celcius"):
                result = (number_value - 32)* 5/9
                # return result
                return {
                "Result":result,
                "Formula": "Value to be converted - 32 *5/9",
                "Conversion factors":{
                              "From unit":from_unit+"("+str(conversion_rates[from_unit],)+")",
                              "To unit":to_unit+"("+str(conversion_rates[to_unit],)+")"
                      }
                }
        elif(from_unit == "Farenheit" and to_unit == "Kelvin"):
                result = (number_value - 32) * 5/9 + 273.15 
                # return result
                return {
                "Result":result,
                "Formula": "Value to be converted - 32 * 5/9 +273.15 ",
                "Conversion factors":{
                              "From unit":from_unit+"("+str(conversion_rates[from_unit],)+")",
                              "To unit":to_unit+"("+str(conversion_rates[to_unit],)+")"
                      }
                   }
        elif(from_unit == "Kelvin" and to_unit == "Celcius"):
                result = number_value - 273.15
                # return result
                return {
                "Result":result,
                "Formula": "Value to be converted - 273.15",
                "Conversion factors":{
                              "From unit":from_unit+"("+str(conversion_rates[from_unit],)+")",
                              "To unit":to_unit+"("+str(conversion_rates[to_unit],)+")"
                      }
                }
        elif(from_unit == "Kelvin" and to_unit == "Farenheit"):
                result = (number_value - 273.15) * 9/5 + 32
                # return result
                return {
                "Result":result,
                "Formula": "Value to be converted - 273.15 *9/5 +32",
                "Conversion factors":{
                              "From unit":from_unit+"("+str(conversion_rates[from_unit],)+")",
                              "To unit":to_unit+"("+str(conversion_rates[to_unit],)+")"
                      }
                 }
        elif(from_unit == "Celcius" and to_unit == "Celcius"):
                result = number_value
                # return result
                return {
                "Result":result,
                "Formula": "No change ...",
                "Conversion factors":{
                              "From unit":from_unit+"("+str(conversion_rates[from_unit],)+")",
                              "To unit":to_unit+"("+str(conversion_rates[to_unit],)+")"
                      }
                 }
        elif(from_unit == "Farenheit" and to_unit == "Farenheit"):
                result = number_value
                # return result
                return {
                "Result":result,
                "Formula": "No change ...",
                "Conversion factors":{
                              "From unit":from_unit+"("+str(conversion_rates[from_unit],)+")",
                              "To unit":to_unit+"("+str(conversion_rates[to_unit],)+")"
                      }
                 }
        elif(from_unit == "Kelvin" and to_unit == "Kelvin"):
                result = number_value
                # return result
                return {
                "Result":result,
                "Formula": "No change ...",
                "Conversion factors":{
                              "From unit":from_unit+"("+str(conversion_rates[from_unit],)+")",
                              "To unit":to_unit+"("+str(conversion_rates[to_unit],)+")"
                      }
                 }
        