from django.shortcuts import render
from doctor.models import SalinePatientEntry
import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import SalinePatientEntrySerializer
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.db.models import Max
from django.utils import timezone
from .utils import send_serial_data

def home(request):
    return render(request, "nurse/home.html")

def nurse_interface(request):

    patient_entry_obj = SalinePatientEntry.objects.all()
    context = {"obj":patient_entry_obj}
    return render(request, 'nurse/nurse_interface.html', context=context)


# Create your views here.
@api_view(['GET'])
def getData(request):
    app = SalinePatientEntry.objects.all()
    serializer = SalinePatientEntrySerializer(app, many=True)
    return Response(serializer.data)


# @csrf_exempt
# def compare_and_display(request):
#     # Step 1: Make a request to the Thingspeak API
#     api_key = "9GG4PNUDQERSCE13"
#     url = f"https://api.thingspeak.com/channels/2386238/feeds.json?api_key={api_key}"
#     response = requests.get(url)
    
#     # Step 2: Parse the JSON response
#     data = response.json()
#     channel_info = data.get("channel", {})
#     feeds = data.get("feeds", [])

#     # Step 3: Compare and filter relevant data
#     relevant_data = []
#     displayed_ids = set()  # To keep track of displayed patient IDs

#     for feed in feeds:
#         patient_id_from_api = feed.get("field2")
#         ml_value_from_api = feed.get("field1")

#         # Check if the patient ID exists in your database and hasn't been displayed yet
#         if (
#             SalinePatientEntry.objects.filter(id=patient_id_from_api).exists() and
#             patient_id_from_api not in displayed_ids
#         ):
#             # Add relevant data to the list
#             relevant_data.append({
#                 'patient_name': SalinePatientEntry.objects.get(id=patient_id_from_api),
#                 'patient_id': patient_id_from_api,
#                 'ml_value': ml_value_from_api,
#             })
            
#             # Mark the patient ID as displayed
#             displayed_ids.add(patient_id_from_api)

#             print(relevant_data)

#     # Step 4: Display a table with relevant information
#     return render(request, 'nurse/live_data.html', {'data': relevant_data})


@csrf_exempt
def compare_and_display(request):
    # Step 1: Make a request to the Thingspeak API
    api_key = "9GG4PNUDQERSCE13"
    url = f"https://api.thingspeak.com/channels/2386238/feeds.json?api_key={api_key}"
    response = requests.get(url)
    
    # Step 2: Parse the JSON response
    data = response.json()
    channel_info = data.get("channel", {})
    feeds = data.get("feeds", [])

    # Step 3: Compare and filter relevant data
    relevant_data = []
    latest_entries = {}

    for feed in feeds:
        patient_id_from_api = feed.get("field2")
        ml_value_from_api = feed.get("field1")
        entry_id = feed.get("entry_id")

        # Check if the patient ID is not None
        if patient_id_from_api is not None:
            # Compare and track the latest entry for each patient ID
            if (
                entry_id > latest_entries.get(patient_id_from_api, 0)
            ):
                latest_entries[patient_id_from_api] = entry_id

    # Fetch the detailed information for each patient's latest entry
    for patient_id, latest_entry_id in latest_entries.items():
        latest_entry_data = next(
            (feed for feed in feeds if feed.get("field2") == patient_id and feed.get("entry_id") == latest_entry_id),
            None
        )

        if latest_entry_data:
            if SalinePatientEntry.objects.get(id=patient_id).saline_ml == latest_entry_data.get("field1"):
                send_serial_data("*", port='COM4', baudrate=9600)
                time.sleep(3)
                
                relevant_data.append({
                    'patient_name': SalinePatientEntry.objects.get(id=patient_id),
                    'patient_id': patient_id,
                    'ml_value': latest_entry_data.get("field1"),
                    'entry_id': latest_entry_id,
                    'warning': readserial('COM4', 9600)
                })
            else:
                relevant_data.append({
                'patient_name': SalinePatientEntry.objects.get(id=patient_id),
                'patient_id': patient_id,
                'ml_value': latest_entry_data.get("field1"),
                'entry_id': latest_entry_id,
                'warning':"Sa low"
                    })




    # Step 4: Display a table with relevant information
    return render(request, 'nurse/live_data.html', {'data': relevant_data})