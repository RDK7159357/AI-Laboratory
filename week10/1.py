def identify_animal(features):
    f = set(f.lower().strip() for f in features)
    rules = [
        ({'tawny color', 'dark spots'}, 'cheetah'),
        ({'tawny color', 'black stripes'}, 'tiger'),
        ({'long neck', 'long legs'}, 'giraffe'),
        ({'black stripes'}, 'zebra'),
        ({'does not fly', 'long neck'}, 'ostrich'),
        ({'does not fly', 'swims', 'black and white in color'}, 'penguin'),
        ({'appears in story ancient mariner', 'flys well'}, 'albatross')
    ]
    for required_features, animal in rules:
        if required_features.issubset(f):
            return animal
    return "unable to determine"

# Example Usage (User Input Simulation)
user_features_1 = ["tawny color", "dark spots", "fast runner"] 
user_features_2 = ["long neck", "long legs"]
user_features_3 = ["swims", "black and white in color"]
user_features_4 = ["has horns", "is small"] 

# Display Results
print(f"Features: {user_features_1} -> Animal: {identify_animal(user_features_1)}")
print(f"Features: {user_features_2} -> Animal: {identify_animal(user_features_2)}")
print(f"Features: {user_features_3} -> Animal: {identify_animal(user_features_3)}")
print(f"Features: {user_features_4} -> Animal: {identify_animal(user_features_4)}")