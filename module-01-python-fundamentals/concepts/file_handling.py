#creating and writing in a new file
file = open("employees.txt","w")
file.write("101,Rahul Jha,Python Developer,45000\n")

lines=["102,Amit Sharma,Java Developer,50000\n",
"103,Priya Singh,Data Analyst,42000\n",
"104,Neha Verma,Frontend Developer,40000\n",
"105,Rohan Kumar,Backend Developer,55000\n",]

#appending in existing file
with open("employees.txt","a") as file:
    file.writelines(lines)

#Reading a file
with open("employees.txt","r") as file:
    content=file.read()
    print(content)

#json handling
#python dict to json string
import json

student = {
    "name": "Rahul",
    "age": 22,
    "course": "B.Tech"
}

json_data = json.dumps(student)

print(json_data)
print(type(json_data))

#json string to python object
student=json.loads(json_data)
print(student)
print(type(student))

#creating a json file
import json

student = {
    "name": "Rahul",
    "age": 22,
    "course": "B.Tech",
    "skills": ["Python", "Java", "SQL"]
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

print("Data saved successfully!")

#reading data from json
with open("student.json","r") as file:
    student=json.load(file)

print(student)
print(student["name"])

#see carefully
#True -> true
#None -> null
import json

data = {
    "name": "Rahul",
    "skills": ("Python", "SQL"),
    "active": True,
    "salary": None
}

json_data=json.dumps(data)

print(json_data)


#Practice
import json
tuf_laptop = {
    "brand": "ASUS",
    "series": "TUF Gaming",
    "model": "FX506HF",
    "price": 64990,
    "is_gaming_laptop": True,
    "specifications": {
        "processor": {
            "brand": "Intel",
            "model": "Core i5-11400H",
            "cores": 6,
            "threads": 12,
            "base_speed": "2.7 GHz"
        },
        "memory": {
            "ram": 16,
            "ram_type": "DDR4",
            "storage": 512,
            "storage_type": "SSD"
        },
        "graphics": {
            "brand": "NVIDIA",
            "model": "GTX 2050",
            "vram": 4
        },
        "display": {
            "size": 15.6,
            "resolution": "1920x1080",
            "refresh_rate": 144
        }
    },
    "ports": [
        "USB Type-A",
        "USB Type-C",
        "HDMI",
        "Ethernet",
        "3.5mm Audio Jack"
    ],
    "features": [
        "RGB Keyboard",
        "Cooling System",
        "Wi-Fi 6",
        "Bluetooth"
    ],
    "battery": {
        "capacity": 48,
        "unit": "Wh"
    }
}

with open("tuf_laptop.json","w") as file:
    json.dump(tuf_laptop,file,indent=4)

with open("tuf_laptop.json","r") as file:
    laptop=json.load(file)

print(laptop)

'''
Tasks
Print:
1. Brand
2. Model
3. Price
4. Is it a gaming laptop?
'''

print(laptop["brand"])
print(laptop["model"])
print(laptop["price"])
print(laptop.get("is_gaming_laptop"))

'''
Extract:
1. Processor model
2. Number of processor cores
3. RAM capacity
4. Storage capacity
5. Graphics card model
6. VRAM capacity
'''
print(laptop["specifications"]["processor"]["model"])
print(laptop["specifications"]["processor"]["cores"])
print(laptop["specifications"]["memory"]["ram"])
print(laptop["specifications"]["memory"]["storage"])
print(laptop["specifications"]["graphics"]["model"])
print(laptop["specifications"]["graphics"]["vram"])


'''
Extract:
1. Display resolution
2. Refresh rate
3. Battery capacity
4. First item in the ports list
5. Last item in the features list
'''
print(laptop["specifications"]["display"]["resolution"])
print(laptop["specifications"]["display"]["refresh_rate"])
print(laptop["battery"]["capacity"])
print(laptop["ports"][0])
print(laptop["features"][len(laptop["features"])-1])


'''
Challenge

1. Print all available ports using a loop.
2. Print all laptop features using a loop.
3. Print all processor details using a loop.
'''
for port in laptop["ports"]:
    print(port)

for feature in laptop["features"]:
    print(feature)

for processor in laptop["specifications"]["processor"]:
    print(processor)


'''
Challenge

1. Check whether RAM is at least 16 GB.
2. Check whether the display refresh rate is at least 120 Hz.
3. Check whether the laptop has an HDMI port.
'''
if laptop["specifications"]["memory"]["ram"]==16:
    print("RAM is 16 GB")
else:
    print("RAM is not 16 GB")



if laptop["specifications"]["display"]["refresh_rate"]>=120:
    print("refresh rate is at least 120 Hz")

if "HDMI" in laptop["ports"]:
    print("Laptop has HDMI port")