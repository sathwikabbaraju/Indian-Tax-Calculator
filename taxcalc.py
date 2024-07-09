#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import string

# global tax_slabs used for calculating tax
tax_slabs = [[250000, 0.], [500000, 10.], [1000000, 20.], [-1, 30.]]

def str_amt_to_float(str_amt):
	'''
	converts amount in string to float.
	string amount can have anything before and after
	like 
	>>> str_amt_to_float("INR 50,000.00/-")
	50000.0
	>>> str_amt_to_float("12,34,567.50/- Rs.")
	1234567.5
	>>> str_amt_to_float("Rs.12,34,567.50/-")
	1234567.5
	>>> str_amt_to_float("12,34,567.50/- Rs")
	1234567.5
	'''
	digits = []
	for c in str_amt:
		if c in "0123456789.":
			if (c != ".") or (c == "." and c not in digits and len(digits)>1):
				digits.append(c)

	return float(''.join(digits))

def amt_to_str(amount, currency="INR", prefix=True, end_amount_with="/-", justify=False):
	'''
	converts input amount (in float/decimal) to string - seprated by coloumns, and with currency
	>>> amt_to_str(123456.78, currency="INR", prefix=True, end_amount_with="/-", justify=False)
	\'INR 1,23,456.78/-\'
	>>> amt_to_str(123456.78)
	\'INR 1,23,456.78/-\'
	>>> amt_to_str(123456.78, currency="INR", prefix=False, end_amount_with="/-", justify=False)
	\'1,23,456.78/- INR\'
	>>> amt_to_str(123456.78, currency="INR", prefix=True, end_amount_with="", justify=False)
	\'INR 1,23,456.78\'
	>>> amt_to_str(123456.78, currency="INR", prefix=True, end_amount_with="/-", justify=True)
	\'INR   1,23,456.78/-\'
	'''
	str_amt = "%.02f" % amount
	dec, frac = str_amt.split('.')

	if amount > 999:
		dec = dec[:-3] + "," + dec[len(dec)-3:]

	if amount > 99999:
		dec = dec[:-6] + "," + dec[len(dec)-6:]

	str_amt = "%s %s.%s%s" % (currency, dec, frac, end_amount_with)
	if not prefix:
		str_amt = "%s.%s%s %s" % (dec, frac, end_amount_with, currency)

	if justify:
		output_amt = "%s.%s%s" % (dec, frac, end_amount_with)
		if prefix:
			str_amt = "%s %s" % (currency, string.rjust(output_amt, 15))
		else:
			str_amt = "%s %s" % (string.rjust(output_amt, 15), currency)

	return str_amt

def calc_tax(net_taxable_income_str, silent=False):
	net_taxable_income = str_amt_to_float(net_taxable_income_str)
	if not silent:
		print("Calculating Tax for:", amt_to_str(net_taxable_income))
	total_tax_amount = 0.
	if not silent:
		print ("\nTax Slab wise calculations:")
	for tax_amount, tax_pcnt in tax_slabs:
		taxable_amount_slab = net_taxable_income

		if tax_amount == -1:
			net_taxable_income = 0.
		elif net_taxable_income > tax_amount:
			net_taxable_income = net_taxable_income - tax_amount
			taxable_amount_slab = tax_amount
		else:
			net_taxable_income = 0.

		if taxable_amount_slab > 0. :
			taxed_amount = ((taxable_amount_slab * tax_pcnt)/100.0)
			total_tax_amount = total_tax_amount + taxed_amount
			if not silent:
				print ("%6.2f %% on %10.2f = %10.2f" %  ( tax_pcnt, taxable_amount_slab, taxed_amount))

	if not silent:
		print ("\nTotal Tax:", amt_to_str(total_tax_amount, justify=True, prefix=False))
		print ("Monthly  :", amt_to_str(total_tax_amount/12, justify=True, prefix=False))

	return total_tax_amount

def reverse_tax(total_monthly_tax_str):
	total_monthly_tax = str_amt_to_float(total_monthly_tax_str)
	yearly_tax_amount = total_monthly_tax * 12

	just = lambda m: string.rjust(m, 28)

	print (just("Calculating Reverse Tax for:"), amt_to_str(total_monthly_tax, justify=True, prefix=False))
	print (just("Total Tax Yearly:"), amt_to_str(yearly_tax_amount, justify=True, prefix=False))

	last_amt = 0.
	last_tax_amt = 0.
	for i in range(100000, 10000000, 10000):
		amt = i + 0.
		str_amt = amt_to_str(amt)
		tax_amt = calc_tax(str_amt, silent=True)

		if yearly_tax_amount >= last_tax_amt and yearly_tax_amount <= tax_amt:
			print (just("Your Taxable Income:"), amt_to_str(amt, justify=True, prefix=False))
			break

		last_tax_amt = tax_amt

	return amt

if __name__ == "__main__":
	amount = sys.argv[1]
	if sys.argv[1] == "-r":
		amount = sys.argv[2]
		reverse_tax(amount)
	else:
		calc_tax(amount)