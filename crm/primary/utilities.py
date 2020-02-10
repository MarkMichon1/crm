from django.contrib.auth.models import User

from .models import Comment, Customer, Job, Technician

def reset_app_sample_state():
    '''This resets the state of the application, removing models and repopulating the tables with sample data.  Used
    to quickly reset the application if someone played around with it, and for dev/debugging purposes.'''

    # Refresh User object data
    User.objects.all().delete()
    user_data_list = [
        []
    ]

    # Refresh Customer object data
    Customer.objects.all().delete()
    customer_data_list = [
        ['John', 'Smith', '123 Example Street', 'Naperville', 'IL', '60540', '6304587412'],
        ['Jane', 'Doe', '321 Willowbrook Ln', 'Naperville', 'IL', '60431', '6309562314'],
        ['Roger', 'Jones', '111 Forest Grove Dr', 'Lisle', 'IL', '60565', '6301597538'],
        ['Rick', 'Johnson', '555 Sandy Creek Rd', 'Willowbrook', 'IL', '60789', '6309983636'],
        ['Chris', 'Thompson', '1 Vincent Court', 'Naperville', 'IL', '60549', '6301234546'],
        ['Ken', 'Williams', '7 Williams Blvd', 'Aurora', 'IL', '60123', '6309876543'],
        ['Claudia', 'Brown', '6 Oak St', 'Naperville', 'IL', '60891', '6305551212'],
        ['Walter', 'Davis', '1683 Pine St', 'St Charles', 'IL', '60531', '6306379017'],
        ['Leopold', 'Wilson', '1434 Spruce St', 'Naperville', 'IL', '60391', '6305918092'],
        ['Conrad', 'Anderson', '3656 Example Blvd', 'Batavia', 'IL', '60248', '6303623883'],
        ['Lydia', 'Taylor', '12 W Example St', 'Bolingbrook', 'IL', '60987', '6308095091'],
        ['Alice', 'Westman', '465 E Example St', 'Burr Ridge', 'IL', '60123', '6303318092'],
        ['Alex', 'Phillips', '1123 Colingwood St', 'Westmont', 'IL', '60874', '6304051813'],
        ['Mary', 'Singh', '1 Example St', 'Hinsdale', 'IL', '60563', '6309014010'],
    ]
    for customer in customer_data_list:
        new_customer = Customer(first_name=customer[0], last_name=customer[1], street_address=customer[2],
                                city=customer[3], state=customer[4], zip_code=customer[5], phone_number=customer[6])
        new_customer.save()