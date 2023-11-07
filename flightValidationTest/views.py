# appname/views.py
from django.http import request
from django.views.generic.edit import CreateView, FormView
from .models import FlightValidation
from .forms import FlightValidationForm
import requests

class FlightValidationView(FormView):
    form_class = FlightValidationForm
    template_name = 'flight_validation.html'
    success_url = '/success/'  # Redirect to a success page

    def __int__(self):
        form_flight_number = None

    def form_valid(self, form):
        form_flight_number = form.cleaned_data.get('textbox_data')

        # TODO: for more API tweaks see the official documentation
        params = {
            'access_key': 'ffa7b0f3717e11df631bcf72e87e1a6e',
            'flight_iata': form_flight_number,
            'flight_status': 'scheduled',
            # 'flight_date': '2023-11-08',
        }

        api_result = requests.get('http://api.aviationstack.com/v1/flights', params)

        api_response = api_result.json()

        print(api_response)

        for flight in api_response["data"]:
            if not flight["arrival"]["actual"]:
                print("Found such flight!")

        # if not api_response["data"]:
        #     print("Error: Found no such flight!")
        # else:
        #     print("Found such flight!")

        # for flight in api_response['results']:
        #     if (flight['live']['is_ground'] is False):
        #         print(u'%s flight %s from %s (%s) to %s (%s) is in the air.' % (
        #             flight['airline']['name'],
        #             flight['flight']['iata'],
        #             flight['departure']['airport'],
        #             flight['departure']['iata'],
        #             flight['arrival']['airport'],
        #             flight['arrival']['iata']))

        return super().form_valid(form)