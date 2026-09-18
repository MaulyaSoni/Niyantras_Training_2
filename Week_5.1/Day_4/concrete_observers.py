from observer import CartObserver

class OrderEntry(CartObserver):
    def status(self):
        print("Order Placed...")

class EmailNotify(CartObserver):
    def status(self):
        print("Order is placed and sending an invoice to the email....")

class StatsUpdate(CartObserver):
    def status(self):
        print("New Order place and successfully generate the id for observing stats")
