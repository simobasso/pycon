from wagtail.wagtailcore import blocks


class MapBlock(blocks.StructBlock):
    longitude = blocks.DecimalBlock()
    latitude = blocks.DecimalBlock()
    zoom_level = blocks.IntegerBlock(min_value=1)

    class Meta:
        form_template = 'map/map.html'
        icon = 'cogs'
        label = 'Map'
