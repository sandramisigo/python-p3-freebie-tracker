#!/usr/bin/env python3

from models import Company, Dev, Freebie, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Connect to the database
engine = create_engine('sqlite:///freebies.db')
Session = sessionmaker(bind=engine)
session = Session()

# Create all tables if they don't exist
Base.metadata.create_all(engine)

# Clear existing data
session.query(Freebie).delete()
session.query(Dev).delete()
session.query(Company).delete()

# Create some companies
company1 = Company(name='TechCorp', founding_year=2005)
company2 = Company(name='WebDev Inc', founding_year=2010)

# Create some devs
dev1 = Dev(name='Alice')
dev2 = Dev(name='Bob')

# Create some freebies
freebie1 = Freebie(item_name='T-shirt', value=20, company=company1, dev=dev1)
freebie2 = Freebie(item_name='Sticker', value=5, company=company2, dev=dev2)
freebie3 = Freebie(item_name='Mug', value=10, company=company1, dev=dev2)

# Add to the session and commit
session.add_all([company1, company2, dev1, dev2, freebie1, freebie2, freebie3])
session.commit()

print("Seed data created!")
