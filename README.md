# Box Inventory

REST APIs to add, view, update and delete boxes of inventory

## Getting Started

1. Clone this repo.
2. pip install -r requirements.txt
3. Make changes in api/params.py for validations/conditions.
4. python manage.py migrate
5. python manage.py createsuperuser
6. python manage.py runserver
7. Open the Admin URL in a web browser to login.
7. Open the BASE API in a web browser.

Login URL:-

```
http://127.0.0.1:8000/admin
```

Base API:-

```
http://127.0.0.1:8000/api/boxes
```

## All APIs:-
* /api/boxes/ - to list all boxes (GET), to add new box (POST)
* /api/boxes/<box_id> - to update (PUT), to delete a box using the box_id (DELETE)
* /api/my-boxes/ - to list current logged in user's boxes (GET)

## Request Content:-
/api/boxes/ - to add new box (POST)
```
{
	"length":<float>,
	"breadth":<float>,
	"height":<float>
}
```
/api/boxes/<box_id> - to add new box (PUT)
```
{
	"length":<float>,
	"breadth":<float>,
	"height":<float>
}
```
## GET Request Optional Parameters - for filtering:-
/api/boxes/
```
length_more_than
length_less_than
breadth_more_than
breadth_less_than
height_more_than
height_less_than
area_more_than
area_less_than
volume_more_than
volume_less_than
created_by
created_before
created_after
```

/api/my-boxes/
```
length_more_than
length_less_than
breadth_more_than
breadth_less_than
height_more_than
height_less_than
area_more_than
area_less_than
volume_more_than
volume_less_than
```
## Validations/Conditions
api/params.py

1. Average area of all added boxes should not exceed A1
2. Average volume of all boxes added by the current user shall not exceed V1
3. Total Boxes added in a week cannot be more than L1
4. Total Boxes added in a week by a user cannot be more than L2

## Prerequisites

* Python 3.6
* A Linux system, preferebly Ubuntu 16.04.