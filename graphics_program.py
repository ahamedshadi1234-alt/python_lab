from graphics.rectangle import area as rect_area, perimeter as rect_perimeter
from graphics.circle import area as circ_area, perimeter as circ_perimeter

from graphics.graphics3D.cuboid import surface_area as cuboid_surface_area, volume as cuboid_volume
from graphics.graphics3D.sphere import surface_area as sphere_surface_area, volume as sphere_volume

length = 5
width = 3
radius = 4
height = 6

print("Rectangle Area:", rect_area(length, width))
print("Rectangle Perimeter:", rect_perimeter(length, width))
print("Circle Area:", circ_area(radius))
print("Circle Perimeter:", circ_perimeter(radius))

print("Cuboid Surface Area:", cuboid_surface_area(length, width, height))
print("Cuboid Volume:", cuboid_volume(length, width, height))
print("Sphere Surface Area:", sphere_surface_area(radius))
print("Sphere Volume:", sphere_volume(radius))
