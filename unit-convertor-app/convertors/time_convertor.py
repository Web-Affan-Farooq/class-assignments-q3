def convert_time(from_unit, to_unit, value_tobe_converted):
          conversion_rates = {
                "Seconds": 1,       # considered as base unit
    "Nanoseconds": 1_000_000_000,    
    "Microseconds": 1_000_000,      
    "Milliseconds": 1_000,           
    "Minutes": 60,               
    "Hours": 3600,        
    "Day": 86400,                  
    "Week": 604800,             
    "Month": 2_592_000,       
    "Year": 31_536_000,      
    "Decade": 315_360_000           
}
          number_value = float(value_tobe_converted)
          converted_seconds = number_value * conversion_rates[from_unit]
          result = converted_seconds / conversion_rates[to_unit]
          return {
                  "Result":result,
                  "Formula":"(Value to be converted * "+ str(conversion_rates[from_unit]) + ") /" + str(conversion_rates[to_unit]),
                   "Conversion factors":{
                              "From unit":from_unit+"("+str(conversion_rates[from_unit],)+")",
                              "To unit":to_unit+"("+str(conversion_rates[to_unit],)+")"
                      }
          }