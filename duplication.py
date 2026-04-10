student_data={
    "id1":{"name":"jhon","Class":"10A","subject_integration":"Science"},
    "id2":{"name":"Alice","Class":"10B","subject_integration":"Math"},
    "id3":{"name":"jhon","Class":"10A","subject_integration":"Science"}, 
    "id4":{"name":"Bob","Class":"10C","subject_integration":"History"},
}
result={}
seen_keys=[]
for student_id,details in student_data.items():
    unique_key=(details["name"],details["Class"],details["subject_integration"])
    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        result[student_id] = details
print("Unique student data:\n")
for student_id,details in result.items():
    print(f"{student_id}: {details}")

