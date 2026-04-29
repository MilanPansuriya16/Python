from loguru import logger

def final_cart_amount (*args,discount = 0.1):
    try:
        result = 0
        for amount in args:
            result = result + amount

        amount_after_discount = result - (result * discount)

        return amount_after_discount
    except TypeError:
        logger.info("Please provide the amount in integer")
        raise Exception("Value provided is not an interger coming from Type Error")
    except Exception:
        logger.info("Can not process the cart amount")
        raise 

try:
    final_amount_to_be_paid = final_cart_amount(100,200,300,400,"500",discount = 0.5)
    logger.info(f"final amount to be paid = {final_amount_to_be_paid}")
except Exception as e:
    logger.info(e)

