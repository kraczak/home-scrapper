_forbidded_places = [
    'jagodno', 'komedy', 'kopycińskiego', 'awicenny', 'partynic', 'zwycięsk', 'buforow', 'psie pole', 'psim polu',
    'wojszyce', 'Nefrytow', 'Stabłowice', 'jordanowska', 'klecin', 'rogowsk', "maślic", "swojczyc",
    "złotnik", "Z dala od zgiełku miasta", "OŁTASZYN", "Łubinowa", "brochów", "Mińśk", "graniczn",
    "muchobór wielki", "Osiedle Malownicze", "marszowice", "Graniczna", "dzierżonia", "Tarasy Grabiszynsskie",
    "Tarasy Grabiszyns", "Parku Grabiszyńskiego", "Park Grabiszyński", "racławicka", "konna", "balonowa",
    "linia autobusowa 111", "Racławickiej", "dokerska", "kozanów", "olszewskiego", "kuźniki", "sarbinowsk",
    "pilczyc", "mały gądów", "borek", "iwaszkiewicza", 'kłodzk', 'nowy dwor',
    'nowy dw', 'Kościańsk', 'cukrow', 'wałbrzysk', 'hłask', 'Kosmonautów', 'Starodworsk',
    'niskie łąki', 'weigla', 'mrągowsk', 'mińsk', 'Leśnic', 'rytownicz', 'Różanka',
    'dokersk', 'kozanow', 'hynk', 'Muchoborze Wielkim', 'rymarsk', 'trawow', 'kamienic'
]

forbidden_places = [place.lower() for place in _forbidded_places] + [
    place.replace(' ', '-') for place in _forbidded_places
]

url = 'https://www.morizon.pl/mieszkania/wroclaw/?ps%5Bprice_from%5D=250000&ps%5Bprice_to%5D=600000&ps%5Bprice_m2_to%5D=12500&ps%5Bliving_area_from%5D=25&ps%5Bliving_area_to%5D=60&ps%5Bnumber_of_rooms_from%5D=2&ps%5Bnumber_of_rooms_to%5D=3&ps%5Bfloor_from%5D=1&ps%5Bfloor_to%5D=10&ps%5Bbuild_year_from%5D=2000&ps%5Bbuild_year_to%5D=2021&ps%5Bhas_balcony%5D=1'

if __name__ == '__main__':
    from common.utils import any_a_in_any_b

    print(any_a_in_any_b(forbidden_places, url))
