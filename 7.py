sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

history = sampleDict["class"]["student"]["marks"]['history']
sampleDict["class"]["student"]["name"] = "Jessa"
print(history)
print(sampleDict)