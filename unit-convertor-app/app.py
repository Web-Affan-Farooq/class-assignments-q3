import streamlit as st

from_value=""
to_value = ""
options = ["Area","Volume","Time","Temperature","Pressure","Speed","Mass","Length",]
selected_option = st.selectbox("Choose quantity", options)

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
    result = (float(value_tobe_converted) * conversion_rates[to_unit]) / conversion_rates[from_unit]
    return result

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
    result = (float(value_tobe_converted) * conversion_rates[to_unit]) / conversion_rates[from_unit]
    return result

def convert_volume(from_unit, to_unit, value_tobe_converted):
    print("Volume")

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
          converted_seconds = float(value_tobe_converted) * conversion_rates[from_unit]
          result = converted_seconds / conversion_rates[to_unit]
          return result
        
def convert_speed(from_unit,to_unit, value_tobe_converted):
    conversion_rate = {
        "Meter per seconds": 1.0,  # considered as base unit
        "Kilometer per hours":3.6,
        "Miles per hours":2.23694,
        "knot":1.94384,
        "Foot per seconds":3.28084,
    }
    result = (float(value_tobe_converted) * conversion_rate[to_unit] ) / conversion_rate[from_unit]
    return result

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
    result = (float(value_tobe_converted) * conversion_rates[to_unit])/ conversion_rates[from_unit]
    return result
    


if(selected_option == "Length"):
    from_value = "1"
    to_value = "1"
    length_options = ["Kilometer","Meter","Centimeter","Millimeter","Micrometer","Nanometer","Mile","Yard","Foot","Inch"]
    from_unit = st.selectbox("From ", length_options)
    to_unit = st.selectbox("To", length_options)

    value_tobe_converted = st.text_area(from_unit,value=from_value)
    converted_value= st.text_area(to_unit,value=convert_length(from_unit, to_unit, value_tobe_converted))

elif(selected_option == "Area"):
        from_value = "1"
        to_value = "1"
        area_options = ["Square meter","Square kilometer", "Square mile","Square yard", "Square foot", "Square inch", "Hectare","Acre"]
        from_unit = st.selectbox("From ", area_options)
        to_unit = st.selectbox("To", area_options)

        value_tobe_converted = st.text_area(from_unit,value=from_value)
        converted_value= st.text_area(to_unit,value=convert_area(from_unit, to_unit, value_tobe_converted))

elif(selected_option == "Time"):
            from_value = "1"
            to_value = "1"
            time_options = ["Nanoseconds","Microseconds","Milliseconds","Seconds","Minutes","Hours","Day" ,"Week" ,"Month","Year","Decade"]
            from_unit = st.selectbox("From ", time_options)
            to_unit = st.selectbox("To", time_options)

            value_tobe_converted = st.text_area(from_unit,value=from_value)
            converted_value= st.text_area(to_unit,value=convert_time(from_unit, to_unit, value_tobe_converted))

elif(selected_option == "Speed"):
                from_value = "1"
                to_value = "1"
                speed_options = ["Meter per seconds","Kilometer per hours","Miles per hours","knot","Foot per seconds"]
                from_unit = st.selectbox("From ", speed_options)
                to_unit = st.selectbox("To", speed_options)

                value_tobe_converted = st.text_area(from_unit,value=from_value)
                converted_value= st.text_area(to_unit,value=convert_speed(from_unit,to_unit, value_tobe_converted))

elif(selected_option == "Mass"):
                from_value = "1"
                to_value = "1"
                mass_options = ["Grams","Kilograms","tonnes","Milligrams","Micrograms","Imperial tons","Stone","Pounds" ,"Ounce"]
                from_unit = st.selectbox("From ", mass_options)
                to_unit = st.selectbox("To", mass_options)

                value_tobe_converted = st.text_area(from_unit,value=from_value)
                converted_value= st.text_area(to_unit,value=convert_mass(from_unit,to_unit, value_tobe_converted))

elif(selected_option == "Volume"):
    print(selected_option)
    # _________Logic to be implemented
elif(selected_option == "Temperature"):
    print(selected_option)
    # _________Logic to be implementedelif(selected_option == "Pressure"):