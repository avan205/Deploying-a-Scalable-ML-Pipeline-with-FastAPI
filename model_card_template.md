# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
This supervised machine-learning model, Random Forest Classifier model, trained to predict if a person's personal income exceeds or is less than $50,000 based on features included on 1994 Census data, also known as the adult dataset. Udacity created this project as a portion of the Machine Learning DevOps course for student use. 
Model Date: The model was constructed August 22, 2026.
Model Version: The model version is 1.0.
Model Type: The model is a Supervised Machine-Learning Classification Model using Random Forest Classification.
Information (Training Algorithms, Fairness Constraints, applied approaches, features): The model utilizes the Random Forest Classification training algorithm. There were no Fairness Constraints included; this model uses protected personal data such as race and gender, so subgroups should be carefully evaluated according to metrics: precision, recall, and error rates to ensure no unfair differences are identified. Do not use this model for real-world decision-making as it has not been evaluated with fidelity to comply with Fairness Constraints. The applied approaches including training on 75% of the data and creating a test set on 25% of the data. Categorical features, such as income > or < $50,000 were binarily encoded to predict income category, > or < $50,000. Metrics used to evaluate the data include precision, recall, and the F1 score. The data was also sliced to include evaluation of subsets of data to identify outcomes amond different demographic strata. The dataset features used to identify the outcome variable, salary > or < $50,000 include age, workclass, education, marital status, family relationship status, race, sex, hours worked per week, and native country.  

## Intended Use
This model is intended for educational use only intended for Udacity students to learn about building, training, and deploying ML models with an intended FASTAPI. Out of scope use cases include all cases not directly involved in student learning. The model is not suitable for real-world use for decisions, predictions, or planning. 

## Training Data
The training data is derived from the Census Income dataset 4/30/1996 donated by R. Kohavi and hosted on the University of California Irvine (UCI) machine learnig repository. https://doi.org/10.24432/C5GP7S
The data was trained on 75% of the data and the test split of 25%. The test split data was not used during training to ensure that training records did not influence test split results. 

## Evaluation Data
The Census Income dataset was split 75% into training data and 25% test data. The test data was not used in training and was used to calculate the precision, recall, and F1 score. The motivation for determination fo the test data metrics is to measure how well the model performs on unseen data.
The motivation of this dataset was to collect demographic factors and global population statistics to determine if an individual make > or < $50,000 per year. The motivation of the ML model was to determine if subgroups of demographic data, or a demographic profile could predict if an individual make > or < $50,000 per year. Preprocessing of the data ensure that unnecessary spaces were removed from the dataset. The salary column was binarily encoded to demonstrate the > or < $50,000 target. Other categorical features were one-hot encoded into numerical data points. The entire dataset underwent the same preprocessing steps. The distribution of the dataset is unequal. For the categorically encoded salary target the distribution values are as follows: 
salary raw numbers
<=50K    24720
>50K      7841

salary percentages
<=50K    0.75919 - 76%
>50K     0.24081 - 24%
Additionally, for other categorical features: 
race
White                 0.854274- 85%
Black                 0.095943- 10%
Asian-Pac-Islander    0.031909- 32%
Amer-Indian-Eskimo    0.009551- 0.9%
Other                 0.008323- 0.8%

sex
Male      0.669205- 67%
Female    0.330795- 33%

native-country
United-States                 0.895857- 90%
Mexico                        0.019748- 2%
?                             0.017905
Philippines                   0.006081
Germany                       0.004207
Canada                        0.003716
Puerto-Rico                   0.003501
El-Salvador                   0.003255
India                         0.003071
Cuba                          0.002918
England                       0.002764
Jamaica                       0.002488
South                         0.002457
China                         0.002303
Italy                         0.002242
Dominican-Republic            0.002150
Vietnam                       0.002058
Guatemala                     0.001966
Japan                         0.001904
Poland                        0.001843
Columbia                      0.001812
Taiwan                        0.001566
Haiti                         0.001351
Iran                          0.001321
Portugal                      0.001136
Nicaragua                     0.001044
Peru                          0.000952
France                        0.000891
Greece                        0.000891
Ecuador                       0.000860
Ireland                       0.000737
Hong                          0.000614
Trinadad&Tobago               0.000584
Cambodia                      0.000584
Thailand                      0.000553
Laos                          0.000553
Yugoslavia                    0.000491
Outlying-US(Guam-USVI-etc)    0.000430
Honduras                      0.000399
Hungary                       0.000399
Scotland                      0.000369
Holand-Netherlands            0.000031

age
36    0.027579
31    0.027272
34    0.027210
23    0.026934
35    0.026903
        ...   
83    0.000184
88    0.000092
85    0.000092
86    0.000031
87    0.000031

## Metrics
The model performance metrics include precision, recall, and F1 score calculated on the test data, or 25% of the untrained data.

Precision: 0.7165 | Recall: 0.6311 | F1: 0.6711

Precision measures that 71.7% of the time, the model correctly predicted that a salary of > $50,000 was correctly identified as earning > $50,000. It is the correctness of the model.
Recall explains how many of the > $50,000 salaries were found by the model. The recall metric shows that the model found 63% of the individuals who actually earned > $50,000. 
The F1 score balances the precision and recall into a single score and indicates that the model is about 67% efffective at finding individuals who earn > $50,000 and predicting a salary of > $50,000. 

## Ethical Considerations
This dataset contains protected demographic information that may infuse bias into any decision-making process. The input demographic information is extremely biased, especially in areas that may affect raw number of salary heavily, such as native-country of the U.S.A. This model should not be used to plan, make decisions, or model any real-world scenario due to implicit biases, unbalanced data, and unethical results owing to these included biases. 

## Caveats and Recommendations
This model is intended for student learning and model building, instruction, training, and deployment uses only. This model should not be used for real-world decision scenarios. The dataset is biased in regards to sex and native-country of origin. Additionally the data was compiled in 1994, 32 years ago, and is not indexed for inflation or currency fluctuations. This model is for student learning purposes only. 
