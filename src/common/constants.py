_forbidded_places = [
    'jagodno', 'komedy', 'kopycińskiego', 'awicenny', 'partynic', 'zwycięsk', 'buforow', 'psie pole', 'psim polu',
    'wojszyce', 'Nefrytow', 'Stabłowice', 'jordanowska', 'klecin', 'rogowsk', "maślic", "swojczyc",
    "złotnik", "Z dala od zgiełku miasta", "OŁTASZYN", "Łubinowa", "brochów", "Mińśk", "graniczn",
    "muchobór wielki", "Osiedle Malownicze", "marszowice", "Graniczna", "dzierżonia", "Tarasy Grabiszynsskie",
    "Tarasy Grabiszyns", "Parku Grabiszyńskiego", "Park Grabiszyński", "racławicka", "konna", "balonowa",
    "linia autobusowa 111", "Racławickiej", "dokerska", "kozanów", "olszewskiego", "kuźniki", "sarbinowsk",
    "pilczyc", "mały gądów", "borek", "iwaszkiewicza", 'kłodzk'
]

forbidden_places = [place.lower() for place in _forbidded_places] + [
    place.replace(' ', '-') for place in _forbidded_places
]

url = 'https://www.olx.pl/d/oferta/sprzedam-mieszkanie-w-atrakcyjnej-lokalizacji-2-pok-55-m2-CID3-IDMtRvq.html#7049ffa38d;promoted'

if __name__ == '__main__':
    from common.utils import any_a_in_any_b

    print(any_a_in_any_b(forbidden_places, url))
