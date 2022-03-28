class Vehicle:

    def __init__(self, vehicleNo: int, isAvailable=True):
        self.vehicleNo = vehicleNo
        self.isAvailable = isAvailable

    def __str__(self):
        return f"Vehicle №{self.vehicleNo}"