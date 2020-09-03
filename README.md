# Notebooks for testing the [OSMnx](https://github.com/gboeing/osmnx) `geometries` module

This is a set of notebooks used during the development of the new `geometries` module for OSMnx.

## Initial study

- [00_InitialStudies_Alresford_MiltonKeynes_Amsterdam.ipynb](https://github.com/AtelierLibre/osmnx_tests/blob/master/notebooks/00_InitialStudies_Alresford_MiltonKeynes_Amsterdam.ipynb)

Demonstrates the ability of `geometries` to convert OSM nodes, ways and multipolygon relations to Shapely points, linestrings, polygons and multipolygons.

## Comparisons between `pois`, `footprints` and `geometries` modules

- [10_comparison_pois_footprints_geometries.ipynb](https://github.com/AtelierLibre/osmnx_tests/blob/master/notebooks/10_comparison_pois_footprints_geometries.ipynb)
- [11_comparison_pois_footprints_geometries.ipynb](https://github.com/AtelierLibre/osmnx_tests/blob/master/notebooks/11_comparison_pois_footprints_geometries.ipynb)
- [12_comparison_pois_geometries_overpass-turbo.ipynb](https://github.com/AtelierLibre/osmnx_tests/blob/master/notebooks/12_comparison_pois_geometries_overpass-turbo.ipynb)

Compare the results of the `pois`, `footprints` and `geometries` modules.

***Notes***
- These notebooks will not work in the latest version of the `geometries` branch as `pois` and `footprints` have been deprecated and are both now interfaces to `geometries`.

## Visual comparisons with [openstreetmap.org](https://www.openstreetmap.org/)

- [20_Visual_Comparison_OSM_Carto.ipynb](https://github.com/AtelierLibre/osmnx_tests/blob/master/notebooks/20_Visual_Comparison_OSM_Carto.ipynb)

Uses a helper function provided alongside the notebooks to apply colours matching the [OpenStreetMap Carto](https://github.com/gravitystorm/openstreetmap-carto) stylesheets to the results from `geometries` to allow for a visual comparison of results with [openstreetmap.org](https://www.openstreetmap.org/).

## Comparisons with [overpass-turbo.eu](https://overpass-turbo.eu/)

- [30_overpass-turbo_comparisons.ipynb](https://github.com/AtelierLibre/osmnx_tests/blob/master/notebooks/30_overpass-turbo_comparisons.ipynb)
- [31_overpass-turbo_comparisons.ipynb](https://github.com/AtelierLibre/osmnx_tests/blob/master/notebooks/31_overpass-turbo_comparisons.ipynb)

Run similar queries through the new `geometries` module and [overpass-turbo.eu](https://overpass-turbo.eu/) using [overpass-turbo.eu](https://overpass-turbo.eu/) as an external benchmark to give confidence that the numbers returned are accurated. There are occasional minor differences but generally the results are very comparable.

***Notes***
- The `geometries` module strictly processes multipolygon relations. An equivalent query using the overpass-turbo.eu wizard would look like `(type:node or type:way or (type:relation and type=multipolygon)) and amenity=school in Berlin`.

## Conversion of XMLs

- [40_XMLs_from_openstreetmap.ipynb](https://github.com/AtelierLibre/osmnx_tests/blob/master/notebooks/40_XMLs_from_openstreetmap.ipynb)
- [41_XMLs_from_geofabrik.ipynb](https://github.com/AtelierLibre/osmnx_tests/blob/master/notebooks/41_XMLs_from_geofabrik.ipynb)
- [42_XMLs_from_bbbike.ipynb](https://github.com/AtelierLibre/osmnx_tests/blob/master/notebooks/42_XMLs_from_bbbike.ipynb)
- [43_XMLs_from_bbbike.ipynb](https://github.com/AtelierLibre/osmnx_tests/blob/master/notebooks/43_XMLs_from_bbbike.ipynb)

Test the ability to extract geometries from OpenStreetMap XMLs

***Notes***
- XMLs often seem to include 'clipped' partial geometries (e.g. only including one node for a way that starts inside but finishes outside the bounding shape). This makes them a good test for error handling but can lead to unexpected results as incomplete geometries are discarded.
- The entirety of an XML file has to be processed before any polygon or tag filter is applied. This means quite a large amount of data may need to be processed to extract quite a small amount of data from a relatively small area. This can limit the parsing of XMLs to quite small areas but good results are possible if they contain complete geometries.
