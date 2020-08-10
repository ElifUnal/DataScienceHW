{
 "cells": [
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "1."
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
      "Silmek istediğiniz günü seçiniz:\n",
      "5\n",
      "Seçilen gün silindi: dict_values(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Saturday', 'Sunday'])\n"
     ]
    }
   ],
   "source": [
    "days={1:\"Monday\",2:\"Tuesday\",3:\"Wednesday\",4:\"Thursday\",5:\"Friday\",6:\"Saturday\",7:\"Sunday\"}\n",
    "kontrol=input(\"Silmek istediğiniz günü seçiniz:\\n\")\n",
    "anahtar=int(kontrol)\n",
    "for x in days.keys():\n",
    "    if x==anahtar:\n",
    "        days.pop(x)\n",
    "        break\n",
    "print(\"Seçilen gün silindi:\",days.values())\n"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "2."
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
      "dict_items([('John', (25, ' Male')), ('Lisa', (28, 'Female')), ('Linda', (32, 'Female')), ('Michael', (41, 'Male'))])\n"
     ]
    }
   ],
   "source": [
    "dictionary={\"John\":(25,\" Male\"),\"Lisa\":(28 ,\"Female\"),\"Linda\":(32, \"Female\"),\"Michael\":(41, \"Male\")}\n",
    "print(dictionary.items())"
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
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "dict_items([('John', {'age': 25, 'gender': 'Male'}), ('Lisa', {'age': 28, 'gender': 'Female'}), ('Linda', {'age': 32, 'gender': 'Female', 'child': {'Susan': {'cinsiyet': 'Female', 'age': 6}}}), ('Michael', {'age': 41, 'gender': 'Male', 'child': {'Karen': {'cinsiyet': 'Female', 'age': 12}, 'Greg': {'cinsiyet': 'Male', 'age': 7}}})])\n"
     ]
    }
   ],
   "source": [
    "calisanveCocuk = {\n",
    "        \"John\":{\n",
    "            \"age\":25,\n",
    "            \"gender\":\"Male\"\n",
    "        },\"Lisa\":{\n",
    "            \"age\":28,\n",
    "            \"gender\":\"Female\"\n",
    "        },\"Linda\":{\n",
    "            \"age\":32,\n",
    "            \"gender\":\"Female\",\n",
    "         \"child\":{\n",
    "            \"Susan\":{\n",
    "                \"cinsiyet\":\"Female\", \n",
    "                \"age\":6\n",
    "                    },\n",
    "                }\n",
    "        },\"Michael\":{\n",
    "            \"age\":41,\n",
    "            \"gender\":\"Male\",\n",
    "        \"child\":\n",
    "        {\n",
    "            \"Karen\":{\n",
    "                \"cinsiyet\":\"Female\",\n",
    "                \"age\":12\n",
    "                \n",
    "            },\n",
    "            \"Greg\":{\n",
    "                \"cinsiyet\":\"Male\",\n",
    "                \"age\":7\n",
    "        }\n",
    "        }\n",
    "            }\n",
    "}\n",
    "print(calisanveCocuk.items())"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "4."
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
      "Michael's childs:  {'Karen': {'cinsiyet': 'Female', 'age': 12}, 'Greg': {'cinsiyet': 'Male', 'age': 7}}\n"
     ]
    }
   ],
   "source": [
    "calisanveCocuk = {\n",
    "        \"John\":{\n",
    "            \"age\":25,\n",
    "            \"gender\":\"Male\"\n",
    "        },\"Lisa\":{\n",
    "            \"age\":28,\n",
    "            \"gender\":\"Female\"\n",
    "        },\"Linda\":{\n",
    "            \"age\":32,\n",
    "            \"gender\":\"Female\",\n",
    "         \"child\":{\n",
    "            \"Susan\":{\n",
    "                \"cinsiyet\":\"Female\", \n",
    "                \"age\":6\n",
    "                    },\n",
    "                }\n",
    "        },\"Michael\":{\n",
    "            \"age\":41,\n",
    "            \"gender\":\"Male\",\n",
    "        \"child\":\n",
    "        {\n",
    "            \"Karen\":{\n",
    "                \"cinsiyet\":\"Female\",\n",
    "                \"age\":12\n",
    "                \n",
    "            },\n",
    "            \"Greg\":{\n",
    "                \"cinsiyet\":\"Male\",\n",
    "                \"age\":7\n",
    "        }\n",
    "        }\n",
    "            }\n",
    "}\n",
    "print(\"Michael's childs: \",calisanveCocuk[\"Michael\"][\"child\"])"
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
