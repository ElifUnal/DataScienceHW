{
 "cells": [
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "# 1. Suppose you invested in Bitcoin at the end of 2017 when Bitcoin gained a lot of value. What would be your money at the end of a week if you had invested $1000 with an average daily increase of 12\\% ? You can solve the problem using Python"
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
      "1840.0\n"
     ]
    }
   ],
   "source": [
    "capital=1000\n",
    "oran=12/100\n",
    "hesap=capital+((capital*oran)*7)\n",
    "print(hesap)"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "# 2. Print the text in quotes with Python. However, you must get the numbers from variables using .format() notation.\n",
    "Because the text is long, you might consider writing in two lines:\n",
    "\n",
    " `\"When we buy bitcoin with 1000 USD at the beginning of the week, we would earn 1210.68 USD at the end of the week, with an average gain of 12\\%.\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "When we buy bitcoin with 1000 USD at the beginning of the week, we would earn 1210.68 USD at the end of the week, with an average gain of 12\\%.\"`\n"
     ]
    }
   ],
   "source": [
    "miktar=1000\n",
    "oran=12\n",
    "gain=1210.68\n",
    "text=\"When we buy bitcoin with {} USD at the beginning of the week, we would earn {} USD at the end of the week, with an average gain of {}\\\\%.\\\"`\"\n",
    "print(text.format(miktar,gain,oran))"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "# 3. Get the temperature in Fahrenheit from user and write a code to convert it to Celcius. For conversion, you can use this formula: C = (5/9) * (F - 32)\n"
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
      "Fahreneit değerini giriniz26\n",
      "Temperature(C): -3.3333333333333335\n"
     ]
    }
   ],
   "source": [
    "deger=input(\"Fahreneit değerini giriniz\")\n",
    "F=int(deger)\n",
    "C = (5/9) * (F - 32)\n",
    "print(\"Temperature(C):\",C)"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "#4. Get a three digit number the from user and calculate the sum of the digits in the integer."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the number:\n",
      "365\n",
      "The sum of digits in the number is:  14\n"
     ]
    }
   ],
   "source": [
    "deger=input(\"Enter the number:\\n\")\n",
    "sayi=int(deger)\n",
    "c=sayi%10\n",
    "sayi/=10\n",
    "b=int(sayi%10)\n",
    "a=int (sayi/10)\n",
    "toplam=a+b+c\n",
    "print(\"The sum of digits in the number is: \",toplam)"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "#5. Write some code to calculate the hypotenuse of a right angled triangle. Get the side lengths from the user."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "First side length:\n",
      "6\n",
      "Second side length\n",
      "8\n",
      "The length of the hypotenuse is 10.0\n"
     ]
    }
   ],
   "source": [
    "deger=input(\"First side length:\\n\")\n",
    "a=int(deger)\n",
    "deger2=input(\"Second side length\\n\")\n",
    "b=int(deger2)\n",
    "hipotenus=(a**2+b**2)**0.5\n",
    "print(\"The length of the hypotenuse is\",hipotenus)"
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
