data = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Shrub",
    "Iris - Flower",
    "Japanese Camellia - Shrub",
    "Lavender - Shrub",
    "Lilac - Shrub",
    "Magnolia - Shrub",
    "Peony - Shrub",
    "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower",
    "Snapdragon - Flower",
    "Sunflower - Flower",
    "Tiger Lily - Flower",
    "Witch Hazel - Shrub",
]

flowers = []
shrubs = []

# write your code here
for check in data:
    #index = int(check)
    print(check)
    #index = int(data[check])
    if " - Shrub" in check:
        check = check.replace(" - Shrub", "")
        print(check)
        shrubs.append(check)
        
        #shrubs[index].strip("- Shrub")
    elif "- Flower" in check:    
        check = check.replace(" - Flower", "")
        flowers.append(check)
print(flowers)
print(shrubs)        