{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Please Enter Student's Attribute:Name\n",
      "Please Enter Student's Attribute:Age\n",
      "Please Enter Student's Attribute:Sex\n"
     ]
    }
   ],
   "source": [
    "#Creta a dictionary as student\n",
    "student = {}\n",
    "#The keys(3) for the student are received from the user\n",
    "seq = []\n",
    "for i in range (0,3):\n",
    "    seq.append(input(\"Please Enter Student's Attribute:\"))\n",
    "#Set the dictionary's default values to none\n",
    "student = dict.fromkeys(seq)\n",
    "student.setdefault(seq[0],None)\n",
    "student.setdefault(seq[1],None)\n",
    "student.setdefault(seq[2],None)\n",
    "#Add the GPA key to the student dictionary\n",
    "#Set the GPA's default values to 0\n",
    "student.setdefault('GPA',0)\n",
    "seq.append('GPA')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Please Enter How Many Student in School5\n",
      "Student0 Name :Aydın\n",
      "Student0 Age :22\n",
      "Student0 Sex :Male\n",
      "Student0 GPA :2.7\n",
      "Student1 Name :Mine\n",
      "Student1 Age :21\n",
      "Student1 Sex :Female\n",
      "Student1 GPA :3.2\n",
      "Student2 Name :Arda\n",
      "Student2 Age :22\n",
      "Student2 Sex :Male\n",
      "Student2 GPA :3.4\n",
      "Student3 Name :Emre\n",
      "Student3 Age :22\n",
      "Student3 Sex :Male\n",
      "Student3 GPA :3.9\n",
      "Student4 Name :Melis\n",
      "Student4 Age :Female\n",
      "Student4 Sex :Female\n",
      "Student4 GPA :2.2\n"
     ]
    }
   ],
   "source": [
    "#Create an empty list of school for holding students\n",
    "School = []\n",
    "#Get how many student enrollments will be from the user.\n",
    "stu_number = int(input(\"Please Enter How Many Student in School\"))\n",
    "#Get student information from user\n",
    "for i in range(0,stu_number): #Okuldaki öğrenci sayısı kadar döner\n",
    "    for j in range(0,len(student.keys())): #Sözlükteki key sayısı kadar döner\n",
    "        r = input(\"Student{} {} :\".format(i,seq[j])) #Kullanıcıdan Key-Value değerleri alınır.\n",
    "        student[seq[j]] = r # Alınan değer sözlüğü kaydedilir\n",
    "    stu_copy = student.copy() # Oluşturulan sözlüğün bir kopyası edinilir\n",
    "    School.append(stu_copy)# Oluşturulan kopya school listesine eklenir."
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
      "[2.7, 3.2, 3.4, 3.9, 2.2]\n",
      "3.0800000000000005\n"
     ]
    }
   ],
   "source": [
    "#Keep students' GPA information in a new list\n",
    "GPAS = []\n",
    "for stu in School: #Okuldaki her öğrenci için öder. stu = okuldaki öğrenci\n",
    "    GPAS.append(float(stu['GPA'])) #öğrencinin GPA değerini GPAS listesine ekler\n",
    "print(GPAS)\n",
    "#Calculate the average GPA of the class\n",
    "avg = 0 # ortalama hesaplamak için avg değişkeni oluşturuldu\n",
    "for note in GPAS: # GPAS listesindeki notları döndürür\n",
    "    avg += note # GPAS daki notlar ortalamayla toplanır\n",
    "avg /= len(GPAS)# Toplam not not sayısına bölünür\n",
    "print(avg)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2.2\n",
      "3.9\n"
     ]
    }
   ],
   "source": [
    "#listedik min max notlar bulunur\n",
    "print(min(GPAS))\n",
    "print(max(GPAS))"
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
      "{'Name': 'Melis', 'Age': 'Female', 'Sex': 'Female', 'GPA': '2.2'}\n",
      "{'Name': 'Emre', 'Age': '22', 'Sex': 'Male', 'GPA': '3.9'}\n"
     ]
    }
   ],
   "source": [
    "#Print the most successful and the least successful student information on the screen\n",
    "print(School[GPAS.index(min(GPAS))])\n",
    "#min(GPAS) en düşük notu bulur\n",
    "#GPAS.index[min(GPAS)] en düşük nota sahip kişinin indexini bulur\n",
    "#School[GPAS.index(min(GPAS))] bulununan index ile okuldaki sözlüğe(öğrenci bilgisine) erişirilir\n",
    "#print(School[GPAS.index(min(GPAS))]) öğrenci bilgisini yazdırır\n",
    "print(School[GPAS.index(max(GPAS))])\n",
    "#yukarıdaki işlemler burada da tekrarlanır"
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
