from paralympics.models import Event, Region
from paralympics import db, ma

# Flask-Marshmallow Schemas
# See https://marshmallow-sqlalchemy.readthedocs.io/en/latest/#generate-marshmallow-schemas

class RegionSchema(ma.SQLAlchemySchema):
    """Marshmallow schema defining the attributes for creating a new region."""

    class Meta:
        model = Region
        load_instance = True
        sqla_session = db.session
        include_relationships = True

    NOC = ma.auto_field()
    region = ma.auto_field()
    notes = ma.auto_field()


class EventSchema(ma.SQLAlchemyAutoSchema):
    """Marshmallow schema for the attributes of an event class. Inherits all the attributes from the Event class."""

    class Meta:
        model = Event
        include_fk = True
        load_instance = True
        sqla_session = db.session
        include_relationships = True

"""
    type = ma.auto_field()
    year = ma.auto_field()
    country = ma.auto_field()
    host = ma.auto_field()
    NOC = ma.auto_field()
    region = ma.auto_field()
    start = ma.auto_field()
    end = ma.auto_field()
    duration = ma.auto_field()
    disabilities_included = ma.auto_field()
    countries = ma.auto_field()
    events = ma.auto_field()
    athletes = ma.auto_field()
    sports = ma.auto_field()
    participants_m = ma.auto_field()
    participants_f = ma.auto_field()
    participants = ma.auto_field()
    highlights = ma.auto_field()
"""