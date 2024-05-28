# Bounding Counterfactuals under Selection Bias

This bundle contains the manuscript submited to the PGM2024 and entitled  "A Divide and Conquer Approach for Solving Structural
Causal Models".
The organisation  is the following:

- _examples_: a toy example for running the method proposed in the paper.
- _ctfzeros_: python sources implementing the method.
- _models_: set of structural causal models in UAI format considered in the experimentation.
- _requirements.txt_: code dependencies.





## Setup
First of all, check the Python version. This sources have been coded with the following Python version:


```python
!python --version
```

    Python 3.11.2


Then, install the dependencies in the `requirement.txt` file. The main dependency is the python packege `bcause` (https://github.com/PGM-Lab/bcause).


```python
!pip install --upgrade pip setuptools wheel
!pip install -r ./requirements.txt
```

    Requirement already satisfied: pip in /Users/rcabanas/venv/2024-PGM-DCCC/lib/python3.11/site-packages (24.0)
    Requirement already satisfied: setuptools in /Users/rcabanas/venv/2024-PGM-DCCC/lib/python3.11/site-packages (70.0.0)
    Requirement already satisfied: wheel in /Users/rcabanas/venv/2024-PGM-DCCC/lib/python3.11/site-packages (0.43.0)
    Collecting bcause@ git+https://github.com/PGM-Lab/bcause@dev-czeros (from -r ./requirements.txt (line 1))
      Cloning https://github.com/PGM-Lab/bcause (to revision dev-czeros) to /private/var/folders/f5/bp1mbmt10w1f_m23nwfgsn_h0000gn/T/pip-install-3ws7r8gj/bcause_6ccfdc155b53490ab0019a6cc247a729
      Running command git clone --filter=blob:none --quiet https://github.com/PGM-Lab/bcause /private/var/folders/f5/bp1mbmt10w1f_m23nwfgsn_h0000gn/T/pip-install-3ws7r8gj/bcause_6ccfdc155b53490ab0019a6cc247a729
      Running command git checkout -b dev-czeros --track origin/dev-czeros
      Switched to a new branch 'dev-czeros'
      branch 'dev-czeros' set up to track 'origin/dev-czeros'.
      Resolved https://github.com/PGM-Lab/bcause to commit b264968827b601ce6cdd99cd8d1c023a6ae69199
      Preparing metadata (setup.py) ... [?25ldone
    [?25hRequirement already satisfied: more-itertools==10.2.0 in /Users/rcabanas/venv/2024-PGM-DCCC/lib/python3.11/site-packages (from -r ./requirements.txt (line 2)) (10.2.0)
    Requirement already satisfied: python-sat==0.1.8.dev15 in /Users/rcabanas/venv/2024-PGM-DCCC/lib/python3.11/site-packages (from -r ./requirements.txt (line 3)) (0.1.8.dev15)
    Requirement already satisfied: numpy~=1.26 in /Users/rcabanas/venv/2024-PGM-DCCC/lib/python3.11/site-packages (from -r ./requirements.txt (line 4)) (1.26.4)
    Requirement already satisfied: six in /Users/rcabanas/venv/2024-PGM-DCCC/lib/python3.11/site-packages (from python-sat==0.1.8.dev15->-r ./requirements.txt (line 3)) (1.16.0)
    Requirement already satisfied: pandas~=2.0.3 in /Users/rcabanas/venv/2024-PGM-DCCC/lib/python3.11/site-packages (from bcause@ git+https://github.com/PGM-Lab/bcause@dev-czeros->-r ./requirements.txt (line 1)) (2.0.3)
    Requirement already satisfied: matplotlib~=3.5.2 in /Users/rcabanas/venv/2024-PGM-DCCC/lib/python3.11/site-packages (from bcause@ git+https://github.com/PGM-Lab/bcause@dev-czeros->-r ./requirements.txt (line 1)) (3.5.3)
    Requirement already satisfied: networkx~=2.6.3 in /Users/rcabanas/venv/2024-PGM-DCCC/lib/python3.11/site-packages (from bcause@ git+https://github.com/PGM-Lab/bcause@dev-czeros->-r ./requirements.txt (line 1)) (2.6.3)
    Requirement already satisfied: pgmpy~=0.1.17 in /Users/rcabanas/venv/2024-PGM-DCCC/lib/python3.11/site-packages (from bcause@ git+https://github.com/PGM-Lab/bcause@dev-czeros->-r ./requirements.txt (line 1)) (0.1.25)
    Requirement already satisfied: cycler>=0.10 in /Users/rcabanas/venv/2024-PGM-DCCC/lib/python3.11/site-packages (from matplotlib~=3.5.2->bcause@ git+https://github.com/PGM-Lab/bcause@dev-czeros->-r ./requirements.txt (line 1)) (0.12.1)
    Requirement already satisfied: fonttools>=4.22.0 in /Users/rcabanas/venv/2024-PGM-DCCC/lib/python3.11/site-packages (from matplotlib~=3.5.2->bcause@ git+https://github.com/PGM-Lab/bcause@dev-czeros->-r ./requirements.txt (line 1)) (4.52.4)
    Requirement already satisfied: kiwisolver>=1.0.1 in /Users/rcabanas/venv/2024-PGM-DCCC/lib/python3.11/site-packages (from matplotlib~=3.5.2->bcause@ git+https://github.com/PGM-Lab/bcause@dev-czeros->-r ./requirements.txt (line 1)) (1.4.5)
    Requirement already satisfied: packaging>=20.0 in /Users/rcabanas/venv/2024-PGM-DCCC/lib/python3.11/site-packages (from matplotlib~=3.5.2->bcause@ git+https://github.com/PGM-Lab/bcause@dev-czeros->-r ./requirements.txt (line 1)) (24.0)
    Requirement already satisfied: pillow>=6.2.0 in /Users/rcabanas/venv/2024-PGM-DCCC/lib/python3.11/site-packages (from matplotlib~=3.5.2->bcause@ git+https://github.com/PGM-Lab/bcause@dev-czeros->-r ./requirements.txt (line 1)) (10.3.0)
    Requirement already satisfied: pyparsing>=2.2.1 in /Users/rcabanas/venv/2024-PGM-DCCC/lib/python3.11/site-packages (from matplotlib~=3.5.2->bcause@ git+https://github.com/PGM-Lab/bcause@dev-czeros->-r ./requirements.txt (line 1)) (3.1.2)
    Requirement already satisfied: python-dateutil>=2.7 in /Users/rcabanas/venv/2024-PGM-DCCC/lib/python3.11/site-packages (from matplotlib~=3.5.2->bcause@ git+https://github.com/PGM-Lab/bcause@dev-czeros->-r ./requirements.txt (line 1)) (2.9.0.post0)
    Requirement already satisfied: pytz>=2020.1 in /Users/rcabanas/venv/2024-PGM-DCCC/lib/python3.11/site-packages (from pandas~=2.0.3->bcause@ git+https://github.com/PGM-Lab/bcause@dev-czeros->-r ./requirements.txt (line 1)) (2024.1)
    Requirement already satisfied: tzdata>=2022.1 in /Users/rcabanas/venv/2024-PGM-DCCC/lib/python3.11/site-packages (from pandas~=2.0.3->bcause@ git+https://github.com/PGM-Lab/bcause@dev-czeros->-r ./requirements.txt (line 1)) (2024.1)
    Requirement already satisfied: scipy in /Users/rcabanas/venv/2024-PGM-DCCC/lib/python3.11/site-packages (from pgmpy~=0.1.17->bcause@ git+https://github.com/PGM-Lab/bcause@dev-czeros->-r ./requirements.txt (line 1)) (1.13.1)
    Requirement already satisfied: scikit-learn in /Users/rcabanas/venv/2024-PGM-DCCC/lib/python3.11/site-packages (from pgmpy~=0.1.17->bcause@ git+https://github.com/PGM-Lab/bcause@dev-czeros->-r ./requirements.txt (line 1)) (1.5.0)
    Requirement already satisfied: torch in /Users/rcabanas/venv/2024-PGM-DCCC/lib/python3.11/site-packages (from pgmpy~=0.1.17->bcause@ git+https://github.com/PGM-Lab/bcause@dev-czeros->-r ./requirements.txt (line 1)) (2.3.0)
    Requirement already satisfied: statsmodels in /Users/rcabanas/venv/2024-PGM-DCCC/lib/python3.11/site-packages (from pgmpy~=0.1.17->bcause@ git+https://github.com/PGM-Lab/bcause@dev-czeros->-r ./requirements.txt (line 1)) (0.14.2)
    Requirement already satisfied: tqdm in /Users/rcabanas/venv/2024-PGM-DCCC/lib/python3.11/site-packages (from pgmpy~=0.1.17->bcause@ git+https://github.com/PGM-Lab/bcause@dev-czeros->-r ./requirements.txt (line 1)) (4.66.4)
    Requirement already satisfied: joblib in /Users/rcabanas/venv/2024-PGM-DCCC/lib/python3.11/site-packages (from pgmpy~=0.1.17->bcause@ git+https://github.com/PGM-Lab/bcause@dev-czeros->-r ./requirements.txt (line 1)) (1.4.2)
    Requirement already satisfied: opt-einsum in /Users/rcabanas/venv/2024-PGM-DCCC/lib/python3.11/site-packages (from pgmpy~=0.1.17->bcause@ git+https://github.com/PGM-Lab/bcause@dev-czeros->-r ./requirements.txt (line 1)) (3.3.0)
    Requirement already satisfied: threadpoolctl>=3.1.0 in /Users/rcabanas/venv/2024-PGM-DCCC/lib/python3.11/site-packages (from scikit-learn->pgmpy~=0.1.17->bcause@ git+https://github.com/PGM-Lab/bcause@dev-czeros->-r ./requirements.txt (line 1)) (3.5.0)
    Requirement already satisfied: patsy>=0.5.6 in /Users/rcabanas/venv/2024-PGM-DCCC/lib/python3.11/site-packages (from statsmodels->pgmpy~=0.1.17->bcause@ git+https://github.com/PGM-Lab/bcause@dev-czeros->-r ./requirements.txt (line 1)) (0.5.6)
    Requirement already satisfied: filelock in /Users/rcabanas/venv/2024-PGM-DCCC/lib/python3.11/site-packages (from torch->pgmpy~=0.1.17->bcause@ git+https://github.com/PGM-Lab/bcause@dev-czeros->-r ./requirements.txt (line 1)) (3.14.0)
    Requirement already satisfied: typing-extensions>=4.8.0 in /Users/rcabanas/venv/2024-PGM-DCCC/lib/python3.11/site-packages (from torch->pgmpy~=0.1.17->bcause@ git+https://github.com/PGM-Lab/bcause@dev-czeros->-r ./requirements.txt (line 1)) (4.12.0)
    Requirement already satisfied: sympy in /Users/rcabanas/venv/2024-PGM-DCCC/lib/python3.11/site-packages (from torch->pgmpy~=0.1.17->bcause@ git+https://github.com/PGM-Lab/bcause@dev-czeros->-r ./requirements.txt (line 1)) (1.12)
    Requirement already satisfied: jinja2 in /Users/rcabanas/venv/2024-PGM-DCCC/lib/python3.11/site-packages (from torch->pgmpy~=0.1.17->bcause@ git+https://github.com/PGM-Lab/bcause@dev-czeros->-r ./requirements.txt (line 1)) (3.1.4)
    Requirement already satisfied: fsspec in /Users/rcabanas/venv/2024-PGM-DCCC/lib/python3.11/site-packages (from torch->pgmpy~=0.1.17->bcause@ git+https://github.com/PGM-Lab/bcause@dev-czeros->-r ./requirements.txt (line 1)) (2024.5.0)
    Requirement already satisfied: MarkupSafe>=2.0 in /Users/rcabanas/venv/2024-PGM-DCCC/lib/python3.11/site-packages (from jinja2->torch->pgmpy~=0.1.17->bcause@ git+https://github.com/PGM-Lab/bcause@dev-czeros->-r ./requirements.txt (line 1)) (2.1.5)
    Requirement already satisfied: mpmath>=0.19 in /Users/rcabanas/venv/2024-PGM-DCCC/lib/python3.11/site-packages (from sympy->torch->pgmpy~=0.1.17->bcause@ git+https://github.com/PGM-Lab/bcause@dev-czeros->-r ./requirements.txt (line 1)) (1.3.0)


## Model and data

In this repository, we provide functionality for preprocessing the model and data so they could work we our inference algorithm:


```python
from ctfzeros.prepro import load_and_preprocess
```


```python
filepath = "./models/synthetic/simple_nparents2_nzr04_zdr05_10.uai"
datapath = "./models/synthetic/simple_nparents2_nzr04_zdr05_10.csv"

model, data, _, _ = load_and_preprocess(filepath, datapath)
model
```




    <StructuralCausalModel (Y:2,X2:2,X1:2|Uy:14,Ux1:2,Ux2:2), dag=[Uy][Y|Uy:X2:X1][X2|Ux2][X1|Ux1][Ux1][Ux2]>




```python
model.draw()
```

![output_8_0.png](data:image/png;base64,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SZg/fz6mT59e7TG73e78oS6TyXD16lVkZ2dXe8MvLS3FM888gyNHjuDHH390bsPT6XRo3bq18w2/Y8eOzmNxawoJCWnU90fiUqlUSEhIQEJCAmbMmCF2OR7BMEBEorJYLI2+RrNmzTBo0CAcPHgQL774YrVdAgcOHIAgCBgxYkSt1wmCgM8//xz5+flITk7G9u3bAcD56b5t27YIDw9HeHg4fvOb38But9e5xqApbFUk6WIYICJRuSMMAMDo0aOxb98+fPXVV+jbt6/z63v37kViYiIMBoPL191///349a9/DZVKhZdeegkKhaLO2wa+vhWRqKF8u2k0ETV57uor0KtXL0RFRWHfvn3Or2VkZODSpUsYOXKky9fIZDJERkaiTZs2AG73H+CKfZIihgEiElVjdzdXvnnL5XKMGDEC//znP52zDfv27UNgYOAd93lzdzURwwARiexOn8Qr78+XlZW5fNxisVS7hz9q1CiUlpbin//8JwRBwP79+9G/f/873s/nTAARwwARiexOnfMq99hfuXKl1mMWiwU5OTnV9uG3a9cOHTt2xL59+5CWlobs7GyMGjWqweMTSQXDABGJSqPR1PlYz549oVKpsGPHjlrbD3fu3AmbzVZtsSAAjBw5El999RW2bduG0NDQWo/XZ3wiqWAkJiJR3enNODw8HLNmzcKqVaswefJkDBgwAGq1GmfPnsWBAwfQp08fDBgwoNprhg8fjpUrV+KLL77AE088cdcmMAwDRAwDRCQytVoNhUJRZ//3mTNnokWLFvjoo4+QkpICu92OmJgYzJkzB9OmTavV5CciIgK9e/fG8ePH69xFUEmhULjsCkgkNQwDRCQqmUwGnU6H/Pz8Op8zcuTIu76xV6VSqXDffffhwQcfvOPzwsLCuICQCFwzQEQ+ICwszG3XysvLw7Fjx+66cBCAy5MQiaSIMwNEJLqAgADodDrnyXANcf36dZw5cwaffvopVCoVJkyYcMfn63Q6rxxfTOQPODNARD5Br9c3apvfqVOn8MorryArKwt/+tOfEBERUedzlUol9Hp9g8ciampkAttvEZGPMJvNyMzM9Pg4rVq14sFCRFVwZoCIfIZWq63zQCF3MRgMDAJENTAMEJFPCQ8P91ggMBgMCA8P98i1ifwZbxMQkU8ym83Iyspyy6mGSqUSMTExnBEgqgPDABH5LLvdDqPR2KhdBjqdDnq9HgqFwo2VETUtDANE5PPKy8thMplQUFBQZ6fCqhQKBcLCwrh9kOgeMQwQkd8QBAFWqxUWiwUWiwU2mw2CIEAmk0GpVEKj0UCj0UCtVrOzIFE9MAwQERFJHHcTEBERSRzDABERkcQxDBAREUkcwwAREZHEMQwQERFJHMMAERGRxDEMEBERSRzDABERkcQxDBAREUkcwwAREZHEMQwQERFJHMMAERGRxDEMEBERSRzDABERkcQxDBAREUkcwwAREZHEMQwQERFJHMMAERGRxDEMEBERSRzDABERkcQxDBAREUkcwwAREZHEMQwQERFJHMMAERGRxP1/8wCDY7XSRc8AAAAASUVORK5CYII=)

```python
data
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>X2</th>
      <th>X1</th>
      <th>Y</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>995</th>
      <td>0</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>996</th>
      <td>0</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>997</th>
      <td>1</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>998</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>999</th>
      <td>0</td>
      <td>0</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
<p>1000 rows × 3 columns</p>
</div>





## Counterfactual inference

First, load corresponding modules for using DCCC and EMCC:


```python
from ctfzeros.divideconquer import DCCC_inverted_tree
from bcause.inference.causal.multi import EMCC
```

Set up the DCCC inference engine with a number of solutions $N=20$. Then calculate the probability of sufficiency $PS(X_2,Y)$:


```python
infDCCC = DCCC_inverted_tree(model, data, num_runs=20)
infDCCC.prob_sufficiency("X2","Y")
```




    [0.8247598578471568, 1.0]



Similarly, with the state of the art method EMCC interating up to 100 iterations each EM run.


```python
infEMCC = EMCC(model,data,num_runs=20, max_iter=100)
infEMCC.prob_sufficiency("X2","Y")

```




    [0.9105167456058657, 0.9975199671164047]


