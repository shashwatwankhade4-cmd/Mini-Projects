info = {
    "brand": "Samsung",
    "model": "A52",
    "price": 25000
}

# Update dictionary
info.update({
    "color": "Black",
    "price": 24000
})

# Remove model
removed = info.pop("model")

print("Removed Value:", removed)
print("Final Dictionary:")
print(info)