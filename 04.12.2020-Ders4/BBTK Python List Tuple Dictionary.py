{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Created on Thu. Dec 4 20:04:00 2020\n",
    "#@author: Aydın CESUR"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'carrot'"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list1 = [ \"apple\",\"carrot\",2020,3.14]\n",
    "list2 = [1,2,3,4,5]\n",
    "list3 = [\"a\",\"b\",\"c\",\"d\"]"
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
      "apple\n",
      "[2, 3]\n",
      "['a', 'b', 'c', 'd']\n"
     ]
    }
   ],
   "source": [
    "print(list1[0])\n",
    "print(list2[1:3])\n",
    "print(list3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['apple', 'carrot', 2021, 3.14]\n"
     ]
    }
   ],
   "source": [
    "list1[2] = 2021\n",
    "print(list1)"
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
      "[1, 2, 3, 4]\n"
     ]
    }
   ],
   "source": [
    "del list2[4]\n",
    "print(list2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(list3)"
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
      "['Aydın', 'BBTK', 1, 2, 3]\n"
     ]
    }
   ],
   "source": [
    "list1 = [\"Aydın\",\"BBTK\"]\n",
    "list2 = [1,2,3]\n",
    "list3 = list1 + list2\n",
    "print(list3)"
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
      "['Hello', 'Hello', 'Hello', 'Hello']\n"
     ]
    }
   ],
   "source": [
    "list1 = [\"Hello\"]\n",
    "list1 = list1 * 4\n",
    "print(list1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "False\n"
     ]
    }
   ],
   "source": [
    "list3 = [\"a\",\"b\",\"c\",\"d\"]\n",
    "print('a' in list3)\n",
    "print(\"aydın\" in list3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "68.2\n"
     ]
    }
   ],
   "source": [
    "notlar = [80,75,24,100,62]\n",
    "sum = 0\n",
    "for i in range(0,len(notlar)):\n",
    "    sum += notlar[i]\n",
    "sum /= len(notlar)\n",
    "print(sum)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "100\n",
      "24\n"
     ]
    }
   ],
   "source": [
    "notlar = [80,75,24,100,62]\n",
    "print(max(notlar))\n",
    "print(min(notlar))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "'<' not supported between instances of 'int' and 'str'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-23-244b71aa9453>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[0mlist1\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;33m[\u001b[0m \u001b[1;34m\"apple\"\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;34m\"carrot\"\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m2020\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m3.14\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[0mmin\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mlist1\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m: '<' not supported between instances of 'int' and 'str'"
     ]
    }
   ],
   "source": [
    "list1 = [ \"apple\",\"carrot\",2020,3.14]\n",
    "min(list1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2, 3, 4, 5, 'Aydın']\n"
     ]
    }
   ],
   "source": [
    "list2 = [1,2,3,4,5]\n",
    "list2.append(\"Aydın\")\n",
    "print(list2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n",
      "3\n"
     ]
    }
   ],
   "source": [
    "list4 = [\"1\",\"1\",\"1\",\"2\",1,2,3,\"aydın\"]\n",
    "\n",
    "count = 0\n",
    "for i in list4:\n",
    "    if i == \"1\":\n",
    "        count += 1\n",
    "print(count)\n",
    "print(list4.count(\"1\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Aydın', 'BBTK', 1, 2, 3]\n"
     ]
    }
   ],
   "source": [
    "list1 = [\"Aydın\",\"BBTK\"]\n",
    "list2 = [1,2,3]\n",
    "list1 += list2\n",
    "list1.extend(list2)\n",
    "print(list1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list1 = [\"Aydın\",\"Python\",\"Mine\",\"BBTK\"]\n",
    "list1.index(\"Mine\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Aydın', 'BBTK', 'Mine', 'Python']\n"
     ]
    }
   ],
   "source": [
    "list1 = [\"Aydın\",\"Python\",\"Mine\",\"BBTK\"]\n",
    "list1.sort()\n",
    "print(list1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Aydın', 'Mine', 'BBTK', 20]\n",
      "Python\n"
     ]
    }
   ],
   "source": [
    "list2 = [\"Aydın\",\"Python\",\"Mine\",\"BBTK\",20]\n",
    "cikan = list2.pop(1)\n",
    "print(list2)\n",
    "print(cikan)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Aydın', 'Python', 'BBTK', 20]\n"
     ]
    }
   ],
   "source": [
    "list2 = [\"Aydın\",\"Python\",\"Mine\",\"BBTK\",20]\n",
    "list2.pop(list2.index(\"Mine\"))\n",
    "print(list2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Python', 'Mine', 'BBTK', 'Aydın']\n"
     ]
    }
   ],
   "source": [
    "list2 = [\"Aydın\",\"Python\",\"Mine\",\"BBTK\"]\n",
    "list2.sort()\n",
    "list2.reverse()\n",
    "print(list2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Sayı girin78\n",
      "Sayı girin4\n",
      "Sayı girin65\n",
      "Sayı girin21\n",
      "Sayı girin3\n",
      "Sayı girin-89\n",
      "Sayı girin74\n",
      "Sayı girin25\n",
      "Sayı girin0\n",
      "-89\n",
      "3\n",
      "4\n",
      "21\n",
      "25\n",
      "65\n",
      "74\n",
      "78\n"
     ]
    }
   ],
   "source": [
    "i = 1\n",
    "list1 = []\n",
    "while i != 0:\n",
    "    i = int(input(\"Sayı girin\"))\n",
    "    list1.append(i)\n",
    "list1.pop()\n",
    "list1.sort()\n",
    "for i in list1:\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "GPA\n"
     ]
    }
   ],
   "source": [
    "tup1 = (14,25,\"Aydın\",\"Python\")\n",
    "ogrenci_bilgisi = (\"Adı\",\"Numara\",\"GPA\",\"Deneme\")\n",
    "print(ogrenci_bilgisi[-2])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'tup1' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-61-aed842374e0c>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;32mdel\u001b[0m \u001b[0mtup1\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mtup1\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m: name 'tup1' is not defined"
     ]
    }
   ],
   "source": [
    "del tup1\n",
    "print(tup1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(1, 2, 3, 'Aydın', 'Mine')\n"
     ]
    }
   ],
   "source": [
    "tup1 = (1,2,3)\n",
    "tup2 = (\"Aydın\",\"Mine\")\n",
    "tup3 = ()\n",
    "tup1 = tup1 + tup2\n",
    "print(tup1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "BBTKBBTKBBTKBBTK\n"
     ]
    }
   ],
   "source": [
    "tup1 = (\"BBTK\")\n",
    "tup1 *= 4\n",
    "print(tup1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'list'>\n",
      "<class 'tuple'>\n"
     ]
    }
   ],
   "source": [
    "ogrenci_bilgisi = [\"Adı\",\"Numara\",\"GPA\",\"Deneme\"]\n",
    "print(type(ogrenci_bilgisi))\n",
    "ogrenci_bilgisi_tup = tuple(ogrenci_bilgisi)\n",
    "del ogrenci_bilgisi\n",
    "print(type(ogrenci_bilgisi_tup))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'tuple'>\n",
      "<class 'list'>\n"
     ]
    }
   ],
   "source": [
    "ogrenci_bilgisi = (\"Adı\",\"Numara\",\"GPA\",\"Deneme\")\n",
    "print(type(ogrenci_bilgisi))\n",
    "ogrenci_bilgisi_list = list(ogrenci_bilgisi)\n",
    "del ogrenci_bilgisi\n",
    "print(type(ogrenci_bilgisi_list))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'Name': 'Aydın', 'Age': 22, 'Class': 3, 'Notlar': [100, 25, 30]}\n"
     ]
    }
   ],
   "source": [
    "person = {\"Name\" : \"Aydın\",\"Age\" : 22,\"Class\" : 3, \"Notlar\" : [100,25,30]}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Aydın\n"
     ]
    }
   ],
   "source": [
    "print(person[\"Name\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[100, 25, 30]\n"
     ]
    }
   ],
   "source": [
    "print(person[\"Notlar\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[100, 25, 30, 75]\n"
     ]
    }
   ],
   "source": [
    "person[\"Notlar\"].append(75)\n",
    "print(person[\"Notlar\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'Name': 'Aydın', 'Age': 23, 'Class': 3, 'Notlar': [100, 25, 30, 75], 'Club': 'BBTK'}\n"
     ]
    }
   ],
   "source": [
    "person[\"Age\"] = 23\n",
    "person[\"Club\"] = \"BBTK\"\n",
    "print(person)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'Name': 'Aydın', 'Age': 23, 'Class': 3, 'Notlar': [100, 25, 30, 75]}\n",
      "{}\n"
     ]
    },
    {
     "ename": "NameError",
     "evalue": "name 'person' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-80-92448278cd27>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mperson\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[1;32mdel\u001b[0m \u001b[0mperson\u001b[0m \u001b[1;31m# delete entire dictionary\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 6\u001b[1;33m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mperson\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;31m# returns error\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m: name 'person' is not defined"
     ]
    }
   ],
   "source": [
    "del person['Club'] #remove entry with key 'Club'\n",
    "print(person)\n",
    "person.clear() #remove all entries in dict\n",
    "print(person)\n",
    "del person # delete entire dictionary\n",
    "print(person) # returns error\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5"
      ]
     },
     "execution_count": 81,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "person = {'Name': 'Aydın', 'Age': 23, 'Class': 3, 'Notlar': [100, 25, 30, 75], 'Club': 'BBTK'}\n",
    "len(person)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'Name': 'Aydın', 'Age': 23, 'Class': 3, 'Notlar': [100, 25, 30, 75], 'Club': 'BBTK'}\n",
      "{'Name': 'Aydın', 'Age': 23, 'Class': 3, 'Notlar': [100, 25, 30, 75], 'Club': 'BBTK'}\n"
     ]
    }
   ],
   "source": [
    "print(person)\n",
    "print(str(person))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'dict'>\n",
      "{'Name': 'Aydın', 'Age': 23, 'Class': 3, 'Notlar': [100, 25, 30, 75], 'Club': 'BBTK'}\n"
     ]
    }
   ],
   "source": [
    "person2 = person.copy()\n",
    "print(type(person2))\n",
    "print(person2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'Adı': None, 'Soyadı': None, 'Numarası': None}\n"
     ]
    }
   ],
   "source": [
    "degerler = (\"Adı\",\"Soyadı\",\"Numarası\")\n",
    "person = dict.fromkeys(degerler)\n",
    "print(person)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "metadata": {},
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "'dict' object has no attribute 'has_key'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-97-3ca051b964ef>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[0mdegerler\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;33m(\u001b[0m\u001b[1;34m\"Adı\"\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;34m\"Soyadı\"\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;34m\"Numarası\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[0mperson\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mdict\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfromkeys\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mdegerler\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m10\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 3\u001b[1;33m \u001b[0mperson\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mhas_key\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"Adı\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      4\u001b[0m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mperson\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mAttributeError\u001b[0m: 'dict' object has no attribute 'has_key'"
     ]
    }
   ],
   "source": [
    "degerler = (\"Adı\",\"Soyadı\",\"Numarası\")\n",
    "person = dict.fromkeys(degerler,10)\n",
    "print(person)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "22\n",
      "None\n",
      "22\n"
     ]
    }
   ],
   "source": [
    "person = {'Name': 'Aydın','Age': 22,'Class': 3}\n",
    "print(person.get('Age'))\n",
    "print(person.get('Club'))\n",
    "print(person.get('Club',\"Any club matched not found\"))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "metadata": {},
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "'dict' object has no attribute 'has_key'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-96-04da2fe472e3>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[0mperson\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;33m{\u001b[0m\u001b[1;34m'Name'\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;34m'Aydın'\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;34m\"Age\"\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m22\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;34m'Class'\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m3\u001b[0m\u001b[1;33m}\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[0mperson\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mhas_key\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"Age\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      3\u001b[0m \u001b[0mperson\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mhas_key\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'Club'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mAttributeError\u001b[0m: 'dict' object has no attribute 'has_key'"
     ]
    }
   ],
   "source": [
    "person = {'Name': 'Aydın',\"Age\": 22,'Class': 3}\n",
    "person.has_key(\"Age\")\n",
    "person.has_key('Club')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dict_items([('Adı', 10), ('Soyadı', 10), ('Numarası', 10)])"
      ]
     },
     "execution_count": 99,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "person.items()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dict_keys(['Adı', 'Soyadı', 'Numarası'])"
      ]
     },
     "execution_count": 100,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "person.keys()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 104,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'Soyadı': 10, 'Numarası': 10, 'Cinsiyeti': 'Belirtmedi', 'Adı': 'Firdevs'}\n"
     ]
    }
   ],
   "source": [
    "person.setdefault(\"Cinsiyeti\",\"Belirtmedi\")\n",
    "del person[\"Adı\"]\n",
    "person.setdefault(\"Adı\",\"Firdevs\")\n",
    "print(person)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 106,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'Sex': 'male', 'Name': 'Aydın', 'Age': 22, 'Class': 3}\n"
     ]
    }
   ],
   "source": [
    "person = {'Name': 'Aydın','Age': 22,'Class': 3}\n",
    "person_extra = {'Sex': 'male'}\n",
    "person.update(person_extra)\n",
    "person_extra.update(person)\n",
    "print(person_extra)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 107,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dict_values(['Aydın', 22, 3])"
      ]
     },
     "execution_count": 107,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "person.values()"
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
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
