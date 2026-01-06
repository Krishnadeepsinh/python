"""create dictionary to store 20 different detail about your ownself 
print dictionary
print name, age, gender, dob 
add key value pair pincode into dictionary 
add key value pair to store your 5 favourite touriest destination 
print all the favourite touriest destination """

details = {
    "name": "KD",
    "age": 19,
    "gender": "Male",
    "dob": "2-05-2006",
    "email": "abc@gmail.com",
    "phone": "+9876543210",
    "nationality": "Indian",
    "occupation": "Software Engineer",
    "education": "BCA",
    "blood_group": "O-Positive",
    "height": "172 cm",
    "weight": "85 kg",
    "marital_status": "Single",
    "languages_known": ["English", "Hindi", "German"],
    "hobbies": ["Photography", "Cycling", "Chess"],
    "skills": ["Python",],
    "des" : ["bhavnagar","surat","simla","manali","goa"]
}
print(details["name"],details["age"],details["gender"])
details['pincode']='364004'
print(details["pincode"])
print(details["des"])