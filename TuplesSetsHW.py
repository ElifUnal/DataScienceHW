{
 "cells": [
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "# 1."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')\n"
     ]
    }
   ],
   "source": [
    "week=(\"Monday\",\"Tuesday\",\"Wednesday\",\"Thursday\",\"Friday\",\"Saturday\",\"Sunday\")\n",
    "print(week)"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "#2."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "('Apple', 'Mango', 'Orange')\n"
     ]
    }
   ],
   "source": [
    "fruits=set(['apple','mango','orange'])\n",
    "print(fruit)"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "#3."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'apple', 'mango', 'peach', 'cherry'}\n"
     ]
    }
   ],
   "source": [
    "new_fruits=set(['cherry','peach','apple','mango'])\n",
    "print(new_fruits)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "#4."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'peach', 'cherry'}\n"
     ]
    }
   ],
   "source": [
    "print(new_fruits.difference(fruits))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "#5."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'apple', 'mango'}\n"
     ]
    }
   ],
   "source": [
    "print(fruits.intersection(new_fruits))"
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
