import ThermalSensor

class ThermalCamera(ThermalSensor.ThermalSensor):
    def __init__(self):
        super(ThermalCamera, self).__init__(30,45)

# def main():
#     thermo = ThermalCamera()
#     print("here")
#     print(thermo.read())
#     thermo.close()

# if __name__ == "__main__":
#     main()