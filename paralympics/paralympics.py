from flask import current_app as app
from paralympics.schemas import RegionSchema, EventSchema
from paralympics import db
from paralympics.models import Region, Event

# Flask-Marshmallow Schemas
regions_schema = RegionSchema(many=True)
region_schema = RegionSchema()
events_schema = EventSchema(many=True)
event_schema = EventSchema()

@app.get("/regions")
def get_regions():
    """Returns a list of NOC regions and their details in JSON."""
    # Select all the regions using Flask-SQLAlchemy
    all_regions = db.session.execute(db.select(Region)).scalars()
    # Get the data using Marshmallow schema (returns JSON)
    result = regions_schema.dump(all_regions)
    # Return the data
    return result

@app.get("/events")
def get_events():
    """Returns a list of paralympics events and their details in JSON."""
    # Select all the regions using Flask-SQLAlchemy
    all_events = db.session.execute(db.select(Event)).scalars()
    # Get the data using Marshmallow schema (returns JSON)
    result = events_schema.dump(all_events)
    # Return the data
    return result

@app.get("/events/<event_id>")
def event_id(event_id):
    """ Returns the event with the given id JSON.

    :param event_id: The id of the event to return
    :param type event_id: int
    :returns: JSON
    """
    event = db.session.execute(
        db.select(Event).filter_by(event_id=event_id)
    ).scalar_one_or_none()
    return events_schema.dump(event)

@app.route('/')
def hello():
    return f"Hello!"
