import csv

from batch.models import Category, State, Site, Iso, Region


def run():
    file = open("batch/unesco.csv")
    reader = csv.reader(file)
    next(reader)  # skip pasr header

    Category.objects.all().delete()
    State.objects.all().delete()
    Site.objects.all().delete()
    Iso.objects.all().delete()
    Region.objects.all().delete()

    n = 1

    for row in reader:
        # print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        # print(row)
        n += 1
        print(n)
        category, created = Category.objects.get_or_create(name=row[7])
        state, created = State.objects.get_or_create(name=row[8])
        region, created = Region.objects.get_or_create(name=row[9])
        iso, created = Iso.objects.get_or_create(name=row[10])
        site, created = Site.objects.get_or_create(name=row[0],
                                                   description=row[1],
                                                   justification=row[2],
                                                   year=row[3],
                                                   longitude=row[4],
                                                   latitude=row[5],
                                                   area_hectares=row[6],
                                                   category=category,
                                                   state=state,
                                                   region=region,
                                                   iso=iso,
                                                   )
        site.save()
        # print("TEst")
