{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import matplotlib as mpl\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "import sys\n",
    "args = sys.argv \n",
    "\n",
    "df = pd.read_csv('wdbc.data', index_col=0)\n",
    "\n",
    "print(len(df))\n",
    "print(len(df.columns))\n",
    "\n",
    "dataExchange = df.iloc[:, [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,0]]\n",
    "print(dataExchange)\n",
    "\n",
    "dataExchange.to_csv('tmp.csv')"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
