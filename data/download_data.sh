#!/bin/bash

base_url="https://github.com/DoranLyong/ModelNet40_preprocess/releases/download/ModelNet40"

files=(
    "modelnet40_shape_names.txt"
    "modelnet40_test.txt"
    "modelnet40_train.txt"
    "modelnet40_test_8192pts_fps.dat"
    "modelnet40_train_8192pts_fps.dat"
)

for file in "${files[@]}"; do
    wget "$base_url/$file"
done
