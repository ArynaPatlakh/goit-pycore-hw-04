from pathlib import Path

def get_cats_info(path):

    path = Path(__file__).parent / path
    
    cats_details = []

    try:
       
        with open(path, encoding="utf-8") as f:
            for line in f:
                id, name, age = line.strip().split(",")
                
                cats_details.append({
                    "id": id,
                    "name": name, 
                    "age": age})
        
        return cats_details
    
    except(OSError, ValueError):
        return cats_details


cats_info = get_cats_info("cats.txt")
print(cats_info)
