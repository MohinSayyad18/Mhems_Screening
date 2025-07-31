from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.

#__________________SCREENING INFO (GET & POST Method)____________
@api_view(['GET', 'POST'])
def agg_sc_screening_info_ViewSet1(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = agg_sc_basic_screening_info.objects.all()
        serializer = agg_sc_screening_info_Serializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = agg_sc_screening_info_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#__________________END VITAL_API(GET INFO API(GET & POST Method)____________________ 

#__________________ SCREENING INFO API(GET & PUT,DELETE Method)____________________
@api_view(['GET', 'PUT', 'DELETE'])
def agg_sc_screening_info_Details_ViewSet1(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = agg_sc_basic_screening_info.objects.get(pk=pk)
    except agg_sc_basic_screening_info.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer =agg_sc_screening_info_Serializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = agg_sc_screening_info_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
#__________________________________END API__________________________________


#__________________PYCHO INFO (GET & POST Method)____________
@api_view(['GET', 'POST'])
def agg_sc_pycho_info_ViewSet1(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = agg_sc_pycho_info.objects.all()
        serializer = agg_sc_pycho_info_Serializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = agg_sc_pycho_info_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#__________________END PYCHO_API(GET INFO API(GET & POST Method)____________________ 

#__________________ PYCHO INFO API(GET & PUT,DELETE Method)____________________
@api_view(['GET', 'PUT', 'DELETE'])
def agg_sc_pycho_info_Details_ViewSet1(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = agg_sc_pycho_info.objects.get(pk=pk)
    except agg_sc_pycho_info.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer =agg_sc_pycho_info_Serializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = agg_sc_pycho_info_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
#__________________________________END API__________________________________

#__________________BMI INFO (GET & POST Method)____________
@api_view(['GET', 'POST'])
def agg_sc_bmi_info_ViewSet1(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = agg_sc_bmi_info.objects.all()
        serializer = agg_sc_bmi_info_Serializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = agg_sc_bmi_info_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#__________________END BMI INFO_API(GET INFO API(GET & POST Method)____________________ 

#__________________ BMI INFO API(GET & PUT,DELETE Method)____________________
@api_view(['GET', 'PUT', 'DELETE'])
def agg_sc_bmi_info_Details_ViewSet1(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = agg_sc_bmi_info.objects.get(pk=pk)
    except agg_sc_bmi_info.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer =agg_sc_bmi_info_Serializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = agg_sc_bmi_info_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
#__________________________________END API__________________________________


#__________________Schedule Screening INFO (GET & POST Method)____________
@api_view(['GET', 'POST'])
def agg_sc_shedule_screening_info_ViewSet1(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = agg_sc_shedule_screening_info.objects.all()
        serializer = agg_sc_shedule_screening_info_Serializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = agg_sc_shedule_screening_info_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#__________________END Schedule Screening INFO_API(GET INFO API(GET & POST Method)____________________ 

#__________________ Schedule Screening INFO API(GET & PUT,DELETE Method)____________________
@api_view(['GET'])
def start_screening_info_ViewSet1(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        screenings = agg_sc_start_screening.objects.all()
        serialized_data = []

        for screening in screenings:
            # Serialize the screening data using the serializer
            serializer = agg_sc_start_screening_Serializer(screening)
            serialized_data.append(serializer.data)
            
            # Retrieve citizen details from the related agg_sc_add_new_citizens instance
            citizen_name = screening.citizen_id.child_name
            citizen_mobile = screening.citizen_id.parents_mobile
            
            # Add citizen_name and citizen_mobile to the serialized data
            serialized_data[-1]['citizen_name'] = citizen_name
            serialized_data[-1]['citizen_mobile'] = citizen_mobile

        return Response(serialized_data)
#__________________________________END API__________________________________


#______________________GET & POST___________________________
@api_view(['GET', 'POST'])
def add_new_source_info_ViewSet1(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = agg_sc_add_new_source.objects.all()
        serializer = add_new_source_Serializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = add_new_source_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

#___________________GET,POST,DELETE_______________________________
@api_view(['GET', 'PUT', 'DELETE'])
def agg_sc_add_new_source_Details_ViewSet1(request, pk):
    """ 
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = agg_sc_add_new_source.objects.get(pk=pk)
    except agg_sc_add_new_source.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer =add_new_source_Serializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = add_new_source_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    



#_______________START SCREENING_______________________#
@api_view(['GET', 'PUT', 'DELETE'])
def start_screening_info_Details_ViewSet1(request, pk):
    """ 
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = agg_sc_start_screening.objects.get(pk=pk)
    except agg_sc_start_screening.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer =agg_sc_start_screening_Serializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = agg_sc_start_screening_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    






##################################################################
##################################################################
#__________________ADD NEW CITIZEN (GET Method)____________
@api_view(['GET'])
def agg_sc_add_new_citizen_get_info_ViewSet1(request):
    """
    List all code snippets, or create a new snippet.
    """
    request.method == 'GET'
    snippets = agg_sc_add_new_citizens.objects.filter(is_deleted=False)
    serializer = agg_sc_add_new_citizens_Serializer(snippets, many=True)
    return Response(serializer.data)

#__________________END ADD NEW CITIZEN (GET Method)_____________________#

#__________________ADD NEW CITIZEN (POST Method)________________________#
# @api_view(['POST'])
# def agg_sc_add_new_citizen_post_info_ViewSet1(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     request.method == 'POST'
#     serializer = agg_sc_add_new_citizens_Serializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def agg_sc_add_new_citizen_post_info_ViewSet1(request):
    if request.method == 'POST':
        # Create the new citizen record
        serializer = agg_sc_add_new_citizens_Serializer(data=request.data)
        if serializer.is_valid():
            new_citizen = serializer.save()

            # Extract the source_name from the newly added citizen's data
            source_name = new_citizen.source_name

            # Find the schedules that match the source_name
            schedules = agg_sc_shedule_screening_info.objects.filter(source_name=source_name)

            # Check if there are schedules for this source_name
            if schedules.exists():
                # Get the schedule_ids as a list
                schedule_ids = [schedule.schedule_id for schedule in schedules]

                # Check if an entry with the same citizen_id and any of the schedule_ids already exists
                existing_entry = agg_sc_citizen_schedule.objects.filter(
                    citizen_id=new_citizen.citizens_id,
                    schedule_id__in=schedule_ids,
                ).first()

                # If no existing entry is found, assign the new citizen to one of the schedules
                if not existing_entry:
                    agg_sc_citizen_schedule.objects.create(
                        citizen_id=new_citizen.citizens_id,
                        schedule_id=schedule_ids[0],  # Assign to the first schedule in the list
                    )

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#__________________END ADD NEW CITIZEN (POST Method)_______________________#

#__________________ADD NEW CITIZEN (PUT/UPDATE Method)________________________#
@api_view(['GET','PUT'])
def agg_sc_add_new_citizen_put_info_ViewSet1(request, pk):
    """ 
    update code snippet.
    """
    try:
        snippet = agg_sc_add_new_citizens.objects.get(pk=pk)
    except agg_sc_add_new_citizens.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer =agg_sc_add_new_citizens_Serializer(snippet)
        return Response(serializer.data)


    elif request.method == 'PUT':
        serializer = agg_sc_add_new_citizens_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#__________________END ADD NEW CITIZEN (PUT Method)_______________________# 

#__________________ADD NEW CITIZEN (DELETE Method)_______________________# 
@api_view(['GET', 'DELETE'])
def agg_sc_add_new_citizen_delete_info_ViewSet1(request, pk):
    try:
        snippet = agg_sc_add_new_citizens.objects.filter(is_deleted=False).get(pk=pk)
    except agg_sc_add_new_citizens.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = agg_sc_add_new_citizens_Serializer(snippet)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        # Soft delete the record by setting is_deleted to True
        snippet.is_deleted = True
        snippet.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

#__________________END ADD NEW CITIZEN (DELETE Method)_______________________# 


#__________________ADD NEW SCHEDULE (GET Method)_______________________#
@api_view(['GET'])
def agg_sc_add_new_schedule_get_info_ViewSet1(request):
    """
    List all code snippets, or create a new snippet.
    """
    request.method == 'GET'
    snippets = agg_sc_shedule_screening_info.objects.filter(is_deleted=False)
    serializer = agg_sc_shedule_screening_info_Serializer(snippets, many=True)
    return Response(serializer.data)

#__________________END ADD NEW SCHEDULE (GET Method)_____________________#

#__________________ADD NEW SCHEDULE (POST Method)________________________#
# @api_view(['POST'])
# def agg_sc_add_new_schedule_post_info_ViewSet1(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     request.method == 'POST'
#     serializer = agg_sc_shedule_screening_info_Serializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response


@api_view(['POST'])
def agg_sc_add_new_schedule_post_info_ViewSet1(request):
    """
    Create a new screening schedule and retrieve citizens under the added source name.
    """
    if request.method == 'POST':
        # Create a new screening schedule
        serializer = agg_sc_shedule_screening_info_Serializer(data=request.data)
        if serializer.is_valid():
            new_schedule = serializer.save()

            try:
                # Retrieve citizens under the added source name
                source_name = new_schedule.source_name
                citizens_under_source = agg_sc_add_new_citizens.objects.filter(source_name=source_name)

                # Get the latest schedule count for this source
                latest_schedule_count_entry = agg_sc_citizen_schedule.objects.filter(
                    schedule_id=new_schedule.schedule_id
                ).order_by('-pk_id').first()

                if latest_schedule_count_entry:
                    # If there is a previous entry for this schedule, get its schedule count
                    schedule_count = int(latest_schedule_count_entry.schedule_count)
                else:
                    # If it's the first entry for this schedule, set the schedule count to 1
                    schedule_count = 1

                # Create entries in the agg_sc_citizen_schedule table for each citizen under the source
                for citizen in citizens_under_source:
                    schedule_entry = agg_sc_citizen_schedule(
                        schedule_count=schedule_count,
                        citizen_id=citizen.citizens_id,
                        schedule_id=new_schedule.schedule_id,
                        added_by=new_schedule.screening_person_name,
                        modify_by=new_schedule.screening_person_name,
                    )
                    schedule_entry.save()

                # Increment the schedule count for the next schedule
                schedule_count += 1

                # Update the schedule count in the latest schedule entry
                if latest_schedule_count_entry:
                    latest_schedule_count_entry.schedule_count = schedule_count
                    latest_schedule_count_entry.save()

                # Return a response with the schedule data and the schedule count
                response_data = {
                    "schedule_id": new_schedule.schedule_id,
                    "from_date": new_schedule.from_date,
                    "to_date": new_schedule.to_date,
                    "source_name": new_schedule.source_name,
                    "source_district": new_schedule.source_district,
                    "disease": new_schedule.disease,
                    "screening_person_name": new_schedule.screening_person_name,
                    "mobile_no": new_schedule.mobile_no,
                    "is_deleted": new_schedule.is_deleted,
                    "schedule_count": schedule_count,
                }

                return Response(response_data, status=status.HTTP_201_CREATED)

            except Exception as e:
                # Handle any exceptions gracefully and return an appropriate error response
                error_message = str(e)
                return Response({"error": error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#__________________END ADD NEW SCHEDULE (POST Method)_______________________#

#__________________ADD NEW SCHEDULE (PUT/UPDATE Method)________________________#
@api_view(['GET','PUT'])
def agg_sc_add_new_schedule_put_info_ViewSet1(request, pk):
    """ 
    update code snippet.
    """
    try:
        snippet = agg_sc_shedule_screening_info.objects.get(pk=pk)
    except agg_sc_shedule_screening_info.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer =agg_sc_shedule_screening_info_Serializer(snippet)
        return Response(serializer.data)


    elif request.method == 'PUT':
        serializer = agg_sc_shedule_screening_info_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#__________________END ADD NEW SCHEDULE (PUT Method)_______________________# 

#__________________ADD NEW SCHEDULE (DELETE Method)_______________________# 
@api_view(['GET', 'DELETE'])
def agg_sc_add_new_schedule_delete_info_ViewSet1(request, pk):
    try:
        # Include a filter to exclude soft-deleted records
        snippet = agg_sc_shedule_screening_info.objects.filter(is_deleted=False).get(pk=pk)
    except agg_sc_shedule_screening_info.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = agg_sc_shedule_screening_info_Serializer(snippet)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        if not snippet.is_deleted:  # Check if it's already marked as deleted
            # Soft delete the record by setting is_deleted to True
            snippet.is_deleted = True
            snippet.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

#__________________END ADD NEW SCHEDULE (DELETE Method)_______________________# 

#_______________START SCREENING_______________________#

@api_view(['GET'])
def start_screening_info_ViewSet1(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        screenings = agg_sc_start_screening.objects.all()
        serialized_data = []

        for screening in screenings:
            # Serialize the screening data using the serializer
            serializer = agg_sc_start_screening_Serializer(screening)
            serialized_data.append(serializer.data)
            
            # Retrieve citizen details from the related agg_sc_add_new_citizens instance
            citizen_name = screening.citizen_id.citizen_name
            citizen_mobile = screening.citizen_id.parents_mobile
            
            # Add citizen_name and citizen_mobile to the serialized data
            serialized_data[-1]['citizen_name'] = citizen_name
            serialized_data[-1]['citizen_mobile'] = citizen_mobile

        return Response(serialized_data)

#__________________ADD NEW SOURCE (GET Method)_______________________#
@api_view(['GET'])
def agg_sc_add_new_source_get_info_ViewSet1(request):
    """
    List all code snippets, or create a new snippet.
    """
    request.method == 'GET'
    snippets = agg_sc_add_new_source.objects.all()
    serializer = add_new_source_Serializer(snippets, many=True)
    return Response(serializer.data)

#__________________END ADD NEW SOURCE (GET Method)_____________________#

#__________________ADD NEW SOURCE (POST Method)________________________#
@api_view(['POST'])
def agg_sc_add_new_source_post_info_ViewSet1(request):
    """
    List all code snippets, or create a new snippet.
    """
    request.method == 'POST'
    serializer = add_new_source_Serializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#__________________END ADD NEW SOURCE (POST Method)_______________________#

#__________________ADD NEW SOURCE (PUT/UPDATE Method)________________________#
@api_view(['GET','PUT'])
def agg_sc_add_new_source_put_info_ViewSet1(request, pk):
    """ 
    update code snippet.
    """
    try:
        snippet = agg_sc_add_new_source.objects.get(pk=pk)
    except agg_sc_add_new_source.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer =add_new_source_Serializer(snippet)
        return Response(serializer.data)


    elif request.method == 'PUT':
        serializer = add_new_source_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#__________________END ADD NEW SOURCE (PUT Method)_______________________# 

#__________________ADD NEW SOURCE (DELETE Method)_______________________# 
@api_view(['GET','DELETE'])
def agg_sc_add_new_source_delete_info_ViewSet1(request, pk):
    """ 
    delete a code snippet.
    """
    try:
        snippet = agg_sc_add_new_source.objects.get(pk=pk)
    except agg_sc_add_new_source.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer =add_new_source_Serializer(snippet)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#__________________END ADD NEW SOURCE (DELETE Method)_______________________# 



#Getting Details from add new citizen table.
#__________________GET ONLY CHILD BASIC INFO (GET Method)_______________________#
@api_view(['GET'])
def agg_sc_get_child_basic_info_ViewSet1(request):
    """
    List all code snippets, or create a new snippet.
    """
    request.method == 'GET'
    snippets = agg_sc_add_new_citizens.objects.all()
    serializer = child_basic_info_Serializer(snippets, many=True)
    return Response(serializer.data)

#__________________END CHILD BASIC INFO (GET Method)_____________________#
#__________________GET ONLY CHILD BASIC INFO (POST Method)_______________________#
@api_view(['POST'])
def agg_sc_post_child_basic_info_ViewSet1(request):
    """
    List all code snippets, or create a new snippet.
    """
    request.method == 'POST'
    serializer = child_basic_info_Serializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#__________________END  CHILD BASIC INFO (POST Method)_____________________#

#__________________ CHILD BASIC INFO (PUT/UPDATE Method)________________________#
@api_view(['GET','PUT'])
def agg_sc_put_child_basic_info_ViewSet1(request, pk):
    """ 
    update code snippet.
    """
    try:
        snippet = agg_sc_add_new_citizens.objects.get(pk=pk)
    except agg_sc_add_new_citizens.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer =child_basic_info_Serializer(snippet)
        return Response(serializer.data)


    elif request.method == 'PUT':
        serializer = child_basic_info_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#__________________END  CHILD BASIC INFO (PUT Method)_______________________# 
#__________________ADD CHILD BASIC INFO (DELETE Method)_______________________# 
@api_view(['GET','DELETE'])
def agg_sc_delete_child_basic_info_ViewSet1(request, pk):
    """ 
    delete a code snippet.
    """
    try:
        snippet = agg_sc_add_new_citizens.objects.get(pk=pk)
    except agg_sc_add_new_citizens.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer =child_basic_info_Serializer(snippet)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#__________________END ADD CHILD BASIC INFO (DELETE Method)_______________________# 
#Getting Family Address from add new citizen table.
#__________________GET ONLY CHILD ADDRESS INFO (GET Method)_______________________#
@api_view(['GET'])
def agg_sc_get_child_address_info_ViewSet1(request):
    """
    List all code snippets, or create a new snippet.
    """
    request.method == 'GET'
    snippets = agg_sc_add_new_citizens.objects.all()
    serializer = child_address_info_Serializer(snippets, many=True)
    return Response(serializer.data)

#__________________END CHILD ADDRESS INFO (GET Method)_____________________#
#__________________GET ONLY CHILD ADDRESS INFO (POST Method)_______________________#
@api_view(['POST'])
def agg_sc_post_child_address_info_ViewSet1(request):
    """
    List all code snippets, or create a new snippet.
    """
    request.method == 'POST'
    serializer = child_address_info_Serializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#__________________END  CHILD ADDRESS INFO (POST Method)_____________________#

#__________________ CHILD ADDRESS INFO (PUT/UPDATE Method)________________________#
@api_view(['GET','PUT'])
def agg_sc_put_child_address_info_ViewSet1(request, pk):
    """ 
    update code snippet.
    """
    try:
        snippet = agg_sc_add_new_citizens.objects.get(pk=pk)
    except agg_sc_add_new_citizens.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer =child_address_info_Serializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = child_address_info_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#__________________END  CHILD ADDRESS INFO (PUT Method)_______________________# 
#__________________ADD CHILD ADDRESS INFO (DELETE Method)_______________________# 
@api_view(['GET','DELETE'])
def agg_sc_delete_child_address_info_ViewSet1(request, pk):
    """ 
    delete a code snippet.
    """
    try:
        snippet = agg_sc_add_new_citizens.objects.get(pk=pk)
    except agg_sc_add_new_citizens.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer =child_address_info_Serializer(snippet)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#__________________END ADD CHILD ADDRESS INFO (DELETE Method)_______________________# 



#Getting GROWTH INFO from add new citizen table.
#__________________GET ONLY CHILD GROWTH INFO (GET Method)_______________________#
@api_view(['GET'])
def agg_sc_get_child_bmi_info_ViewSet1(request):
    """
    List all code snippets, or create a new snippet.
    """
    request.method == 'GET'
    snippets = agg_sc_add_new_citizens.objects.all()
    serializer = child_growth_info_Serializer(snippets, many=True)
    return Response(serializer.data)

#__________________END CHILD GROWTH INFO (GET Method)_____________________#
#__________________GET ONLY CHILD GROWTH INFO (POST Method)_______________________#
@api_view(['POST'])
def agg_sc_post_child_bmi_info_ViewSet1(request):
    """
    List all code snippets, or create a new snippet.
    """
    request.method == 'POST'
    serializer = child_growth_info_Serializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#__________________END  CHILD GROWTH INFO (POST Method)_____________________#

#__________________ CHILD GROWTH INFO (PUT/UPDATE Method)________________________#
@api_view(['GET', 'PUT'])
def agg_sc_put_child_bmi_info_ViewSet1(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = agg_sc_add_new_citizens.objects.get(pk=pk)
    except agg_sc_add_new_citizens.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer =child_growth_info_Serializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = child_growth_info_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#__________________END  CHILD GROWTH INFO (PUT Method)_______________________# 
#__________________ADD CHILD GROWTH INFO (DELETE Method)_______________________# 
@api_view(['GET','DELETE'])
def agg_sc_delete_child_bmi_info_ViewSet1(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = agg_sc_add_new_citizens.objects.get(pk=pk)
    except agg_sc_add_new_citizens.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer =child_growth_info_Serializer(snippet)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#__________________END ADD CHILD GROWTH INFO (DELETE Method)_______________________# 


#__________________GET CHILD VITAL INFO (GET Method)_______________________#
@api_view(['GET'])
def agg_sc_get_child_vital_info_ViewSet1(request):
    """
    List all code snippets, or create a new snippet.
    """
    request.method == 'GET'
    snippets = agg_sc_vital_info.objects.all()
    serializer = agg_sc_vital_info_Serializer(snippets, many=True)
    return Response(serializer.data)

#__________________END CHILD VITAL INFO (GET Method)_____________________#
#__________________GET CHILD VITAL INFO (POST Method)_______________________#
@api_view(['POST'])
def agg_sc_post_child_vital_info_ViewSet1(request):
    """
    List all code snippets, or create a new snippet.
    """
    request.method == 'POST'
    serializer = agg_sc_vital_info_Serializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#__________________END  CHILD VITAL INFO (POST Method)_____________________#

#__________________ CHILD VITAL INFO (PUT/UPDATE Method)________________________#
@api_view(['GET', 'PUT'])
def agg_sc_put_child_vital_info_ViewSet1(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = agg_sc_vital_info.objects.get(pk=pk)
    except agg_sc_vital_info.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer =agg_sc_vital_info_Serializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = agg_sc_vital_info_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#__________________END  CHILD VITAL INFO (PUT Method)_______________________# 
#__________________ADD CHILD VITAL INFO (DELETE Method)_______________________# 
@api_view(['GET','DELETE'])
def agg_sc_delete_child_vital_info_ViewSet1(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = agg_sc_vital_info.objects.get(pk=pk)
    except agg_sc_vital_info.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer =agg_sc_vital_info_Serializer(snippet)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#__________________END ADD CHILD VITAL INFO (DELETE Method)_______________________# 


#_____________________________________________________________________
#___________________________STATE_____________________________________
#__________________GET STATE INFO (GET Method)_______________________#
@api_view(['GET'])
def agg_sc_get_state_info_ViewSet1(request):
    """
    List all code snippets, or create a new snippet.
    """
    request.method == 'GET'
    snippets = agg_sc_State.objects.all()
    serializer = agg_sc_state_info_Serializer(snippets, many=True)
    return Response(serializer.data)
#_________________END GET STATE INFO (GET Method)_______________________#
#__________________POST STATE INFO (POST Method)_______________________#
@api_view(['POST'])
def agg_sc_post_state_info_ViewSet1(request):
    """
    List all code snippets, or create a new snippet.
    """
    request.method == 'POST'
    serializer = agg_sc_state_info_Serializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#__________________END POST STATE INFO (POST Method)_____________________#


#__________________ STATE INFO (PUT/UPDATE Method)________________________#
@api_view(['GET', 'PUT'])
def agg_sc_put_state_info_ViewSet1(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = agg_sc_State.objects.get(pk=pk)
    except agg_sc_State.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer =agg_sc_state_info_Serializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = agg_sc_state_info_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#__________________END  STATE INFO (PUT Method)_______________________# 


#__________________STATE INFO (DELETE Method)_______________________# 
@api_view(['GET','DELETE'])
def agg_sc_delete_state_info_ViewSet1(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = agg_sc_State.objects.get(pk=pk)
    except agg_sc_State.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer =agg_sc_state_info_Serializer(snippet)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#__________________END STATE DELETE INFO (DELETE Method)_______________________#

#______________________DISTRICT INFO (GET METHOD)_______________________________
@api_view(['GET'])
def agg_sc_get_district_info_ViewSet1(request):
    """
    List all code snippets, or create a new snippet.
    """
    request.method == 'GET'
    snippets = agg_sc_District.objects.all()
    serializer = agg_sc_district_info_Serializer(snippets, many=True)
    return Response(serializer.data)
#______________________END DISTRICT INFO (GET METHOD)_______________________________
#__________________POST DISTRICT INFO (POST Method)_______________________#
@api_view(['POST'])
def agg_sc_post_district_info_ViewSet1(request):
    """
    List all code snippets, or create a new snippet.
    """
    request.method == 'POST'
    serializer = agg_sc_district_info_Serializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#__________________END POST DISTRICT INFO (POST Method)_____________________#


#__________________DISTRICT INFO (PUT Method)_______________________# 
@api_view(['GET', 'PUT'])
def agg_sc_put_district_info_ViewSet1(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = agg_sc_District.objects.get(pk=pk)
    except agg_sc_District.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer =agg_sc_district_info_Serializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = agg_sc_district_info_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#__________________END DISTRICT PUT INFO (PUT Method)_______________________#


#__________________DISTRICT INFO (DELETE Method)_______________________# 
@api_view(['GET','DELETE'])
def agg_sc_delete_district_info_ViewSet1(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = agg_sc_District.objects.get(pk=pk)
    except agg_sc_District.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer =agg_sc_district_info_Serializer(snippet)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#__________________END DISTRICT DELETE INFO (DELETE Method)_______________________#


#______________________TAHSIL INFO (GET METHOD)_______________________________
@api_view(['GET'])
def agg_sc_get_tahsil_info_ViewSet1(request):
    """
    List all code snippets, or create a new snippet.
    """
    request.method == 'GET'
    snippets = agg_sc_Tehsil.objects.all()
    serializer = agg_sc_tahsil_info_Serializer(snippets, many=True)
    return Response(serializer.data)
#______________________END TAHSIL INFO (GET METHOD)_______________________________

#__________________POST TAHSIL INFO (POST Method)_______________________#
@api_view(['POST'])
def agg_sc_post_tahsil_info_ViewSet1(request):
    """
    List all code snippets, or create a new snippet.
    """
    request.method == 'POST'
    serializer = agg_sc_tahsil_info_Serializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#__________________END POST TAHSIL INFO (POST Method)_____________________#

#__________________TAHSIL INFO (PUT Method)_______________________# 
@api_view(['GET', 'PUT'])
def agg_sc_put_tahsil_info_ViewSet1(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = agg_sc_Tehsil.objects.get(pk=pk)
    except agg_sc_Tehsil.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer =agg_sc_tahsil_info_Serializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = agg_sc_tahsil_info_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#__________________END TAHSIL PUT INFO (PUT Method)_______________________#

#__________________DISTRICT INFO (DELETE Method)_______________________# 
@api_view(['GET','DELETE'])
def agg_sc_delete_tahsil_info_ViewSet1(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = agg_sc_Tehsil.objects.get(pk=pk)
    except agg_sc_Tehsil.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer =agg_sc_tahsil_info_Serializer(snippet)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#__________________END DISTRICT DELETE INFO (DELETE Method)_______________________#


#______________________DISEASE INFO (GET METHOD)_______________________________
@api_view(['GET'])
def agg_sc_get_disease_info_ViewSet1(request):
    """
    List all code snippets, or create a new snippet.
    """
    request.method == 'GET'
    snippets = agg_sc_disease.objects.all()
    serializer = agg_sc_disease_info_Serializer(snippets, many=True)
    return Response(serializer.data)
#______________________END DISEASE INFO (GET METHOD)_______________________________



#______________________IMMUNIZATION INFO (GET METHOD)_______________________________
@api_view(['GET'])
def agg_sc_get_immunization_info_ViewSet1(request):
    """
    List all code snippets, or create a new snippet.
    """
    request.method == 'GET'
    snippets = agg_sc_immunization_info.objects.all()
    serializer = agg_sc_immunization_info_Serializer(snippets, many=True)
    return Response(serializer.data)
#______________________END IMMUNIZATION INFO (GET METHOD)_______________________________

#______________________IMMUNIZATION INFO (POST METHOD)___________________________________
@api_view(['POST'])
def agg_sc_post_immunization_info_ViewSet1(request):
    """
    List all code snippets, or create a new snippet.
    """
    request.method == 'POST'
    serializer = agg_sc_immunization_info_Serializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#____________________________END IMMUNIZATION INFO (POST METHOD)___________________________


#__________________ CHILD VITAL INFO (PUT/UPDATE Method)________________________#
@api_view(['GET', 'PUT'])
def agg_sc_put_immunization_info_ViewSet1(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = agg_sc_immunization_info.objects.get(pk=pk)
    except agg_sc_immunization_info.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer =agg_sc_immunization_info_Serializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = agg_sc_immunization_info_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#__________________END  CHILD VITAL INFO (PUT Method)_______________________# 
#__________________ADD CHILD VITAL INFO (DELETE Method)_______________________# 
@api_view(['GET','DELETE'])
def agg_sc_delete_immunization_info_ViewSet1(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = agg_sc_immunization_info.objects.get(pk=pk)
    except agg_sc_immunization_info.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer =agg_sc_immunization_info_Serializer(snippet)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#__________________END ADD CHILD VITAL INFO (DELETE Method)_______________________# 


#______________________Treatment INFO (GET METHOD)___________________________________
@api_view(['GET'])
def agg_sc_get_treatment_info_ViewSet1(request):
    """
    List all code snippets, or create a new snippet.
    """
    request.method == 'GET'
    snippets = agg_sc_treatment_info.objects.all()
    serializer = agg_sc_treatment_info_Serializer(snippets, many=True)
    return Response(serializer.data)
#______________________END Treatment INFO (GET METHOD)________________________________


#______________________Treatment INFO (POST METHOD)___________________________________
@api_view(['POST'])
def agg_sc_post_treatment_info_ViewSet1(request):
    """
    List all code snippets, or create a new snippet.
    """
    request.method == 'POST'
    serializer = agg_sc_treatment_info_Serializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#______________________Treatment INFO (POST METHOD)___________________________________


#__________________ Treatment INFO (PUT/UPDATE Method)________________________#
@api_view(['GET', 'PUT'])
def agg_sc_put_treatment_info_ViewSet1(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = agg_sc_treatment_info.objects.get(pk=pk)
    except agg_sc_treatment_info.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer =agg_sc_treatment_info_Serializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = agg_sc_treatment_info_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#__________________END  Treatment INFO (PUT Method)_______________________# 

#__________________TreatmentL INFO (DELETE Method)_______________________# 
@api_view(['GET','DELETE'])
def agg_sc_delete_treatment_info_ViewSet1(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = agg_sc_treatment_info.objects.get(pk=pk)
    except agg_sc_treatment_info.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer =agg_sc_treatment_info_Serializer(snippet)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#__________________END Treatment INFO (DELETE Method)_______________________# 


#___________________Citizen Basic Info(GET METHOD)___________________________
@api_view(['GET'])
def agg_sc_get_citizen_basic_info_ViewSet1(request):
    """
    List all code snippets, or create a new snippet.
    """
    request.method == 'GET'
    snippets = agg_sc_add_new_citizens.objects.all()
    serializer = agg_sc_citizen_basic_info_Serializer(snippets, many=True)
    return Response(serializer.data)
#______________________________________________________________________
@api_view(['POST'])
def agg_sc_post_citizen_basic_info_ViewSet1(request):
    """
    List all code snippets, or create a new snippet.
    """
    request.method == 'POST'
    serializer = agg_sc_citizen_basic_info_post_Serializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#_________________________________________________________________________


# from rest_framework.views import APIView
# class demotest1(APIView):
#     serilaizer_class = agg_sc_citizen_basic_info_post_Serializer
#     def get(self, request, format=None):
#         queryset = agg_sc_citizen_basic_info.objects.all()
#         serializers = self.serilaizer_class(data=queryset, many=True)
#         serializers.is_valid()
#             # serializers.save()
#         return Response(serializers.data)
    
    
#     def post(self, request, format=None):
#         queryset = agg_sc_citizen_basic_info.objects.all()
#         serializers = self.serilaizer_class(data=queryset, many=True)
#         if serializers.is_valid():
#             serializers.save()
#         return Response(serializers.data)
        

#______________________________________________________________
@api_view(['GET'])
def agg_sc_get_citizen_family_info_ViewSet1(request):
    """
    List all code snippets, or create a new snippet.
    """
    request.method == 'GET'
    snippets = agg_sc_add_new_citizens.objects.all()
    serializer = agg_sc_citizen_family_info_Serializer(snippets, many=True)
    return Response(serializer.data)
#_________________________________________________________________________

#___________________Medical_Event_Info(GET METHOD)___________________________
@api_view(['GET'])
def agg_sc_get_citizen_medical_events_info_ViewSet1(request):
    """
    List all code snippets, or create a new snippet.
    """
    request.method == 'GET'
    snippets = agg_sc_medical_event_info.objects.all()
    serializer = agg_sc_medical_event_info_Serializer(snippets, many=True)
    return Response(serializer.data)
#___________________End Medical_Event_Info(GET METHOD)___________________________
@api_view(['POST'])
def agg_sc_post_citizen_medical_events_info_ViewSet1(request):
    """
    List all code snippets, or create a new snippet.
    """
    request.method == 'POST'
    serializer = agg_sc_medical_event_info_Serializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import abc
from .serializers import abcSerializer  # You need to import your serializer here

@api_view(['POST'])
def add_abc_items(request):
    if request.method == 'POST':
        # Get the number of times to add the data
        num_times = int(request.data.get('num_times', 10))
        
        # Extract the data from the request
        data = request.data

        # Validate the input data
        serializer = abcSerializer(data=data)
        if serializer.is_valid():
            # Add the data multiple times using a for loop
            for _ in range(num_times):
                abc.objects.create(**data)
                
            return Response({'message': 'Items added successfully'})
        else:
            return Response(serializer.errors, status=400)
    else:
        return Response({'message': 'Invalid request method'}, status=400)




@api_view(['GET'])
def agg_sc_get(request):
    """
    List all code snippets, or create a new snippet.
    """
    request.method == 'GET'
    snippets = abc.objects.all()
    serializer = abcSerializer(snippets, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def agg_sc_get_growth_monitoring_info_ViewSet1(request):
    """
    List all code snippets, or create a new snippet.
    """
    request.method == 'GET'
    snippets = GrowthMonitoring.objects.all()
    serializer = BMISerializer(snippets, many=True)
    return Response(serializer.data)




# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .models import agg_sc_citizen_schedule, agg_sc_add_new_citizens
# from .serializers import CitizenScheduleSerializer
# from rest_framework import status

# @api_view(['POST'])
# def assign_citizens_to_schedule(request):
#     if request.method == 'POST':
#         source_name = request.data.get('source_name', '')
#         print(f"Received source_name: {source_name}")

#         citizens = agg_sc_add_new_citizens.objects.filter(source_name=source_name)
        

#         if not citizens:
#             return Response({'error': 'No citizens found for the specified source_name'}, status=status.HTTP_404_NOT_FOUND)

      
#         schedule_id = request.data.get('schedule_id', '')  
#         for citizen in citizens:
#             agg_sc_citizen_schedule.objects.create(
#                 citizen_id=citizen.citizens_id,
#                 schedule_id=schedule_id,
                
#             )

#         return Response({'message': 'Citizens assigned to schedule successfully'}, status=status.HTTP_201_CREATED)

#     return Response({'error': 'Invalid request method'}, status=status.HTTP_400_BAD_REQUEST)








@api_view(['GET'])
def agg_sc_get_start_screening_info_ViewSet1(request):
    if request.method == 'GET':
        schedules = agg_sc_citizen_schedule.objects.all()
        response_data = []

        for schedule in schedules:
            citizen_id = schedule.citizen_id
            citizen = agg_sc_add_new_citizens.objects.get(citizens_id=citizen_id)
            serializer = CitizenSerializer(citizen)
            
            response_data.append({
                'citizen_id': schedule.citizen_id,
                'schedule_id': schedule.schedule_id,
                'citizen_info': serializer.data,
            })

        return Response(response_data)