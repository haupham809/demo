def checklist():
    listint=[1,2,3,4,334,34,234,234,2]
    if listint[0]==listint[len(listint)-1]:
        return True
    return False
print(checklist())