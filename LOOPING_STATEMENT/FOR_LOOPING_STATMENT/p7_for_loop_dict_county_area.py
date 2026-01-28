#7) write a program to findout coutries whose area is greater given area. use chatgpt to create dictionaries which country name as key and its' area as value. 

countries_area = {
    "Russia": 17098242,
    "Canada": 9984670,
    "China": 9596961,
    "United States": 9833517,
    "Brazil": 8515767,
    "Australia": 7692024,
    "India": 3287263,
    "Argentina": 2780400,
    "Kazakhstan": 2724900,
    "Algeria": 2381741
}

area_by_user=int(input("ENTER THE AREA "))

for area in countries_area:
    if countries_area[area]>area_by_user:
        print(area,countries_area[area])