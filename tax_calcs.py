def paye(salary):
    taxable_income = salary - salary * 0.055
    accrued_tax = 0
    if taxable_income > 319:
        if taxable_income >= 419:
            accrued_tax += 100 * 0.05
            if taxable_income >= 539:
                accrued_tax += 120 * 0.1
                if taxable_income >= 3539:
                    accrued_tax += 3000 * 0.175
                    if taxable_income == 20000:
                        accrued_tax += 16461 * 0.25
                        return accrued_tax
                    elif taxable_income > 20000:
                        return taxable_income * 0.30
                    else:
                        accrued_tax += (taxable_income - 3539) * 0.25
                        return accrued_tax
                else:
                    accrued_tax += (taxable_income - 539) * 0.175
                    return accrued_tax
            else:
                accrued_tax += (taxable_income - 419) * 0.1
                return accrued_tax
        else:
            accrued_tax += (taxable_income - 319) * 0.05
            return accrued_tax
    else:
        return accrued_tax


def ssnit(salary):
    return salary * 0.135


def ssnit_tier2(salary):
    return salary * 0.05
