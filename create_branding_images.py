#!/usr/bin/env python3
"""
Script to create branding images for the presentation
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from pathlib import Path

# Create output directory
output_dir = Path('assets/screenshots/branding')
output_dir.mkdir(parents=True, exist_ok=True)

# Spotify colors
SPOTIFY_GREEN = '#1DB954'
SPOTIFY_BLACK = '#191414'
SPOTIFY_WHITE = '#FFFFFF'

# 1. Create a simple Spotify-themed banner
print("1. Creating title banner...")
fig, ax = plt.subplots(figsize=(16, 4))
ax.set_xlim(0, 16)
ax.set_ylim(0, 4)
ax.axis('off')

# Background gradient
gradient = np.linspace(0, 1, 256).reshape(1, -1)
gradient = np.vstack((gradient, gradient))
ax.imshow(gradient, aspect='auto', extent=[0, 16, 0, 4], 
          cmap='Greys', alpha=0.3)

# Add title text
ax.text(8, 2.2, '🎵 Análise Spotify', fontsize=60, fontweight='bold',
        ha='center', va='center', color=SPOTIFY_GREEN,
        family='sans-serif')

ax.text(8, 1.2, 'Machine Learning para Predição de Popularidade', 
        fontsize=24, ha='center', va='center', color=SPOTIFY_WHITE,
        family='sans-serif', style='italic')

# Add decorative elements
circle1 = patches.Circle((2, 2), 0.8, color=SPOTIFY_GREEN, alpha=0.3)
circle2 = patches.Circle((14, 2), 0.8, color=SPOTIFY_GREEN, alpha=0.3)
ax.add_patch(circle1)
ax.add_patch(circle2)

# Save with dark background
fig.patch.set_facecolor(SPOTIFY_BLACK)
plt.tight_layout(pad=0)
plt.savefig(output_dir / 'title_banner.png', dpi=300, 
            bbox_inches='tight', facecolor=SPOTIFY_BLACK)
plt.close()
print(f"   Saved: {output_dir / 'title_banner.png'}")

# 2. Create a data science themed icon
print("2. Creating data science icon...")
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.axis('off')
fig.patch.set_facecolor('white')

# Draw brain/network representation
# Central circle
circle_main = patches.Circle((0, 0), 0.5, color=SPOTIFY_GREEN, alpha=0.8)
ax.add_patch(circle_main)

# Surrounding nodes
angles = np.linspace(0, 2*np.pi, 8, endpoint=False)
for angle in angles:
    x = 1.0 * np.cos(angle)
    y = 1.0 * np.sin(angle)
    circle = patches.Circle((x, y), 0.2, color=SPOTIFY_GREEN, alpha=0.5)
    ax.add_patch(circle)
    # Connection lines
    ax.plot([0, x], [0, y], color=SPOTIFY_GREEN, linewidth=2, alpha=0.3)

# Add text
ax.text(0, 0, 'ML', fontsize=40, fontweight='bold',
        ha='center', va='center', color='white')

plt.tight_layout(pad=0)
plt.savefig(output_dir / 'ml_icon.png', dpi=300, bbox_inches='tight',
            facecolor='white', transparent=True)
plt.close()
print(f"   Saved: {output_dir / 'ml_icon.png'}")

# 3. Create a music note graphic
print("3. Creating music note graphic...")
fig, ax = plt.subplots(figsize=(6, 8))
ax.set_xlim(0, 6)
ax.set_ylim(0, 8)
ax.axis('off')
fig.patch.set_facecolor('white')

# Draw a stylized music note
# Note head
circle = patches.Circle((2, 2), 0.8, color=SPOTIFY_GREEN)
ax.add_patch(circle)

# Note stem
ax.plot([2.8, 2.8], [2, 6.5], color=SPOTIFY_GREEN, linewidth=15)

# Note flag (curved)
x_flag = np.linspace(2.8, 4.5, 50)
y_flag = 6.5 - 1.5 * np.sin((x_flag - 2.8) * np.pi / 1.7)
ax.plot(x_flag, y_flag, color=SPOTIFY_GREEN, linewidth=12)

plt.tight_layout(pad=0)
plt.savefig(output_dir / 'music_note.png', dpi=300, bbox_inches='tight',
            facecolor='white', transparent=True)
plt.close()
print(f"   Saved: {output_dir / 'music_note.png'}")

# 4. Create insights/lightbulb graphic
print("4. Creating insights graphic...")
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.axis('off')
fig.patch.set_facecolor('white')

# Lightbulb representation
# Bulb
circle = patches.Circle((0, 0.3), 0.7, color='#FFD700', alpha=0.8)
ax.add_patch(circle)

# Base
rect = patches.Rectangle((-0.3, -0.6), 0.6, 0.4, color='#888888')
ax.add_patch(rect)

# Rays
for angle in [0, 45, 90, 135, 180, 225, 270, 315]:
    rad = np.radians(angle)
    x1 = 0.9 * np.cos(rad)
    y1 = 0.3 + 0.9 * np.sin(rad)
    x2 = 1.3 * np.cos(rad)
    y2 = 0.3 + 1.3 * np.sin(rad)
    ax.plot([x1, x2], [y1, y2], color='#FFD700', linewidth=5)

# Add sparkles
ax.text(0, 0.3, '💡', fontsize=80, ha='center', va='center')

plt.tight_layout(pad=0)
plt.savefig(output_dir / 'insights_icon.png', dpi=300, bbox_inches='tight',
            facecolor='white', transparent=True)
plt.close()
print(f"   Saved: {output_dir / 'insights_icon.png'}")

# 5. Create methodology diagram
print("5. Creating CRISP-DM diagram...")
fig, ax = plt.subplots(figsize=(10, 10))
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.axis('off')
fig.patch.set_facecolor('white')

# CRISP-DM phases in circle
phases = ['Business\nUnderstanding', 'Data\nUnderstanding', 'Data\nPreparation',
          'Modeling', 'Evaluation', 'Deployment']
n_phases = len(phases)
angles = np.linspace(0, 2*np.pi, n_phases, endpoint=False) + np.pi/2

colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7', '#DDA15E']

for i, (angle, phase, color) in enumerate(zip(angles, phases, colors)):
    x = 1.3 * np.cos(angle)
    y = 1.3 * np.sin(angle)
    
    # Phase circle
    circle = patches.Circle((x, y), 0.4, color=color, alpha=0.7, ec='black', linewidth=2)
    ax.add_patch(circle)
    
    # Phase text
    ax.text(x, y, phase, fontsize=9, fontweight='bold',
            ha='center', va='center', color='black')
    
    # Arrows to next phase
    next_angle = angles[(i + 1) % n_phases]
    x_next = 1.3 * np.cos(next_angle)
    y_next = 1.3 * np.sin(next_angle)
    
    # Arrow from current to next
    dx = x_next - x
    dy = y_next - y
    ax.annotate('', xy=(x_next - 0.4 * dx/np.sqrt(dx**2 + dy**2), 
                        y_next - 0.4 * dy/np.sqrt(dx**2 + dy**2)),
                xytext=(x + 0.4 * dx/np.sqrt(dx**2 + dy**2),
                       y + 0.4 * dy/np.sqrt(dx**2 + dy**2)),
                arrowprops=dict(arrowstyle='->', lw=2, color='gray'))

# Center circle with text
circle_center = patches.Circle((0, 0), 0.5, color=SPOTIFY_GREEN, alpha=0.8)
ax.add_patch(circle_center)
ax.text(0, 0, 'CRISP-DM', fontsize=16, fontweight='bold',
        ha='center', va='center', color='white')

plt.tight_layout(pad=0)
plt.savefig(output_dir / 'crisp_dm_diagram.png', dpi=300, bbox_inches='tight')
plt.close()
print(f"   Saved: {output_dir / 'crisp_dm_diagram.png'}")

print("\n" + "="*80)
print("ALL BRANDING IMAGES CREATED SUCCESSFULLY!")
print("="*80)
print(f"\nOutput directory: {output_dir}")
print(f"Total files created: 5")
