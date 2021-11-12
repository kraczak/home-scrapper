from db.db_models import HomeDB

if __name__ == '__main__':
    homes = list(HomeDB.select())
    for home in homes:
        print(home.to_dataclass())