from taxcalc import calc_tax, reverse_tax

# please instal nose package to run these test
# nosetests --with-doctest
def test_calc_tax():
	tax_calc_data_test = [
		["  10,000/-", 0.0],
		["2,50,000/-", 0.0],
		["2,50,001/-", 0.1],
		["4,50,000/-", 20000.0],
	]

	for amount, expected_tax in tax_calc_data_test:
		assert expected_tax == calc_tax(amount, silent=True)

def test_reverse_tax():
	reverse_tax_data_test = [
		[20000.0, 450000.0],
		[5000*12., 800000.0],
		[40000.0, 650000.0],
		[100000.0, 1000000.0],
	]

	for yearly_tax, yearly_taxable_income in reverse_tax_data_test:
		monthly_tax = "%d" % (yearly_tax/12)
		assert yearly_taxable_income == reverse_tax(monthly_tax)