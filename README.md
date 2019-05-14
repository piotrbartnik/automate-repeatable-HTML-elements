automate-repeatable-HTML-elements
============

With this script you can automate creating duplicated parts of html code.
If you want edit template you must also edit py file to assign proper values.

Example python file use csv file with saved:
- person/company,
- person/company countries,
- person/company images,
- person/company descriptions.

Only thing that is not automated is adding images to server.

## Instalation and use on Linux

Download repository.

##### 1.

If it is first time run please type in console:

```
sudo apt-get install python-pip

sudo pip install Jinja2
```
##### 2.

Prepare csv file named input.csv with 4 columns:

| person/company | person/company countries | person/company images  | person/company descriptions |
| ------- | --- | --- | --- |

Example is included.


##### 3.

In console opened in project directory run:

```
python htmlTemplating.py
```

## Instalation and use on Windows

Download repository.

##### 1.

If it is first time run please type in console:

```
python get-pip.py

pip install Jinja2
```

##### 2.

Prepare csv file named input.csv with 4 columns:

| person/company | person/company countries | person/company images  | person/company descriptions |
| ------- | --- | --- | --- |

Example is included.

Client country can be empty for polish clients but it has to be included as an empty column.


##### 3.

In console opened in project directory run:

```
python htmlTemplating.py
```

