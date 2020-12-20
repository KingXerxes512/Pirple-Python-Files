
class Vehicle:
    def __init__(self, make, model, year, weight, needs_maintenance=False, trips_since_maintenance=0):
        self.Make = make
        self.Model = model
        self.Year = year
        self.Weight = weight
        self.needs_maintenance = needs_maintenance
        self.trips_since_maintenance = trips_since_maintenance

    def setMake(self, make):
        self.Make = make

    def setModel(self, model):
        self.Model = model

    def setYear(self, year):
        self.Year = year

    def setWeight(self, weight):
        self.Weight = weight

    def Repair(self):
        self.trips_since_maintenance = 0
        self.needs_maintenance = False


class Cars(Vehicle):
    def __init__(self, make, model, year, weight, isDriving=False):
        Vehicle.__init__(self, make, model, year, weight)
        self.isDriving = isDriving

    def Drive(self):
        self.isDriving = True

    def Stop(self):
        if self.isDriving:
            self.trips_since_maintenance += 1
            if self.trips_since_maintenance > 100:
                self.needs_maintenance = True
        self.isDriving = False

    def __str__(self):
        return "Make: " + str(self.Make) + " Model: " + str(self.Model) + " Year: " + str(self.Year) + " Weight: " + \
               str(self.Weight) + " Needs Maintenance: " + str(self.needs_maintenance) + " Trips Since Maintenance: " + \
               str(self.trips_since_maintenance)


Honda = Cars("Honda", "Civic", 2011, 2000)
Subaru = Cars("Subaru", "Outback", 2021, 3000)
Nissan = Cars("Nissan", "Altima", 2011, 1500)

for i in range(100):
    Honda.Drive()
    Honda.Stop()

for i in range(50):
    Subaru.Drive()
    Subaru.Stop()

for i in range(500):
    Nissan.Drive()
    Nissan.Stop()

print(Honda)
print(Subaru)
print(Nissan)
