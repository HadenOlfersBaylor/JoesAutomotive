class ServiceQuote:
    def __init__(self, pcharge, lcharge):
        self.__parts_charges = pcharge
        self.__labor_changes = lcharge
        self.__sales_tax = 0
        self.__order_total = 0

    def set_parts_charges(self, pcharge):
        self.__parts_charges = pcharge

    def set_labor_charges(self, lcharge):
        self.__labor_changes = lcharge

    def get_parts_charges(self):
        return self.__parts_charges

    def get_labor_charges(self):
        return self.__labor_changes

    def getSalesTax(self):
        salesTax = 0.0825
        self.__order_total = self.__parts_charges + self.__labor_changes
        self.__sales_tax = self.__order_total * salesTax
        return self.__sales_tax

    def get_total_charges(self):
        # total = self.pcharge + self.lcharge
        self.__order_total += self.__sales_tax
        return self.__order_total
