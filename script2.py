student = {
            "name": "Josiah", 
            "id": "00-02-11", 
            "degree": "MSc Computing",
            "courses": [
                {
                    "title": "Introduction to Machine Learning", 
                    "code": "60012"
                },
                { 
                    "title": "Computer Vision",
                    "code": "60006"
                }
            ]
          }
print(student["courses"])
print(student["courses"][0])
print(student["courses"][0]["title"])
print(student["courses"][0]["code"])
