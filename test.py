#from taxi import Taxi

#from taxi import UnreliableCar


from taxi import SilverServiceTaxi
#t = Taxi("Prius 1", 100)
#t.drive(40)
#print(t)

#pp = UnreliableCar("gg", 40, 44)

#pp.drive(43)

#print(pp)

gg = SilverServiceTaxi("qq", 100, 2)
print(gg)
gg.start_fare()
gg.drive(10)
gg.get_fare()


