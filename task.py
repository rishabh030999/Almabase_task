from fuzzywuzzy import fuzz


class Profile(object):
    
    def __init__(self,arr):
        self.first_name = arr.get("first_name")
        self.last_name = arr.get("last_name")
        self.date_of_birth = arr.get("date_of_birth") # format will be YYYY-MM-DD
        self.class_year = arr.get("class_year")
        self.email_field = arr.get("email_field")


def fuzzymatching(profile1:Profile,profile2:Profile,field:list=["first_name","last_name","email_field"]):
        Score= 0
        profile_str_1=""
        profile_str_2=""
        for i in field:
            profile_str_1+=getattr(profile1,i)
        for i in field:
            profile_str_2+=getattr(profile2,i)
            
        result=fuzz.ratio(profile_str_1,profile_str_2)
        
        if(result>80):
            Score = Score + 1
            # print(Total_Score)
            field.append('profile1')
            field.append('profile2')
            return field
        else:
             return []
        



def FieldMatching_general(field,profile1:Profile,profile2:Profile):
    score=0
    fields=[]
    if(getattr(profile1,field)==None or getattr(profile2,field)==None):
        return score 
    if(getattr(profile1,field)==getattr(profile2,field)):
        score=score+1
        Score = Score + score
        fields.append(field)
    else:
        score=score-1
        fields.append(score)
    return fields

# -------------
def ScoreCalculator(profile1:Profile,profile2:Profile,fields:list):
    Score=0
    if "last_name" in fields  and "first_name" in fields:
        Score = Score + fuzzymatching(profile1=profile1,profile2=profile2)
    if "class_year" in fields:
        Score= Score + FieldMatching_general('class_year',profile1=profile1,profile2=profile2)
    if "date_of_birth" in fields:
        Score= Score + FieldMatching_general('date_of_birth',profile1=profile1,profile2=profile2)
    return Score
    
def marge_profile(profile1:Profile,profile2:Profile,fields:list,score):
    all_attribute = set(profile1.__dict__.keys()+profile2.__dict__.keys)
    all_attribute = list(all_attribute)
    ignored_attributes = all_attribute - fields
    print(profile1,profile2,f"total match score :{score}",f"matching_attribute :{str(fields)}", f"ignored_attributes:{str(ignored_attributes)}")

def find_duplicates(profiles:list, fields:list):
    for i in range(len(profiles)):
        for j in range(i+1,len(profiles)):
            score = ScoreCalculator(profile1=profiles[i])
        

profile_1 = { "id": 1,
              "email_field": 'knowkanhai@gmail.com', 
              "first_name": "Kanhai",  
              "last_name": "Shah", 
              "class_year": "2012", 
              "date_of_birth": "1990-10-11"}

profile_2 = { "id": 2, 
             "email_field": "knowkanhai@gmail.com", 
             "first_name": "Kanhai1", 
             "last_name": "Shah", 
             "class_year": "2012", 
             "date_of_birth": "1990-10-11"}     
        
profile_1 = Profile(profile_1)
profile_2 = Profile(profile_2)
