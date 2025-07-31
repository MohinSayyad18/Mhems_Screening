from rest_framework import serializers
from .models import *


class agg_sc_add_new_citizens_Serializer(serializers.ModelSerializer):
   class Meta:
      model = agg_sc_add_new_citizens
      fields = '__all__'
      #fields = ('child_name', 'gender', 'blood_groups','dob','year','months','days','aadhar_id') 


class agg_sc_immunization_info_Serializer(serializers.ModelSerializer):
   class Meta:
      model = agg_sc_immunization_info
   #    fields = ['id','bcg','bcg_date_from','bcg_date_to','opv0','opv0_date_from','opv0_date_to',
   #              'hep_b','hep_b_date_from','hep_b_date_to','opv1','opv1_date_from','opv1_date_to',
   #              'opv2','opv2_date_from','opv2_date_to','opv3','opv3_date_from','opv3_date_to',
   #              'ipv1','ipv1_date_from','ipv1_date_to','ipv2','ipv2_date_from','ipv2_date_to',
   #              'mr1','mr1_date_from','mr1_date_to','mr2','mr2_date_from','mr2_date_to',
   #              'je1','je1_date_from','je1_date_to','je2','je2_date_from','je2_date_to',
   #              'opv_boos','opv_boos_date_from','opv_boos_date_to','dpt1','dpt1_date_from','dpt1_date_to',
   #              'dpt_2','dpt_2_date_from','dpt_2_date_to','dpt_3','dpt_3_date_from','dpt_3_date_to',	
   #              'rvv1','rvv1_date_from','rvv1_date_to','rvv2','rvv2_date_from','rvv2_date_to',
   #              'rvv3','rvv3_date_from','rvv3_date_to','PCV1','PCV1_date_from','PCV1_date_to',
   #              'PCV2','PCV2_date_from','PCV2_date_to','PCVBoost','PCVBoost_date_from','PCVBoost_date_to',
   #              'vitA','vitA_date_from','vitA_date_to','dpt_boost','dpt_boost_date_from','dpt_boost_date_to',
   #              'vitA2','vitA2_date_from','vitA2_date_to','vitA3','vitA3_date_from','vitA3_date_to',
   #              'vitA4','vitA4_date_from','vitA4_date_to','vitA5','vitA5_date_from','vitA5_date_to',
   #              'vitA6','vitA6_date_from','vitA6_date_to','vitA7','vitA7_date_from','vitA7_date_to',
   #              'vitA8','vitA8_date_from','vitA8_date_to','vitA9','vitA9_date_from','vitA9_date_to',
   #              'dptboost_2','dptboost_2_date_from','dptboost_2_date_to','ttd','ttd_date_from','ttd_date_to',
   #              'vacin_covid1_type','vacin_covid1','vacin_covid1_date_from','vacin_covid1_date_to',
   #              'vacin_covid2_type','vacin_covid2','vacin_covid2_date_from','vacin_covid2_date_to'

   #  ]
      fields = '__all__'


class agg_sc_screening_info_Serializer(serializers.ModelSerializer):
   class Meta:
      model = agg_sc_basic_screening_info
      fields = '__all__'
      

class agg_sc_pycho_info_Serializer(serializers.ModelSerializer):
   class Meta:
      model = agg_sc_pycho_info
      fields = '__all__'
      

class agg_sc_bmi_info_Serializer(serializers.ModelSerializer):
   class Meta:
      model = agg_sc_bmi_info
      fields = '__all__'
      
class agg_sc_shedule_screening_info_Serializer(serializers.ModelSerializer):
   class Meta:
      model = agg_sc_shedule_screening_info
      fields = '__all__'


class add_new_source_Serializer(serializers.ModelSerializer):
   class Meta:
      model = agg_sc_add_new_source
      fields = '__all__'

#______________________________________________________________________
class child_basic_info_Serializer(serializers.ModelSerializer):
   class Meta:
      model = agg_sc_add_new_citizens
      fields = ('child_name', 'gender', 'blood_groups','dob','year','months','days','aadhar_id') 
#_________________________________________________________________________________________________
class child_address_info_Serializer(serializers.ModelSerializer):
    class Meta:
      model = agg_sc_add_new_citizens
      fields = ('source_name', 'state','district', 'tehsil','pincode', 'address')
#_________________________________________________________________________________________________
class child_growth_info_Serializer(serializers.ModelSerializer):
    class Meta:
      model = agg_sc_add_new_citizens
      fields = ('dob','year','months','days','height','weight','bmi','weight_for_age','height_for_age','weight_for_height','arm_size','symptoms','gender','remark')
#___________________________________________________________________________________________________________
class agg_sc_vital_info_Serializer(serializers.ModelSerializer):
   class Meta:
      model = agg_sc_vital_info
      fields = ['pulse','sys_mm','dys_mm','rr','oxygen_saturation','hb','temp']
      # fields = '__all__'

#________________________________________________________________________________________
#________________________________________STATE___________________________________________
#________________________________________________________________________________________
class agg_sc_state_info_Serializer(serializers.ModelSerializer):
   class Meta:
      model = agg_sc_State
      fields = '__all__'
#________________________________District_________________________________ 
class agg_sc_district_info_Serializer(serializers.ModelSerializer):
   class Meta:
      model = agg_sc_District
      fields = '__all__'
#_______________________________TAHSIL________________________________________
class agg_sc_tahsil_info_Serializer(serializers.ModelSerializer):
   class Meta:
      model = agg_sc_Tehsil
      fields = '__all__'
#________________________Disease_________________________________
class agg_sc_disease_info_Serializer(serializers.ModelSerializer):
   class Meta:
      model = agg_sc_disease
      fields = '__all__'

#____________________________Start Screening____________________________
class agg_sc_start_screening_Serializer(serializers.ModelSerializer):
   class Meta:
      model = agg_sc_start_screening
      fields = ['citizen_name','citizen_id','schedule_id','source_id','citizen_mobile']
#________________________________________________________________________________________

class agg_sc_treatment_info_Serializer(serializers.ModelSerializer):
   class Meta:
      model = agg_sc_treatment_info
      fields = '__all__'
      
#_______________________________GET API___________________________________
class agg_sc_citizen_basic_info_Serializer(serializers.ModelSerializer):
   class Meta:
      model = agg_sc_add_new_citizens
      fields = ['id','citizen_name','gender','blood_group','dob','year','months','days','aadhar_id']
#________________________________POST API____________________________________

# from rest_framework import serializers
# from .models import agg_sc_citizen_basic_info, agg_sc_add_new_citizens

# class get_citizen_id(serializers.ModelSerializer):
#     class Meta:
#         model = agg_sc_add_new_citizens
#         fields = ['citizens_id']

# class agg_sc_citizen_basic_info_post_Serializer(serializers.ModelSerializer):
#     citizen_id = get_citizen_id()  # Define it as a serializer field, not an instance

#     class Meta:
#         model = agg_sc_citizen_basic_info
#         fields = ['citizen_id', 'citizen_name', 'gender', 'dob', 'year', 'months', 'days', 'aadhar_id']


class agg_sc_citizen_basic_info_post_Serializer(serializers.ModelSerializer):
    class Meta:
        model = agg_sc_citizen_basic_info
        fields = ['citizen_name', 'gender','blood_group','dob', 'year', 'months', 'days', 'aadhar_id']
        
class agg_sc_citizen_family_info_Serializer(serializers.ModelSerializer):
   class Meta:
      model = agg_sc_add_new_citizens
      fields = ['id','father_name', 'mother_name', 'occupation_of_father','occupation_of_mother','parents_mobile','sibling_count']
      # fields = '__all__'

class agg_sc_medical_event_info_Serializer(serializers.ModelSerializer):
   class Meta:
      model = agg_sc_medical_event_info
      fields = '__all__'
   
   
class abcSerializer(serializers.ModelSerializer):
    class Meta:
        model = abc
        fields = '__all__'

class BMISerializer(serializers.ModelSerializer):
   class Meta:
      model = GrowthMonitoring
      fields = '__all__'
      
# class CitizenScheduleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = agg_sc_citizen_schedule
#         fields = '__all__'
        
        



# serializers.py
from rest_framework import serializers
from .models import agg_sc_add_new_citizens

class CitizenSerializer(serializers.ModelSerializer):
    class Meta:
        model = agg_sc_add_new_citizens
        fields = ['citizen_name', 'parents_mobile']



      
