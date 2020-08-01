from .models import Box

def get_area(length, breadth, height):
    return 2 * ( (length * breadth) + (length * height ) + (breadth * height))

def get_volume(length, breadth, height):
    return length * breadth * height


def get_box_queryset(filters, creator=None):
    boxes = Box.objects.all()
    if creator:
    	boxes = boxes.filter(creator=creator)

    length_more_than = filters.get('length_more_than')
    if length_more_than:
        boxes = boxes.filter(length__gt=length_more_than)

    length_less_than = filters.get('length_less_than')
    if length_less_than:
        boxes = boxes.filter(length__lt=length_less_than)

    breadth_more_than = filters.get('breadth_more_than')
    if breadth_more_than:
        boxes = boxes.filter(breadth__gt=breadth_more_than)

    breadth_less_than = filters.get('breadth_less_than')
    if breadth_less_than:
        boxes = boxes.filter(breadth__lt=breadth_less_than)

    height_more_than = filters.get('height_more_than')
    if height_more_than:
        boxes = boxes.filter(height__gt=height_more_than)

    height_less_than = filters.get('height_less_than')
    if height_less_than:
        boxes = boxes.filter(height__lt=height_less_than)

    area_more_than = filters.get('area_more_than')
    if area_more_than:
        boxes = boxes.filter(area__gt=area_more_than)

    area_less_than = filters.get('area_less_than')
    if area_less_than:
        boxes = boxes.filter(area__lt=area_less_than)

    volume_more_than = filters.get('volume_more_than')
    if volume_more_than:
        boxes = boxes.filter(volume__gt=volume_more_than)

    volume_less_than = filters.get('volume_less_than')
    if volume_less_than:
        boxes = boxes.filter(volume__lt=volume_less_than)

    created_by = filters.get('created_by')
    if created_by and creator is None:
        boxes = boxes.filter(creator__username=created_by)

    created_before = filters.get('created_before')
    if created_before and creator is None:
        boxes = boxes.filter(created__lt=created_before)

    created_after = filters.get('created_after')
    if created_after and creator is None:
        boxes = boxes.filter(created__gt=created_after)

    return boxes