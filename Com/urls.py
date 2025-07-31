from django.urls import path
from . import views
from .views import *

urlpatterns = [
  
   
    #__________________________SCREENING INFO______________________________________#
    # path('screening_info/',views.start_screening_info_ViewSet1), 
    # path('screening_info_Details_1/<int:pk>/',views.agg_sc_screening_info_Details_ViewSet1),
    #___________________________END SCREENING INFO_________________________________#
    
    
    #_____________________________PYCHO INFO________________________________#
    path('pycho_info/',views.agg_sc_pycho_info_ViewSet1), 
    path('pycho_info_Details_1/<int:pk>/',views.agg_sc_pycho_info_Details_ViewSet1),
    #_____________________________END PYCHO INFO_____________________________#
    
    
    #_____________________________BMI INFO________________________________#
    path('bmi_info/',views.agg_sc_bmi_info_ViewSet1), 
    path('bmi_info_Details_1/<int:pk>/',views.agg_sc_bmi_info_Details_ViewSet1),
    #_____________________________END BMI INFO_____________________________#
  
  

  
  #______________________________ADD NEW CITIZENS___________________________________
  path('add_citizen_get/',views.agg_sc_add_new_citizen_get_info_ViewSet1),
  path('add_citizen_post/',views.agg_sc_add_new_citizen_post_info_ViewSet1),
  path('add_citizen_put/<int:pk>/',views.agg_sc_add_new_citizen_put_info_ViewSet1),
  path('add_citizen_delete/<int:pk>/',views.agg_sc_add_new_citizen_delete_info_ViewSet1),
  #______________________________END ADD NEW CITIZENS________________________________
  
  #______________________________ADD NEW SCHEDULE____________________________________
  path('add_schedule_get/',views.agg_sc_add_new_schedule_get_info_ViewSet1),
  path('add_schedule_post/',views.agg_sc_add_new_schedule_post_info_ViewSet1),
  path('add_schedule_put/<int:pk>/',views.agg_sc_add_new_schedule_put_info_ViewSet1),
  path('add_schedule_delete/<int:pk>/',views.agg_sc_add_new_schedule_delete_info_ViewSet1),
  #______________________________END ADD NEW SCHEDULE________________________________
  
  #______________________________ADD NEW SOURCE_____________________________________
  path('add_source_get/',views.agg_sc_add_new_source_get_info_ViewSet1),
  path('add_source_post/',views.agg_sc_add_new_source_post_info_ViewSet1),
  path('add_source_put/<int:pk>/',views.agg_sc_add_new_source_put_info_ViewSet1),
  path('add_source_delete/<int:pk>/',views.agg_sc_add_new_source_delete_info_ViewSet1),
  #______________________________END ADD NEW SCHEDULE______________________________
  
  #___________GETTING CHILD BASIC INFO DETAILS FROM ADD NEW CITIZEN TABLE__________
  path('child_basic_info_get/',views.agg_sc_get_child_basic_info_ViewSet1),
  path('child_basic_info_post/',views.agg_sc_post_child_basic_info_ViewSet1),
  path('child_basic_info_put/<int:pk>/',views.agg_sc_put_child_basic_info_ViewSet1),
  path('child_basic_info_delete/<int:pk>/',views.agg_sc_delete_child_basic_info_ViewSet1),
  #___________END GETTING CHILD BASIC INFO DETAILS FROM ADD NEW CITIZEN TABLE________
  
  
  #___________GETTING CHILD FAMILY INFO DETAILS FROM ADD NEW CITIZEN TABLE__________
  # path('child_family_info_get/',views.agg_sc_get_child_family_info_ViewSet1),
  # path('child_family_info_post/',views.agg_sc_post_child_family_info_ViewSet1),
  # path('child_family_info_put/<int:pk>/',views.agg_sc_put_child_family_info_ViewSet1),
  # path('child_family_info_delete/<int:pk>/',views.agg_sc_delete_child_family_info_ViewSet1),
  # #___________END GETTING CHILD FAMILY INFO DETAILS FROM ADD NEW CITIZEN TABLE________
  
  
  #___________GETTING CHILD ADDRESS INFO DETAILS FROM ADD NEW CITIZEN TABLE__________
  path('child_address_info_get/',views.agg_sc_get_child_address_info_ViewSet1),
  path('child_address_info_post/',views.agg_sc_post_child_address_info_ViewSet1),
  path('child_address_info_put/<int:pk>/',views.agg_sc_put_child_address_info_ViewSet1),
  path('child_address_info_delete/<int:pk>/',views.agg_sc_delete_child_address_info_ViewSet1),
  #___________END GETTING CHILD ADDRESS INFO DETAILS FROM ADD NEW CITIZEN TABLE________
  
  
  #___________GETTING CHILD GROWTH INFO DETAILS FROM ADD NEW CITIZEN TABLE__________
  path('child_bmi_info_get/',views.agg_sc_get_child_bmi_info_ViewSet1),
  path('child_bmi_info_post/',views.agg_sc_post_child_bmi_info_ViewSet1),
  path('child_bmi_info_put/<int:pk>/',views.agg_sc_put_child_bmi_info_ViewSet1),
  path('child_bmi_info_delete/<int:pk>/',views.agg_sc_delete_child_bmi_info_ViewSet1),
  #___________END GETTING CHILD GROWTH INFO DETAILS FROM ADD NEW CITIZEN TABLE________
  
  
  #____________________________________VITAL'S______________________________________________
  path('child_vital_info_get/',views.agg_sc_get_child_vital_info_ViewSet1),
  path('child_vital_info_post/',views.agg_sc_post_child_vital_info_ViewSet1),
  path('child_vital_info_put/<int:pk>/',views.agg_sc_put_child_vital_info_ViewSet1),
  path('child_vital_info_delete/<int:pk>/',views.agg_sc_delete_child_vital_info_ViewSet1),
  #____________________________________END VITAL'S______________________________________________
  
  #_____________________________________STATE_______________________________________
  path('child_state_info_get/',views.agg_sc_get_state_info_ViewSet1),
  path('child_state_info_post/',views.agg_sc_post_state_info_ViewSet1),
  path('child_state_info_put/<int:pk>/',views.agg_sc_put_state_info_ViewSet1),
  path('child_state_info_delete/<int:pk>/',views.agg_sc_delete_state_info_ViewSet1),
  
  #_________________________________DISTRICT________________________________________
  path('child_district_info_get/',views.agg_sc_get_district_info_ViewSet1),
  path('child_district_info_post/',views.agg_sc_post_district_info_ViewSet1),
  path('child_district_info_put/<int:pk>/',views.agg_sc_put_district_info_ViewSet1),
  path('child_district_info_delete/<int:pk>/',views.agg_sc_delete_district_info_ViewSet1),
  
  #________________________________TAHSIL_______________________________________________
  path('child_tahsil_info_get/',views.agg_sc_get_tahsil_info_ViewSet1),
  path('child_tahsil_info_post/',views.agg_sc_post_tahsil_info_ViewSet1),
  path('child_tahsil_info_put/<int:pk>/',views.agg_sc_put_tahsil_info_ViewSet1),
  path('child_tahsil_info_delete/<int:pk>/',views.agg_sc_delete_tahsil_info_ViewSet1),
  
  #______________________________DISEASE_____________________________________________
  path('child_disease_info_get/',views.agg_sc_get_disease_info_ViewSet1),

  #__________________START SCREENING______________________
  path('child_start_screening_info_get/',views.start_screening_info_ViewSet1),  
  path('start_screen_Details_1/<int:pk>/',views.start_screening_info_Details_ViewSet1),
  
  #________________________Immunization info________________________________
  path('child_immunization_info_get/',views.agg_sc_get_immunization_info_ViewSet1),
  path('child_immunization_info_post/',views.agg_sc_post_immunization_info_ViewSet1),
  path('child_immunization_info_put/<int:pk>/',views.agg_sc_put_immunization_info_ViewSet1),
  path('child_immunization_info_delete/<int:pk>/',views.agg_sc_delete_immunization_info_ViewSet1),
  
  #________________________________Treatment info____________________________________
  path('child_treatment_info_get/',views.agg_sc_get_treatment_info_ViewSet1),
  path('child_treatment_info_post/',views.agg_sc_post_treatment_info_ViewSet1),
  path('child_treatment_info_put/<int:pk>/',views.agg_sc_put_treatment_info_ViewSet1),
  path('child_treatment_info_delete/<int:pk>/',views.agg_sc_delete_treatment_info_ViewSet1),
  
  
  #______________________________Citizen Basic Info_________________________
  path('citizen_basic_info_get/',views.agg_sc_get_citizen_basic_info_ViewSet1),
  path('citizen_basic_info_post/',views.agg_sc_post_citizen_basic_info_ViewSet1),
  # path('testhii/',views.demotest1.as_view(), name='demo'),
  path('citizen_family_info_get/',views.agg_sc_get_citizen_family_info_ViewSet1),


#___________________________Medical Events___________________________
  path('citizen_medical_events_info_get/',views.agg_sc_get_citizen_medical_events_info_ViewSet1),
  path('citizen_medical_events_info_post/',views.agg_sc_post_citizen_medical_events_info_ViewSet1),


  path('add_items/', views.add_abc_items, name='add_items'),
  path('add_items_get/',views.agg_sc_get),


  path('citizen_growth_monitoring_info_get/',views.agg_sc_get_growth_monitoring_info_ViewSet1),

  # path('assign_citizens_to_schedule/', assign_citizens_to_schedule, name='assign_citizens_to_schedule'),
  path('start_screening_info/',views.agg_sc_get_start_screening_info_ViewSet1),
    
]