import cv2
import numpy as np
from sklearn.cluster import KMeans
import os
import sqlite3;

def preprocess_image(image_path):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = image.reshape(image.shape[0] * image.shape[1], 3)
    return image

def get_dominant_color(image, n_colors):
    kmeans = KMeans(n_clusters=n_colors)
    kmeans.fit(image)
    colors = kmeans.cluster_centers_
    labels = kmeans.labels_
    return colors, labels

def find_dominant_color(image_path, n_colors=1):
    image = preprocess_image(image_path)
    colors, labels = get_dominant_color(image, n_colors)
    dominant_color = colors[0]
    return dominant_color.astype(int)

connection = sqlite3.connect('database.db')
cursor = connection.cursor()
cursor.execute('DROP TABLE IF EXISTS imageAnalyzeResults')
cursor.execute('CREATE TABLE imageAnalyzeResults (id INTEGER PRIMARY KEY, image TEXT, RGBColor TEXT)')

image_folder_path = "./images"  

# List all files in the directory
files = os.listdir(image_folder_path)

# Filter list to only include jpg files
images = [file for file in files if file.endswith('.jpg')]

for image_file in images:
    image_path = os.path.join(image_folder_path, image_file)
    dominant_color = find_dominant_color(image_path)
    print(f"Dominant color for {image_file}: {dominant_color}")
    cursor.execute("INSERT INTO imageAnalyzeResults (image, RGBColor) VALUES (?, ?)", (image_file, str(dominant_color)))

# Commit the transaction
connection.commit()

# Close the connection
connection.close()
