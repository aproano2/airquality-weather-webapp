from flask import Flask, render_template, request, redirect, jsonify, url_for,\
                  flash, make_response
from flask import session as login_session
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
from database_setup import Base, Category, Item, User


app = Flask(__name__)
APPLICATION_NAME = "Weather and Air Quality Application"

# Connect to Database and create database session                                                    
engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)


@app.route('/categories/<int:category_id>/JSON')
def categoryItemsJSON(category_id):
    """Get all items in a category in json format                                                   
       category_id: Database id of the category

       Returns:
       json object
    """
    
    session = DBSession()
    points = session.query(Point).filter_by(
        category_id=category_id).all()
    return jsonify(Items=[i.serialize for i in points])

