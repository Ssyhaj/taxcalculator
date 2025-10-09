class TaxCalculator(object):
    SOCIAL_SECURITY_TAX = 9.76
    HEALTH_SOCIAL_SECURITY_TAX = 1.5
    SICKNESS_SOCIAL_SECURITY_TAX = 2.45
    HEALTH_TAX_1 = 9.0
    HEALTH_TAX_2 = 7.75
    ADVANCE_TAX = 18.0
    TAX_FREE_INCOME = 46.33 #podaje dane jako stale i uzywam ich jako zmiennych, raczej niz za kazdym razem wpisywac wartosc do obliczen
    DEDUCTIBLE_EXPENSES = 111.25 #zmieniam nazwy zmiennych na zrozumiale

    def __init__(self): #zmiany z wartosci klasy na wartosci instancji, zeby latwiej bylo to potem refaktorowac
        self.income = 0.0
        self.contract_type = ""
        self.advance_tax = 0.0
        self.advance_tax_rounded = 0.0

    def main(self):
        try:
            self.income=float(input("Enter income: "))
            self.contractType=input("Contract Type: (E)mployment, (C)ivil")[0]
        except ValueError:
            print("Incorrect")
            return
        if self.contractType=="E":
            print("EMPLOYMENT")
            print("Income ", self.income)
            d_income = self.calculateIncome(self.income)
            print("Social security tax: "+"{0:.2f}".format(self.SOCIAL_SECURITY_TAX))
            print("Health social security tax: "+"{0:.2f}".format(self.HEALTH_SOCIAL_SECURITY_TAX))
            print("Sickness social security tax: "+"{0:.2f}".format(self.SICKNESS_SOCIAL_SECURITY_TAX))
            print("Income basis for healt social security: ",d_income)
            self.calculateOtherTaxes(d_income)
            print("Healt social security tax: 9% = " \
                  +"{0:.2f}".format(self.HEALTH_TAX_1)+" 7,75% = "+"{0:.2f}".format(self.HEALTH_TAX_2))
            print("Tax deductible expenses: ",self.DEDUCTIBLE_EXPENSES)
            taxedIncome = d_income - self.DEDUCTIBLE_EXPENSES
            taxedIncome0 = float("{0:.0f}".format(taxedIncome))
            print("Income: ",taxedIncome," rounded: "+"{0:.0f}".format(taxedIncome0))
            self.calculateTax(taxedIncome0)
            print("Advance tax 18% = ",self.ADVANCE_TAX)
            print("Tax free income =",self.TAX_FREE_INCOME)
            taxPaid = self.ADVANCE_TAX - self.TAX_FREE_INCOME
            print("Reduced tax = "+"{0:.2f}".format(taxPaid))
            self.calculateAdvanceTax()
            self.advanceTax0 = float("{0:.0f}".format(self.advanceTax))
            print("Advance paid tax = "+"{0:.2f}".format(self.advanceTax)+\
                  " rounded "+"{0:.0f}".format(self.advanceTax0))
            netIncome = self.income - ((self.SOCIAL_SECURITY_TAX + self.HEALTH_SOCIAL_SECURITY_TAX \
                            + self.SICKNESS_SOCIAL_SECURITY_TAX) + self.HEALTH_TAX_1 + self.advanceTax0)
            print()
            print("Net income = "+"{0:.2f}".format(netIncome))
            

        elif self.contractType=="C":
            print("CIVIL")
            print("Income",self.income)
            d_income = self.calculateIncome(self.income)
            print("Social security tax: "+"{0:.2f}".format(self.SOCIAL_SECURITY_TAX))
            print("Health social security tax: "+"{0:.2f}".format(self.HEALTH_SOCIAL_SECURITY_TAX))
            print("Sickness social security tax  "+"{0:.2f}".format(self.SICKNESS_SOCIAL_SECURITY_TAX))
            print("Income for calculating health security tax: ",d_income)
            self.calculateOtherTaxes(d_income)
            print("Health security tax: 9% = " \
                  +"{0:.2f}".format(self.HEALTH_TAX_1)+" 7,75% = "+"{0:.2f}".format(self.HEALTH_TAX_2))
            self.TAX_FREE_INCOME = 0
            self.DEDUCTIBLE_EXPENSES = (d_income * 20) / 100
            print("Tax deductible expenses = ",self.DEDUCTIBLE_EXPENSES)
            taxedIncome = d_income - self.DEDUCTIBLE_EXPENSES
            taxedIncome0 = float("{0:.0f}".format(taxedIncome))
            print("income to be taxed: ",taxedIncome," rounded: "+"{0:.0f}".format(taxedIncome0))
            self.calculateTax(taxedIncome0)
            print("Advance tax 18% =",self.ADVANCE_TAX)
            taxPaid = self.ADVANCE_TAX            
            print("Already paid tax = "+"{0:.2f}".format(taxPaid))
            self.calculateAdvanceTax()
            self.advanceTax0 = float("{0:.0f}".format(self.advanceTax))
            print("Advance tax = "+"{0:.2f}".format(self.advanceTax)+\
                  " rounded "+"{0:.0f}".format(self.advanceTax0))
            netIncome = self.income - ((self.SOCIAL_SECURITY_TAX + self.HEALTH_SOCIAL_SECURITY_TAX \
                          + self.SICKNESS_SOCIAL_SECURITY_TAX) + self.HEALTH_TAX_1 + self.advanceTax0)
            print()
            print("Net income = "+"{0:.2f}".format(netIncome))
             
        else:
            print("Unknowne type of contract!")

    def calculateAdvanceTax(self):
        self.advanceTax=self.ADVANCE_TAX - self.HEALTH_TAX_2 - self.TAX_FREE_INCOME

    def calculateTax(self, income):
        self.ADVANCE_TAX = (income * 18) / 100

    def calculateIncome(self, income):
        self.SOCIAL_SECURITY_TAX = (income * 9.76) / 100        
        self.HEALTH_SOCIAL_SECURITY_TAX = (income * 1.5) / 100
        self.SICKNESS_SOCIAL_SECURITY_TAX = (income * 2.45) / 100
        return (income - self.SOCIAL_SECURITY_TAX- self.HEALTH_SOCIAL_SECURITY_TAX - self.SICKNESS_SOCIAL_SECURITY_TAX)

    def calculateOtherTaxes(self, income):
        self.HEALTH_TAX_1 = (income * 9) / 100
        self.HEALTH_TAX_2 = (income * 7.75) / 100

        
if __name__=='__main__':
    calc = TaxCalculator()
    calc.main()
