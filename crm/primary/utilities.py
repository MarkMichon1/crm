from django.contrib.auth.models import User
import lorem

import datetime
import random

from .models import Customer, Job, Technician

def generate_fake_identity(quantity_desired, email=False):
    first_names = ['James', 'David', 'John', 'Robert', 'Michael', 'William', 'David', 'Richard', 'Charles', 'Joseph',
                   'Thomas', 'Christopher', 'Daniel', 'Paul', 'Mark', 'Donald', 'George', 'Kenneth', 'Steven', 'Edward',
                   'Brian', 'Ronald', 'Anthony', 'Kevin', 'Jason', 'Jeff', 'Mary', 'Patricia', 'Linda', 'Barbara',
                   'Elizabeth', 'Jennifer', 'Maria', 'Susan', 'Margaret', 'Dorothy', 'Lisa', 'Nancy', 'Karen', 'Betty',
                   'Helen', 'Sandra', 'Donna', 'Carol', 'Ruth', 'Sharon', 'Michelle', 'Laura', 'Sarah', 'Kimberly',
                   'Deborah']
    last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Rodriguez',
                  'Martinez', 'Hernandez', 'Lopez', 'Gonzalez', 'Wilson', 'Anderson', 'Thomas', 'Taylor', 'Moore',
                  'Jackson', 'Martin', 'Lee', 'Perez', 'Thompson', 'White', 'Harris', 'Sanchez', 'Clark', 'Ramirez',
                  'Lewis', 'Robinson', 'Walker', 'Young', 'Allen', 'King', 'Wright', 'Scott', 'Torres', 'Nguyen',
                  'Hill', 'Flores', 'Green', 'Adams', 'Nelson', 'Baker', 'Hall', 'Rivera', 'Campbell', 'Mitchell',
                  'Carter', 'Roberts']
    street_names = ['Main', '2nd', '1st', '3rd', '4th', '5th', 'Park', '6th', 'Oak', 'Maple', 'Pine', 'Washington',
                    'Cedar', 'Elm', 'Walnut', 'Lake', 'Sunset', 'Lincoln', 'Jackson', 'Church', 'River', 'Willow',
                    'Jefferson', 'Center', 'North', 'Lakeview', 'Ridge', 'Hickory', 'Adams', 'Cherry', 'Highland',
                    'Johnson', 'South', 'Dogwood', 'West', 'Chestnut', 'Spruce', 'Wilson', 'Meadow', 'Forest', 'Hill',
                    'Madison']
    street_suffixes = ['Rd', 'Blvd', 'St', 'Ave', 'Ln', 'Pl', 'Fwy', 'Ct']
    city_names = ['Naperville', 'Bolingbrook', 'Woodridge', 'Downers Grove', 'Warrenville', 'Lemont', 'Burr Ridge',
                  'Willowbrook', 'Hinsdale', 'Western Springs', 'Oak Brook', 'Lisle']
    email_domains = ['gmail', 'yahoo', 'msm', 'outlook', 'icloud']
    identity_list = []

    for individual in range(quantity_desired):
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        street_address = f'{random.randint(1, 9999)} {random.choice(street_names)} {random.choice(street_suffixes)}'
        city = random.choice(city_names)
        zip_code = random.randint(60001, 62999)
        phone_number = random.randint(6300000000, 8159999999)
        if email:
            generated_email = f'{first_name.lower()}{last_name.lower()}{random.randint(1, 9999)}' \
                              f'@{random.choice(email_domains)}.com'
            identity = (first_name, last_name, street_address, city, zip_code, phone_number, generated_email)
        else:
            identity = (first_name, last_name, street_address, city, zip_code, phone_number)
        identity_list.append(identity)
    return identity_list

def reset_app_sample_state():
    '''This resets the state of the application, removing models and repopulating the tables with sample data.  Used
    to quickly reset the application if someone played around with it, and for dev/debugging purposes.'''

    TOTAL_CUSTOMERS = random.randint(75, 150)
    TOTAL_TECHNICIANS = random.randint(20, 30)
    TOTAL_JOBS = random.randint(300, 400)


    # Refresh User object data
    User.objects.all().delete()
    demo_user = User(first_name='Test', last_name='User', username='TestUser')
    demo_user.set_password('testPassword12321')
    demo_user.save()

    Customer.objects.all().delete()
    Job.objects.all().delete()
    Technician.objects.all().delete()

    # Generate Customer object data
    customer_identities = generate_fake_identity(TOTAL_CUSTOMERS)
    for customer in customer_identities:
        new_customer = Customer(first_name=customer[0], last_name=customer[1], street_address=customer[2],
                                city=customer[3], state='IL', zip_code=customer[4], phone_number=customer[5],
                                author=demo_user)
        new_customer.save()

    # Generate Technician object data
    technician_identities = generate_fake_identity(TOTAL_TECHNICIANS, email=True)
    for technician in technician_identities:
        if random.randrange(100) < 80:
            is_active = True
        else:
            is_active = False
        new_technician = Technician(first_name=technician[0], last_name=technician[1], street_address=technician[2],
                                city=technician[3], state='IL', zip_code=technician[4], phone_number=technician[5],
                                email=technician[6], is_active=is_active, author=demo_user)
        new_technician.save()

    # Generate Job object data
    customers = Customer.objects.all()
    technicians = Technician.objects.all()
    for job in range(TOTAL_JOBS):
        random_customer = random.choice(customers)
        random_technicians = random.choices(technicians, k=random.randrange(1, 5))
        if random.randrange(100) < 95:
            is_complete = True
            date_completed = datetime.datetime.now()
        else:
            is_complete = False
            date_completed = None
        cost_of_job = random.randrange(100, 1000)
        job_details = lorem.paragraph()

        new_job = Job(author=demo_user, customer=random_customer, cost_of_job=cost_of_job, is_complete=is_complete,
                      date_completed=date_completed, job_details=job_details)
        new_job.save()
        for random_technician in random_technicians:
            new_job.technicians.add(random_technician)
        new_job.save()