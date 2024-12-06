import numpy as np
from sklearn.preprocessing import LabelEncoder

# Prior probability 
def prior_prob(y_train, label):
    total_examples = y_train.shape[0]
    class_examples = np.sum(y_train == label)
    return class_examples / float(total_examples)

# Conditional probability 
def conditional_prob(x_train, y_train, feature_col, feature_val, label):
    x_filtered = x_train[y_train == label]
    numerator = np.sum(x_filtered[:, feature_col] == feature_val)
    denominator = np.sum(y_train == label)
    return numerator / float(denominator)


def predict(x_train, y_train, x_test):
    classes = np.unique(y_train)
    n_features = x_train.shape[1]
    post_probs = []
    
    # posterior probabilities for each class
    for label in classes:
        likelihood = 1.0
        for f in range(n_features):
            cond = conditional_prob(x_train, y_train, f, x_test[f], label)
            likelihood *= cond

        prior = prior_prob(y_train, label)
        post = likelihood * prior
        post_probs.append(post)
    
    # Choose the class with the highest posterior probability
    pred = np.argmax(post_probs)
    return classes[pred]

# Original data
data = [
    ['Rainy', 'Hot', 'High', 'f', 'no'],
    ['Rainy', 'Hot', 'High', 't', 'no'],
    ['Overcast', 'Hot', 'High', 'f', 'yes'],
    ['Sunny', 'Mild', 'High', 'f', 'yes'],
    ['Sunny', 'Cool', 'Normal', 'f', 'yes'],
    ['Sunny', 'Cool', 'Normal', 't', 'no'],
    ['Overcast', 'Cool', 'Normal', 't', 'yes'],
    ['Rainy', 'Mild', 'High', 'f', 'no'],
    ['Rainy', 'Cool', 'Normal', 'f', 'yes'],
    ['Sunny', 'Mild', 'Normal', 'f', 'yes'],
    ['Rainy', 'Mild', 'Normal', 't', 'yes'],
    ['Overcast', 'Mild', 'High', 't', 'yes'],
    ['Overcast', 'Hot', 'Normal', 'f', 'yes'],
    ['Sunny', 'Mild', 'High', 't', 'no']
]

#numpy array
data = np.array(data)

x_train = data[:, :-1]  # Features (Outlook, Temp, Humidity, Windy)
y_train = data[:, -1]   # Labels (Play)

#label encdoing
le_outlook = LabelEncoder()
le_temp = LabelEncoder()
le_humidity = LabelEncoder()
le_windy = LabelEncoder()
le_play = LabelEncoder()


x_train[:, 0] = le_outlook.fit_transform(x_train[:, 0])  
x_train[:, 1] = le_temp.fit_transform(x_train[:, 1])      
x_train[:, 2] = le_humidity.fit_transform(x_train[:, 2])  
x_train[:, 3] = le_windy.fit_transform(x_train[:, 3])     
y_train = le_play.fit_transform(y_train)                  

x_train = x_train.astype(int)
y_train = y_train.astype(int)

#test
x_test = np.array(['Sunny', 'Mild', 'High', 'f'])

x_test[0] = le_outlook.transform([x_test[0]])[0]   
x_test[1] = le_temp.transform([x_test[1]])[0]      
x_test[2] = le_humidity.transform([x_test[2]])[0]  
x_test[3] = le_windy.transform([x_test[3]])[0]    
x_test = x_test.astype(int)

prediction = predict(x_train, y_train, x_test)


predicted_label = le_play.inverse_transform([prediction])[0]

print(f"Predicted class for the test input {x_test} (encoded) is: {predicted_label}")