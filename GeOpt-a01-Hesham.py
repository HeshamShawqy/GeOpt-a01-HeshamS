
import Rhino.Geometry as rg
import rhinoscriptsyntax as rs
import math
#Manipulate mesh points based on the intersection between the sun vector and the mesh
#INPUT
# base mesh = mesh
# distortion height = depth
# attractor point = attractor
# attractor radius = radius
# OUTPUT
# manipulated mesh = newmesh
# closest points = closest

#create the vector attractor function
def Attractor(d):
    #assigning a default value for the min dist
    min_dist = -1
    #creating a loop to measure the closest distance to the vector
    for i in attractors: 
        dist = rs.Distance(d, i)
        if( min_dist < 0 or dist < min_dist ):
            min_dist = dist
            closest = i
            #
    if(min_dist < radius):
        vec = d - closest
        vec *= (radius - min_dist)/(radius)
        return vec
        #move points with value = 0 if they are out of range
    return rg.Vector3d(0,0,0)

#create points movement function
def moveVertecies(mesh):
    meshb = rg.Mesh()
    mv_a = mesh.Vertices.ToPoint3dArray()
    for i in range(len(mv_a)):
        distance=Attractor(mv_a[i])
        mv_b = mv_a[i] + Attractor(mv_a[i]) * depth 
        meshb.Vertices.Add(mv_b )
    
    meshb.Faces.AddFaces(mesh.Faces)
    meshb.Normals.ComputeNormals()
    meshb.Vertices.CombineIdentical(True, True)
    meshb.Vertices.CullUnused()
    meshb.Weld(3.14159265358979)
    meshb.UnifyNormals()
    meshb.Compact()
    #return meshlist=[meshb,mv_b]
    return meshb

#manipulated mesh as an output
newmesh=moveVertecies(mesh)

#query the closest points to the attractor curve
def moveVertecies(mesh):
    f=[]
    meshb = rg.Mesh()
    mv_a = mesh.Vertices.ToPoint3dArray()
    for i in range(len(mv_a)):
        mv_b =Attractor(mv_a[i]) * depth
        f.append(mv_b)
    return f
    
closest=moveVertecies(mesh)
