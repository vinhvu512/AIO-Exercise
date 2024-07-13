import numpy as np


# Basic operations
def compute_vector_length(vector):
    len_of_vector = np.sqrt(np.sum(vector ** 2))
    return len_of_vector


def compute_dot_product(vector1, vector2):
    result = np.dot(vector1, vector2)
    return result


def matrix_multi_vector(matrix, vector):
    result = np.dot(matrix, vector)
    return result


def matrix_multi_matrix(matrix1, matrix2):
    result = np.dot(matrix1, matrix2)
    return result


def inverse_matrix(matrix):
    result = np.linalg.inv(matrix)
    return result


# Eigenvalues and eigenvectors

def compute_eigenvalues_eigenvectors(matrix):
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    return eigenvalues, eigenvectors


# Cosine similarity

def compute_cosine(v1, v2):
    result = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
    return result


# Background subtraction
import cv2
import matplotlib.pyplot as plt

bg1_image = cv2.imread('GreenBackground.png', 1)
bg1_image = cv2.resize(bg1_image, (678, 381))

ob_image = cv2.imread('Object.png', 1)
ob_image = cv2.resize(ob_image, (678, 381))

bg2_image = cv2.imread('NewBackground.jpg', 1)
bg2_image = cv2.resize(bg2_image, (678, 381))


def compute_difference(bg_img, input_img):
    difference_single_channel = cv2.absdiff(bg_img, input_img)
    return difference_single_channel


def compute_binary_mask(difference_single_channel):
    _, threshold = cv2.threshold(difference_single_channel, 50, 255, cv2.THRESH_BINARY)
    return threshold


def replace_background(bg1_image, bg2_image, ob_image):
    difference_single_channel = compute_difference(bg1_image, ob_image)

    binary_mask = compute_binary_mask(difference_single_channel)

    output = np.where(binary_mask == 255, ob_image, bg2_image)
    plt.imshow(cv2.cvtColor(output, cv2.COLOR_BGR2RGB))

    return output

replace_background(bg1_image, bg2_image, ob_image)


vector = np.array([-2, 4, 9, 21])
result = compute_vector_length(vector)
print(round(result, 2))

v1 = np.array([0, 1, -1, 2])
v2 = np.array([2, 5, 1, 0])
result = compute_dot_product(v1, v2)
print(round(result, 2))

x = np.array([[1, 2],
              [3, 4]])
k = np.array([1, 2])
print('result \n', x.dot(k))

x = np.array([[-1, 2],
              [3, -4]])
k = np.array([1, 2])
print('result \n', x @ k)

m = np.array([[-1, 1, 1], [0, -4, 9]])
v = np.array([0, 2, 1])
result = matrix_multi_vector(m, v)
print(result)

m1 = np.array([[0, 1, 2], [2, -3, 1]])
m2 = np.array([[1, -3], [6, 1], [0, -1]])
result = matrix_multi_matrix(m1, m2)
print(result)

m1 = np.eye(3)
m2 = np.array([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
result = m1 @ m2
print(result)

m1 = np.eye(2)
m1 = np.reshape(m1, (-1, 4))[0]
m2 = np.array([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]])
result = m1 @ m2
print(result)

m1 = np.array([[1, 2], [3, 4]])
m1 = np.reshape(m1, (-1, 4), "F")[0]
m2 = np.array([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]])
result = m1 @ m2
print(result)

m1 = np.array([[-2, 6], [8, -4]])
result = inverse_matrix(m1)
print(result)

matrix = np.array([[0.9, 0.2], [0.1, 0.8]])
eigenvalues, eigenvectors = compute_eigenvalues_eigenvectors(matrix)
print(eigenvectors)

x = np.array([1, 2, 3, 4])
y = np.array([1, 0, 3, 0])
result = compute_cosine(x, y)
print(round(result, 3))
