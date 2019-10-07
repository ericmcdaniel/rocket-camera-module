# Rocket Camera Module Rotation and Image Capture
### A Raspberry Pi powered Python script embedded within the camera module of a student-built high-powered rocket to automate the rotation and capture a horizontal panoramic image of the landing site.



![UW Fox Valley Collegiate Rocketry Launch team](https://i.imgur.com/4QADz7q.jpg)
<center><i>Image 1. Students from the University of Wisconsin - Fox Valley competing in the Wisconsin Space Grant Consortium's (WSGC) Collegiate Rocketry Launch (CRL) competition group recover the rocket after its third and final launch on April 21st, 2018.</i></center>


[The UW Oshkosh Today published an article detailing the CRL and UW Fox Valley's extraordinary achievement, which can be viewed here.](https://uwosh.edu/today/70366/uwfox-team-repeats-first-place-finish-in-statewide-rocket-launch-competition/) In addition, the team received recognition on local news broadcast, at the 28th annual Wisconsin Space Conference, and had even received a handwritten congratulatory card written from our local Wisconsin state Senator Roger Roth.

The official proceedings paper written by the team can be viewed [here directly from the WSGC's website.](https://wsgc.carthage.edu/ojs/index.php/wsc/article/view/264/271) All details concerning the teams goals, the rocket's flight and performance data, test flights, engineering reconsiderations, and the team's methodology are explained in greater detail. This README focuses on the software used by the rocket's camera module.

---

### Purpose
The Wisconsin Space Grant Consortium (WSGC) is an educational outreach program funded by NASA to enhance STEM education in higher education settings, and fund academic research in aerospace and aerospace technology. Every academic year, the WSGC hosts the Collegiate Rocketry Launch (CRL) for Wisconsin universities to have an opportunity to design, build, test, and launch high-powered rockets in a safe and controlled environment. Under rigorous supervision from aerospace professionals, students were required to submit design and build reports updating the staff of each team's current status of the build. Teams were provided opportunities to test launch their rocket prior to the competition on April 21st, 2018.

### Objective
The WSGC's 2017-2018 CRL objective was to have each team's high-powered rocket reach a target apogee of 3,000 feet, land safely using a combination of main and drogue parachutes, and capture a horizontal panoramic image of its landing site. The process was to be completely automated without human intervention, and individual photos taken could be stitched together after landing if they were not already panoramic.

---

## The University of Wisconsin - Fox Valley Rocketeers' Methodology

### Our Design
The 3D-printed camera module was mounted on top of the booster section of the rocket, shielded by the rocket's fiberglass exterior. An altimeter mounted within the avionics bay determined when the target apogee of 3,000 feet was reached, and charges were set that would separate the booster section from the nose cone and remaining bays. The camera module would then be exposed and free to operate. After the rocket would land upright on its carbon fiber tripod legs, the Raspberry Pi embedded within the camera module was timed to begin its duty cycle. The Python script would run immediately after the Pi completed its boot process.

![Electrical schematic of the rocket](https://i.imgur.com/SdGWfzW.jpg)
<center><i>Figure 2. General schematic of the rocket's cohesive electrical systems.

![](https://i.imgur.com/qhMKwtc.jpg)

Figure 3. CAD image of the camera module featuring the Raspberry Pi Zero, the Pi camera, and the continuous servo motor. Under the PLA exterior is a Delrin bearing milled with the Geneva stop to physically rotate the outer cylinder. The Delrin bearing would remain fixed on the rocket's booster section through the rocket's flight.</i></center>

<br>

### Implementation of the software
A pulse-width modulation activated continuous servo motor rotated the entire module, intermittently stopping once every eighth of a rotation. A Geneva mechanism and a microswitch connected to the Pi's GPIO facilitated the physical rotation as well as a physical sensor to determine if rotation had occurred or not. When the script was live, the Raspberry Pi continuously looped until a positive signal was received from the microswitch via a pull-down switch. If the module had successfully advanced from its previous state and made a complete stop, the Pi instructed the Pi Camera to capture a new photo, save it into a directory appending the photo number via string formatting, and activate the servo motor until the next node is reached. This process would repeat until the 24th photo was taken, a number arbitrarily chosen to maximize the chance of capturing eight linear photos that can be stitched with minimal issue.

### Results
The UW Fox Valley Rocketeers successfully presented a seven minute oral presentation at Carthage College on Friday evening, April 20th, 2018, in front of the competing schools and a panel of judges. In the following morning, the team was able to successfully launch and recover the rocket three times, achieving the highest score awarded by the judges throughout the day. UW Fox Valley's first launch apogee was the closest that any competing rocket was able to obtain, reaching 3,041 feet. On July 4th, 2018, WSGC announced UW Fox Valley as the first place winner in the competition, continuing their streak for a second year in a row. The team presented their rocket at the following WSGC Space Conference in August 10th, 2018.

<center><i>

![Rocketeers prepare for oral presentation](https://i.imgur.com/1htcE90.jpg)

Image 4. The UW Fox Valley Rocketeers waits to begin demonstrating their build and performance data for the judges' panel at the oral presentations required for participating CRL competitors.<br>


![UW Fox Valley rocket launching from the launchpad](https://i.imgur.com/boaqDUq.jpg)

Image 5. The rocket's J500G engine launches the rocket with a velocity over several hundred feet per second. Shown here is a view of the rocket nearly impossible to see with the naked eye.

</i></center>

### Conclusion and Disclaimer
There is a plethora of information regarding the design and build of the rocket omitted, making this page overly simplified. This repository focuses on simply the source code of the camera module, disregarding the engineering process behind the design and build the custom rocket. Details of the camera module additionally were simplified. An official copy of the proceedings paper written by the team can be obtained [here directly from the WSGC Space Conference webpage. All details concerning flight and performance data, test flights, engineering reconsiderations, and methodology can be obtained and referenced.](https://wsgc.carthage.edu/ojs/index.php/wsc/article/view/264/271)

#### Contact the Author
Should you wish to contact me for any suggestions, improvements, or comments, you can use GitHub's `@McDanielES` mention system to contact me. I will try to respond as soon as I am available.

I am a second-year computer science student at the University of Wisconsin - Fox Valley. I am learning the fundamentals of programming in Java, Visual Basic.NET, Python, and C++. This program was written primarily for my benefit and to apply the skills learned in class into a real-world context. I am aware that it may not be realistic and often crude or unsophisticated. But <i>live and learn.</i>

You are free to clone, fork, modify and use this application as you please.