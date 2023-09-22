class Illness:

    def __init__(self, id=None, type=None, symptoms=None, treatment=None, medicine=None, support=None, financialaid=None):
        self.id = id
        self.type = type
        self.symptoms = symptoms
        self.treatment = treatment
        self.medicine = medicine
        self.support = support
        self.financialaid = financialaid
    

    def gettype(self):
        return self.type

    def settype(self, type):
        self.type = type
        