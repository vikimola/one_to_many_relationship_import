import csv


# to run:
# python manage.py runscript cats_load
from cats.models import Cat, Breed


def run():
    # fhand = open("cats/meow.csv")
    # reader = csv.reader(fhand)
    # next(reader)  # skip past header
    #
    # Cat.objects.all().delete()
    # Breed.objects.all().delete()
    #
    # for row in reader:
    #     print(row)
    #     b, created = Breed.objects.get_or_create(name=row[1])
    #     # get breed or create breed if it doesnt already exist
    #     # created -> Boolean -> True if created, False if not
    #     print(b, created)
    #     print("\n")
    #     c = Cat(nickname=row[0], breed=b, weight=row[2])
    #     c.save()
    print("TEst")
