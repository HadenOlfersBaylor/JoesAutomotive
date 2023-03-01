import CustomerClass as cust
import CarClass as car
import ServiceQuoteClass as serv

# name = 'John Doe'
# address = '123 Main St. Waco TX 76706'
# phone = '214-555-1112'
# make = 'Honda'
# model = 'Accord LX'
# car_year = 2016
# Parts: $1,210.50
# Labor: $765.00
# Sales Tax: $162.98
# Total Charges: $2,138.48

cust1 = cust.Customer('John Doe', '123 Main St. Waco TX 76706', '214-555-1112')
car1 = car.Car('Honda', 'Accord LX', '2016')
quote1 = serv.ServiceQuote(1210.50, 765.00)


print(
    f"Customer: {cust1.get_name()}\tAddress: {cust1.get_address()}\tPhone: {cust1.get_phone()}\n")
print(
    f"Car Make: {car1.get_make()} \tCar Model: {car1.get_model()}\tCar Year: {car1.get_year()}\n")
print('Service Quote\n')
print(f"Parts: ${quote1.get_parts_charges():,.2f}\n")
print(f"Labor: ${quote1.get_labor_charges():,.2f}\n")
print(f"Sales Tax: {quote1.getSalesTax():,.2f}\n")
print(f"Total Charge: {quote1.get_total_charges():,.2f}\n")
