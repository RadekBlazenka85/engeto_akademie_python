import requests

from bs4 import BeautifulSoup

import csv

import sys

def main():

	lokality = get_seznam_lokalit()
	write_do_csv(lokality)

def get_seznam_lokalit():

	link = input(' Vložte odkaz s výsledky voleb z Vašeho okresu:').strip()
	soup = get_soup(link)

	cisla_lokalit = get_cisla_lokalit(soup)
	jmena_lokalit = get_jmena_lokalit(soup)
	linky_lokalit = get_linky_lokalit(soup)

	return list(zip(cisla_lokalit, jmena_lokalit, linky_lokalit))

def write_do_csv(list_lokalit):

	jmeno_souboru = input(' Zadejte jméno Vašeho souboru (bez koncovky): ').strip()
	link = 'https://www.volby.cz/pls/ps2017nss/' + list_lokalit[0][2]
	hlavni_soup = get_soup(link)
	hlavni = udelej_csv_hlavicku(hlavni_soup)
	with open('{}.csv'.format(jmeno_souboru), 'w', newline='') as file:
		zapis = csv.writer(file)
		zapis.writerow(hlavni)
		for lokalita in list_lokalit:
			print(' zpracovává se lokalita {}.'.format(lokalita[1]))
			link = 'https://www.volby.cz/pls/ps2017nss/' + lokalita[2]
			soup = get_soup(link)
			vysledky = get_vysledky_lokalit(soup)
			zapis.writerow([lokalita[0], lokalita[1]] + vysledky)

def get_soup(link):

	try:
		odpověď = requests.get(link)
	except Exception as exc:
		print('Byl problém s: %s' % (exc))
		sys.exit()
	return BeautifulSoup(odpověď.text, 'html.parser')

def get_cisla_lokalit(soup_obj):

	td_elementy = get_td_elementy(soup_obj, 't1sa1 t1sb1', 't2sa1 t2sb1', 't3sa1 t3sb1')
	td_cisla = []

	for td in td_elementy:
		if td.find('a'):
			kotvici_element = td.find('a')
			td_cisla.append(kotvici_element.text)
	return td_cisla

def get_jmena_lokalit(soup_obj):

	td_elementy = get_td_elementy(soup_obj, 't1sa1 t1sb2', 't2sa1 t2sb2', 't3sa1 t3sb2')
	return [td.text for td in td_elementy]

def get_linky_lokalit(soup_obj):

	td_elementy = get_td_elementy(soup_obj, 't1sa1 t1sb1', 't2sa1 t2sb1', 't3sa1 t3sb1')
	td_links = []
	for td in td_elementy:
		if td.find('a'):
			kotvici_element = td.find('a')
			td_links.append(kotvici_element.get('href'))
	return td_links

def get_td_elementy(soup_obj, *args):

	elementy = []
	for arg in args:
		elementy += soup_obj.select('td[headers="{}"]'.format(arg))
	return elementy

def udelej_csv_hlavicku(soup_obj):

	infos = ['code', 'location', 'registered', 'envelopes', 'valid']
	jmena_stran = get_jmena_stran(soup_obj)
	return infos + jmena_stran

def get_jmena_stran(soup_obj):

	elementy = get_td_elementy(soup_obj, 't1sa1 t1sb2', 't2sa1 t2sb2')
	return [element.text for element in elementy if element.text != '-']

def get_vysledky_lokalit(soup_obj):

	return get_info_hodnoty(soup_obj) + get_volene_strany(soup_obj)

def get_info_hodnoty(soup_obj):

	info_hlavicky = ['sa2', 'sa3', 'sa6']
	info_hodnoty = []
	for info_hlavicka in info_hlavicky:
		hodnota_element = soup_obj.find('td', {'headers':'{}'.format(info_hlavicka)})
		hodnota_element = hodnota_element.text
		hodnota_element = hodnota_element.replace('\xa0', '')
		info_hodnoty.append(int(hodnota_element))
	return info_hodnoty

def get_volene_strany(soup_obj):

	elementy = get_td_elementy(soup_obj, 't1sa2 t1sb3', 't2sa2 t2sb3')
	volene_strany = []
	for element in elementy:
		if element.text != '-':
			element = element.text.replace('\xa0', '')
			volene_strany.append(int(element))
	return volene_strany

if __name__ == '__main__':
	main()