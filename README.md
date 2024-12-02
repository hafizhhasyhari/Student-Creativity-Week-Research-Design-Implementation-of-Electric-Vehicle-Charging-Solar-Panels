# Student-Creativity-Week-Research-Design-Implementation-of-Electric-Vehicle-Charging-Solar-Panels 2024/2025
Student Creativity Week Research Title Design and Implementation of Electric Vehicle Charging System Using Solar Panels

2 September 2024 
## Anggota Tim :
Hafizh HIlman Asyhari
Rakha Nugroho
Putra Nias

## Arsitektur Sistem
Client Layer: Antarmuka pengguna desktop (Tkinter).
Middleware Layer: Manajemen logika menggunakan Python OOP.
Hardware Layer: Arduino atau Raspberry Pi untuk mengontrol perangkat keras.


## Diagram Sistem
UML High-Level
Class Diagram:
Robot: Mengatur operasi utama robot.
TaskManager: Implementasi stack dan queue untuk antrian tugas dan riwayat perintah.
DatabaseManager: Mengelola koneksi dan operasi basis data.
HardwareController: Berinteraksi dengan mikrokontroler (Arduino, Raspberry Pi).
Relasi:
Robot memiliki hubungan dengan TaskManager, DatabaseManager, dan HardwareController.
