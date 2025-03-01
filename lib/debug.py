#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Company, Dev, Freebie

if __name__ == '__main__':
    # Connect to the database
    engine = create_engine('sqlite:///freebies.db')
    
    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Place the ipdb breakpoint after the session is initialized
    import ipdb; ipdb.set_trace()
