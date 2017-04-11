#! /bin/bash

opencv_annotation --annotations=annotations.txt --images=positives/ 

opencv_createsamples -info annotations.txt -bg negatives.txt -vec positives.txt -w 24 -h 24  

opencv_traincascade -data cascade_dir -vec positives.txt -bg negatives.txt -numPos 430 -numNeg 450 -w 24 -h 24 -precalcValBufSize 1024 -precalcIdxBufSize 1024 -numStages 25 -acceptanceRatioBreakValue 1.0e-5