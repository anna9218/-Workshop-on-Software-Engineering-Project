from src.Logger import logger
from src.main.DomainLayer.StoreComponent.DiscountPolicyComposite.CompositeFlag import CompositeFlag
from src.main.DomainLayer.StoreComponent.DiscountPolicyComposite.DiscountComponent import DiscountComponent
from src.main.DomainLayer.UserComponent.DiscountType import DiscountType
import jsonpickle


class DiscountComponent_As_Jsonpickle:
    pass


class DiscountPolicy(DiscountComponent):

    def is_worthy(self, amount: int, basket_price: float, prod_lst: [str]):
        if self.__flag.value == CompositeFlag.AND.value:
            return self.__policy1.is_worthy(amount, basket_price, prod_lst) and self.__policy2.is_worthy(amount,
                                                                                                         basket_price,
                                                                                                         prod_lst)
        if self.__flag.value == CompositeFlag.OR.value:
            return self.__policy1.is_worthy(amount, basket_price, prod_lst) or self.__policy2.is_worthy(amount,
                                                                                                        basket_price,
                                                                                                        prod_lst)
        if self.__flag.value == CompositeFlag.XOR.value:
            return not (self.__policy1.is_worthy(amount, basket_price, prod_lst) ==
                        self.__policy2.is_worthy(amount, basket_price, prod_lst))

    def get_discount_type(self):
        return DiscountType.COMPOSITE

    def get_percentage(self):
        return self.__percentage

    def __init__(self, policy1: DiscountComponent_As_Jsonpickle, policy2: DiscountComponent_As_Jsonpickle,
                 flag: CompositeFlag, percentage: float, name: str):
        super().__init__()
        self.__policy1: DiscountComponent = jsonpickle.decode(policy1)
        self.__policy2: DiscountComponent = jsonpickle.decode(policy2)
        self.__flag = flag
        self.__percentage = percentage
        self.__product = self.__policy1.get_product_name()
        self.__name = name

    @logger
    def update(self, percentage: float = -999,
               discount_details: {'name': str,
                                  'product': str} = None,
               discount_precondition: {'product': str,
                                       'min_amount': int or None,
                                       'min_basket_price': str or None} or None = None):

        if discount_precondition is not None:
            return {'response': False, 'msg': "Composite discount can't have not-policy precondition."}

        if percentage != -999:
            if 0 <= percentage <= 100:
                self.__percentage = percentage
            else:
                return {'response': False, 'msg': "Composite discount can't have not-policy precondition."}

        if discount_details is not None:
            self.__name = discount_details['name']
            self.__product = discount_details['product']
        return {'response': True, 'msg': "Policy updated successfully."}

    @logger
    def get_name(self):
        return self.__name

    @logger
    def get_product_name(self):
        return self.__product

    @logger
    def get_price_after_discount(self, price: float):
        return price*((100-self.__percentage)/100)

    @logger
    def __repr__(self):
        return repr("DiscountPolicy")