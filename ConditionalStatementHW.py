{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Celcius veya Fahrenheit derecesini girin25C\n",
      "25C--> 77.0\n"
     ]
    }
   ],
   "source": [
    "deger=input(\"Celcius veya Fahrenheit derecesini girin\")\n",
    "if deger.endswith(\"C\"):\n",
    "    C=deger.replace(\"C\",\" \")\n",
    "    sayi=int(C)\n",
    "    F=(sayi*1.8)+32\n",
    "    print(deger+\"-->\",F)\n",
    "elif deger.endswith(\"F\"):\n",
    "    F=deger.replace(\"F\",\" \")\n",
    "    sayi=float(F)\n",
    "    C=(5/9)*(sayi-32)\n",
    "    print(deger+\"-->\",round(C,2))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the salary: 2000\n",
      "Enter the year of service: 25\n",
      "Net bonus amount: 100.0\n"
     ]
    }
   ],
   "source": [
    "deger=input(\"Enter the salary: \")\n",
    "deger2=input(\"Enter the year of service: \")\n",
    "maas=int(deger)\n",
    "hzmt=int(deger2)\n",
    "if hzmt>5:\n",
    "    bonus=(maas*5)/100\n",
    "    print(\"Net bonus amount:\",bonus)\n",
    "else:\n",
    "    print(\"Sorry.Year of Service is less than 5 year\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the first number: 65\n",
      "Enter the second number: 78\n",
      "Enter the third number: 14\n",
      "The biggest number:  65\n",
      "The smallest number:  14\n"
     ]
    }
   ],
   "source": [
    "s1=input(\"Enter the first number: \")\n",
    "s1=int(s1)\n",
    "s2=input(\"Enter the second number: \")\n",
    "s2=int(s2)\n",
    "s3=input(\"Enter the third number: \")\n",
    "s3=int(s3)\n",
    "\n",
    "if s1>s2 & s1>s3:\n",
    "    if s2>s3:\n",
    "        enk=s3\n",
    "    else:\n",
    "        enk=s2\n",
    "    enb=s1\n",
    "elif s2>s1 & s2>s3:\n",
    "    if s1>s3:\n",
    "        enk=s3\n",
    "    else:\n",
    "        enk=s1\n",
    "    enb=s2\n",
    "else:\n",
    "    enb=s3\n",
    "    if s2>s1:\n",
    "        enk=s1\n",
    "    else:\n",
    "        enk=s2\n",
    "\n",
    "\n",
    "print(\"The biggest number: \",enb)\n",
    "print(\"The smallest number: \",enk)   "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the number of classes held:\n",
      "20\n",
      "Enter the number of classes attended\n",
      "10\n",
      "The student is not allowed to attend in exam:\n",
      "\n",
      "Percentage of classes attended:  15.0\n"
     ]
    }
   ],
   "source": [
    "sumC=input(\"Enter the number of classes held:\\n\")\n",
    "attendC=input(\"Enter the number of classes attended\\n\")\n",
    "\n",
    "countCourse=int(sumC)\n",
    "if (countCourse*75)/100 > int(attendC):\n",
    "    print(\"The student is not allowed to attend in exam:\\n\")  \n",
    "else:\n",
    "    print(\"The student is allowed to attend in exam:\\n\")\n",
    "print(\"Percentage of classes attended: \",(countCourse*75)/100 )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter a letter of the alphabet: r\n",
      "r is a consonant\n"
     ]
    }
   ],
   "source": [
    "a=input(\"Enter a letter of the alphabet: \")\n",
    "if a==\"a\" or a==\"e\" or a==\"i \"or a==\"o\" or a==\"u\":\n",
    "    print(a,\"is a vowel\")\n",
    "elif a==\"y\":\n",
    "    print(a,\"is sometimes a vowel and sometimes a consonant\")\n",
    "else:\n",
    "    print(a,\"is a consonant\")"
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
