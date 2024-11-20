import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import convolve
from skimage import io, color
import skfuzzy as fuzz

# Step 1: Import RGB Image and Convert to Grayscale
Irgb = io.imread('peppers.png')  # Load the RGB image
Igray = color.rgb2gray(Irgb)  # Convert RGB image to grayscale

# Display the grayscale image
plt.figure()
plt.imshow(Igray, cmap='gray')
plt.title('Input Image in Grayscale')
plt.axis('off')
plt.show()

# Step 2: Convert Image to Double-Precision Data
I = Igray.astype(np.float64)

# Step 3: Obtain Image Gradient
# Define simple gradient filters
Gx = np.array([[-1, 1]])
Gy = Gx.T

# Compute the gradients along the x and y axes
Ix = convolve(I, Gx, mode='nearest')
Iy = convolve(I, Gy, mode='nearest')

# Display the gradients
plt.figure()
plt.imshow(Ix, cmap='gray')
plt.title('Ix')
plt.axis('off')
plt.show()

plt.figure()
plt.imshow(Iy, cmap='gray')
plt.title('Iy')
plt.axis('off')
plt.show()

# Step 4: Define Fuzzy Inference System (FIS) for Edge Detection
# Fuzzy membership functions for the gradients
sx = 0.1  # standard deviation for Ix
sy = 0.1  # standard deviation for Iy

# Create fuzzy sets for the input gradient values (Ix, Iy)
x = np.linspace(-1, 1, 1000)
Ix_zero = fuzz.gaussmf(x, 0, sx)  # Zero membership for Ix
Iy_zero = fuzz.gaussmf(x, 0, sy)  # Zero membership for Iy

# Display the membership functions for Ix and Iy
plt.figure(figsize=(8, 4))

plt.subplot(1, 2, 1)
plt.plot(x, Ix_zero, label='Ix=zero', color='blue')
plt.title('Membership Function for Ix')
plt.xlabel('Ix')
plt.ylabel('Membership Degree')

plt.subplot(1, 2, 2)
plt.plot(x, Iy_zero, label='Iy=zero', color='blue')
plt.title('Membership Function for Iy')
plt.xlabel('Iy')
plt.ylabel('Membership Degree')

plt.tight_layout()
plt.show()

# Step 5: Define Membership Functions for Output (Iout)
# Triangular membership functions for output (Iout)
white = fuzz.trimf(x, [0.1, 0.5, 1])  # White
black = fuzz.trimf(x, [0, 0, 0.7])    # Black

# Plot the membership functions for Iout
plt.figure(figsize=(8, 4))

plt.subplot(1, 2, 1)
plt.plot(x, white, label='White', color='white')
plt.title('Membership Function for White')
plt.xlabel('Iout')
plt.ylabel('Membership Degree')

plt.subplot(1, 2, 2)
plt.plot(x, black, label='Black', color='black')
plt.title('Membership Function for Black')
plt.xlabel('Iout')
plt.ylabel('Membership Degree')

plt.tight_layout()
plt.show()

# Step 6: Define FIS Rules
# Rule 1: If Ix and Iy are zero, then Iout is white (uniform region)
# Rule 2: If either Ix or Iy is non-zero, then Iout is black (edge)
def fuzzy_inference(Ix, Iy):
    # Membership degrees for Ix and Iy
    Ix_deg = fuzz.interp_membership(x, Ix_zero, Ix)
    Iy_deg = fuzz.interp_membership(x, Iy_zero, Iy)
    
    # Apply the fuzzy rules
    if Ix_deg > 0 and Iy_deg > 0:
        return fuzz.interp_membership(x, white, 1)  # Iout = White
    else:
        return fuzz.interp_membership(x, black, 1)  # Iout = Black

# Step 7: Evaluate FIS and Generate Edge Image
Ieval = np.zeros_like(I)

for ii in range(I.shape[0]):
    for jj in range(I.shape[1]):
        # Apply fuzzy inference for each pixel (Ix[ii,jj], Iy[ii,jj])
        Ieval[ii, jj] = fuzzy_inference(Ix[ii, jj], Iy[ii, jj])

# Step 8: Plot Results
# Plot the original grayscale image
plt.figure()
plt.imshow(I, cmap='gray')
plt.title('Original Grayscale Image')
plt.axis('off')
plt.show()

# Plot the edge-detected image
plt.figure()
plt.imshow(Ieval, cmap='gray')
plt.title('Edge Detection Using Fuzzy Logic')
plt.axis('off')
plt.show()
