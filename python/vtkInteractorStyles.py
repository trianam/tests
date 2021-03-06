#!/bin/python

import vtk
import vtk.util.colors

points = vtk.vtkPoints()
points.InsertNextPoint(0, 0, 0)
points.InsertNextPoint(0, 1, 0)
points.InsertNextPoint(1, 0, 0)
points.InsertNextPoint(0, 0, 1)

unstructuredGrid = vtk.vtkUnstructuredGrid()
unstructuredGrid.SetPoints(points)
unstructuredGrid.InsertNextCell(vtk.VTK_TETRA, 4, [0,1,2,3])

mapper = vtk.vtkDataSetMapper()
mapper.SetInputData(unstructuredGrid)

actor = vtk.vtkActor()
actor.SetMapper(mapper)
actor.GetProperty().SetColor(vtk.util.colors.banana)

renderer = vtk.vtkRenderer()

renderWindow = vtk.vtkRenderWindow()
renderWindow.AddRenderer(renderer)

renderWindowInteractor = vtk.vtkRenderWindowInteractor()
renderWindowInteractor.SetRenderWindow(renderWindow)

#interactorStyle = vtk.vtkInteractorStyleFlight()
interactorStyle = vtk.vtkInteractorStyleUnicam()


renderer.AddActor(actor)
renderer.SetBackground(0.3,0.6,0.3)

renderWindowInteractor.Initialize()
renderWindowInteractor.SetInteractorStyle(interactorStyle)

axes = vtk.vtkAxesActor()
widget = vtk.vtkOrientationMarkerWidget()
widget.SetOutlineColor(0.9300, 0.5700, 0.1300)
widget.SetOrientationMarker(axes)
widget.SetInteractor(renderWindowInteractor)
widget.SetViewport(0.0, 0.0, 0.1, 0.1)
widget.SetEnabled(True)
widget.InteractiveOn()


renderer.ResetCamera()
#interactorStyle.SetWorldUpVector((0.0,1.0,0.0))
#interactorStyle.SetWorldUpVector(renderer.GetActiveCamera().GetViewUp())
print(renderer.GetActiveCamera().GetViewUp())
print(renderer.GetActiveCamera().GetViewShear())
print(renderer.GetActiveCamera().GetPosition())
print(renderer.GetActiveCamera().GetFocalPoint())
camPos = renderer.GetActiveCamera().GetPosition()
renderer.GetActiveCamera().SetPosition((camPos[2],camPos[1],camPos[0]))
renderer.GetActiveCamera().SetViewUp((0.0,0.0,1.0))
#renderer.GetActiveCamera().SetViewShear((1.0,0.0,0.0))
#renderer.GetActiveCamera().Zoom(1.5)

renderWindow.Render()
renderWindowInteractor.Start()

