# Simple Smart Hub 

This is my final year IoT project — a smart home system that controls lights and fans based on time, temperature, and whether someone is in the room. It uses an ESP32 (simulated in Wokwi), a FastAPI backend, and a simple web interface to control everything.

---

## What It Does

- **Time-based lighting**: Turns lights on/off at scheduled times. Allows users to schedule lights to turn on at a fixed time or at sunset, with an automatic shutoff after a custom duration.

- **Temperature-based fan control**: Turns the fan on if it’s hot, off if it’s cool. Automatically turns the fan ON/OFF based on the temperature value received from the ESP32 and the threshold set by the user.

- **Motion detection**: Uses a motion sensor to know if someone’s in the room. 

- **Web control**: Change settings and see sensor data from a webpage.

- **ESP32 (Wokwi)**: All hardware is simulated using Wokwi’s online tools.

-  **Sensor Data Logging**  
  Stores a history of temperature and motion data to be used for graph plotting and analysis.

-  **Custom User Settings**  
  Users can configure the system with their own preferred temperature threshold and lighting time via API requests.

-  **CORS Support**  
  Fully accessible from browser-based frontends and Postman thanks to wide-open CORS policy. CORS stands for Cross-Origin Resource Sharing. It's a security feature implemented by web browsers to control how resources (like APIs) can be requested from a different domain, port, or protocol than the one the web page was served from.



## Initially I was using the PCB however upon arrival in the US I realized I never had the fan so I had to improvised and struggled through wokwi. anywho I survived made it to the finish line. 


A little off topic: 
I also want to say thank you sir, for your reception for the course.Thank you for your overall reception and understanding, correction and reassurance when I misplaced and misinterpreted your actions as neglect when it was wholey push so that I could grow and become better. I can say what we spoke about, where I told you my reason for my paranoia lmao best believe he has made his way back into course and now at this present moment I almost never write this readme file as lol the grades are out and somehow again my maths script is missing again lol so yea rep rep.... Thank you for all that you have seen in me best believe I have lost myself in this abuse and harassment since 2023 and completelky this year since things has just been out of control though they say he is fired, I am exposed now to lol every discipline and now the first years know because of a stunt they pulled in math presentation. So sir it has been rufffffaaaaa since April. However, I remember your words and I know your expectations and so yea rep rep rep with tears and in the depression I still had to pull through so thank you for your words thank you for your beliefs lol mi a come to you wid mi capstone ideas soon lol rep rep please so you can give me your expert advice thanks would also ask if you would and could please please consider being one of my advisors, I would appreciate this please as after all I have been going through at the faculty respectfully mi only trust you, Mr. Mangaroo and Sir. Falconer a try redeem himself lol so theres potential but yea I would really really appreciate this sir thanks.

