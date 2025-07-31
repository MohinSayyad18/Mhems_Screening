from django.db import models
# from django.db.models import Max
from django_enumfield import enum
from datetime import date
# Create your models here.
from django.db import models
from django_enumfield import enum
from django.utils import timezone 
import datetime
# Create your models here.

#___________STATE___________
class is_deleted(models.TextChoices):
    YES     = '0'
    NO      = '1'

# class is_deleted(enum.Enum):
#     YES     = '0'
#     NO      = '1'
#     SIXTY_TO_120   = '2'
    
class agg_sc_State(models.Model):
    st_id = models.AutoField(primary_key=True)
    st_code = models.IntegerField(unique=True)
    st_name = models.CharField(max_length=100)
    stis_deleted = models.CharField(max_length=10, choices=is_deleted.choices)
    modify_date_sync = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.st_name

#_____________District_________________
class agg_sc_District(models.Model):
    dst_id = models.AutoField(primary_key=True)
    dst_code = models.IntegerField(unique=True)
    dst_name = models.CharField(max_length=100)
    dstis_deleted = models.CharField(max_length=10, choices=is_deleted.choices)
    dst_state = models.ForeignKey(agg_sc_State, on_delete=models.CASCADE)

    def __str__(self):
        return self.dst_name

#___________________Tehsil_______________________
class agg_sc_Tehsil(models.Model):
    thl = models.AutoField(primary_key=True)
    thl_code = models.IntegerField()
    thl_name = models.CharField(max_length=100)
    thl_district_code = models.ForeignKey(agg_sc_District, on_delete=models.CASCADE)
    thlis_deleted = models.CharField(max_length=10, choices=is_deleted.choices)

    def __str__(self):
        return self.thl_name



#_____________________________________ADD NEW CITIZENS______________________________________________#
#____________________________________________________________
class Age_groups(enum.Enum):
    ZERO_TO_10     = '0'
    TEN_TO_60      = '1'
    SIXTY_TO_120   = '2'
    
    
Gender_CHOICES = (
        ('MALE', 'MALE'),
        ('FEMALE', 'FEMALE'),
        ('OTHER', 'OTHER'),
    )
 
class Screening_Source(models.TextChoices):
    SCHOOL  = '0'
    CAMP    = '1'
    NGO     = '2'
    SOCIETY = '3'


class Disease(models.TextChoices):
    COVID_19 = '0'
    CANCER   = '1'
    HIV      = '2'
    

Blood_groups_CHOICES = (
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    )
    
class Sibling_Count(enum.Enum):
    ZERO  = '0'
    ONE   = '1'
    TWO   = '2'
    THREE = '3'
    FOUR  = '4'


from django.utils import timezone 
class agg_sc_add_new_citizens(models.Model):
    age = enum.EnumField(Age_groups)
    gender = models.CharField(max_length=255,choices=Gender_CHOICES)
    screening_source = models.CharField(max_length=255,choices=Screening_Source.choices,null=False)
    disease = models.CharField(max_length=255,choices=Disease.choices)

#__________CHILD DETAILS________________
    citizens_id = models.CharField(max_length=50,editable=False,unique=True)
    citizen_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255,choices=Gender_CHOICES)
    dob = models.DateField()
    blood_group = models.CharField(max_length=255,choices=Blood_groups_CHOICES)
    year = models.IntegerField()
    months = models.IntegerField()
    days = models.IntegerField()
    aadhar_id = models.CharField(max_length=12,unique=True)
    # created_date = models.DateField(default=timezone.now, editable=False)

#_____________FAMILY INFORMATION_____________
    father_name = models.CharField(max_length=255,null=False)
    mother_name = models.CharField(max_length=255,null=False)
    occupation_of_father = models.CharField(max_length=255)
    occupation_of_mother = models.CharField(max_length=255)
    parents_mobile = models.CharField(max_length=10,null=False)
    sibling_count =enum.EnumField(Sibling_Count)

#___________ADDRESS_____________________________
    state = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    tehsil = models.CharField(max_length=255)
    pincode = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    source_name = models.CharField(max_length=255)

#___________GROWTH MONITORING________________
    height = models.FloatField(null=False)
    weight = models.FloatField(null=False)
    weight_for_age = models.CharField(max_length=50, blank=True, null=True)
    height_for_age = models.CharField(max_length=50, blank=True, null=True)
    weight_for_height =models.CharField(max_length=50, blank=True, null=True)
    bmi = models.FloatField(blank=True, null=True)
    arm_size = models.FloatField()
#____________Medical EVENT________________________
    symptoms = models.CharField(max_length=255)
    remark = models.CharField(max_length=500)
    is_deleted = models.BooleanField(default=False)
    def save(self, *args, **kwargs):
        # Calculate age in years based on dob
        age_in_years = (timezone.now().date() - self.dob).days / 365.25

        if age_in_years > 10:
            # Calculate BMI only if age is above 5 years
            self.bmi = self.weight / ((self.height / 100) ** 2)

            # Categorize the BMI
            if self.bmi < 18.5:
                self.weight_for_height = 'Underweight'
            elif 18.5 <= self.bmi < 25:
                self.weight_for_height = 'Normal weight'
            elif 25 <= self.bmi < 30:
                self.weight_for_height = 'Overweight'
            else:
                self.weight_for_height = 'Obese'
        else:
            # Set BMI and related fields to None if age is 5 years or younger
            self.bmi = None
            self.weight_for_height = None
            self.weight_for_age = None
            self.height_for_age = None
        
        #___________Trial__________________
         # Calculate weight_for_age
        if self.age == Age_groups.ZERO_TO_10:
            if self.weight < 10:
                self.weight_for_age = 'Underweight'
            elif 10 <= self.weight < 18:
                self.weight_for_age = 'Normal weight'
            else:
                self.weight_for_age = 'Overweight'
        elif self.age == Age_groups.TEN_TO_60:
            if 18 <= self.weight < 25:
                self.weight_for_age = 'Normal weight'
            else:
                self.weight_for_age = 'Overweight'
        else:
            if self.weight >= 25:
                self.weight_for_age = 'Overweight'
            else:
                self.weight_for_age = 'Normal weight'

        # Calculate height_for_age
        if self.age == Age_groups.ZERO_TO_10:
            if self.height < 80:
                self.height_for_age = 'Short stature'
            elif 80 <= self.height < 120:
                self.height_for_age = 'Normal height'
            else:
                self.height_for_age = 'Tall stature'
        elif self.age == Age_groups.TEN_TO_60:
            if 120 <= self.height < 160:
                self.height_for_age = 'Normal height'
            else:
                self.height_for_age = 'Tall stature'
        else:
            if self.height < 160:
                self.height_for_age = 'Short stature'
            elif 160 <= self.height < 180:
                self.height_for_age = 'Normal height'
            else:
                self.height_for_age = 'Tall stature'
        
        

        # Generate and assign citizens_id if not present
        if not self.citizens_id:
            last_id = agg_sc_add_new_citizens.objects.filter().order_by('-citizens_id').first()
            if last_id:
                last_id_value = int(last_id.citizens_id.split('-')[1][-4:])
                new_id_value = last_id_value + 1
                generated_id = int(str(timezone.now().strftime('%d%m%Y')) + str(new_id_value).zfill(5))
            else:
                generated_id = int(str(timezone.now().strftime('%d%m%Y')) + '00001')

            self.citizens_id = f"CI-{generated_id}"

        super(agg_sc_add_new_citizens, self).save(*args, **kwargs)

    # def __str__(self):
    #     return self.citizens_id
# #__________________________________________________________________________________________   
#_______________________________UNDER CONSTRUCTION_________________________________________
#__________________________________________________________________________________________
    # # def generate_id(self):
    # #     last_id = agg_sc_add_new_citizens.objects.filter(created_date=self.created_date).order_by('-citizens_id').first()
    # #     if last_id:
    # #         last_id_value = int(last_id.citizens_id.split('-')[1][-4:])
    # #         new_id_value = last_id_value + 1
            
    # #         return int(str(self.created_date.strftime('%d%m%Y')) + str(new_id_value).zfill(5))
    # #     else:
    # #         return int(str(self.created_date.strftime('%d%m%Y')) + '00001')

    # # def save(self, *args, **kwargs):
    # #     if not self.citizens_id:
    # #         generated_id = self.generate_id()
    # #         self.citizens_id = f"CI-{generated_id}"
    # #         super(agg_sc_add_new_citizens, self).save(*args, **kwargs)
        
    
    # def save(self, *args, **kwargs):
    #     # Calculate the BMI before saving
    #     self.bmi = self.weight / ((self.height/100) ** 2)

    #     # Categorize the BMI
    #     if self.bmi < 18.5:
    #         self.weight_for_height = 'Underweight'
    #     elif 18.5 <= self.bmi < 25:
    #         self.weight_for_height = 'Normal weight'
    #     elif 25 <= self.bmi < 30:
    #         self.weight_for_height = 'Overweight'
    #     else:
    #         self.weight_for_height = 'Obese'

    #     super().save(*args, **kwargs)
    
    
    
    
    # def __str__(self):
    #     return self.child_name
#________________________CITIZEN BASIC INFO____________________________+
    
class agg_sc_citizen_basic_info1(models.Model):
    citizen_basic_info_id = models.AutoField(primary_key=True)
    schedule_id  = models.CharField(max_length=255)
    citizen_id = models.CharField(max_length=255)
    citizen_adhar_id = models.CharField(max_length=12)
    schedule_count = models.IntegerField()
    schedule_id_old = models.CharField(max_length=255)
    past_medical_history = models.CharField(max_length=255)
    prev_hospitalization = models.CharField(max_length=255)
    current_medication = models.CharField(max_length=255)
    allergies = models.CharField(max_length=255)
    vacines = models.CharField(max_length=255)
    deworming_history = models.CharField(max_length=255)
    deworming_date = models.DateField()
    added_by = models.CharField(max_length=255)
    added_date = models.DateField()
    modify_by = models.CharField(max_length=255)
    modify_date = models.DateField(auto_now=True)
    is_deleted = models.CharField(max_length=10, choices=is_deleted.choices)
    modify_date_sync = models.DateTimeField(auto_now=True)
    
    def __str__(self):
          return self.added_by


#__________________IMMUNIZATION_INFO_____________________
class agg_sc_immunization_info(models.Model):
    pk_id = models.IntegerField(primary_key=True)
    schedule_id	= models.CharField(max_length=255)
    citizen_id	= models.CharField(max_length=255)
    schedule_count	= models.IntegerField()
    schedule_id_old	= models.CharField(max_length=255)
    bcg		= models.CharField(max_length=255)
    bcg_date_from	= models.DateField()
    bcg_date_to	= models.DateField()
    opv0	= models.CharField(max_length=255)
    opv0_date_from	= models.DateField()
    opv0_date_to	= models.DateField()
    hep_b		= models.CharField(max_length=255)
    hep_b_date_from	= models.DateField()
    hep_b_date_to	= models.DateField()
    opv1	= models.CharField(max_length=255)
    opv1_date_from	= models.DateField()
    opv1_date_to	= models.DateField()
    opv2	= models.CharField(max_length=255)
    opv2_date_from	= models.DateField()
    opv2_date_to	= models.DateField()
    opv3	= models.CharField(max_length=255)
    opv3_date_from	= models.DateField()
    opv3_date_to	= models.DateField()
    ipv1	= models.CharField(max_length=255)
    ipv1_date_from	= models.DateField()
    ipv1_date_to	= models.DateField()
    ipv2	= models.CharField(max_length=255)
    ipv2_date_from	= models.DateField()
    ipv2_date_to	= models.DateField()
    mr1	= models.CharField(max_length=255)
    mr1_date_from	= models.DateField()
    mr1_date_to	= models.DateField()
    je1	= models.CharField(max_length=255)
    je1_date_from	= models.DateField()
    je1_date_to	= models.DateField()
    mr2	= models.CharField(max_length=255)
    mr2_date_from	= models.DateField()
    mr2_date_to	= models.DateField()
    opv_boos	= models.CharField(max_length=255)
    opv_boos_date_from	= models.DateField()
    opv_boos_date_to	= models.DateField()
    dpt1	= models.CharField(max_length=255)
    dpt1_date_from	= models.DateField()
    dpt1_date_to	= models.DateField()
    je2	= models.CharField(max_length=255)
    je2_date_from	= models.DateField()
    je2_date_to	= models.DateField()
    dpt_2	= models.CharField(max_length=255)
    dpt_2_date_from	= models.DateField()
    dpt_2_date_to	= models.DateField()
    dpt_3	= models.CharField(max_length=255)
    dpt_3_date_from	= models.DateField()
    dpt_3_date_to	= models.DateField()
    rvv1	= models.CharField(max_length=255)
    rvv1_date_from	= models.DateField()
    rvv1_date_to	= models.DateField()
    rvv2	= models.CharField(max_length=255)
    rvv2_date_from	= models.DateField()
    rvv2_date_to	= models.DateField()
    rvv3	= models.CharField(max_length=255)
    rvv3_date_from	= models.DateField()
    rvv3_date_to	= models.DateField()
    PCV1	= models.CharField(max_length=255)
    PCV1_date_from	= models.DateField()
    PCV1_date_to	= models.DateField()
    PCV2	= models.CharField(max_length=255)
    PCV2_date_from	= models.DateField()
    PCV2_date_to	= models.DateField()
    PCVBoost	= models.CharField(max_length=255)
    PCVBoost_date_from	= models.DateField()
    PCVBoost_date_to = models.DateField()	
    vitA	= models.CharField(max_length=255)
    vitA_date_from	= models.DateField()
    vitA_date_to = models.DateField()	
    dpt_boost	= models.CharField(max_length=255)
    dpt_boost_date_from	= models.DateField()
    dpt_boost_date_to   = models.DateField()	
    vitA2	= models.CharField(max_length=255)
    vitA2_date_from	= models.DateField()
    vitA2_date_to	= models.DateField()
    vitA3	= models.CharField(max_length=255)
    vitA3_date_from	= models.DateField()
    vitA3_date_to	= models.DateField()
    vitA4	= models.CharField(max_length=255)
    vitA4_date_from	= models.DateField()
    vitA4_date_to	= models.DateField()
    vitA5	= models.CharField(max_length=255)
    vitA5_date_from	= models.DateField()
    vitA5_date_to	= models.DateField()
    vitA6= models.CharField(max_length=255)
    vitA6_date_from	= models.DateField()
    vitA6_date_to	= models.DateField()
    vitA7	= models.CharField(max_length=255)
    vitA7_date_from	= models.DateField()
    vitA7_date_to	= models.DateField()
    vitA8	= models.CharField(max_length=255)
    vitA8_date_from = models.DateField()
    vitA8_date_to = models.DateField()	
    vitA9	= models.CharField(max_length=255)
    vitA9_date_from	= models.DateField()
    vitA9_date_to	= models.DateField()
    dptboost_2	= models.CharField(max_length=255)
    dptboost_2_date_from = models.DateField()	
    dptboost_2_date_to	= models.DateField()
    ttd	= models.CharField(max_length=255)
    ttd_date_from	= models.DateField()
    ttd_date_to	 = models.DateField()
    vacin_tt1	= models.CharField(max_length=255)
    tt1_date = models.DateField()
    vacin_tt2	= models.CharField(max_length=255)
    tt2_date	= models.DateField()
    vacin_covid1_type = models.CharField(max_length=255)	
    vacin_covid1	= models.CharField(max_length=255)
    vacin_covid1_date_from	= models.DateField()
    vacin_covid1_date_to	= models.DateField()
    vacin_covid2_type	= models.CharField(max_length=255)
    vacin_covid2	= models.CharField(max_length=255)
    vacin_covid2_date_from = models.DateField()	
    vacin_covid2_date_to	= models.DateField()
    added_by	= models.CharField(max_length=255)
    added_date	= models.DateField()
    modify_by	= models.CharField(max_length=255)
    modify_date	= models.DateField(auto_now=True)
    is_deleted	= models.CharField(max_length=10, choices=is_deleted.choices)
    modify_date_sync	= models.DateTimeField(auto_now=True)
#__________________END IMMUNIZATION_INFO_____________________

#_______________Screening_Info_________________________#
class agg_sc_basic_screening_info(models.Model):
    pk_id = models.IntegerField(primary_key=True)
    citizen_id = models.ForeignKey(agg_sc_add_new_citizens, on_delete=models.CASCADE,to_field='citizens_id')
    schedule_count  = models.IntegerField()
    schedule_id_old = models.CharField(max_length=255)
    schedule_id = models.ForeignKey('agg_sc_shedule_screening_info', on_delete=models.CASCADE,to_field='schedule_id')
    #___HEAD/SCALP
    head = models.CharField(max_length=255)
    hair_color = models.CharField(max_length=255)
    hair_density = models.CharField(max_length=255)
    hair_texture = models.CharField(max_length=255)
    alopecia = models.CharField(max_length=255)
    neck = models.CharField(max_length=255)
    #__________SKIN___________
    skin_color = models.CharField(max_length=255)
    skin_texture = models.CharField(max_length=255)
    skin_lesions = models.CharField(max_length=255)
    #________MOUTH__________
    lips = models.CharField(max_length=255)
    gums = models.CharField(max_length=255)
    dentition = models.CharField(max_length=255)
    oral_mucosa = models.CharField(max_length=255)
    tongue = models.CharField(max_length=255)
    #_________OTHER________
    chest = models.CharField(max_length=255)
    abdomen = models.CharField(max_length=255)
    extremity = models.CharField(max_length=255)
    added_by = models.DateField()
    added_date = models.DateField()
    modify_by = models.CharField(max_length=255)
    modify_date = models.DateField(auto_now=True)
    is_deleted = models.CharField(max_length=10, choices=is_deleted.choices)
    modify_date_sync = models.DateTimeField(auto_now=True)
#____________________END Screening Info_______________________

#_______________EAR SCREENING____________________
class agg_sc_ear_screening_info(models.Model):
    citizen_id  = models.ForeignKey(agg_sc_add_new_citizens, on_delete=models.CASCADE,to_field='citizens_id')
    schedule_count = models.IntegerField()
    schedule_id_old = models.CharField(max_length=255)
    schedule_id = models.ForeignKey('agg_sc_shedule_screening_info', on_delete=models.CASCADE,to_field='schedule_id')
    allergic_reaction = models.CharField(max_length=255)
    cleft_ip = models.CharField(max_length=255)
    hearing_loss = models.CharField(max_length=255)
    congenital_abnormality_of_ear = models.CharField(max_length=255)
    cleft_palate = models.CharField(max_length=255)
    tongue_tie = models.CharField(max_length=255)
    remark =  models.CharField(max_length=500)
    added_by = models.CharField(max_length=255)
    added_date = models.DateField()
    modify_by = models.CharField(max_length=255)
    modify_date = models.DateField(auto_now=True)
    is_deleted = models.CharField(max_length=10, choices=is_deleted.choices)
    modify_date_sync = models.DateTimeField(auto_now=True)

#________________DENTAL SCREENING____________________
class agg_sc_dental_screening(models.Model):
    citizen_id  = models.ForeignKey(agg_sc_add_new_citizens, on_delete=models.CASCADE,to_field='citizens_id')
    schedule_count = models.IntegerField()
    schedule_id_old = models.CharField(max_length=255)
    schedule_id = models.ForeignKey('agg_sc_shedule_screening_info', on_delete=models.CASCADE,to_field='schedule_id')
    oral_hygiene = models.CharField(max_length=255)
    oral_hygiene_remark = models.CharField(max_length=255)
    gum_condition = models.CharField(max_length=255)
    gum_condition_remark = models.CharField(max_length=255)
    oral_ulcers = models.CharField(max_length=255)
    oral_ulcers_remark = models.CharField(max_length=255)
    gum_bleeding = models.CharField(max_length=255)
    gum_bleeding_remark = models.CharField(max_length=255)
    discolouration_of_teeth = models.CharField(max_length=255)
    discolouration_of_teeth_remark = models.CharField(max_length=255)
    food_impaction = models.CharField(max_length=255)
    food_impaction_remark = models.CharField(max_length=255)
    carious_teeth = models.CharField(max_length=255)
    carious_teeth_remark = models.CharField(max_length=255)
    extraction_done = models.CharField(max_length=255)
    extraction_done_remark = models.CharField(max_length=255)
    fluorosis = models.CharField(max_length=255)
    fluorosis_remark = models.CharField(max_length=255)
    tooth_brushing_frequency = models.CharField(max_length=255)
    tooth_brushing_frequency_remark = models.CharField(max_length=255)
    reffered_to_specialist = models.CharField(max_length=255)
    reffered_to_specialist_remark = models.CharField(max_length=255)
    comment = models.CharField(max_length=255)
    treatment_given = models.CharField(max_length=255)
    added_by = models.CharField(max_length=255)
    added_date = models.DateField()
    modify_by = models.CharField(max_length=255)
    modify_date = models.DateField(auto_now=True)
    is_deleted = models.CharField(max_length=10, choices=is_deleted.choices)
    modify_date_sync = models.DateTimeField(auto_now=True)

#____________________pychology_table___________________________
class agg_sc_pycho_info(models.Model):
    pk_id = models.AutoField(primary_key=True)
    student_id = models.CharField(max_length=255)
    schedule_count = models.IntegerField()
    schedule_id_old = models.CharField(max_length=255)
    schedule_id = models.CharField(max_length=255)
    diff_in_read = models.CharField(max_length=255)
    diff_in_read_text = models.CharField(max_length=255)
    diff_in_write = models.CharField(max_length=255)
    diff_in_write_text = models.CharField(max_length=255)
    hyper_reactive = models.CharField(max_length=255)
    hyper_reactive_text = models.CharField(max_length=255)
    aggresive = models.CharField(max_length=255)
    aggresive_text = models.CharField(max_length=255)
    urine_stool = models.CharField(max_length=255)
    urine_stool_text = models.CharField(max_length=255)
    peers = models.CharField(max_length=255)
    peers_text = models.CharField(max_length=255)
    poor_contact = models.CharField(max_length=255)
    poor_contact_text = models.CharField(max_length=255)
    scholastic = models.CharField(max_length=255)
    scholastic_text = models.CharField(max_length=255)
    any_other = models.CharField(max_length=255)
    is_deleted = models.CharField(max_length=10, choices=is_deleted.choices)
    added_by = models.CharField(max_length=255)
    added_date = models.DateField()
    modify_by = models.CharField(max_length=255)
    modify_date = models.DateField(auto_now=True)
    modify_date_sync = models.DateTimeField(auto_now=True)  
    
#___________________BMI & Symptoms INFO__________________________
class agg_sc_bmi_info(models.Model):
    pk_id = models.AutoField(primary_key=True)
    citizen_id = models.ForeignKey(agg_sc_add_new_citizens, on_delete=models.CASCADE,to_field='citizens_id')
    schedule_count = models.IntegerField()
    schedule_id_old = models.CharField(max_length=255)
    schedule_id = models.ForeignKey('agg_sc_shedule_screening_info', on_delete=models.CASCADE,to_field='schedule_id')
    height = models.FloatField()
    weight = models.FloatField()
    bmi = models.FloatField()
    weight_for_ht = models.CharField(max_length=255)
    weight_for_age = models.CharField(max_length=255)
    height_for_age = models.CharField(max_length=255)    
    arm_size = models.FloatField()
    note = models.CharField(max_length=255)
    general_exam = models.CharField(max_length=255)
    chief_complaint = models.IntegerField()
    symptoms = models.CharField(max_length=255)
    other_sign = models.CharField(max_length=255)
    stud_symptoms = models.CharField(max_length=255)
    remark = models.CharField(max_length=255)
    added_date = models.DateField()
    bmi_clg_id = models.CharField(max_length=255)
    added_by = models.CharField(max_length=255)
    modify_by = models.CharField(max_length=255)
    is_deleted = models.CharField(max_length=10, choices=is_deleted.choices)
    modify_date = models.DateTimeField(auto_now=True)
    
#__________________Auditory_________________
class agg_sc_audit_info(models.Model):
    pk_id = models.AutoField(primary_key=True)
    student_id = models.CharField(max_length=255)
    schedule_count = models.IntegerField()
    schedule_id = models.CharField(max_length=255)
    schedule_id_old = models.CharField(max_length=255)
    hearing_right = models.CharField(max_length=255)
    hearing_left = models.CharField(max_length=255)
    otoscopic_exam = models.CharField(max_length=255)
    ent_comment = models.CharField(max_length=255)
    ent_check_if_present = models.CharField(max_length=255)
    treatment_given = models.CharField(max_length=255)
    is_deleted = models.CharField(max_length=10, choices=is_deleted.choices)
    added_by = models.CharField(max_length=255)
    added_date = models.DateField()
    modify_by = models.CharField(max_length=255)
    modify_date = models.DateField(auto_now=True)
    modify_date_sync = models.DateTimeField(auto_now=True)
    
    def __str__(self) :
        return self.pk_id
    
#____________________SCHEDULE SCREENING________________________
class agg_sc_shedule_screening_info(models.Model):
    schedule_id = models.CharField(max_length=20,editable=False,unique=True)
    from_date = models.DateField()
    to_date = models.DateField()
    source_name = models.CharField(max_length=255)
    source_district = models.CharField(max_length=255)
    disease = models.CharField(max_length=255)
    screening_person_name = models.CharField(max_length=255,null=False)
    mobile_no = models.CharField(max_length=10,null=False)
    is_deleted = models.BooleanField(default=False)
    
    
    def save(self, *args, **kwargs):
                if not self.schedule_id:
                    last_record = agg_sc_shedule_screening_info.objects.all().order_by('-schedule_id').first()
                    if last_record:
                        last_sequence = int(last_record.schedule_id[5:]) + 1
                    else:
                        last_sequence = 1
                    self.schedule_id = f"SCH-{last_sequence:05d}"
                super().save(*args, **kwargs)

    def __str__(self):
        return self.schedule_id
    
#___________________ADD NEW SOURCE________________________#
class Screening_Source(models.TextChoices):
    SCHOOL  = 'SCHOOL'
    CAMP    = 'CAMP'
    NGO     = 'NGO'
    SOCIETY = 'SOCIETY'
    
    
class agg_sc_add_new_source(models.Model):
    source_id = models.CharField(max_length=20, editable=False,unique=True)
    screening_source = models.CharField(max_length=255,choices=Screening_Source.choices)
    source_name = models.CharField(max_length=255)
    registration_no = models.IntegerField()
    mobile_no = models.CharField(max_length=10)
    email_id = models.EmailField()
    Registration_details = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    tehsil = models.CharField(max_length=255)
    pincode = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    
    def save(self, *args, **kwargs):
                if not self.source_id:
                    last_record = agg_sc_add_new_source.objects.all().order_by('-source_id').first()
                    if last_record:
                        last_sequence = int(last_record.source_id[5:]) + 1
                    else:
                        last_sequence = 1
                    self.source_id = f"SI-{last_sequence:05d}"
                super().save(*args, **kwargs)

    def __str__(self):
        return self.source_id
#_____________________Start Screening_________________________ 
from django.db import models
from django.utils import timezone

class agg_sc_start_screening(models.Model):
    screening_id = models.CharField(max_length=20, primary_key=True, editable=False)
    citizen_id = models.ForeignKey(agg_sc_add_new_citizens, on_delete=models.CASCADE, to_field='citizens_id')
    citizen_name = models.CharField(max_length=255, blank=True)  # Add appropriate max_length
    citizen_mobile = models.CharField(max_length=10, blank=True)  # Add appropriate max_length
    schedule_id = models.ForeignKey(agg_sc_shedule_screening_info, on_delete=models.CASCADE, to_field='schedule_id')
    source_id = models.ForeignKey(agg_sc_add_new_source, on_delete=models.CASCADE, to_field='source_id')
    created_date = models.DateField(default=timezone.now, editable=False)
    
    def generate_id(self):
        last_id = agg_sc_start_screening.objects.filter(created_date=self.created_date).order_by('-screening_id').first()
        if last_id:
            last_id_value = int(last_id.screening_id.split('-')[1][-4:])
            new_id_value = last_id_value + 1
            return int(str(self.created_date.strftime('%d%m%Y')) + str(new_id_value).zfill(5))
        else:
            return int(str(self.created_date.strftime('%d%m%Y')) + '00001')

    def save(self, *args, **kwargs):
        if not self.screening_id:
            generated_id = self.generate_id()
            self.screening_id = f"SS-{generated_id}"

            # Retrieve citizen details from the related agg_sc_add_new_citizens instance
            if self.citizen_id:
                self.citizen_name = self.citizen_id.citizen_name
                self.citizen_mobile = self.citizen_id.parents_mobile

            super(agg_sc_start_screening, self).save(*args, **kwargs)

    # def __str__(self):
    #     return self.screening_id


#__________________VITAL_INFO_____________________
class agg_sc_vital_info(models.Model):
    citizen_id  = models.ForeignKey(agg_sc_add_new_citizens, on_delete=models.CASCADE,to_field='citizens_id')
    schedule_count = models.IntegerField()
    schedule_id_old = models.CharField(max_length=255)
    schedule_id = models.ForeignKey(agg_sc_shedule_screening_info, on_delete=models.CASCADE,to_field='schedule_id')
    pulse = models.FloatField()
    sys_mm = models.FloatField()
    dys_mm = models.FloatField()
    rr = models.FloatField()
    oxygen_saturation = models.FloatField()
    hb = models.FloatField()
    temp = models.FloatField()
    added_by = models.CharField(max_length=255)
    added_date = models.DateField()
    modify_by = models.CharField(max_length=255)
    modify_date = models.DateField(auto_now=True)
    is_deleted = models.CharField(max_length=10, choices=is_deleted.choices)
    modify_date_sync = models.DateTimeField(auto_now=True)
    
    # def __str__(self):
    #     return self.citizen_id
#__________________END_VITAL_INFO_____________________

class agg_sc_disease(models.Model):
    disease_id = models.AutoField(primary_key=True)
    disease = models.CharField(max_length=255)
    added_by = models.CharField(max_length=255)
    added_date = models.DateField()
    modify_by = models.CharField(max_length=255)
    modify_date = models.DateField(auto_now=True)
    is_deleted = models.CharField(max_length=10, choices=is_deleted.choices)
    modify_date_sync = models.DateTimeField(auto_now=True)

# from django.db import models
# from datetime import datetime

# class Person(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     date_of_birth = models.DateField()
#     age = models.IntegerField(blank=True)
#     months = models.IntegerField(blank=True)
#     days = models.IntegerField(blank=True)

#     def calculate_age(self):
#         today = datetime.today()
#         dob = self.date_of_birth
#         years = today.year - dob.year
#         months = today.month - dob.month
#         days = today.day - dob.day

#         if months < 0 or (months == 0 and days < 0):
#             years -= 1
#             months += 12
        
#         if days < 0:
#             months -= 1
#             days += 30  # Assuming each month has 30 days for simplicity
        
#         return years, months, days
   

#     def save(self, *args, **kwargs):
#         self.age, self.months, self.days = self.calculate_age()  # Update the fields
#         super().save(*args, **kwargs)


USER_GROUP = (
        ('OPERATION MANAGER(SA)', 'OPERATION MANAGER(SA)'),
        ('CHO', 'CHO'),
        ('DRCHO', 'DRCHO'),
        ('DOCTOR', 'DOCTOR'),
        ('THO', 'THO'),
        ('MO', 'MO'),
        ('CO', 'CO'),
        ('RMO', 'RMO'),
        ('RBSK', 'RBSK'),
        ('MS', 'MS'),
        ('CDPO', 'CDPO'),
        ('SUPERVISOR', 'SUPERVISOR'),
        ('EXPERT', 'EXPERT'),
    )  
class agg_sc_add_new_users(models.Model):
    clg_ref_id = models.CharField(max_length=10, unique=True, default='EMP-1',blank=True)
    name = models.CharField(max_length=255)
    mobile_no = models.CharField(max_length=255)
    email_id = models.EmailField()
    dob = models.DateField()
    gender = models.CharField(max_length=255,choices=Gender_CHOICES)
    group = models.CharField(max_length=255,choices=USER_GROUP)
    address = models.CharField(max_length=255)
    added_by = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    modify_by = models.CharField(max_length=255)
    modified_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.clg_ref_id:
            # Generate a new clg_ref_id if it's not set
            latest_student = agg_sc_add_new_users.objects.order_by('-clg_ref_id').first()
            if latest_student:
                last_number = int(latest_student.clg_ref_id.split('-')[1])
                new_number = last_number + 1
                self.clg_ref_id = f'EMP-{new_number}'
            else:
                self.clg_ref_id = 'EMP-1'
        super(agg_sc_add_new_users, self).save(*args, **kwargs)

    def __str__(self):
        return self.clg_ref_id











# from django.db import models
# from django.utils import timezone

# class agg_sc_add_new_citizens1(models.Model):
#     # ______________________ ID's _____________________________________________
#     citizens_pk_id = models.AutoField(editable=False, primary_key=True)
#     citizens_id = models.CharField(max_length=50, editable=False, unique=True)

#     # _______________________ Search_Fields _____________________________________
#     age = models.CharField(max_length=255)
#     gender = models.CharField(max_length=255)
#     source = models.CharField(max_length=255)
#     disease = models.CharField(max_length=255)

#     #________________________ CHILD DETAILS______________________________________
#     name = models.CharField(max_length=255)
#     child_gender = models.CharField(max_length=255)  # Use different name to avoid conflict
#     dob = models.DateField()
#     blood_groups = models.CharField(max_length=255, null=False)
#     year = models.CharField(max_length=12)
#     months = models.CharField(max_length=12)
#     days = models.CharField(max_length=12)
#     aadhar_id = models.CharField(max_length=12, unique=True, null=False)

#     #_____________FAMILY INFORMATION_____________
#     father_name = models.CharField(max_length=255)
#     mother_name = models.CharField(max_length=255)
#     occupation_of_father = models.CharField(max_length=255, null=False)
#     occupation_of_mother = models.CharField(max_length=255, null=False)
#     parents_mobile = models.CharField(max_length=10, null=False)
#     sibling_count = models.CharField(max_length=10, null=False)

#     #___________ADDRESS_____________________________
#     source_name = models.CharField(max_length=255)
#     state = models.CharField(max_length=255)
#     district = models.CharField(max_length=255)
#     tehsil = models.CharField(max_length=255)
#     pincode = models.CharField(max_length=255)
#     address = models.CharField(max_length=255, null=False)

#     #___________GROWTH MONITORING________________
#     height = models.FloatField()
#     weight = models.FloatField()
#     weight_for_age = models.CharField(max_length=255)
#     height_for_age = models.CharField(max_length=255)
#     weight_for_height = models.CharField(max_length=255, null=False, blank=True)
#     bmi = models.FloatField(null=False, blank=True)
#     arm_size = models.FloatField(null=False)
#     symptoms = models.CharField(max_length=255, null=False)

#     created_date = models.DateField(default=timezone.now, editable=False)
#     added_by = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True)
#     modify_by = models.CharField(max_length=255)
#     modified_at = models.DateTimeField(auto_now=True)
#     is_deleted = models.CharField(max_length=10)  # Make sure is_delete is defined

#     def generate_id(self):
#         last_id = agg_sc_add_new_citizens1.objects.filter(created_date=self.created_date).order_by('-citizens_id').first()

#         if last_id and '-' in last_id.citizens_id:
#             last_id_parts = last_id.citizens_id.split('-')
#             if len(last_id_parts) >= 2:
#                 last_id_value = int(last_id_parts[1][-6:])
#                 new_id_value = last_id_value + 1   
#                 return int(str(self.created_date.strftime('%d%m%Y')) + str(new_id_value).zfill(6))

#         return int(str(self.created_date.strftime('%d%m%Y')) + '000001')

#     def save(self, *args, **kwargs):
#         if not self.citizens_id:
#             generated_id = self.generate_id()
#             self.citizens_id = f"CTZN-{generated_id}"

#         if not self.citizens_pk_id:
#             # Calculate the BMI before saving
#             self.bmi = self.weight / ((self.height / 100) ** 2)

#             # Categorize the BMI
#             if self.bmi < 18.5:
#                 self.weight_for_height = 'Underweight'
#             elif 18.5 <= self.bmi < 25:
#                 self.weight_for_height = 'Normal weight'
#             elif 25 <= self.bmi < 30:
#                 self.weight_for_height = 'Overweight'
#             else:
#                 self.weight_for_height = 'Obese'

#         super(agg_sc_add_new_citizens1, self).save(*args, **kwargs)
        
#     def __str__(self):
#         return self.name
    
    
class agg_sc_treatment_info(models.Model):
    treatment_for = models.CharField(max_length=255)
    referral = models.CharField(max_length=255)
    reason_for_referral = models.CharField(max_length=255)
    place_referral = models.CharField(max_length=255)
    outcome = models.CharField(max_length=255)
    
    def __str__(self):
        return self.place_referral
    
    
class agg_sc_citizen_basic_info(models.Model):
    basic_info_id= models.AutoField(primary_key=True)
    citizen_id  = models.ForeignKey(agg_sc_start_screening, on_delete=models.CASCADE,null=True)
    schedule_id = models.ForeignKey(agg_sc_shedule_screening_info, on_delete=models.CASCADE, to_field='schedule_id',null=True)
    citizen_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    blood_group = models.CharField(max_length=255)
    dob = models.CharField(max_length=255)
    year = models.IntegerField()
    months = models.IntegerField()
    days = models.IntegerField()
    aadhar_id = models.CharField(max_length=255)
    added_by = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    modify_by = models.CharField(max_length=255)
    modified_at = models.DateTimeField(auto_now=True)
    
    

class agg_sc_medical_event_info(models.Model):
    medical_event_id =  models.AutoField(primary_key=True)
    citizens_id  = models.ForeignKey(agg_sc_add_new_citizens,on_delete=models.CASCADE)
    schedule_id = models.ForeignKey(agg_sc_start_screening,on_delete=models.CASCADE)
    symptoms_if_any = models.CharField(max_length=255)
    remark = models.CharField(max_length=255)
    added_by = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    modify_by = models.CharField(max_length=255)
    modified_at = models.DateTimeField(auto_now=True)
    
    
    # def __str__(self):
    #     return self.added_by




class zerototwo(models.Model):
    birth_year = models.IntegerField()
    birth_month = models.IntegerField()
    minus_three_sd = models.FloatField()
    minus_two_sd = models.FloatField()
    minus_one_sd = models.FloatField()
    one_sd = models.FloatField()
    two_sd = models.FloatField()
    three_sd = models.FloatField()
    gender = models.CharField(max_length=255)
    
    def __str__(self):
        return self.gender
    
class sm(models.Model):
    name = models.CharField(max_length=255)
    height = models.FloatField()
    weight = models.FloatField()
    
    
    
# models.py
from django.db import models

class abc(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField()
    mobile = models.CharField(max_length=10)
    email = models.EmailField()
    gender = models.CharField(max_length=10)
    blood_group = models.CharField(max_length=10)
    

from django.db import models
from django.utils import timezone

class GrowthMonitoring(models.Model):
    gender = models.CharField(max_length=255)
    dob = models.DateField()
    height = models.FloatField(null=False)
    weight = models.FloatField(null=False)
    weight_for_age = models.CharField(max_length=50, blank=True, null=True)
    height_for_age = models.CharField(max_length=50, blank=True, null=True)
    weight_for_height = models.CharField(max_length=50, blank=True, null=True)
    bmi = models.FloatField(blank=True, null=True)

    def save(self, *args, **kwargs):
        # Calculate age using dateutil.relativedelta for precise age calculation
        age_in_years = (timezone.now().date() - self.dob).days / 365.25

        if age_in_years > 10:
            # Calculate BMI only if age is above 10 years
            self.bmi = self.weight / ((self.height / 100) ** 2)

            # Categorize the BMI
            if self.bmi < 18.5:
                self.weight_for_height = 'Underweight'
            elif 18.5 <= self.bmi < 25:
                self.weight_for_height = 'Normal weight'
            elif 25 <= self.bmi < 30:
                self.weight_for_height = 'Overweight'
            else:
                self.weight_for_height = 'Obese'
        else:
            # Set BMI and related fields to None if age is 10 years or younger
            self.bmi = None
            self.weight_for_height = None
            self.weight_for_age = None
            self.height_for_age = None

        super(GrowthMonitoring, self).save(*args, **kwargs)


      
class agg_sc_citizen_schedule(models.Model):
    pk_id = models.AutoField(primary_key=True)
    schedule_count = models.CharField(max_length=255)
    citizen_id = models.CharField(max_length=255) 
    schedule_id = models.CharField(max_length=255)
    added_by = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    modify_by = models.CharField(max_length=255)
    modified_at = models.DateTimeField(auto_now=True)
    closing_status = models.BooleanField(default=False)
    schedule_is_deleted = models.BooleanField(default=False)
    
        
    
    



