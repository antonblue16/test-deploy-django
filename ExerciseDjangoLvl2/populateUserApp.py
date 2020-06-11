import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ExerciseDjangoLvl2.settings')

import django
django.setup()

from faker import Faker
from userApp.models import UserData

fake = Faker()


def populate(N=5):

    for i in range(1,N+1):
        fake_name = fake.name()
        flagName = fake_name.split()

        fake_firstName = flagName[0]
        fake_lastName = flagName[1]

        fake_email = fake.email()
        fake_address = fake.address()

        #print("\t{}\n First Name:{},\n Last Name:{},\n Email:{},\n Address:{}\n".format(i, fake_firstName, fake_lastName, fake_email, fake_address))
        user = UserData.objects.get_or_create(firstName=fake_firstName, lastName=fake_lastName, email=fake_email, address=fake_address)[0]

if __name__ == "__main__":
    print("Populating faker Script!")
    populate(20)
    print("Complete!")