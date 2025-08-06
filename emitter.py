import particle

BLUE = (0, 0, 255)

class Emitter():

    def particle_die(self, index):
        self.particle_pool[index][1] = "dead"

    def check_life_val(self, index):
        return self.particle_pool[index][0].life

    
    def check_dead(self):
        for i in range(len(self.particle_pool)):
            life_val = self.check_life_val(i)
            if life_val != None:
                if life_val < 0:
                    self.particle_die(i)
                    # scan pool for alive
                    # if dead particle has index less than alive switch them
                    j = self.check_alive()
                    if j != None:
                        if i < j:
                            self.particle_pool[i], self.particle_pool[j] = self.particle_pool[j], self.particle_pool[i]

    def check_alive(self):
        for i in range(len(self.particle_pool)):
            if self.particle_pool[i][1] == "alive":
                return i
            




    def request_amount(self, val):
        self.requested_particle_amount = val

    def setEmittingStatus(self, bool):
        self.isEmitting = bool
    
    def getEmittingStatus(self):
        return self.isEmitting
    
    def fill_particle_pool(self):
        for i in range(self.particle_amount):
            self.particle_pool.append([particle.Particle(50, 50, 400, 400, BLUE, 5, 90, 90, 1), "alive"])

    def emitt_particle(self, index):
        self.group.add(self.particle_pool[index][0])

    def emitt_requested_amount(self):
        for i in range(self.requested_particle_amount):
            self.emitt_particle(i)

    def update(self):
        self.getEmittingStatus()
        self.check_dead()

        for i in range(len(self.particle_pool)):
            print(self.particle_pool[i][1])

        if self.isEmitting:
            self.emitt_requested_amount()
    
    def __init__(self, particle_amount, group):
        self.particle_pool = []
        self.requested_particle_amount = self.particle_amount = particle_amount
        self.group = group
        self.isEmitting = False

        self.fill_particle_pool()