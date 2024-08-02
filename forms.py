
import pandas as pd
from flask_wtf import FlaskForm

from wtforms import (
    SelectField,
    DateField,
    TimeField,
    IntegerField,
    SubmitField
)

from wtforms.validators import (
    DataRequired
)


# getting the data
train = pd.read_csv("E:/IIT Bombay/Placements/Projects/ML with Deployment/Flight Price Predictions_CampusX/Data/train.csv")
val = pd.read_csv("E:/IIT Bombay/Placements/Projects/ML with Deployment/Flight Price Predictions_CampusX/Data/val.csv")

X_data = pd.concat([train, val], axis=0).drop(columns="price")


class InputForm(FlaskForm):
    airline = SelectField(
        label="Airline",
        choices=X_data.airline.unique().tolist(),     #unique converts 'pandas series' to 'np array'; tolist converts it to 'python list'
        validators=[DataRequired()]
    )

    date_of_journey= DateField(
        label="Date of Journey",
        validators=[DataRequired()]  
    )
    source = SelectField(
        label="Source",
        choices=X_data.source.unique().tolist(),     #unique converts 'pandas series' to 'np array'; tolist converts it to 'python list'
        validators=[DataRequired()]
    )
    destination= SelectField(
        label="Destination",
        choices=X_data.destination.unique().tolist(),     #unique converts 'pandas series' to 'np array'; tolist converts it to 'python list'
        validators=[DataRequired()]
    )
    dep_time= TimeField(
        label="Departure Time",
        validators= [DataRequired()]
    )
    arrival_time= TimeField(
        label="Arrival Time",
        validators= [DataRequired()]
    )
    duration= IntegerField(
        label= "Duration",
        validators= [DataRequired()]
    )
    total_stops= IntegerField(
        label= "Total Stops",
        validators= [DataRequired()]
    )
    additional_info= SelectField(
       label= "Additional Info",
       choices= X_data.additional_info.unique().tolist(),
       validators=[DataRequired()]
    )
    submit= SubmitField("Predict")
