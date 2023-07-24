#!/bin/bash
for i in {1..1000} 
do
    curl http://localhost:5000
    sleep 0.5
done