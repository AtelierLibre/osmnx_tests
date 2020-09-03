import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.patches import Patch

# colours https://github.com/gravitystorm/openstreetmap-carto/blob/master/style/landcover.mss
# default value already set as 'other'

tag_styles = {
    'aerialway': {
        'cable_car': {'linecolor': '#808080'},
        'chair_lift': {'linecolor': '#808080'},
        'draglift': {'linecolor': '#808080'},
        'gondola': {'linecolor': '#808080'},
        'j-bar': {'linecolor': '#808080'},
        't-bar': {'linecolor': '#808080'},
        'mixed_lift': {'linecolor': '#808080'},
        'platter': {'linecolor': '#808080'},
        'pylon': {'markercolor': '#808080'},
        'rope_tow': {'linecolor': '#808080'},
        'station': {'facecolor': 'none', 'edgecolor':'none'},
        'zip_line': {'linecolor': '#808080'},
    },
    'aeroway': {
        # generic
        'airtransport': {'facecolor': '#e9e7e2', 'edgecolor': '#83827e', 'markercolor': '#8461C4'},
        #
        'runway': {'facecolor': '#bbc', 'linecolor': '#bbc', 'linewidth': 30},
    },
    'amenity': {
        # generic base styles (not a tag)
        'amenity-brown': {'markercolor': '#734a08'},
        'gastronomy-icon': {'markercolor': '#C77400'},
        'health-color': {'markercolor': '#BF0000'},
        'man-made-icon': {'markercolor': '#666666'},
        'place_of_worship': {'facecolor': '#d0d0d0', 'edgecolor': '#929292', 'markercolor': '#000000'},
        'religious-icon': {'markercolor': '#000000'},
        'societal_amenities': {'facecolor': '#ffffe5', 'edgecolor': '#595950'},
        'transportation-icon': {'markercolor': '#0092da'},
        # tags
        'fire_station': {'facecolor': '#F3E3DD'},
        'parking': {'facecolor': '#eeeeee', 'edgecolor': '#616161'}, # added edgecolor
        'pub': {'facecolor': 'none'},
        'other': {'facecolor': 'none'},
    },
    'barrier': {
        # generic base styles (not a tag)
        'barrier-icon':{'markercolor': '#3f3f3f'},
        # tags
        'fence': {'facecolor': 'none', 'linecolor': 'dimgrey'},
        'hedge': {'facecolor': 'none', 'linecolor': '#add19e'},
        'kerb': {'linecolor': 'none'},
        'other': {'linecolor': '#444'},
    },
    'boundary': {
        'administrative': {'facecolor': 'none', 'edgecolor': '#8d618b', 'linecolor': '#8d618b'},
        'other': {'facecolor': 'none', 'edgecolor': '#8d618b', 'linecolor': '#8d618b'},
    },
    'building': {
        'apartments': {'facecolor': '#d9d0c9', 'edgecolor': '#b6a99c', 'linecolor': '#b6a99c'},
        'other': {'facecolor': '#d9d0c9', 'edgecolor': '#b6a99c', 'linecolor': '#b6a99c'},
        'yes': {'facecolor': '#d9d0c9', 'edgecolor': '#b6a99c', 'linecolor': '#b6a99c'},
    },
    'highway': {
        # generic base styles (not a tag)
        'transportation-icon':{'markercolor': '#0092da'},
        # tags
        'crossing': {'markercolor': 'none'},
        'cycleway': {'linecolor': 'blue', 'linestyle': 'dashed'},
        'footway': {'linecolor': 'salmon', 'linestyle': 'dotted'},
        'giveway': {'markercolor': 'none'},
        'living_street': {'linecolor': '#ededed'},
        'motorway': {'linecolor': '#e892a2'},
        'path': {'linecolor': 'salmon', 'linestyle': 'dotted'},
        'pedestrian': {'facecolor': '#dddde8', 'linecolor': '#dddde8'},
        'primary': {'linecolor': '#fcd6a4'},
        'residential': {'linecolor': '#ffffff', 'linewidth': 4},
        'road': {'linecolor': '#ddd'},
        'secondary': {'linecolor': '#f7fabf'},
        'streetlamp': {'markercolor': 'none'},
        'tertiary': {'linecolor': '#ffffff', 'linewidth': 8},
        'track': {'linecolor': '#996600', 'linestyle': 'dashdot'},
        'traffic_signals': {'markercolor': '#545454'},
        'trunk': {'linecolor': '#f9b29c'},
        'turning_circle': {'markercolor': '#ffffff'},
        'other': {'facecolor': 'red', 'linecolor': 'red'},
    },
    'landuse': {
        'aquaculture': {'facecolor': 'yellow'},
        'allotments': {'facecolor': '#c9e1bf'},
        'cemetery': {'facecolor': '#aacbaf'},
        'commercial': {'facecolor': '#f2dad9', 'edgecolor': '#d1b2b0', 'linecolor': '#d1b2b0'},
        'construction': {'facecolor': '#c7c7b4', 'edgecolor': 'none'},
        'farm': {'facecolor': 'red'},
        'farmland': {'facecolor': '#eef0d5', 'edgecolor': '#c7c9ae', 'linecolor': '#c7c9ae'},
        'farmyard': {'facecolor': '#f5dcba', 'edgecolor': '#d1b48c', 'linecolor': '#d1b48c'},
        'forest': {'facecolor': '#add19e', 'edgecolor': 'none'},
        'garages': {'facecolor': '#dfddce', 'edgecolor': 'none'},
        'grass': {'facecolor': '#cdebb0', 'edgecolor': 'none'},
        'greenfield': {'facecolor': 'none'},
        'industrial': {'facecolor': '#ebdbe8', 'edgecolor': '#c6b3c3', 'linecolor': '#c6b3c3'},
        'meadow': {'facecolor': '#cdebb0'},
        'military': {'facecolor': '#f55', 'edgecolor': '#f55'},
        'railway': {'facecolor': '#ebdbe8'},
        'residential': {'facecolor': '#e0dfdf', 'edgecolor': '#b9b9b9', 'linecolor': '#b9b9b9'},
        'retail': {'facecolor': '#ffd6d1', 'edgecolor': '#d99c95', 'linecolor': '#d99c95'},
        'park': {'facecolor': '#c8facc', 'edgecolor': '#8bad8d'}, # leisure?
        'other': {'facecolor': 'red', 'linecolor': 'red'},
    },
    'leisure': {
        'common': {'facecolor': 'none'},
        'nature_reserve': {'facecolor': 'none', 'edgecolor': '#add19e'}, # added
        'marina': {'facecolor': 'none', 'edgecolor': 'blue', 'linecolor': 'blue'}, # added
        'park': {'facecolor': '#c8facc', 'edgecolor':'#4e614f'},
        'pitch': {'facecolor': '#aae0cb', 'edgecolor': '#6e9d8a'},
        'stadium': {'facecolor': 'none'},
        'other': {'facecolor': 'red'},
    },
    'natural': {
        # generic
        'bare_ground': {'facecolor': '#eee5dc', 'edgecolor': 'none'},
        'beach': {'facecolor': '#fff1ba', 'edgecolor': 'none'},
        'land-color': {'facecolor': '#f2efe9', 'edgecolor': 'none'},
        'landform-color': {'markercolor': '#d08f55'},
        # tags
        'cliff': {'facecolor': 'none', 'linecolor': 'lightgrey'}, # added
        'coastline': {'facecolor': 'none', 'edgecolor': 'none', 'linecolor': 'none'},
        'forest': {'facecolor': '#add19e', 'edgecolor': 'none'},
        'glacier': {'facecolor': '#ddecec', 'edgecolor': '#9cf'},
        'heath': {'facecolor': '#d6d99f', 'edgecolor': 'none'},
        'sand': {'facecolor': '#f5e9c6', 'edgecolor': 'none'},
        'scrub': {'facecolor': '#c8d7ab', 'edgecolor': 'none'},
        'tree': {'markercolor': 'green'},
        'tree_row': {'linecolor': 'green'},
        'water': {'facecolor': '#aad3df', 'edgecolor': '#9cf', 'linecolor': '#9cf', 'markercolor': '#9cf'},
        'wetland': {'facecolor': '#add6c8', 'edgecolor': 'none'},
        'other': {'facecolor': 'red'},
    },
    'place': {
        'island': {'facecolor': '#f2efe9', 'edgecolor': '#8d618b', 'linecolor': '#8d618b'},
        'other': {'facecolor': 'none'},
    },
    'power': {
        'other': {'facecolor': 'red'},
        'pole': {'markercolor': '#928f8f'},
    },
    'railway': {
        'abandoned': {'linecolor': 'none'},
        'bridge-casing': {'linecolor': 'black'},
        'station-color': {'markercolor': '#7981b0'},
    },
    'shop': {
        'shop-icon': {'markercolor': '#ac39ac'},
        'other': {'facecolor': '#ac39ac', 'linecolor': '#ac39ac', 'markercolor': '#ac39ac'},
    },
    'waterway': {
        'other': {'facecolor': '#aad3df', 'linecolor': '#aad3df', 'markercolor': '#aad3df'},
    },
}

tag_styles['aeroway']['aerodrome'] = tag_styles['aeroway']['airtransport']
tag_styles['aeroway']['taxiway'] = tag_styles['aeroway']['runway']
# generic bases like other generic bases
tag_styles['amenity']['culture'] = tag_styles['amenity']['amenity-brown']
tag_styles['amenity']['public-service'] = tag_styles['amenity']['amenity-brown']
# tags that are styled like other tags
tag_styles['amenity']['art_centre'] = tag_styles['amenity']['societal_amenities']
tag_styles['amenity']['atm'] = tag_styles['amenity']['amenity-brown']
tag_styles['amenity']['bank'] = tag_styles['amenity']['public-service']
tag_styles['amenity']['bbq'] = tag_styles['amenity']['gastronomy-icon']
tag_styles['amenity']['bench'] = tag_styles['amenity']['man-made-icon']
tag_styles['amenity']['bicycle_parking'] = tag_styles['highway']['transportation-icon']
tag_styles['amenity']['bicycle_rental'] = tag_styles['highway']['transportation-icon']
tag_styles['amenity']['cafe'] = tag_styles['amenity']['amenity-brown']
tag_styles['amenity']['cemetery'] = tag_styles['landuse']['cemetery']
tag_styles['amenity']['community_centre'] = tag_styles['amenity']['culture']
tag_styles['amenity']['courthouse'] = tag_styles['amenity']['public-service']
tag_styles['amenity']['drinking_water'] = tag_styles['amenity']['amenity-brown']
tag_styles['amenity']['fast_food'] = tag_styles['amenity']['gastronomy-icon']
tag_styles['amenity']['fuel'] = tag_styles['highway']['transportation-icon']
tag_styles['amenity']['grave_yard'] = tag_styles['landuse']['cemetery']
tag_styles['amenity']['hospital'] = tag_styles['amenity']['societal_amenities']
tag_styles['amenity']['ice_cream'] = tag_styles['amenity']['gastronomy-icon']
tag_styles['amenity']['kindergarten'] = tag_styles['amenity']['societal_amenities']
tag_styles['amenity']['library'] = tag_styles['amenity']['culture']
tag_styles['amenity']['pharmacy'] = tag_styles['amenity']['health-color']
tag_styles['amenity']['post_box'] = tag_styles['amenity']['amenity-brown']
tag_styles['amenity']['post_office'] = tag_styles['amenity']['public-service']
tag_styles['amenity']['pub'] = tag_styles['amenity']['gastronomy-icon']
tag_styles['amenity']['public-service'] = tag_styles['amenity']['amenity-brown']
tag_styles['amenity']['recycling'] = tag_styles['amenity']['amenity-brown']
tag_styles['amenity']['restaurant'] = tag_styles['amenity']['gastronomy-icon']
tag_styles['amenity']['school'] = tag_styles['amenity']['societal_amenities']
tag_styles['amenity']['shelter'] = tag_styles['amenity']['man-made-icon']
tag_styles['amenity']['street_lamp'] = tag_styles['highway']['streetlamp']
tag_styles['amenity']['toilets'] = tag_styles['amenity']['amenity-brown']
tag_styles['amenity']['waste_basket'] = tag_styles['amenity']['man-made-icon']

tag_styles['barrier']['cattle_grid'] = tag_styles['barrier']['barrier-icon']
tag_styles['barrier']['cycle_barrier'] = tag_styles['barrier']['barrier-icon']
tag_styles['barrier']['full-height_turnstile'] = tag_styles['barrier']['barrier-icon']
tag_styles['barrier']['kissing_gate'] = tag_styles['barrier']['barrier-icon']
tag_styles['barrier']['lift_gate'] = tag_styles['barrier']['barrier-icon']
tag_styles['barrier']['motorcycle_barrier'] = tag_styles['barrier']['barrier-icon']
tag_styles['barrier']['stile'] = tag_styles['barrier']['barrier-icon']

tag_styles['highway']['bus_stop'] = tag_styles['highway']['transportation-icon']
tag_styles['highway']['primary_link'] = tag_styles['highway']['primary']
tag_styles['highway']['secondary_link'] = tag_styles['highway']['secondary']
tag_styles['highway']['service'] = tag_styles['highway']['residential']
tag_styles['highway']['steps'] = tag_styles['highway']['footway']
tag_styles['highway']['unclassified'] = tag_styles['highway']['residential']

tag_styles['landuse']['brownfield'] = tag_styles['landuse']['construction']
tag_styles['landuse']['grave_yard'] = tag_styles['landuse']['cemetery']
tag_styles['landuse']['leisure'] = tag_styles['landuse']['park']
tag_styles['landuse']['recreation_ground'] = tag_styles['landuse']['leisure']

tag_styles['leisure']['garden'] = tag_styles['landuse']['grass']
tag_styles['leisure']['playground'] = tag_styles['landuse']['leisure']
tag_styles['leisure']['recreation_ground'] = tag_styles['landuse']['leisure']
tag_styles['leisure']['track'] = tag_styles['leisure']['pitch']

tag_styles['natural']['bare_rock'] = tag_styles['natural']['bare_ground']
tag_styles['natural']['bay'] = tag_styles['natural']['water']
tag_styles['natural']['grassland'] = tag_styles['landuse']['grass']
tag_styles['natural']['peak'] = tag_styles['natural']['landform-color']
tag_styles['natural']['saddle'] = tag_styles['natural']['landform-color']
tag_styles['natural']['scree'] = tag_styles['natural']['bare_ground']
tag_styles['natural']['spring'] = tag_styles['natural']['water']
tag_styles['natural']['wood'] = tag_styles['natural']['forest']
#tag_styles['natural']['wetland'] = tag_styles['landuse']['grass']

tag_styles['place']['islet'] = tag_styles['place']['island']

tag_styles['power']['other'] = tag_styles['landuse']['industrial']
tag_styles['power']['tower'] = tag_styles['power']['pole']

tag_styles['railway']['monorail'] = tag_styles['railway']['bridge-casing']
tag_styles['railway']['preserved'] = tag_styles['railway']['bridge-casing']
tag_styles['railway']['rail'] = tag_styles['railway']['bridge-casing']
tag_styles['railway']['station'] = tag_styles['railway']['station-color']

tag_styles['shop']['butcher'] = tag_styles['shop']['shop-icon']
tag_styles['shop']['convenience'] = tag_styles['shop']['shop-icon']
tag_styles['shop']['pet'] = tag_styles['shop']['shop-icon']

# Personal added
tag_styles['landuse']['aquaculture'] = tag_styles['landuse']['leisure']
tag_styles['landuse']['conservation'] = tag_styles['natural']['forest']

tag_styles['waterway']['riverbank'] = tag_styles['natural']['water']

def _get_style(tag_styles, style_element, default_value):
    '''
    get style values from the tag_styles dictionary

    the default_value is the value to return if that tag does not
    have a key:value in the dictionary
    
    Parameters
    ----------
    tag_styles: dict
        dictionary of style elements for particular tag values
    style_element: string
        the particular style element to retrieve
        e.g. 'facecolor', 'edgecolor', 'linecolor', 'lineweight'
    default_value: string, float
        e.g. 'red', 'none', 0.1

    Returns
    -------
    styles: dict
    '''

    styles = {k:{k_:v_.get(style_element, default_value) for k_,v_ in v.items()} for k,v in tag_styles.items()}

    return styles

def carto_plot(gdf, tags=None, left=None, right=None, top=None, bottom=None, figsize=(16,16)):
    '''
    Crude approximation of the OSM carto stylesheet for visual comparison with osm.org
    
    See: https://github.com/gravitystorm/openstreetmap-carto/blob/master/style/
    
    leaving tags=None will plot all geometry but smaller geometries may be hidden by
    larger ones, passing tags in in order will help to plot in that order (e.g.
    tags={'place': True, 'landuse': True, 'building': True}) putting smaller geometries
    on top.
    
    With apologies to the OpenStreetMap Carto team
    
    Parameters
    ----------
    gdf : GeoDataFrame
        the GeoDataFrame to plot
    figsize : tuple
        image size in inches
    tags : 
        the tags to plot, None will plot all
    left, right : numbers
        coordinates to limit the plot area - have to be specified together
    top, bottom : numbers
        coordinates to limit the plot area - have to be specified together
    '''

    geometry_types = [['Polygon', 'MultiPolygon'],['LineString'],['Point']]
    #tags_to_plot = ['landuse', 'power', 'amenity', 'natural', 'building', 'highway', 'waterway']
    
    fig, ax = plt.subplots(figsize=figsize)
    ax.set_facecolor('#f2efe9')

    if left and right:
        ax.set_xlim(left=left, right=right)
    if top and bottom:
        ax.set_ylim(top=top, bottom=bottom)
        
    #ax.grid()
    
    for geometry_type in geometry_types:

        if tags:
            tags_ = tags
        else:
            tags_ =  tag_styles

        for tag in tags_:

            if tag in gdf.columns:

                geometry_mask = (gdf['geometry'].geom_type).isin(geometry_type)
                # geometry_mask = alr['geometry'].geom_type == 'Polygon' # add multipolygon
                tag_mask = gdf[tag].notna()
                geometry_and_tag_mask = geometry_mask & tag_mask

                if geometry_type == ['Polygon', 'MultiPolygon']:

                    # retrieve tag_styles and edgecolors in the tag_styles dictionary
                    facecolors = _get_style(tag_styles, 'facecolor', 'green')
                    edgecolors = _get_style(tag_styles, 'edgecolor', 'green')

                    # map them onto a series
                    facecolors_series = gdf[tag].map(facecolors.get(tag))
                    facecolors_series.fillna(facecolors.get(tag).get('other', 'red'), inplace=True)
                    
                    edgecolors_series = gdf[tag].map(edgecolors.get(tag))
                    edgecolors_series.fillna(edgecolors.get(tag).get('other', 'red'), inplace=True)

                    # use the series to apply the style
                    gdf[geometry_and_tag_mask].plot(ax=ax,
                                                    facecolor=facecolors_series[geometry_and_tag_mask],
                                                    edgecolor=edgecolors_series[geometry_and_tag_mask],
                                                )

                elif geometry_type == ['LineString']:

                    linecolors = _get_style(tag_styles, 'linecolor', 'red')
                    linestyles = _get_style(tag_styles, 'linestyle', 'solid')
                    linewidths = _get_style(tag_styles, 'linewidth', 1)
                    
                    linestyles_series = gdf[tag].map(linestyles.get(tag))
                    linestyles_series.fillna(linestyles.get(tag).get('other', 'solid'), inplace=True)
                    
                    linecolors_series = gdf[tag].map(linecolors.get(tag))
                    linecolors_series.fillna(linecolors.get(tag).get('other', 'red'), inplace=True)
                    
                    linewidths_series = gdf[tag].map(linewidths.get(tag))
                    linewidths_series.fillna(linewidths.get(tag).get('other', 1), inplace=True)

                    gdf[geometry_and_tag_mask].plot(ax=ax,
                                                    color=linecolors_series[geometry_and_tag_mask],
                                                    linestyle=linestyles_series[geometry_and_tag_mask],)
#                                                    linewidth=linewidths_series[geometry_and_tag_mask],
#                                                )
                    
                elif geometry_type == ['Point']:

                    markercolors = _get_style(tag_styles, 'markercolor', 'red')
                    
                    markercolors_series = gdf[tag].map(markercolors.get(tag))
                    markercolors_series.fillna(markercolors.get(tag).get('other', 'red'), inplace=True)

                    gdf[geometry_and_tag_mask].plot(ax=ax, color=markercolors_series[geometry_and_tag_mask])
                    
    return fig, ax

def comparison_report(osmnx_result, overpassturbo_result, query_polygon):
    comparison_df = pd.concat([osmnx_result.geom_type.value_counts(),
                               overpassturbo_result.geom_type.value_counts()], axis=1)
    comparison_df.rename(columns={0:'osmnx', 1:'overpass-turbo'}, inplace=True)

    print(len(set(osmnx_result['unique_id']).intersection(set(overpassturbo_result['@id']))),
          "ids that are in both GeoDataFrames\n"
    )
    
    url = "https://www.openstreetmap.org/"
    ids_not_in_both = set(osmnx_result['unique_id']).symmetric_difference(set(overpassturbo_result['@id']))
    print(f"{len(ids_not_in_both)} ids that are not in both GeoDataFrames")
    
    print("\nids not in overpassturbo_result:\n"
          f"{[url + _id for _id in set(osmnx_result['unique_id']).difference(set(overpassturbo_result['@id']))]}")
    print("ids not in osmnx_result:\n"
          f"{[url + _id for _id in set(overpassturbo_result['@id']).difference(set(osmnx_result['unique_id']))]} \n")

    print(comparison_df)
    
    if len(ids_not_in_both)>0:
        ax=query_polygon.plot(figsize=(8,8),
                              zorder=0)
        osmnx_result[osmnx_result['unique_id'].isin(ids_not_in_both)].plot(ax=ax,
                                                                           color='red',
                                                                           label='osmnx result',
                                                                           legend=True,
                                                                           zorder=1)
        overpassturbo_result[overpassturbo_result['@id'].isin(ids_not_in_both)].plot(ax=ax,
                                                                                     color='green',
                                                                                     label='overpass-turbo result',
                                                                                     legend=True,
                                                                                     zorder=1)
        
        # legend
        legend_elements = [Patch(facecolor='red',
                                 edgecolor='red',
                                 label='osmnx result'),
                           Patch(facecolor='green',
                                 edgecolor='green',
                                 label='overpass-turbo result')
                          ]
        
        # minx, miny, maxx, maxy
        tba = osmnx_result[osmnx_result['unique_id'].isin(ids_not_in_both)].total_bounds
        tbb = overpassturbo_result[overpassturbo_result['@id'].isin(ids_not_in_both)].total_bounds
        tb = np.array([tba, tbb])
        tb_max = np.nanmax(tb, axis=0)
        tb_min = np.nanmin(tb, axis=0)
        left = tb_min[0]
        right = tb_max[2]
        extra_width = (right-left) + 0.01
        top = tb_max[3]
        bottom = tb_min[1]
        extra_height = (top-bottom) + 0.01
        ax.set_xlim(left-extra_width, right+extra_width)
        ax.set_ylim(bottom-extra_height, top+extra_height)
        ax.legend(handles=legend_elements)