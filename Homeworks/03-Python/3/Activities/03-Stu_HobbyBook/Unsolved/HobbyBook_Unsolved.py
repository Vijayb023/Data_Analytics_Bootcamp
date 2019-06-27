# @TODO: Your code here
About_me = {
    "name":"Vijay Bagavatula",
    "age": 19,
    "Hobbies":[
        "Basketball",
        "Weight training",
        "Tennis",
        "Reading"
    ],
    "wake_up":{
        "weekdays":5,
        "weekends":10
    }
    }
print(f'Hello my name is {About_me["name"]}. I have {len(About_me["Hobbies"])} hobbies. My hobbies include {About_me["Hobbies"]}. I wake up at {About_me["wake_up"]["weekdays"]}')