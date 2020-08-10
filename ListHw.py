{
 "cells": [
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "#1. Write a code to compute the sum of the two lowest numbers and the two highest numbers in the following list.\n",
    "\n",
    " my_list = [34, 56, 76, 45, 2, 12, 67, 98, 37, 54, 66]"
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
      "Sıralanan liste: [2, 12, 34, 37, 45, 54, 56, 66, 67, 76, 98]\n",
      "Two longest sum:\n",
      " 14\n",
      "Two biggest sum:\n",
      " 174\n"
     ]
    }
   ],
   "source": [
    "my_list = [34, 56, 76, 45, 2, 12, 67, 98, 37, 54, 66]\n",
    "my_list.sort()\n",
    "print(\"Sıralanan liste:\",my_list)\n",
    "two_longest_sum=my_list[0]+my_list[1]\n",
    "two_biggest_sum=my_list[9]+my_list[10]\n",
    "print(\"Two longest sum:\\n\",two_longest_sum)\n",
    "print(\"Two biggest sum:\\n\",two_biggest_sum)"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "2.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "David   99\n",
      "Michael   87\n",
      "John   78\n",
      "James   86\n",
      "Greg   68\n",
      "Mark   94\n",
      "William   76\n",
      "Richard   97\n",
      "Thomas   56\n",
      "Steven   98\n",
      "Mary   76\n",
      "Susan   87\n",
      "Maria   79\n",
      "Karen   90\n",
      "Lisa   73\n",
      "Linda   93\n",
      "Donna   82\n",
      "Patricia   69\n",
      "Debra   97\n",
      "Eric   98\n"
     ]
    }
   ],
   "source": [
    "names = [\"David\", \"Michael\", \"John\",\"James\",\"Greg\",\"Mark\",\"William\",\"Richard\",\"Thomas\", \"Steven\",\"Mary\",\"Susan\",\"Maria\",\"Karen\",\"Lisa\", \"Linda\", \"Donna\", \"Patricia\", \"Debra\",\"Eric\"]\n",
    "scores = [99, 87, 78, 86, 68, 94, 76, 97, 56, 98, 76, 87, 79, 90, 73, 93, 82, 69, 97, 98]\n",
    "students=[names,scores]\n",
    "i=0\n",
    "while i<20:\n",
    "    print(students[0][i],\" \",students[1][i])\n",
    "    i+=1\n",
    "    "
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "3."
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "4.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "January 31\n",
      "February 29\n",
      "March 31\n",
      "April 30\n",
      "May 31\n",
      "June 30\n",
      "July 31\n",
      "August 31\n",
      "September 30\n",
      "October 31\n",
      "November 30\n",
      "December 31\n"
     ]
    }
   ],
   "source": [
    "Months= [ 'January', 'February','March', 'April', 'May','June', 'July', 'August','September', 'October', 'November','December']\n",
    "count_of_day=[31,29,31,30,31,30,31,31,30,31,30,31]\n",
    "months_of_days=[Months,count_of_day]\n",
    "i=0\n",
    "while i<12:\n",
    "    print(months_of_days[0][i],months_of_days[1][i])\n",
    "    i=i+1"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "5."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "March 31\n",
      "April 30\n",
      "May 31\n",
      "June 30\n",
      "July 31\n",
      "August 31\n",
      "September 30\n",
      "October 31\n",
      "November 30\n",
      "December 31\n",
      "January 31\n",
      "February 29\n"
     ]
    }
   ],
   "source": [
    "months_by_season = [['March', 'April', 'May'],['June', 'July', 'August'],['September', 'October', 'November'],['December', 'January', 'February']]\n",
    "count_of_days=[[31,30,31],[30,31,31],[30,31,30],[31,31,29]]\n",
    "seasons=['Springs','Summer','Autumn','Winter']\n",
    "i=0\n",
    "while i<4:\n",
    "    j=0\n",
    "    while j<3:\n",
    "        print(months_by_season[i][j],count_of_days[i][j])\n",
    "        \n",
    "        j+=1\n",
    "    i+=1"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "6."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "June 30\n",
      "July 31\n",
      "August 31\n",
      "Sum of summer season days: 92\n"
     ]
    }
   ],
   "source": [
    "months_by_season = [['March', 'April', 'May'],['June', 'July', 'August'],['September', 'October', 'November'],['December', 'January', 'February']]\n",
    "count_of_days=[[31,30,31],[30,31,31],[30,31,30],[31,31,29]]\n",
    "j=0\n",
    "count=0\n",
    "while j<3:\n",
    "    print(months_by_season[1][j],count_of_days[1][j])\n",
    "    count+=count_of_days[1][j]\n",
    "    j+=1\n",
    "print(\"Sum of summer season days:\",count)"
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
