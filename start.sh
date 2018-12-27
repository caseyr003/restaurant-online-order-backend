#!/bin/bash
rm restaurant-online-order.db
python3 database.py
python3 populate.py
python3 app.py
