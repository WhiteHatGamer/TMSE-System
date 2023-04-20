#multi dimensional dictionary
#stud_list = [
    #{'admn':'17/246/CS/TKR', 'univ':'TKR17CS027', 'name':'Muhammed Thahir M'},
    #{'admn':'18/215/CS/TKR', 'univ':'TKR18CS016', 'Name':'Asiya Sheenu'},
    #{'admn':'18/113/CS/TKR', 'univ':'TKR18CS021', 'name':'Drishya T'},
    #{'admn':'18/071/CS/TKR', 'univ':'TKR18CS039', 'name':'Safaa C'}
#]
#access by result = [i['name'] for i in stud_list if i['admn'] == student_id]



#another(Its an interesting List of Dictionaries)
student_db = [
    #'TKR18CS001': 'ABHILASH',
    {'admn':'18/007/CS/TKR', 'univ':'TKR18CS002', 'name':'ABIN JOSE SHAJU'},
    #'TKR18CS003': 'AKSHAY C K',
    {'admn':'18/152/CS/TKR', 'univ':'TKR18CS004', 'name':'AMITH V'},
    {'admn':'18/123/CS/TKR', 'univ':'TKR18CS005', 'name':'AMRITHESH VALSAN P'},
    #'TKR18CS006': 'ANAKHA KRISHNA',
    #'TKR18CS007': 'ANNOWAYA E V',
    #'TKR18CS008': 'ANUGRAHA MANOHARAN',
    {'admn':'18/102/CS/TKR', 'univ':'TKR18CS009', 'name':'ANUJITH M V'},
    #'TKR18CS010': 'ANUPRIYA P',
    #'TKR18CS011': 'APARNA K P',
    #'TKR18CS012': 'ARJUN K V',
    #'TKR18CS013': 'ARJUN M',
    #'TKR18CS014': 'ASHEEQA ANJUM AHMED',
    #'TKR18CS015': 'ASHOP P K',
    {'admn':'18/215/CS/TKR', 'univ':'TKR18CS016', 'Name':'Asiya Sheenu'},
    #'TKR18CS017': 'ATHUL T',
    #'TKR18CS018': 'AVINASH JAYAPRAKASH',
    #'TKR18CS019': 'DEVA YADHU RAG',
    #'TKR18CS020': 'DRISHYA C K',
    {'admn':'18/113/CS/TKR', 'univ':'TKR18CS021', 'name':'Drishya T'},
    #'TKR18CS022': 'FATHIMATH ASFANA K',
    #'TKR18CS023': 'FATHIMATH JASNA P',
    #'TKR18CS024': 'FATHIMA V P P',
    #'TKR18CS025': 'GOPIKRISHNAN N M',
    #'TKR18CS026': 'JISHNU T K',
    #'TKR18CS027': 'KAVYA K',
    #'TKR18CS028': 'KIRAN KRISHNAN K',
    {'admn':'18/178/CS/TKR', 'univ':'TKR18CS029', 'name':'Merin Job'},
    #'TKR18CS030': 'MOHAMMED HAMIR',
    {'admn':'18/111/CS/TKR', 'univ':'TKR18CS031', 'name':'Muhammed Ashid M T C'},
    {'admn':'18/227/CS/TKR', 'univ':'TKR18CS032', 'name':'Muhammed Thajudeen T C'},
    #'TKR18CS033': 'NIJIN P S',
    {'admn':'18/040/CS/TKR', 'univ':'TKR18CS035', 'name':'Nived K'},
    #'TKR18CS035': 'NIVED K V',
    #'TKR18CS036': 'RAHMATHUNISA T K',
    #'TKR18CS037': 'RAMITHA',
    {'admn':'18/107/CS/TKR', 'univ':'TKR18CS038', 'name':'Roopesh Shankar P'},
    {'admn':'18/071/CS/TKR', 'univ':'TKR18CS039', 'name':'Safaa C'},
    #'TKR17CS040': 'SANOOP T V',
    #'TKR18CS041': 'SARANGI K',
    #'TKR18CS042': 'SHAHANAS A G',
    #'TKR18CS043': 'SHAHMA JABEEN JAMAL',
    #'TKR18CS044': 'SNEHA PRIYA M',
    #'TKR18CS045': 'SOURAV K',
    #'TKR18CS046': 'SREE KUTTAN',
    #'TKR18CS047': 'shreeshma c p',
    #'TKR18CS048': 'SUDINA T',
    #'TKR18CS049': 'SURYA SURESH S',
    #'TKR18CS050': 'THEERTHA JAYARAM',
    #'LTKR18CS051': 'ARUNIMA V',
    {'admn':'19/197/CS/LTKR', 'univ':'LTKR18CS052', 'name':'ASHITHA JOY'},
    #'LTKR18CS053': 'JIMITH K C',
    #'LTKR18CS054': 'SOORYA K V',
    #'VAK18CS040': 'SNEHA T V',
    #'TKR17CS009': 'ANJANA C H',
    #'TKR17CS010': 'ANUVIND SASIDHARAN',
    #'TKR17CS012': 'ARJUN RAJ K M',
    {'admn':'17/246/CS/TKR', 'univ':'TKR17CS027', 'name':'Muhammed Thahir M'}
]

#For Main Program
def findnm(student_id):
    try:
        for i in student_db:
            if (i['admn'] == student_id):
                student_name = i['name']
                student_univ = i['univ']
        return student_name,student_univ
    except NameError:
        return student_id,student_id

#def findun(student_id):
    #try:
        #for i in stud_list:
            #if (i['univ'] == student_id):
                #student_un = i['name'] 
        #return student_un
    #except NameError:
        #return student_id
#studname = studentcode[student_id]

#[studentcode = {
    #'TKR18CS001': 'ABHILASH',
    #'TKR18CS002': 'ABIN JOSE SHAJU',
    #'TKR18CS003': 'AKSHAY C K',
    #'TKR18CS004': 'AMITH V',
    #'TKR18CS005': 'AMRITHESH VALSAN P',
    #'TKR18CS006': 'ANAKHA KRISHNA',
    #'TKR18CS007': 'ANNOWAYA E V',
    #'TKR18CS008': 'ANUGRAHA MANOHARAN',
    #'TKR18CS009': 'ANUJITH M V',
    #'TKR18CS010': 'ANUPRIYA P',
    #'TKR18CS011': 'APARNA K P',
    #'TKR18CS012': 'ARJUN K V',
    #'TKR18CS013': 'ARJUN M',
    #'TKR18CS014': 'ASHEEQA ANJUM AHMED',
    #'TKR18CS015': 'ASHOP P K',
    #'TKR18CS016': 'ASIYA SHEENU',
    #'TKR18CS017': 'ATHUL T',
    #'TKR18CS018': 'AVINASH JAYAPRAKASH',
    #'TKR18CS019': 'DEVA YADHU RAG',
    #'TKR18CS020': 'DRISHYA C K',
    #'TKR18CS021': 'DRISHYA T',
    #'TKR18CS022': 'FATHIMATH ASFANA K',
    #'TKR18CS023': 'FATHIMATH JASNA P',
    #'TKR18CS024': 'FATHIMA V P P',
    #'TKR18CS025': 'GOPIKRISHNAN N M',
    #'TKR18CS026': 'JISHNU T K',
    #'TKR18CS027': 'KAVYA K',
    #'TKR18CS028': 'KIRAN KRISHNAN K',
    #'TKR18CS029': 'MERIN JOB',
    #'TKR18CS030': 'MOHAMMED HAMIR',
    #'TKR18CS031': 'MUHAMMED ASHID M T C',
    #'TKR18CS032': 'MUHAMMED THAJUDEEN T C',
    #'TKR18CS033': 'NIJIN P S',
    #'TKR18CS034': 'NIVED K',
    #'TKR18CS035': 'NIVED K V',
    #'TKR18CS036': 'RAHMATHUNISA T K',
    #'TKR18CS037': 'RAMITHA',
    #'TKR18CS038': 'ROOPESH SHANKAR P',
    #'TKR18CS039': 'SAFAA C',
    #'TKR17CS040': 'SANOOP T V',
    #'TKR18CS041': 'SARANGI K',
    #'TKR18CS042': 'SHAHANAS A G',
    #'TKR18CS043': 'SHAHMA JABEEN JAMAL',
    #'TKR18CS044': 'SNEHA PRIYA M',
    #'TKR18CS045': 'SOURAV K',
    #'TKR18CS046': 'SREE KUTTAN',
    #'TKR18CS047': 'shreeshma c p',
    #'TKR18CS048': 'SUDINA T',
    #'TKR18CS049': 'SURYA SURESH S',
    #'TKR18CS050': 'THEERTHA JAYARAM',
    #'LTKR18CS051': 'ARUNIMA V',
    #'LTKR18CS052': 'ASHITHA JOY',
    #'LTKR18CS053': 'JIMITH K C',
    #'LTKR18CS054': 'SOORYA K V',
    #'VAK18CS040': 'SNEHA T V',
    #'TKR17CS009': 'ANJANA C H',
    #'TKR17CS010': 'ANUVIND SASIDHARAN',
    #'TKR17CS012': 'ARJUN RAJ K M',
    #'TKR17CS027': 'MUHAMMED THAHIR'
#}
