# Fruit-Shelf-Life-Detection
MAULANA AZAD 
NATIONAL INSTITUTE OF TECHNOLOGY 
BHOPAL INDIA, 462003

DEPARTMENT OF COMPUTER SCIENCE & ENGINEERING

Fruit Shelf Life Predictor
Minor Project Report
Semester V th
Submitted by:

Prateek Verma
171112291
Ammar Alavi
171112292
Mayank Verma
171112260
Franklin Toppo 
171112209
 Under the Guidance of
Mr. Bholanath Roy
DEPARTMENT OF COMPUTER SCIENCE AND ENGINEERING
Session: 2019-2020


MAULANA AZAD 
NATIONAL INSTITUTE OF TECHNOLOGY 
BHOPAL INDIA, 462003









DEPARTMENT OF COMPUTER SCIENCE & ENGINEERING

CERTIFICATE


This is to certify that the project report carried out on “Fruit Shelf Life
Predictor” by the 3rd year students:
Prateek Verma
171112291
Ammar Alavi
171112292
Mayank Verma
171112260

Have successfully completed their project in partial fulfilment of their Degree in
Bachelor of Technology in Computer Science and Engineering.



   Mr. Bholanath Roy 
  (Minor Project Mentor)

DECLARATION


 We, hereby declare that the following report which is being presented in the Minor Project Documentation Entitled as “Fruit Shelf Life Predictor”  is an authentic documentation of our own original work and to best of our knowledge. The following project and its report, in part or whole, has not been presented or submitted by us for any purpose in any other institute or organization. Any contribution made to the research by others, with whom we have worked at Maulana Azad National Institute of Technology, Bhopal or elsewhere, is explicitly acknowledged in the report.




Prateek Verma
171112291
Ammar Alavi
171112292
Mayank Verma
171112260
Franklin Toppo 
171112209



ACKNOWLEDGEMENT




With due respect, we express our deep sense of gratitude to our respected guide 
and coordinator Mr. Bholanath Roy, for his valuable help and guidance. We are 
thankful for the encouragement that he has given us in completing this project 
successfully.

It is imperative for us to mention the fact that the report of minor project could
not have been accomplished without the periodic suggestions and advice of our
project guide Mr. Bholanath Roy , and project coordinators
Dr. Dhirendra Pratap Singh and Dr. Jaytrilok Choudhary.

We are also grateful to our respected director Dr. N. S. Raghuwanshi for 
permitting us to utilize all the necessary facilities of the college.

We are also thankful to all the other faculty, staff members and laboratory 
attendants of our department for their kind cooperation and help. Last but 
certainly not the least; we would like to express our deep appreciation towards 
our family members and batch mates for providing the much needed support and 
encouragement.







TABLE OF CONTENTS




Certificate	ii
Declaration	iii
Acknowledgement	iv

Introduction	1
Literature review and survey	3
Gaps identified	3
Proposed work and methodology	4
Proposed Work
Methodology
Tools and technology to be used (hardware and software)	6
Software requirement
Hardware requirement
Conclusion	7
References	  8

1.INTRODUCTION

Computer vision is one of the fastest growing and one of the most researched disciplines in this day and age. Computer vision is the hardware and software involved in capturing and analyzing an image with a computer. It has found a home on inspection lines because of its speed, accuracy, reliability, and objectivity.
Computer vision excels on systems such as inspection lines at finding defects in well-defined objects. When a computer vision system has an ideal representation of what a, say, electronic component looks like, it is very easy to detect deviations from the norm. However, a field that is still in its infancy is applying computer vision to non-uniform objects. The purpose of this thesis is to present a process that applies existing computer vision techniques to build a predictive model of the shelf-life of fruit. 

Increasingly, computer vision is being used in the agriculture industry. Agriculture is a good fit for computer vision because of the sheer volume of fruit that most factories process every day and the time, effort, and money that goes into quality control and distribution decisions. Today, some factories use computer vision to detect for bruises and other defects that would detract customers. This type of inspection falls under the broader category of fruit quality grading.

In most agricultural businesses, this grading is done by humans. Essentially, the grading is a rating on a scale from one to five of the external quality of the fruit. Fruits with ratings of three and above are sold while those with ratings of two and below are discarded. This type of grading is a binary process that is beginning to be (somewhat reliably) performed by computers. Another, much more advanced, application is to use computer vision to classify distinct categories of fruit with similar characteristics and place all of one group of fruit into one room, dose the entire room with ethylene, and then sell the entirety of that group when it is ripe. However, this takes up time, space, and money to store and wait for the fruit. It is also frequently wasteful and inaccurate. The purpose of this thesis is to present a process that uses computer vision to extract color features of a large group of the fruit and then builds a predictive model of the shelf-life for the fruit (specifically bananas for the purposes of this thesis). While the thesis demonstrates the process on bananas, the process can theoretically be repeated for any climacteric fruit that changes colors distinctly as it ripens. Essentially, a camera would scan each piece of fruit, extract features, and then plug the values into the created model to get an accurate prediction of the shelf-life of that particular piece of fruit. This would allow fruit with a shorter shelf-life to be shipped across the state whereas fruit with a longer shelf-life would be shipped across the country. This would save money and space. It would also allow more fruit to be sold because fruit that may have been given an unacceptable rating would still be able to be sold (if the fruit is deemed to ripe to be shipped, it can still be sold locally). Fundamentally, instead of making distribution decisions based on current features (as is done in the industry today), this thesis proposes a model which allows current features to be used to predict future features, which are used to inform distribution decisions.

 Finally, the proposed technique would be advantageous because it allows for an objective, accurate, and concrete shelf-life prediction system as opposed to the current fruit grading procedure. This thesis develops an experimental process to undergo and the subsequent statistical analysis to build a predictive model of color features against shelf-life. The thesis uses bananas as a proof of concept of the process. There are two experiments: the first one captures images of a few samples of fruit and then destructively measures sugar content. The purpose of the second experiment is to correlate color representations with sugar content to determine the end point of shelf-life. A sugar content of 23% indicates a ripe banana, which, for the purposes of this thesis will serve as the last day of data collection. The color of many samples of bananas on the first day that their sugar content reaches or exceeds 23% is recorded and the color range is then set as the end color of the second experiment. The second experiment involves capturing images of many samples of the fruit each day until it becomes spoiled. The color features are extracted every day using computer vision. For statistical analysis, each fruit is plotted to measure color as a function of time. Postprocessing then occurs with different representations of color being calculated (using existing computer vision algorithms). Then, for each fruit, shelf-life is calculated at a given color value. This is repeated for each selected color and each fruit. Finally, shelflife as a function of color can be modeled (with the corresponding standard deviation at each color) to ultimately give a model of shelf-life based on color.







2.LITERATURE REVIEW AND SURVEY
The purpose of this literature review is to provide the readers with an 
understanding of how computer vision is applied in the agriculture industry
today.  This will identify current industry standards as well as active areas of
research.  Additionally, this literature review will serve to identify gaps in the 
current research. 
Computer vision is the hardware and software involved in image processing of an 
object by a computer.  Essentially, an object is analyzed by capturing an image of
it and extracting features and characteristics for downstream processing
(characterization, discrimination, model building, etc.).  Over the past thirty
years, computer vision has increasingly found a home in the agriculture industry.
Common applications of computer vision systems in the agricultural industry 
involve automatic sorting, grading, and estimation of quality of fruits, vegetables, 
and meat.  Traditionally, sorting and grading of fruits has been done by a panel of
experts.  However, in many ways, computer vision systems are better because 
they can be faster and more reliable than human graders.  One of the advantages
of computer vision systems are that computers can detect light in the ultraviolet
and infrared spectrum, which humans cannot do .  Also, computers are generally 
much faster and more accurate (consistent) than humans.
There is no bias in computer vision systems, unlike humans.
	
Computer vision needs three things: a source of light, an object to be analyzed, 
and a receptor to detect the light . Lighting is one of the most important aspects
of computer vision.  Illumination must be uniform, constant, and repeatable. 



3. GAPS IDENTIFIED
This project is currently focused on bananas only, but it can be done for other fruits as well.





4.1 PROPOSED WORK 

The process proposed in this thesis develops certain discrete steps to undertake to build a model that predicts shelf-life based on empirically measured color features. The first step is to undertake an experiment that correlates color to sugar content (and, therefore, literature values of ripeness). The process uses color features to estimate sugar content to estimate ripeness. That is, sugar content is predicted by color, so the color is the criterion for shelf-life.

In this project, twenty bananas are chosen as proof of concept of the process. Every day of experimentation, two bananas are chosen, their colors are measured by taking pictures of the banana and then using computer vision to find the colors, and finally the refractometer is used to destructively measure sugar content. The result of this experiment is a color range where the sugar content of the banana first becomes “ripe”. 

Ultimately, this step is necessary because measures of “ripeness” are fundamentally subjective, so this first experiment determines a color range that serves as the end-point of the second experiment (large scale data collection that the model is actually built off of).

The second experiment uses thirty-six bananas and takes a picture of each banana on every day of the experiment. Each day, after the picture is taken of each banana, computer vision is used to extract features and the color of every banana is recorded every day. The first day that the experimental banana falls into the “ripe” color range (determined in experiment one) indicates the end of life for that specific banana. 










4.2. METHODOLOGY

Every day of data collection, the hue value of every sample banana was found using computer vision (as described above in the experimental procedures). At the end of data collection, the hue value over every banana’s lifetime is recorded. Then, the hue values of every banana in the sample can be plotted as a function of days passed (time). This plotting gives a visual representation of how the hue values of the bananas in the sample change over the respective banana’s 
lifetime. 
In order to build the model, hue has to be standardized among each banana in the sample because each banana starts at a unique hue and has a unique shelf-life. That is, it is necessary to calculate every sample fruit’s shelf-life at a specific given hue. However, it is common that the exact hue value of interest was not recorded (if the hue value of interest is 40, the fruit may have gone from a hue of 41.2 on day one to a hue of 39.9 on day two), so it is necessary to interpolate between existing data points. For each hue value: {40, 38, 36, 34, 32, 30}, the line between the two points closest to the point of interest will be interpolated. A second-order polynomial is used when there are at least five data points in the hue range of interest and hence a second order polynomial of the form 

Shelf life = a*hue^2 + b*hue + c 

will be formed which will give the relationship between hue and shelf life. 

Another method is to use linear regression for the two variables shelf life and hue and form a line relationship between them and calculate the coefficient of hue and constant to give a relationship

Shelf life = a*hue + b

Then at the end of the project the two methods are validated and the model with the highest accuracy will be chosen from the two




5. Tools and technology to be used (hardware and software)	

PANDAS

In computer programming, pandas is a software library written for the Python programming language for data manipulation and analysis. In particular, it offers data structures and operations for manipulating numerical tables and time series. It is free software released under the three-clause BSD license.

SCIKIT-LEARN

Scikit-learn is a free software machine learning library for the Python programming language. It features various classification, regression and clustering algorithms including support
vector machines.


PYTHON

Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.

NUMPY

NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices along with a large collection of high-level mathematical functions to operate on these arrays.
	
OPEN CV

OpenCV is a library of programming functions mainly aimed at real-time computer vision. Originally developed by Intel, it was later supported by Willow Garage then Itseez. The library is cross-platform and free for use under the open-source BSD license.



JUPYTER NOTEBOOK

The Jupyter Notebook is an open-source web application that allows you to create and share documents that contain live code, equations,  visualizations and narrative text. Uses include: data cleaning and transformation, numerical simulation, statistical modeling, data visualization, machine learning, and much more.


6. CONCLUSION
Ultimately, this thesis has demonstrated proof of concept of a process to use computer vision to build a predictive model of shelf-life of fruit.  Computer vision is becoming widespread in many industries and is, therefore, a burgeoning field of research.  
It is most widely used on inspection lines of electronic components.  Computer vision holds many advantages to its human counterpart: it is faster, more reliable, cheaper in the long-term, and more accurate.  Naturally, computer vision is starting to become implemented in other industries.  One of the most important fields that computer vision is starting to move into is the agriculture industry.  
Computer vision excels at doing a well defined process many times.  This lends well to industries such as electronics production because every piece of one electronic component must look the same.  This means that a computer can rapidly capture an image of an electronic component coming onto an inspection line, compare certain regions to an ideal (correctly produced) image of the component, and then make a decision to sell or discard the component. 
This thesis lays the groundwork for a myriad of further experiments as well as a multitude of alternations of the process. Naturally, the process may be able to be applied to any fruit that adheres to the two criteria enumerated above.  Future work can possibly apply the process to many fruits.  Among the best candidates for future fruits are mangoes, apples, avocados, blackberries, melons, and tomatoes.  This is because they are climacteric and have the most distinct color changes in their life-time of ripeness.   
While this thesis has focused on the distribution aspect of fruit decision making, there is possibly an application of the thesis process earlier in the fruit’s lifetime.  On the farm, the process presented in this thesis can be used to determine time to ripeness, time to harvest, etc. (perhaps with the help of virtual reality, the thesis process can be integrated with current virtual reality glasses).  
Another related application of the process proposed in this thesis would be in the growing area of robot farming and harvesting.  Instead of measuring shelf-life, the robot harvesters could measure days until harvest using a similar methodology but different inputs. 
 

7. REFERENCES
Thesis by Faculty of California Polytechnic State University
