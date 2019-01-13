# Rocket Camera Module Rotation and Image Capture
### Python script used on a Raspberry Pi contained within a high-powered rocket to automate a camera module's capture of a horizontal panoramic image

![UW Fox Valley Collegiate Rocketry Launch team](https://i.imgur.com/4QADz7q.jpg)
The UW Fox Valley Collegiate Rocketry Launch (CRL) competition team posing in front of the rocket after its final launch.

---

#### Purpose
The Wisconsin Space Grant Consortium (WSGC) hosts the CRL for Wisconsin universities to have an oportunity to design, build, test, and launch high-powered rockets in a controlled environment. Under supervision by professional rocketeers, students were required to submit reports updating the current status of the build, and were provided opportunities to test launch prior to the competition.

#### Objective
The WSGC's 2017-2018 CRL objective was to have the rocket reach an apogee of 3,000ft, land safely, and take a horizontal panoramic image of its landing site. The process has to be completely automated without interference, and individual photos can be stitched together after landing.

#### Design
The 3D-printed camera module was mounted on top of the booster section of the rocket, shielded until the rocket reached apogee. After the rocket lands, the Raspberry Pi is timed to begin its duty. The Raspberry Pi was configured to automatically launch this script after it completes it's boot process.

#### Implementation of the software
A pulse width modulation activated continuous servo motor rotates the entire module, intermittently stopping once every eighth of a rotation due to a compination of a geneva mechanism and a microswitch connected to the RPi's GPIO. When the script is running, the Raspberry Pi continuously loops until a signal is received from the microswitch. If the module successfuly advanced from its previous state and made a complete stop, the Pi takes a photo, save it into a directory appending the photo number via string formatting, and activates the servo motor until the next node is reached.

#### Results
UW Fox Valley won first place in the completition, winning 1st two back-to-back years. The team presented their rocket at the WSGC Space Conference in August 2018.

![UW Fox Valley rocket launching from the launchpad](https://i.imgur.com/boaqDUq.jpg)

#### Note
There are tons of information reguarding the design and build of the rocket omitted of overly simplified. This repo focuses on simply the source code of the camera module, disregarding the engineering process behing designing and building the custom rocket. Many details for the camera module additionally were simplified. 