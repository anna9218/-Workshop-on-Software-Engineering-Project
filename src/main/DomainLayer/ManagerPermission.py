class ManagerPermission:  # TODO- maybe should be removed into User

    # def ManageStock(self, store):
    # CheckIfOwnesTheStore (store) # check pre conditions
    # basically this func appears on the use case and includes prints- should we keep it?
    # if we keeps it there is no need to check those terms below

    def check_if_ownes_the_store(self, store):
        # TODO - check if the user is registered
        # TODO - check if the user is login
        # TODO - check if the user is own this store
        return 1

    def add_products(self, store, names_and_prices):
        self.check_if_ownes_the_store(store)  # check pre conditions
        store.add_products(names_and_prices)  # TODO - remember its different on s.AddProducts

    def remove_products(self, store, products):
        self.check_if_ownes_the_store(store)  # check pre conditions
        # TODO - present the products and let the user choose them
        if store.empty_inventory():
            return  # TODO- print something?
        store.remove_products(products)

    def edit_products(self, store, product, newPrice):
        self.check_if_ownes_the_store(store)  # check pre conditions
        # TODO - print the inventory and let the manager a way to choose?
        store.ChangePrice(product, newPrice)
        # TODO- in use case he can also change the name, price, amount and info (can be description, category)

    pass
