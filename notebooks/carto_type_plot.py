import matplotlib.pyplot as plt

# colours https://github.com/gravitystorm/openstreetmap-carto/blob/master/style/landcover.mss
# default value already set as 'other'

tag_styles = {
    'aeroway': {
        'runway':{'facecolor': '#bbc', 'linecolor': '#bbc', 'linewidth': 30},
    },
    'amenity': {
        # generic base styles (not a tag)
        'amenity-brown': {'markercolor': '#734a08'},
        'gastronomy-icon': {'markercolor': '#C77400'},
        'health-color': {'markercolor': '#BF0000'},
        'man-made-icon':{'markercolor': '#666666'},
        'societal_amenities': {'facecolor': '#ffffe5', 'edgecolor': '#595950'},
        # tags
        'fire_station': {'facecolor': '#F3E3DD'},
        'parking': {'facecolor': '#eeeeee'},
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
    'building': {
        'other': {'facecolor': '#d9d0c9', 'edgecolor': '#b6a99c', 'linecolor': '#b6a99c'},
        'yes': {'facecolor': '#d9d0c9', 'edgecolor': '#b6a99c', 'linecolor': '#b6a99c'},
    },
    'highway': {
        # generic base styles (not a tag)
        'transportation-icon':{'markercolor': '#0092da'},
        # tags
        'crossing': {'markercolor': 'none'},
        'cycleway': {'linecolor': 'blue'},
        'footway': {'linecolor': 'salmon', 'linestyle': 'dotted'},
        'giveway': {'markercolor': 'none'},
        'motorway': {'linecolor': '#e892a2'},
        'path': {'linecolor': 'limegreen'},
        'pedestrian': {'facecolor': '#dddde8', 'linecolor': '#dddde8'},
        'primary': {'linecolor': '#fcd6a4'},
        'residential': {'linecolor': '#ffffff', 'linewidth': 4},
        'road': {'linecolor': '#ddd'},
        'secondary': {'linecolor': '#f7fabf'},
        'streetlamp': {'markercolor': 'none'},
        'tertiary': {'linecolor': '#ffffff', 'linewidth': 8},
        'track': {'linecolor': '#996600'},
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
        'construction': {'facecolor': '#c7c7b4'},
        'farm': {'facecolor': 'red'},
        'farmland': {'facecolor': '#eef0d5', 'edgecolor': '#c7c9ae', 'linecolor': '#c7c9ae'},
        'farmyard': {'facecolor': '#f5dcba', 'edgecolor': '#d1b48c', 'linecolor': '#d1b48c'},
        'forest': {'facecolor': '#add19e'},
        'grass': {'facecolor': '#cdebb0'},
        'greenfield': {'facecolor': 'none'},
        'industrial': {'facecolor': '#ebdbe8', 'edgecolor': '#c6b3c3', 'linecolor': '#c6b3c3'},
        'meadow': {'facecolor': '#cdebb0'},
        'railway': {'facecolor': '#ebdbe8'},
        'residential': {'facecolor': '#e0dfdf', 'edgecolor': '#b9b9b9', 'linecolor': '#b9b9b9'},
        'retail': {'facecolor': '#ffd6d1', 'edgecolor': '#d99c95', 'linecolor': '#d99c95'},
        'park': {'facecolor': '#c8facc', 'edgecolor': '#8bad8d'}, # leisure?
        'other': {'facecolor': 'red', 'linecolor': 'red'},
    },
    'leisure': {
        'common': {'facecolor': 'none'},
        'park': {'facecolor': '#c8facc'},
        'pitch': {'facecolor': '#aae0cb', 'edgecolor': '#6e9d8a'},
        'stadium': {'facecolor': 'none'},
        'other': {'facecolor': 'red'},
    },
    'natural': {
        'forest': {'facecolor': '#add19e'},
        'scrub': {'facecolor': '#c8d7ab'},
        'tree': {'markercolor': 'green'},
        'water': {'facecolor': '#aad3df', 'edgecolor': '#9cf', 'linecolor': '#9cf'},
        'other': {'facecolor': 'red'},
    },
    'power': {
        'other': {'facecolor': 'red'},
    },
    'shop': {
        'other': {'facecolor': '#ac39ac', 'linecolor': '#ac39ac', 'markercolor': '#ac39ac'},
    },
    'waterway': {
        'other': {'facecolor': '#aad3df', 'linecolor': '#aad3df', 'markercolor': '#aad3df'},
    },
}

# generic bases like other generic bases
tag_styles['amenity']['culture'] = tag_styles['amenity']['amenity-brown']
tag_styles['amenity']['public-service'] = tag_styles['amenity']['amenity-brown']
# tags that are styled like other tags
tag_styles['amenity']['atm'] = tag_styles['amenity']['amenity-brown']
tag_styles['amenity']['bank'] = tag_styles['amenity']['public-service']
tag_styles['amenity']['bench'] = tag_styles['amenity']['man-made-icon']
tag_styles['amenity']['bicycle_parking'] = tag_styles['highway']['transportation-icon']
tag_styles['amenity']['cafe'] = tag_styles['amenity']['amenity-brown']
tag_styles['amenity']['cemetery'] = tag_styles['landuse']['cemetery']
tag_styles['amenity']['community_centre'] = tag_styles['amenity']['culture']
tag_styles['amenity']['fast_food'] = tag_styles['amenity']['gastronomy-icon']
tag_styles['amenity']['fuel'] = tag_styles['highway']['transportation-icon']
tag_styles['amenity']['grave_yard'] = tag_styles['landuse']['cemetery']
tag_styles['amenity']['hospital'] = tag_styles['amenity']['societal_amenities']
tag_styles['amenity']['library'] = tag_styles['amenity']['culture']
tag_styles['amenity']['pharmacy'] = tag_styles['amenity']['health-color']
tag_styles['amenity']['post_box'] = tag_styles['amenity']['amenity-brown']
tag_styles['amenity']['post_office'] = tag_styles['amenity']['public-service']
tag_styles['amenity']['pub'] = tag_styles['amenity']['gastronomy-icon']
tag_styles['amenity']['public-service'] = tag_styles['amenity']['amenity-brown']
tag_styles['amenity']['recycling'] = tag_styles['amenity']['amenity-brown']
tag_styles['amenity']['school'] = tag_styles['amenity']['societal_amenities']
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
tag_styles['highway']['service'] = tag_styles['highway']['residential']
tag_styles['highway']['unclassified'] = tag_styles['highway']['residential']

tag_styles['landuse']['brownfield'] = tag_styles['landuse']['construction']
tag_styles['landuse']['grave_yard'] = tag_styles['landuse']['cemetery']
tag_styles['landuse']['leisure'] = tag_styles['landuse']['park']
tag_styles['landuse']['recreation_ground'] = tag_styles['landuse']['leisure']

tag_styles['leisure']['playground'] = tag_styles['landuse']['leisure']
tag_styles['leisure']['recreation_ground'] = tag_styles['landuse']['leisure']
tag_styles['leisure']['track'] = tag_styles['leisure']['pitch']

tag_styles['natural']['wood'] = tag_styles['natural']['forest']
tag_styles['natural']['wetland'] = tag_styles['landuse']['grass']

tag_styles['power']['other'] = tag_styles['landuse']['industrial']

# Personal added
tag_styles['landuse']['aquaculture'] = tag_styles['landuse']['leisure']
tag_styles['landuse']['conservation'] = tag_styles['natural']['forest']

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

def carto_plot(gdf, tags=None, left=None, right=None, top=None, bottom=None):

    geometry_types = [['Polygon', 'MultiPolygon'],['LineString'],['Point']]
    #tags_to_plot = ['landuse', 'power', 'amenity', 'natural', 'building', 'highway', 'waterway']
    
    fig, ax = plt.subplots(figsize=(24,24))
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