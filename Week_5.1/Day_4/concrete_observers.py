from observer import CartObserver

class OrderEntry(CartObserver):
    def status(self) -> None:
        print("Order Placed...")

class EmailNotify(CartObserver):
    def status(self) -> None:
        print("Order is placed and sending an invoice to the email....")

class StatsUpdate(CartObserver):
    def status(self) -> None:
        print("New Order place and successfully generate the id for observing stats")
        