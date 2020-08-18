{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2 den listede  2 tane var.\n",
      "2 den listede  2 tane var.\n",
      "1 den listede  1 tane var.\n",
      "5 den listede  2 tane var.\n",
      "6 den listede  2 tane var.\n",
      "7 den listede  1 tane var.\n",
      "3 den listede  1 tane var.\n",
      "4 den listede  1 tane var.\n",
      "5 den listede  2 tane var.\n",
      "6 den listede  2 tane var.\n",
      "[2, 2, 1, 5, 6, 7, 3, 4, 5, 6]\n"
     ]
    }
   ],
   "source": [
    "def fonk1(liste):\n",
    "    for x in liste:\n",
    "        print(x,\"den listede \",liste.count(x),\"tane var.\")\n",
    "    return liste\n",
    "liste2=[2,2,1,5,6,7,3,4,5,6]\n",
    "print(fonk1(liste2))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
