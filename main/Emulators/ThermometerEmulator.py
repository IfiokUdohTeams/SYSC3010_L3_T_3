import ThermalSensor

class ThermometerEmulator(ThermalSensor.ThermalSensor):
    def __init__(self):
        super(ThermometerEmulator, self).__init__(14,30)

# def main():
#     thermo = ThermometerEmulator()
#     print("here")
#     print(thermo.read())
#     thermo.close()

# if __name__ == "__main__":
#     main()