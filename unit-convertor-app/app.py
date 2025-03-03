import streamlit as st

# _____importing convertor functions
from convertors import pressure_convertor
from convertors import area_convertor
from convertors import mass_convertor
from convertors import time_convertor
from convertors import volume_convertor
from convertors import length_convertor
from convertors import speed_convertor
from convertors import temperature_convertor

#  Test case-1: concurrency check
#  Test case-2: Unit conversion: Calculate the values with the conversion metrics defined in convertors
#  Test case-3: Concurrent unit conversion.

#____initializer for input values ...

st.title("Unit Convertor Application")
from_value=""
to_value = ""

# ____Main select box for selection b/w quantities ...

options = ["Length","Area","Volume","Time","Temperature","Pressure","Speed","Mass"]
selected_option = st.selectbox("Choose quantity", options)

# ___if length is selected ...       
if(selected_option == "Length"):

# ____Change the values
    from_value = "1"
    to_value = "1"

# ____Select boxes for sellection selection b/w desired and target units
    length_options = ["Kilometer","Meter","Centimeter","Millimeter","Micrometer","Nanometer","Mile","Yard","Foot","Inch"]
    from_unit = st.selectbox("From ", length_options)
    to_unit = st.selectbox("To", length_options)

# ____Taking value to be converted to another unit from user
    value_tobe_converted = st.text_input(from_unit,value=from_value)

# ____Using imported functions for calculation
    calculated_data = length_convertor.convert_length(from_unit, to_unit, value_tobe_converted) # return {"Result", "Formula"}
    calculated_result = calculated_data["Result"]
    calculated_formula = calculated_data["Formula"]
    conversion_factors = calculated_data["Conversion factors"]  
# ____Assigning result into input field
    converted_value= st.text_input(to_unit,value=calculated_result)
# ____Display formula along with conversion factors...
    st.title("Conversion factors :")
    st.write("From Unit :" , conversion_factors["From unit"])
    st.write("To Unit :" , conversion_factors["To unit"])
    st.write("Formula :", calculated_formula)
# ___if area is selected ...       
elif(selected_option == "Area"):
# ____Change the values
        from_value = "1"
        to_value = "1"
# ____Select boxes for sellection selection b/w desired and target units
        area_options = ["Square meter","Square kilometer", "Square mile","Square yard", "Square foot", "Square inch", "Hectare","Acre"]
        from_unit = st.selectbox("From ", area_options)
        to_unit = st.selectbox("To", area_options)
# ____Taking value to be converted to another unit from user
        value_tobe_converted = st.text_input(from_unit,value=from_value)
# ____Using imported functions for calculation
        calculated_data = area_convertor.convert_area(from_unit, to_unit, value_tobe_converted)# return {"Result", "Formula"}
        calculated_result = calculated_data["Result"]
        calculated_formula = calculated_data["Formula"]
        conversion_factors = calculated_data["Conversion factors"]  
# ____Assigning result into input field
        converted_value= st.text_input(to_unit,value=calculated_result)
# ____Display formula along with conversion factors...
        st.title("Conversion factors :")
        st.write("From Unit :" , conversion_factors["From unit"])
        st.write("To Unit :" , conversion_factors["To unit"])
        st.write("Formula :", calculated_formula)
# ___if time is selected ...       
elif(selected_option == "Time"):
# ____Change the values
            from_value = "1"
            to_value = "1"
# ____Select boxes for sellection selection b/w desired and target units
            time_options = ["Nanoseconds","Microseconds","Milliseconds","Seconds","Minutes","Hours","Day" ,"Week" ,"Month","Year","Decade"]
            from_unit = st.selectbox("From ", time_options)
            to_unit = st.selectbox("To", time_options)
# ____Taking value to be converted to another unit from user
            value_tobe_converted = st.text_input(from_unit,value=from_value)
# ____Using imported functions for calculation
            calculated_data = time_convertor.convert_time(from_unit, to_unit, value_tobe_converted) # return {"Result", "Formula"}
            calculated_result = calculated_data["Result"]
            calculated_formula = calculated_data["Formula"]
            conversion_factors = calculated_data["Conversion factors"]  
# ____Assigning result into input field
            converted_value= st.text_input(to_unit,value=calculated_result)
# ____Display formula along with conversion factors...
            st.title("Conversion factors :")
            st.write("From Unit :" , conversion_factors["From unit"])
            st.write("To Unit :" , conversion_factors["To unit"])
            st.write("Formula :", calculated_formula)
# ___if speedis selected ...       
elif(selected_option == "Speed"):
# ____Change the values
                from_value = "1"
                to_value = "1"
# ____Select boxes for sellection selection b/w desired and target units
                speed_options = ["Meter per seconds","Kilometer per hours","Miles per hours","knot","Foot per seconds"]
                from_unit = st.selectbox("From ", speed_options)
                to_unit = st.selectbox("To", speed_options)
# ____Taking value to be converted to another unit from user
                value_tobe_converted = st.text_input(from_unit,value=from_value)
# ____Using imported functions for calculation
                calculated_data = speed_convertor.convert_speed(from_unit, to_unit, value_tobe_converted)# return {"Result", "Formula"}
                calculated_result = calculated_data["Result"]
                calculated_formula = calculated_data["Formula"]  
                conversion_factors = calculated_data["Conversion factors"]
# ____Assigning result into input field
                converted_value= st.text_input(to_unit,value=calculated_result)
# ____Display formula along with conversion factors...
                st.title("Conversion factors :")
                st.write("From Unit :" , conversion_factors["From unit"])
                st.write("To Unit :" , conversion_factors["To unit"])
                st.write("Formula :", calculated_formula)
# ___if mass is selected ...       
elif(selected_option == "Mass"):
# ____Change the values
                from_value = "1"
                to_value = "1"
# ____Select boxes for sellection selection b/w desired and target units
                mass_options = ["Grams","Kilograms","tonnes","Milligrams","Micrograms","Imperial tons","Stone","Pounds" ,"Ounce"]
                from_unit = st.selectbox("From ", mass_options)
                to_unit = st.selectbox("To", mass_options)
# ____Taking value to be converted to another unit from user
                value_tobe_converted = st.text_input(from_unit,value=from_value)
# ____Using imported functions for calculation
                calculated_data = mass_convertor.convert_mass(from_unit, to_unit, value_tobe_converted)# return {"Result", "Formula"}
                calculated_result = calculated_data["Result"]
                calculated_formula = calculated_data["Formula"]
                conversion_factors = calculated_data["Conversion factors"]
# ____Assigning result into input field
                converted_value= st.text_input(to_unit,value=calculated_result)
# ____Display formula along with conversion factors...
                st.title("Conversion factors :")
                st.write("From Unit :" , conversion_factors["From unit"])
                st.write("To Unit :" , conversion_factors["To unit"])
                st.write("Formula :", calculated_formula)
# ___if volume is selected ...       
elif(selected_option == "Volume"):
# ____Change the values
                from_value = "1"
                to_value = "1"
# ____Select boxes for sellection selection b/w desired and target units
                volume_options = ["Cubic meter","Cubic decimeter","Cubic centimeter","Cubic millimeter","Liter","Milliliter","Hectoliter","Kiloliter","Megaliter"
,"Imperial gallon","Imperial quart","Imperial pint","Imperial cup","Imperial fluid ounce"
,"Us gallon","Us quart","Us pint","Us cup","Us fluid ounce"
,"Cubic inch","Cubic foot","Cubic yard","Oil barrel","Bushel"]
                from_unit = st.selectbox("From ", volume_options)
                to_unit = st.selectbox("To", volume_options)
# ____Taking value to be converted to another unit from user
                value_tobe_converted = st.text_input(from_unit,value=from_value)
# ____Using imported functions for calculation
                calculated_data = volume_convertor.convert_volume(from_unit, to_unit, value_tobe_converted)# return {"Result", "Formula"}
                calculated_result = calculated_data["Result"]
                calculated_formula = calculated_data["Formula"]
                conversion_factors = calculated_data["Conversion factors"]
# ____Assigning result into input field
                converted_value= st.text_input(to_unit,value=calculated_result)
# ____Display formula along with conversion factors...
                st.title("Conversion factors :")
                st.write("From Unit :" , conversion_factors["From unit"])
                st.write("To Unit :" , conversion_factors["To unit"])
                st.write("Formula :", calculated_formula)

# ___if temperature is selected ...       
elif(selected_option == "Temperature"):
# ____Change the values
                from_value = "1"
                to_value = "1"
# ____Select boxes for sellection selection b/w desired and target units
                temperature_options =["Celcius","Farenheit","Kelvin"]                
                from_unit = st.selectbox("From ", temperature_options)
                to_unit = st.selectbox("To", temperature_options)
# ____Taking value to be converted to another unit from user
                value_tobe_converted = st.text_input(from_unit,value=from_value)
# ____Using imported functions for calculation
                calculated_data = temperature_convertor.convert_temperature(from_unit, to_unit, value_tobe_converted) # return {"Result", "Formula", "Conversion factors"}
                calculated_result = calculated_data["Result"]
                calculated_formula = calculated_data["Formula"]
                conversion_factors = calculated_data["Conversion factors"]
# ____Assigning result into input field
                # converted_value= st.text_input(to_unit,value=calculated_result)
                converted_value= st.text_input(to_unit,value=calculated_result)
# ____Display formula along with conversion factors...
                st.title("Conversion factors :")
                st.write("From Unit :" , conversion_factors["From unit"])
                st.write("To Unit :" , conversion_factors["To unit"])
                st.write("Formula :", calculated_formula)

# ___if pressure is selected ...       
elif(selected_option == "Pressure"):
# ____Change the values
                from_value = "1"
                to_value = "1"
# ____Select boxes for sellection selection b/w desired and target units
                pressure_options =["Pascal","Bar","Pound per square inch","Standard atmosphere","Torr"]               
                from_unit = st.selectbox("From ", pressure_options)
                to_unit = st.selectbox("To", pressure_options)
# ____Taking value to be converted to another unit from user
                value_tobe_converted = st.text_input(from_unit,value=from_value)
# ____Using imported functions for calculation
                calculated_data = pressure_convertor.convert_pressure(from_unit, to_unit, value_tobe_converted)# return {"Result", "Formula"}
                calculated_result = calculated_data["Result"]
                calculated_formula = calculated_data["Formula"]
                conversion_factors = calculated_data["Conversion factors"]
# ____Assigning result into input field
                converted_value= st.text_input(to_unit,value=calculated_result)
# ____Display formula along with conversion factors...
                st.title("Conversion factors :")
                st.write("From Unit :" , conversion_factors["From unit"])
                st.write("To Unit :" , conversion_factors["To unit"])
                st.write("Formula :", calculated_formula)