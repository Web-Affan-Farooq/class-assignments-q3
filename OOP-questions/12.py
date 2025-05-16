class TemperatureConvertor:
    @staticmethod
    def celcius_to_farenheit(c):
        f = (c*(9/5)) + 32
        return f
convertor =TemperatureConvertor()
print(convertor.celcius_to_farenheit(50))