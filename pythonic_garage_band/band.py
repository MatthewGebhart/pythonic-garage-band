# Collection
class Band:
    def __init__(self, name, members=None):
        self.name = name
        self.members = members or []

    def play_solos(self):
        solos = [str(member.play_solo()) for member in self.members]
        return solos

    def __str__(self):
        return f"Our Band is called {self.name} and it is comprised {self.members}"

    def __repr__(self):
        return f"Band instance. Name = {self.name}"


# base class
class Musician:
    def __init__(self, name, instrument="unknown"):
        self.name = name
        self.instrument = instrument

    def get_instrument(self):
        return str(self.instrument)

    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"

    def __repr__(self):
        return f"Musician instance. Name = {self.name}. Instrument = {self.instrument}"

    def play_solo(self):
        solo = str(self.name.play_solo())
        return solo


# derived class
class Guitarist(Musician):
    def __init__(self, name="unknown", instrument="guitar"):
        self.name = name
        self.instrument = instrument

    # def __str__(self):
    #     return f"My name is {self.name} and I play {self.instrument}"

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"

    def play_solo(self):
        return "face melting guitar solo"
class Drummer(Musician):
    def __init__(self, name="unknown", instrument="drums"):
        self.name = name
        self.instrument = instrument

    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"

    def play_solo(self):
        return "rattle boom crash"

class Bassist(Musician):
    def __init__(self, name="unknown", instrument="bass"):
        self.name = name
        self.instrument = instrument

    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"

    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"

    def play_solo(self):
        return "bom bom buh bom"

# Category
