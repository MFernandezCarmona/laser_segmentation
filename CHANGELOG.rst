^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package laser_segmentation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

2.0.1 (16-10-2022)
------------------
* Added default launch file.

2.0.0 (15-10-2022)
------------------
* First ROS2 (Humble) version.
* Contributors: Manuel Fernandez-Carmona

1.2.1 (20-10-2022)
------------------
* Rename segment_topic to segments_topic.

1.2.0 (03-05-2022)
------------------
* Added noise reduction parameter.
* Push a delete marker before the others. I hope this fix the RViz problem.

1.1.3 (13-01-2022)
------------------
* Refactoring jump distance and jump distance merge.
* Added jump between points with NaN values.
* Fix merge of first and last segments.

1.1.2 (12-01-2022)
------------------
* Update simple_laser_geometry to 3.2.0.
* Checking of NaN points.
* Change lifetime of markers.

1.1.1 (23-12-2021)
------------------
* Check publisher before doing any calculations.

1.1.0 (15-12-2021)
------------------
* Change segment marker to markerArray.
* Publish id of the segment as markerArray.
* Change the color palette.
* Fix jump distance merge.

1.0.1 (15-12-2021)
------------------
* Update simple_laser_geometry to 3.0.0.

1.0.0 (14-12-2021)
------------------
* Changes to new simple laser geometry library.
* Add max width filter.
* Remove readDataPoints.
* Added option to select threshold method.
* Update dynamic jump distance methods.
* Improve jump distance merge.

0.0.0 (-)
------------------
* Initial release.
* Create README.md.
* Added laserSegmentation class (.h and .cpp files).
* Added segmentationJumpDistance class (.h and .cpp files).
* Added segmentationJumpDistanceMerge class (.h and .cpp files).
* Added SegmentationParameters.cfg configuration files.
* Added launch files.
* Contributors: Alberto Tudela
