from order import Order


class LogisticSystem:
    def __init__(self, vehicles):
        self.orders = []
        self.vehicles = vehicles

    def placeOrder(self, order: Order):
        for vehicle in self.vehicles:
            if vehicle.isAvailable:
                order.assignVehicle(vehicle)
                self.orders.append(order)
                return
        print("There is no available vehicle for this order")

    def trackOrder(self, orderId: int):
        for order in self.orders:
            if order.orderId == orderId:
                return f"Your order #{orderId} is sent to {order.location.city}." \
                       f" Total price: {order.calculateAmount()} UAH."
        return f"There is not such order with id #{orderId}"
