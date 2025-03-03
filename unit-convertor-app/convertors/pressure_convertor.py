## Convvertor function for converting pressure

def convert_pressure(from_unit, to_unit, value_tobe_converted):
        conversion_rates = {
    "Pascal": 1,                      # Base unit (1 Pa)
    "Bar": 100000,                     # 1 bar = 100,000 Pa
    "Pound per square inch": 6894.76,  # 1 psi = 6,894.76 Pa
    "Standard atmosphere": 101325,     # 1 atm = 101,325 Pa
    "Torr": 133.322,                   # 1 Torr = 133.322 Pa
}
        result = float(value_tobe_converted) * conversion_rates[to_unit] / conversion_rates[from_unit]

        return {
                "Result":result,
                "Formula": "Value to be converted * "+str(conversion_rates[to_unit])+ "/" + str(conversion_rates[from_unit]),
                "Conversion factors":{
                              "From unit":from_unit+"("+str(conversion_rates[from_unit],)+")",
                              "To unit":to_unit+"("+str(conversion_rates[to_unit],)+")"
                      }
        }