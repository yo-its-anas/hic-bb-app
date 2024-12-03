def get_blood_banks(location, blood_group):
blood_banks = [
    {"name": "Clifton Blood Bank", "location": "Clifton", "contact": "021-1234567", "distance": 2.5},
    {"name": "Saddar Blood Bank", "location": "Saddar", "contact": "021-9876543", "distance": 3.0},
    {"name": "Gulshan Blood Bank", "location": "Gulshan-e-Iqbal", "contact": "021-1122334", "distance": 4.0},
    {"name": "Defence Blood Bank", "location": "DHA", "contact": "021-4455667", "distance": 1.8},
    {"name": "Nazimabad Blood Bank", "location": "Nazimabad", "contact": "021-7788990", "distance": 2.7},
    {"name": "North Nazimabad Blood Bank", "location": "North Nazimabad", "contact": "021-5544332", "distance": 3.5},
    {"name": "PECHS Blood Bank", "location": "PECHS", "contact": "021-6677885", "distance": 2.9},
    {"name": "Korangi Blood Bank", "location": "Korangi", "contact": "021-9988776", "distance": 5.0},
    {"name": "Liaquatabad Blood Bank", "location": "Liaquatabad", "contact": "021-3366998", "distance": 3.8},
    {"name": "Malir Blood Bank", "location": "Malir", "contact": "021-7766554", "distance": 6.2},
    {"name": "Landhi Blood Bank", "location": "Landhi", "contact": "021-6655443", "distance": 6.5},
    {"name": "Orangi Blood Bank", "location": "Orangi Town", "contact": "021-5566778", "distance": 7.1},
    {"name": "Gulistan Blood Bank", "location": "Gulistan-e-Jauhar", "contact": "021-4433221", "distance": 4.4},
    {"name": "Shah Faisal Blood Bank", "location": "Shah Faisal Colony", "contact": "021-9988776", "distance": 5.5},
    {"name": "Model Colony Blood Bank", "location": "Model Colony", "contact": "021-5577990", "distance": 4.9},
    {"name": "Mehmoodabad Blood Bank", "location": "Mehmoodabad", "contact": "021-9900775", "distance": 2.3},
    {"name": "Shershah Blood Bank", "location": "Shershah", "contact": "021-6655447", "distance": 5.8},
    {"name": "Keamari Blood Bank", "location": "Keamari", "contact": "021-3344556", "distance": 6.0},
    {"name": "New Karachi Blood Bank", "location": "New Karachi", "contact": "021-8899007", "distance": 7.0},
    {"name": "FB Area Blood Bank", "location": "Federal B Area", "contact": "021-6677889", "distance": 3.2},
    {"name": "Tariq Road Blood Bank", "location": "Tariq Road", "contact": "021-2200998", "distance": 3.4},
    {"name": "Kharadar Blood Bank", "location": "Kharadar", "contact": "021-9977443", "distance": 3.6},
    {"name": "Lyari Blood Bank", "location": "Lyari", "contact": "021-5544332", "distance": 4.8},
    {"name": "Jamshed Town Blood Bank", "location": "Jamshed Town", "contact": "021-4433227", "distance": 3.1},
    {"name": "Garden Blood Bank", "location": "Garden", "contact": "021-1122443", "distance": 2.4}
]
return [bank for bank in blood_banks if bank["location"] == location]
