# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class StripePaymentHandler:
    def handle_payment(self, amount: int) -> None:
        print(f"Charging ${amount / 100:.2f} using Stripe")


PRICES = {
    "burger": 10_00,
    "fries": 5_00,
    "drink": 2_00,
    "salad": 15_00
}


# dependency injection of StripePaymentHandler
def order_food(items: list[str], payment_handler: StripePaymentHandler) -> None:
    total = sum(PRICES[item] for item in items)
    print(f"Your order is ${total / 100:.2f}")
    payment_handler.handle_payment(total)
    print("Thanks for your business!")


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    order_food(["burger", "fries", "drink"], StripePaymentHandler())  # inject StripePaymentHandler

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
