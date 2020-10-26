## SENIOR DESIGN PROJECT REPORT

## CSE/EEE/ETE

Communicator for Deaf and Dumb

## SUBMITTED BY

```
Md. Jahid Hasan Naiem ID# 1620266642
Md. Mushfiqur Rahman Bhuiyan ID# 1620379042
MD. Faiyaz Bin Younus ID# 1611073642
```
## SUPERVISOR

```
Dr. Shahnewaz Siddique
Assistant Professor, Department of Electrical and Computer Engineering
North South University, Dhaka, Bangladesh
```
## ELECTRICAL AND COMPUTER ENGINEERING

```
NORTH SOUTH UNIVERSITY
SUMMER 2020
```

Agreement Form

We take great pleasure in submitting our senior design project report on “Communicator for
Deaf and Dumb” This report is prepared as a requirement of the Capstone Design Project
CSE/EEE/ETE 499 A & B which is a two semester long senior design course. This course involves
multidisciplinary teams of students who build and test custom designed systems, components or
engineering processes. We would like to request you to accept this report as a partial fulfilment of
Bachelor of Science degree under Electrical and Computer Engineering Department of North South
University.

## DECLARED BY:

### ......................................................

Name: Md. Jahid Hasan Naiem

## ID:

### ......................................................

Name: Md. Mushfiqur Rahman Bhuiyan

## ID:

### ......................................................

Name: MD. Faiyaz Bin Younus
ID: 1611073642


APPROVAL

The project entitled **“Communicator for Deaf and Dumb”** by Md. Jahid
Hasan Naiem (ID#1620266042), Md. Mushfiqur Rahman Bhuiyan
(ID#1620379042) and MD. Faiyaz Bin Younus is approved in partial
fulfilment of the requirement of the Degree of Bachelor of Science in
Computer Science and Engineering on September and has been accepted as
satisfactory.

## APPROVED BY:

## SUPERVISOR

```
Dr. Shahnewaz Siddique
Assistant Professor, Department of Electrical and Computer Engineering
```
## NORTH SOUTH UNIVERSITY, DHAKA, BANGLADESH

## DR. REZAUL BARI

```
Chair, Department of Electrical and Computer Engineering
North South University, Dhaka, Bangladesh
```

Acknowledgement

First of all, we would like to express our profound gratitude to our honourable course instructor,

Dr. Shahnewaz Siddique ,for his constant and meticulous supervision, valuable suggestions, his
patience and encouragement to complete the thesis work.

We would also like to thank the ECE department of North South University for providing us with the
opportunity to have an industrial level design experience as part of our curriculum for the
undergraduate program.

Finally, we would like to thank our families and everybody who supported us and provided with
guidance for the completion of this project.


[Title of project]

[Abstract]

## DETAILS OF YOUR PROJECT WITH SIGNIFICANCE, IN 10-20 LINES.

Focus general reader, and do not use any abbreviation, write in such a way that a reader from non-
engineering background can get overall idea.


## Table of Contents



- SENIOR DESIGN PROJECT REPORT
- CSE/EEE/ETE
- SUBMITTED BY
- SUPERVISOR
- ELECTRICAL AND COMPUTER ENGINEERING
- DECLARED BY:
- ID:16202666042
- ID:
- ID:
- APPROVED BY:
- SUPERVISOR
- DR. REZAUL BARI
- NORTH SOUTH UNIVERSITY, DHAKA, BANGLADESH
- DETAILS OF YOUR PROJECT WITH SIGNIFICANCE, IN 10-20 LINES.
- CHAPTER 1 PROJECT OVERVIEW
- 1.1 INTRODUCTION
- CHAPTER 2 RELATED WORK
- 2.1 INTRODUCTION
- 2.2 EXISTING WORK RELATED TO SIGN RECOGNITION
- 2.2.1 SIGN LANGUAGE TO SPEECH CONVERSION
- 2.2.2 DEAF TALK USING 3D ANIMATED SIGN LANGUAGE
- 2.3 EXISTING WORK RELATED TO SPEECH RECOGNITION
- 2.3.1 DEAF TALK USING 3D ANIMATED SIGN LANGUAGE
- 2.3.2 SPEECH-TO-THAI SIGN LANGUAGE CONVERSION FOR THAI DEAF: A CASE STUDY OF CRIME NEWS
- 2.3.3
- 2.4 SUMMARY
- CHAPTER 3 THEORY
- 3.1 INTRODUCTION
- 3.2 SPEECH RECOGNITION AND SPEECH TO TEXT CONVERSION
- 3.2.1 GOOGLE SPEECH RECOGNITION
- 3. 3 SIGN LANGUAGE RECOGNITION
- 3.4 ALGORITHM AND MODEL
- 3.4.1 CONVOLUTIONAL NEURAL NETWORK
- 3.4.2 VGG16
- 3.4.3 FINE-TUNING VGG16
- 3.4.4 REGULARIZATION
- 3.4.5 DATA AUGMENTATION
- 3.5 HYPER - PARAMETER
- 3.6 SUMMARY
- CHAPTER 4 DATASET
- 4.1 INTRODUCTION
- 4.2 OUR DATASET
- 4.3 SUMMARY
- CHAPTER 5 STRUCTURE OF THE SYSTEM
- 5.1 INTRODUCTION
- 5.2 SYSTEM DESIGN AND PROCEDURE
- 5.2.1 SPEECH TO TEXT
- 5.2.2 SIGN LANGUAGE TO TEXT
- 5.3 SUMMARY
- CHAPTER 6 USER INTERFACE
- 6.1 SIGN TO TEXT
- 6.2 SIGN LANGUAGE TO TEXT
- 6.3 SUMMARY
- CHAPTER 7 DEVICE AND SOFTWARE
- 7.1 MODULES USED FOR SPEECH RECOGNITION
- 7.2 MODULES USED FOR SIGH LANGUAGE RECOGNITION
- CHAPTER 8 RESULTS AND DISCUSSION
- 8.1 INTRODUCTION
- 8.2 TRAINING RESULT
- 8.2.1 FIRST TRAINING SESSION
- 8.2.2 SECOND TRAINING SESSION
- 8.2. 3 THIRD TRAINING SESSION
- 8.2.4 FINAL TRAINING SESSION
- 8.3 DISCUSSION
- CHAPTER 9 FUTURE WORK
- CHAPTER 10 BIBLIOGRAPHY
- APPENDICES
- APPENDIX A
- APPENDIX B
- APPENDIX C
- FIGURE 1.1 : PREVALENCE OF DISABILITY BY TYPE AND INTENSITY OF DIFFICULTY IN BANGLADESH. Table of Figures
- LOSSES. FIGURE 1.2 ABSOLUTE NUMBER OF PEOPLE IN BANGLADESH SUFFERING FROM VARIOUS EAR DISEASES AND HEARING
- FIGURE 3. 1 WORKING PRINCIPLES OF SPEECH RECOGNITION [9].
- FIGURE 3. 2 CONFIGURATION OF COVNET
- FIGURE 3. 3 OUTPUT AFTER FINE TUNING THE MODEL.
- FIGURE 3. 4 RELU ACTIVATION
- FIGURE 3. 5 CODE FOR EARLYSTOPPING
- FIGURE 3. 6 EARLY STOPPING AFTER 51 EPOCHS
- FIGURE 3. 7 CODE FOR DATA AUGMENTATION
- FIGURE 3. 8 CODE FOR LEARNING RATE REDUCTION
- FIGURE 4. 1 FOLDER STRUCTURE OF THE TRAINING DATASET
- FIGURE 4. 2 EXAMPLES OF DATASET (A – Z AND SPACE)
- FIGURE 5. 1 DIAGRAM OF HOW OUR PROJECT IS GOING TO WORK.
- FIGURE 5. 2 DIAGRAM OF HOW SPEECH TO TEXT IS GOING TO WORK.
- FIGURE 5. 3 HOW WE COLLECTED THE DATASET FOR TRAINING.
- FIGURE 5. 4 HOW THE MACHINE WILL DETECT THE SIGN LANGUAGE.
- FIGURE 6. 1 LAYOUT OF OUR APPLICATION.
- FIGURE 6. 2 RECOGNIZED SPEECH SHOWN AS TEXT IN THE TEXT BOX.
- FIGURE 6. 3 RECOGNIZED SIGN SHOWN IN OUR APPLICATION.............................................................................................................
- FIGURE 8. 1 NUMBER OF IMAGES AND PARAMETERS IN OUR PROJECT FROM SECOND TRAINING SESSION.
- FIGURE 8. 2 NUMBER OF EPOCHS RAN IN SECOND TRAINING..............................................................................................................
- FIGURE 8. 3 LOSS AND ACCURACY CURVE FROM SECOND TRAINING.
- FIGURE 8. 4 NUMBER OF IMAGES, PARAMETERS AND EPOCHS RAN IN OUR PROJECT FROM SECOND TRAINING SESSION.
- FIGURE 8. 5 LOSS AND ACCURACY CURVE FROM THIRD TRAINING.
- FIGURE 8. 6 NUMBER OF IMAGES AND PARAMETERS IN OUR PROJECT FROM FINAL TRAINING SESSION.
- FIGURE 8. 7 NUMBER OF EPOCHS RAN IN FINAL TRAINING.
- FIGURE 8. 8 LOSS AND ACCURACY CURVE FROM FINAL TRAINING.


## CHAPTER 1 PROJECT OVERVIEW

## 1.1 INTRODUCTION

According to disability welfare act of 2001 the definition of disability has been approved as follows:

A person with disability is one who is physically disabled either congenitally or a result of a disease
or being a victim of an accident, or due to improper or maltreatment or for any other reasons has
become physically incapacitated or mentally imbalanced as a result of such disabled ness or one to
mentally impaired ness has become incapacitated, either partially or fully and is unable to lead a normal
life.

Hearing impairment and speech impairment are defined as:

- Persons with a hearing impairment are classified as: Loss of hearing capacity in the better ear
    in the conversation range of frequencies at 40 decibels (hearing unit) or more, or damaged or
    ineffective hearing abilities.
- Persons with a speech impairment are classified as: Loss of one's capacity to utter/pronounce
    meaningful vocabulary sounds, or damaged, partly or wholly or Dysfunctional.

```
Fig
Figure 1. 1 : Prevalence of disability by type and intensity of difficulty in Bangladesh.
```

Millions of people across the world live with disabling hearing loss. Most of them live in low- and
middle-income countries where they often do not have access to appropriate ear and hearing care
services. Without proper care hearing loss poses a significant challenge in the lives of those affected.
There are 466 million people in the world with disabling hearing loss [1]. This is over 5% of the
world’s population. 34 million of them are children. Unless action is taken, by 2030 there will be
nearly 630 million people with disabling hearing loss. By 2050, the number could rise to over 900
million [1].

Unaddressed hearing loss poses an annual global cost of US$ 750 billion [1]. These costs include
health, education and employment sectors as well as the costs which are associated with loss of
productivity. It is estimated that up to five out of every 1000 babies are born with hearing loss or
acquire it soon after birth [1]. Hearing loss can have a significant impact on a child’s development and
educational achievements.

Over 30% of hearing loss in children is caused by diseases such as measles, mumps, rubella, meningitis
and ear infections [1]. It is estimated that up to 330 million people suffer with chronic ear infections
or chronic otitis media globally. If these people are left untreated then its infections lead to hearing
loss and can cause life-threatening complications and mortality.

After a long wait the first national level survey using standard WHO methods to describe the
prevalence of hearing impairment was conducted in Bangladesh in 2013. This study reports that one-
quarter of Bangladeshi people in general suffer from some sort of ear diseases with or without hearing
impairment [2]. One-third of Bangladeshi people suffer from some sort of hearing impairment and one
in ten of them suffer from disabling hearing losses [2]. This magnitude of [3]problem hampers daily
life unless they are corrected.

The only previous study in Bangladesh which was conducted in 2002 that reported a little lower rate
of disabling hearing loss (7.9% versus 9.6% in the current study) [2]. However, the magnitude of any
hearing loss was almost the same (34.2% versus 34.6%) [2]. These two studies conducted in 2002 and
2013 shows that the prevalence of hearing loss remained almost static in the last few years in
Bangladesh.

The study showed a prevalence of hearing impairment similar to Indian population (9.8%). But the
prevalence reported from Sri Lanka (21.7%) and Nepal was higher than Bangladesh [2].


```
Figure 1. 2 Absolute number of people in Bangladesh suffering from various ear diseases and hearing losses.
```
Bangladesh is a country with 142 million population as per 2011 Census. Absolute number of people
suffering from diseases or impairments are given in fig. 1. In terms of numbers it gives us a frightening
figure of the huge suffering of humanity. Some of these figures are larger than the total population of
many countries.

So, to communicate hearing impairment people use sign language and captioning services. Deaf people
often use sign language as a means of communication.

Despite everything, hearing impairment people face a lot of problems. The very first problem is
suppression of ‘Deaf people’ to raise their voice about their academic and social needs. It began in
their family and this suppression continues throughout every sphere in their life including schools,
colleges, community and workplace. Some of the main challenges they face are lack of job
opportunities. Inaccessibility to information in public offices and private firms because most of the
information is available in verbal mode. There is a lack of sign language interpreters and teachers who
know sign language in the education sector.

In our opinion education is the most important right for anyone. But because of the communication
gap between the teachers and these deaf students they never get proper education after a certain stage.
This lack of education is also narrowing down their job opportunities. So, it is quite unfair for them as
a human being. As they are not getting those facilities we get.


## CHAPTER 2 RELATED WORK

## 2.1 INTRODUCTION

In this section, we are going to discuss about the existing works related to sign language to speech
conversion. Here, we are going to observe two different sections, such as, sign language recognition
and another one is speech recognition system. There are lots of work in this field but most of the
existing works converts the sign language gesture/motion into speech and the speech is converted to
text using Text-to-Speech module. We have searched for similar projects there are very few software-
based applications in this area most of the projects are based on hardware implementation, for example,
sensor-based gloves are used for speech recognition system. We also went through many research
papers in order to compare and analyse the algorithm we have used. In our project, we have followed
VGG-16 which is a Convolutional Neural Network and, in many projects, Hidden Markov model and
Support Vector Machine algorithm is used. However, though there are some similarities in existing
solutions but we have followed different methods and built our own dataset.

## 2.2 EXISTING WORK RELATED TO SIGN RECOGNITION

There are some researches based on speech recognition system. Most of the sign recognition system
is based on hardware implementation. The project (Sign Language to Speech Conversion) stated that
there are two categories of gesture recognition system- Vision based system and Sensor based system
[4]. In case of vision-based recognition system a camera is utilized for capturing images of gestures.
Then captured images are processed and from those processed images features are extracted following
specific algorithms which gives the corresponding gesture for particular images. On the other hand,
there is sensor-based recognition system which is more accurate than the vision-based system. The
sensor-based recognition system is invaluable over vision-based framework, since it requires just a
movement sensor as opposed to a camera that makes it as a compact gadget with minimal effort. It
moreover gives quick reaction in perceiving the motions which in turn diminish the computational
time continuously applications. Continuously, acknowledgment pace of 99% can be accomplished
utilizing flex sensor-based recognition system. Here they used Flex sensor, Tactile sensor, Atmega-
328 microcontroller and 3-axis Accelerometer.


Deaf Talk using 3D Animated Sign language uses Microsoft Kinect for windows V2 to convert the
sign language to text and then to speech [5]. Here the gesture and pattern recognition are used to
translate the sign language to speech. For this they used Microsoft technology of “Kinect v2” which
helps to track the motion, depth and gestures. For usage of this module, devices and libraries given by
Microsoft to Kinect improvement have been utilized which incorporate Kinect Studio for signals
recording in explicit designs, Visual Gestures Builder (VGB) for preparing of the motions through
which signals information base can be produced.

## 2.2.1 SIGN LANGUAGE TO SPEECH CONVERSION

In the proposed framework, flex sensors are utilized to gauge how much the fingers are twisted. In the
sensor-based system three 4.5 inches and two 2.2 inches designed flex sensors are used. The speciality
of flex sensor is that through the measurement of its resistance it can be determined that how much the
flex sensor is bent. Accelerometer inside the signal acknowledgment framework is utilized as a tilt
detecting component, which thusly finds how much the finger is inclined. Material sensor is utilized
to detect the physical cooperation between the fingers. The yields from the sensor frameworks are sent
to the Arduino microcontroller unit. In Arduino microcontroller unit, information got from the sensor
yield is then contrasted and the pre-characterized values. The relating signals (coordinated motions)
are sent to the content to-discourse change module in the type of text. The yield of text-to-discourse
union framework is heard through a speaker. The fundamental highlights of this framework remember
it's pertinence for everyday life, versatility and its minimal effort. The flex sensors are mounted on the
glove and they are fitted along the length of every one of the fingers. Contingent on the twist of hand
development unique signals relating to x-axis, y-axis and z-axis are produced. Flex sensors yields the
information stream contingent upon the degree and measure of curve delivered, when a sign is
motioned. The microcontroller unit will contrast these readings and the pre-characterized limit esteems
and the comparing signals are perceived and the relating text is shown.

## 2.2.2 DEAF TALK USING 3D ANIMATED SIGN LANGUAGE

Deaf Talk, a communication through signing mediator has been proposed which offers a characteristic
method of correspondence to the consultation and talking disabled people, improving their
burdensome undertaking of correspondence. The Kinect v2 SDK gives an instrument, named gesture
builder, which has been explicitly intended for basic signals acknowledgment from Kinect producers.
It gives the straightforwardness by


abstracting the subtleties of diving deep down into facilitates, points, states and profundity for signals
acknowledgment. This device is prepared on the put away signals and it identifies the motion when
the hand movement is performed by the client. The motion manufacturer apparatus utilizes information
driven AI calculations for trainings of the signals. The framework gets the signals input outline by
outline utilizing Kinect and it coordinates each motion with pre-put away motion's information base.
For each coordinated signal, there is a catchphrase. At that point, a sentence is built utilizing those
catchphrases. This is how sign language is converted into a text form. In sign recognition, the live
stream of Kinect sensor or at the end of the day the live motion or hand movement is perused outline
by outline. This motion is contrasted them and the as of now put away motions in the information base.
On the off chance that the approaching gesture matches with the put away signal (there is a limit
estimation of certainty too), the watchword against that motion is included the sentence. The sign
recognition system in Visual motion developer are assembled in two principle classifications,
AdaBoost and RFRProgress. AdaBoost is a trigger which gives us a genuine Boolean worthwhile the
individual is playing out a specific motion, it utilizes Adaptive Boost AI calculation. RFRProgress on
other hand produces consistent outcomes giving us Analog information of progress while the client is
playing out the motion empowering the framework to distinguish the amount of the motion is finished
and what amount is the hit rate at the specific edge of the signal, it utilizes Random Forest Regression
AI calculation. For precise sign in the framework mix of the two has been utilized. The AdaBoost
trigger empowers the framework to recognize beginning and finishing purposes of characterized
signals set having comparable nature by returning valid/bogus worthwhile the motion is being
performed. Once AdaBoost trigger returns genuine worth distinguishing the discrete signal the
framework at that point utilizes RFRProgress to recognize the right motion by perusing nonstop
advancement of gesture, for this situation progress is possibly empowered if trigger is identified
(AdaBoost brings valid back). So, the AdaBoost decides the setting of the signal being performed and
RFRProgress distinguishes motion by constantly planning the client's development. On the off chance
that the hit rate is sufficient for a specific signal by consolidating both AdaBoost and RFRProgress it
is viewed as a genuine positive.

## 2.3 EXISTING WORK RELATED TO SPEECH RECOGNITION

In this section, we will discuss about the related works that are based on speech recognition system.
In a dual phase project where sign language is converted to speech, the output text of the given sign or
gesture is sent into a text-to-speech module where the text is finally converted to speech. In the project


(Deaf Talk Using 3D Animated Sign language) has a dual phase where first the sign language is
translated to speech and secondly speech is again translated to sign language [5]. Here the speech is
first converted into text and the text is taken as an input of the system. The converted text search for
the particular gesture that is stored in the database. The system components are- Modeling, Animation,
Speech to text API, Integration with unity framework.

Another study (Speech-to-Thai Sign language Conversion for Thai Deaf: A Case Study of Crime
News) converts the speech in the crime news videos to text and the text is later converted into Thai
sign language [6]. To implement the full process there are mainly three modules- Speech-to-text
conversion, Thai words segmentation and Gesture recognition.

The paper Speech-To-Text Conversion (STT) System Using Hidden Markov Model (HMM)
presents a way to deal with extricate highlights by utilizing Mel Frequency Cepstral Coefficients
(MFCC) from the speech signs of disconnected verbally expressed word [7]. Also, Hidden Markov
Model (HMM) strategy is applied to prepare and test the sound records to get the perceived verbally
expressed word. The discourse information base is made by utilizing MATLAB. Then, the first
discourse signals are pre-processed and these discourse tests are separated to the component vectors
which are utilized as the perception groupings of the Hidden Markov Model (HMM) recognizer. The
component vectors are investigated in the HMM relying upon the quantity of states. MATLAB is used
to imply MFCC and HMM.

## 2.3.1 DEAF TALK USING 3D ANIMATED SIGN LANGUAGE

This will be finished utilizing outside library for speech to text change which will accept the sentence
or word as information and distinguish the watchwords in the info. Framework will at that point look
for the sign/motion against the catchphrase from the information base. As there must exist a sign record
for every watchword so this module will get a substantial motion and give it to the showcase module.
An information structure, inside Unity3D, is utilized that will plan the motion movements to a 3D
model. Subsequently, 3D activity relating to the planned motion will be played on the screen. The
essential for changing the speech into gesture is to change over the speech into text or a string. For this
object, AT&T's online API alongside its SDK for Unity3D was utilized. 3D biped model has been
utilized to show a word or a sentence in the gesture-based communication. The thought is to utilize
displaying as a vehicle of speaking to a sentence so it very well may be effectively appreciated by an
individual with hearing incapacities. The transformation could be only discourse into text yet text isn't


as amicable vehicle of articulation as a 3D model for a hard of hearing individual. Movements were
utilized to reenact words continuously simply like a video or a film. 3D Studio Max was the apparatus
used to make animation for words that were then planned against their separate words and these
activities were played when such a word was gotten as information.

## 2.3.2 SPEECH-TO-THAI SIGN LANGUAGE CONVERSION FOR THAI DEAF: A CASE STUDY OF CRIME NEWS

In this project the main module, Speech to text, is the module that separates discourse from video and
changes over it to message. This module begins with downloading the wrongdoing news video from
YouTube utilizing the youtube_dl library in python. This cycle gets a contribution of YouTube's URL
of wrongdoing news and makes the wave document (.wav) a short time later. The following cycle is
to change over discourse to message. The SpeechRecognition library dependent on the Google Speech
Recognition API is utilized to play out this cycle. The last yield of this module is the caption of the
wrongdoing news video in the interim the precision of the content (caption) relies upon the Google
SpeechRecognition API. In this paper, we utilize the crime related news from YouTube around 20
recordings to test the precision of this library and we have discovered that all of caption get certainty
score more than 0.94 (94%).

2.3.3 Speech-To-Text Conversion (STT) System Using Hidden

Markov Model (HMM)

To change over information discourse to message yield, the four principle steps are created by utilizing
MATLAB. These steps are speech data set, pre-processing, include extraction and acknowledgment.
Initially, five sound documents are recorded with the assistance of PC. Every sound document contains
ten diverse articulation sound records. Along these lines, there are complete of fifty sound documents
are recorded in

discourse information base. The discourse signals at low frequencies have more vitality than at high
frequencies. Thusly, the energies of sign are important to be help at high frequencies. As per the
immersion of condition, the undesirable clamor may influence the acknowledgment rate more
regrettable. This issue can be overwhelmed by end point discovery technique. In the wake of pre-
processing stage is done, the discourse tests are removed to highlights or coefficients by the utilization
of Mel Frequency Cepstral Coefficient (MFCC). At last, these MFCC coefficients are utilized as the


contribution of Hidden Markov Model (HMM) recognizer to arrange the ideal expressed word. The
ideal content yield can be produced by HMM strategy regardless of whether the test sound document
is remembered for the current discourse information base. Here they have taken five sample keywords,
for example, apple, banana, computer, flower and key. The simulation was displayed at the sampling
rate of 8Khz. The speech recognition is based on HMM so when the number of states are increased
the accuracy of recognition is increased as well. In this project the number of states they used are 5
and the accuracy level is 87.6%.

## 2.4 SUMMARY

In this chapter, we have discussed the speech recognition system and sign recognition system that is
related to our project.

## CHAPTER 3 THEORY

## 3.1 INTRODUCTION

In this chapter, we will discuss the theory of our system. Our system is basically a two-way
communication system where a normal person’s speech will be converted into text and also sign
language will be converted to text. Here we can notice the system is divided into two sections

1. Speech recognition and speech to text conversion
2. Sing language recognition and sign language to text conversion

## 3.2 SPEECH RECOGNITION AND SPEECH TO TEXT CONVERSION

In this section, we will discuss about converting speech into on screen text or computer command.
Though it seems simple but the internal process of recognizing text and then converting into on
screen text is quiet complex process. The process is basically carried out by a computer and Speech
recognition is one of the most complex areas of computer science—and partly because it's
interdisciplinary: it involves a mixture of extremely complex linguistics, mathematics, and
computing itself. To convert speech to on-screen text or a computer command, a computer has to go
through several complex steps. When you speak, you create vibrations in the air. The analog-to-
digital converter (ADC) translates this analog wave into digital data that the computer can
understand. To do this, its samples, or digitizes, the sound by taking precise measurements of the
wave at frequent intervals. The system filters the digitized sound to remove unwanted noise, and
sometimes to separate it into different bands of frequency (frequency is the wavelength of the sound


waves, heard by humans as differences in pitch). It also normalizes the sound, or adjusts it to a
constant volume level. It may also have to be temporally aligned. People don't always speak at the
same speed, so the sound must be adjusted to match the speed of the template sound samples already
stored in the system's memory.

Next the signal is divided into small segments as short as a few hundredths of a second, or even
thousandths in the case of plosive consonant sounds -- consonant stops produced by obstructing
airflow in the vocal tract -- like "p" or "t." The program then matches these segments to known
phonemes in the appropriate language. A phoneme is the smallest element of a language -- a
representation of the sounds we make and put together to form meaningful expressions. There are
roughly 40 phonemes in the English language (different linguists have different opinions on the
exact number), while other languages have more or fewer phonemes.

The next step seems simple, but it is actually the most difficult to accomplish and is the is focus of
most speech recognition research. The program examines phonemes in the context of the other
phonemes around them. It runs the contextual phoneme plot through a complex statistical model and
compares them to a large library of known words, phrases and sentences. The program then
determines what the user was probably saying and either outputs it as text or issues a computer
command.

There are four different approaches a computer can take if it wants to turn spoken sounds into
written words:

1. Simple pattern matching (where each spoken word is recognized in its entirety—the way you
    instantly recognize a tree or a table without consciously analysing what you're looking at)
2. Pattern and feature analysis (where each word is broken into bits and recognized from key
    features, such as the vowels it contains)
3. Language modelling and statistical analysis (in which a knowledge of grammar and the
    probability of certain words or sounds following on from one another is used to speed up
    recognition and improve accuracy)
4. Artificial neural networks (brain-like computer models that can reliably recognize patterns,
    such as word sounds, after exhaustive training).


## 3.2.1 GOOGLE SPEECH RECOGNITION

Algorithm for artificial intelligence is very much popular nowadays and Google also uses those
algorithms to recognize spoken sentences, stores voice data anonymously for analysis purposes, and
cross matches spoken data with written queries on the server. Client application starts up and
prompts the user to input using Google Speech Recognition. Input data is sent to the Google server
for processing and text is returned to the client.

Google Cloud Speech API enables developers to convert audio to text by applying powerful neural
network models in an easy to use API. The API recognizes over 80 languages and variants, to
support a global user base. Software developers can provide speech support access in their
applications to Google's technology through a set of cloud-based interfaces. One can transcribe the
text of users dictating to an application’s microphone, enable command-and-control through voice,
or transcribe audio files, among many other use cases. It will work with any application in real-time
streaming or batch mode, will offer full set of APIs for applications. It is based on the same neural
network tech that powers Google’s voice search in the Google app and voice typing in Google’s
Keyboard.

- Speech to text conversion powered by machine learning: The most advanced deep learning
    neural network algorithms are applied to the user's audio for speech recognition with
    unparalleled accuracy. Speech API accuracy improves over time as Google improves the
    internal speech recognition technology used by Google products.
- Global vocabulary: Speech API recognizes over 80 languages and variants to support a global
    user base.
- Return text results in real-time: Speech API can stream text results, returning partial
    recognition results as they become available, with the recognized text appearing immediately
    while speaking. Alternatively, Speech API can return recognized text from audio stored in a
    file
- Accurate in noisy environments: We don’t need advanced signal processing or noise
    cancellation before sending audio to Speech API. The service can successfully handle noisy
    audio from a variety of environments.
- Context-aware recognition: Speech recognition can be tailored to context by providing a
    separate set of word hints with each API call. Useful especially for device/app control use
    cases.
- Works with apps across any device: Speech API supports any device that can send a REST or
    gRPC request including phones, PCs, tablets and IoT devices (e.g., cars, TVs, speakers)


Speech to Text Using Python

Speech is the most common means of communication around the world. Most of the population
in the world relies on speech to communicate with each other. In our project, we are going to use
speech recognition to decrease the communication gap between the teachers and their deaf students.
We are going to use the speech recognition module in python for our project.

● Python Modules
Modules are simply a ‘program logic’ or a ‘python script’ that can be used for a variety of applications
or functions. We can declare functions, classes in a module [8].

The focus is to break down the code into different modules so that there will be no or minimum
dependencies on one another. Using modules in a code helps to write a lesser line of codes. It also
eliminates the need to write the same logic again and again.

● What is speech recognition and how it works? [9]

1. Speech Recognition is a process in which a computer or device records the speech of humans
    and converts it into text format.
2. It is also known as Automatic Speech Recognition (ASR), computer speech recognition or
    Speech to Text (STT).
3. Linguistics, computer science, and electrical engineering are some fields that are associated
    with Speech Recognition.


## FIGURE 3. 1 WORKING PRINCIPLES OF SPEECH RECOGNITION [9].

Speech recognition is based on the algorithm of acoustic and language modelling. Acoustic modelling
represents the relationship between linguistic units of speech and audio signals and language modelling
matches sounds with word sequences to help distinguish between words that sound similar [9].

Any speech recognition program is evaluated using two factors. Accuracy and speed [9].

Speech recognition system basically translates the spoken utterances to text. The advantage of using a
speech recognition system is that it overcomes the barrier of literacy. A speech recognition model can
serve both literate and illiterate audiences as well, since it focuses on spoken utterances [8]. The Speech
Recognition System also faces a lot of challenges. Among them style of speaking, speaker’s
characteristics, language constraints and background noise are the one we should consider the most.

● Packages available for speech recognition in python [8] [10]

1. Apiai
2. SpeechRecognition
3. Google_speech_cloud
4. Assemblyai
5. Pocketsphinx
6. Watson_developer_cloud
7. Wit
● Installing the package SpeechRecognition [8] [11]
We are going to use the SpeechRecognition package for our project. After installing it successfully we
will see that the package has a Recognizer class. It is basically a class which is used to recognize the
speech. There are seven methods which can read various audio sources using different APIs.


1. recognize_bing( )
2. recognize_google( )
3. recognize_google_cloud( )
4. recognize_houndify( )
5. recognize_ibm( )
6. recognize_wit( )
7. recognize_sphinx( )
From these seven methods we will use recognize_google().

● Taking Input from Microphone [8] [11]
To use the microphones, we will have to install PyAudio module as well. We use the microphone
class to get the input speech from the microphone instead of any other input method like an audio file.
To capture the input from the microphone we use the listen method.

## 3. 3 SIGN LANGUAGE RECOGNITION

In this section, we will discuss about converting sign language into on screen text. This is the hardest
and most crucial part of our project. We need to use machine learning to successfully do so. In
training a machine, we had a lot of choice in choosing our model. But we wanted to choose a model
which will perform the best in our case. So, we choose VGG16 as our pre-trained model. In our
project the most problem we faced was collecting the dataset. The dataset we wanted to work with
was not available anywhere. We had to create our own dataset from scratch.

## 3.4 ALGORITHM AND MODEL

## 3.4.1 CONVOLUTIONAL NEURAL NETWORK

Convolutional Neural Networks are a category of Neural Networks that have proven very
effective in areas such as image recognition and classification [12]. A Convolutional Neural Network
is comprised of one or more convolutional layers and then followed by one or more fully connected
layers as in a standard multilayer neural network [13]. The architecture of a CNN is designed to take
advantage of the 2D structure of an input image [13]. A grey scale image, has just one channel. For
the purpose of this post, we will only consider grey scale images, so we will have a single 2d matrix


representing an image. The value of each pixel in the matrix will range from 0 to 255 – zero indicating
black and 255 indicating white [12].

- Architecture
A CNN comprises of various convolutional and subsampling layers alternatively followed by
completely associated layers [13]. CNN's expect models to prepare and test. Each info picture goes
through a progression of convolution layers with channels, Pooling, completely associated layers (FC)
and apply softmax capacity to order an article with probabilistic qualities somewhere in the range of 0
and 1. This is the explanation each picture in CNN's gets spoken to as a network of pixel esteems.
Convolution and Pooling layers together go about as highlight extractors from the information picture
while a completely associated layer goes about as a classifier. The entirety of all probabilities in the
yield layer ought to be one however. There are four primary tasks in the CNN:
1. Convolution Layer-This holds the crude pixel estimations of the preparation picture as
information. This layer guarantees the spatial connection between pixels by learning picture
highlights utilizing little squares of information [14]. The size of the component map is
constrained by three parameters:
Depth- Number of channels utilized for the convolution activity [14].
Stride- Stride is the quantity of pixels by which we slide our channel network over the info
lattice. At the point when the step is 1 then we move the channels each pixel in turn. At the
point when the step is 2, at that point the channels bounce 2 pixels one after another as we
slide them around. Having a bigger step will deliver littler element maps.
Padding- Sometimes, it is advantageous to cushion the information network with zeros
around the fringe, so the channel to flanking components of an information picture
framework can be applied. A decent element of zero cushioning is that it permits to control
the size of the element maps. Including zero-cushioning is additionally called wide
convolution, and not utilizing zero-cushioning would be a tight convolution [14] [12].
Calculating total error at the output layer [14]:
**Total Error = ∑** ½ (target probability **–** output probability) ²
2. Rectified Linear Unit Layer- A non-linear operation. This layer applies a component astute
actuation work. ReLU is utilized after each Convolution activity. It is applied per pixel and
replaces all negative pixel esteems in the element map by zero [14]. This leaves the size of the
volume unaltered ([32x32x16]). ReLU is a non-straight activity [14].
3. Pooling Layer- Spatial Pooling decreases the dimensionality of each element map however
holds the most significant data [12]. Spatial Pooling can be of various sorts: Max, Average,


```
Sum and so on. If there should be an occurrence of Max Pooling, we characterize a spatial
neighbourhood and take the biggest component from the redressed highlight map inside that
window [12]. Rather than taking the biggest component we could likewise take the normal
(Average Pooling) or aggregate of all components in that window [12].
```
4. Fully Connected Layer-In Fully Connected Layer every hub is associated with each other hub
    in the adjoining layer [14]. FC layer figures the class scores with a customary multilayer
    perceptron that utilizes a SoftMax initiation work in the yield layer [14]. It brings about the
    volume of size [1x1x10], where every one of the 10 numbers compare to a class score, for
    example, among the 10 classifications of CIFAR-10. The yield from the convolutional and
    pooling layers speak to elevated level highlights of the information picture [12]. The motivation
    behind the Fully Connected layer is to utilize these highlights for characterizing the info picture
    into different classes dependent on the preparation dataset [12].
- Steps we need to follow
Step1: We instate all channels and parameters/loads with irregular qualities.
Step2: The system takes a preparation picture as info, experiences the forward spread advance
(convolution, ReLU and pooling activities alongside forward proliferation in the Fully Connected
layer) and finds the yield probabilities for each class.
Step3: Calculate the total error at the output layer (summation over all 4 classes)
**Total Error = ∑** ½ (target probability **–** output probability) ²

```
Step4: Use Backpropagation to ascertain the angles of the mistake regarding all loads in the system
and use gradient descent to refresh all channel loads and parameter esteems to limit the yield
mistake. The weights are adjusted in proportion to their contribution to the total error.
Step5: Repeat steps 2-4 with all images in the training set.
```
The above steps train the ConvNet – this essentially means that all the weights and parameters of
the ConvNet have now been optimized to correctly classify images from the training set [12].


## 3.4.2 VGG16

VGG16 is a convolutional neural network model proposed by K. Simonyan and A. Zisserman from
the University of Oxford in the paper “Very Deep Convolutional Networks for Large-Scale Image
Recognition”. The model achieves 92.7% top-5 test accuracy in ImageNet, which is a dataset of over
14 million images belonging to 1000 classes [1]. The ImageNet Large Scale Visual Recognition
Challenge (ILSVRC) is a yearly computer vision rivalry. Every year, groups contend on two
undertakings. The first is to identify objects inside a picture originating from 200 classes, which is
called object limitation. The second is to group pictures, each marked with one of 1000 classes, which
is called image classification [2]. Most novel thing about VGG16 is that as opposed to having an
enormous number of hyper-boundary they zeroed in on having convolution layers of 3x3 channel with
a step 1 and consistently utilized same cushioning and maxpool layer of 2x2 channel of step 2. It
follows this plan of convolution and max pool layers reliably all through the entire engineering. In the
end it has 2 FC(fully associated layers) trailed by a softmax for yield. The 16 in VGG16 alludes to it
has 16 layers that have loads. 16 layers of VGG-16 is given below [3]:

1. Convolution using 64 filters.
2. Convolution using 64 filters + Max pooling.
3. Convolution using 128 filters.
4. Convolution using 128 filters + Max Pooling.
5. Convolution using 256 filters.
6. Convolution using 256 filters.
7. Convolution using 256 filters + Max pooling.
8. Convolution using 512 filters.
9. Convolution using 512 filters.
10. Convolution using 512 filters + Max pooling.
11. Convolution using 512 filters.
12. Convolution using 512 filters.
13. Convolution using 512 filters + Max pooling.
14. Fully connected with 4096 nodes.
15. Fully connected with 4096 nodes.
16. Output layer with Softmax activation with 1000 nodes.

The contribution to cov1 layer is of fixed size 224 x 224 RGB picture. The picture is gone through a
heap of convolutional (conv.) layers, where the channels were utilized with a little open field: 3×3


(which is the littlest size to catch the idea of left/right, up/down, focus). In one of the designs, it
additionally uses 1×1 convolution channels, which can be viewed as a direct change of the information
channels (trailed by non-linearity). The convolution step is fixed to 1 pixel; the spatial cushioning of
conv. layer input is with the end goal that the spatial goal is safeguarded after convolution, for example
the cushioning is 1-pixel for 3×3 conv. layers. Spatial pooling is done by five max-pooling layers,
which follow a portion of the conv. layers (not all the conv. layers are trailed by max-pooling). Max-
pooling is performed over a 2×2 pixel window, with step 2. Three Fully-Connected (FC) layers follow
a pile of convolutional layers (which has an alternate profundity in various structures): the initial two
have 4096 channels each, the third performs 1000-way ILSVRC grouping and subsequently contains
1000 channels (one for each class). The last layer is the delicate max layer. The arrangement of the
completely associated layers is the equivalent in all organizations. All shrouded layers are furnished
with the correction (ReLU) non-linearity. It is likewise noticed that none of the organizations (aside
from one) contain Local Response Normalization (LRN), such standardization doesn't improve the
presentation on the ILSVRC dataset, yet prompts expanded memory utilization and calculation time.
In the below figure the CovNet configuration is shown. The nets are alluded to their names. All setups
follow the conventional plan present in engineering and contrast just in the profundity: from 11 weight
layers in the organization A (8 conv. what's more, 3 FC layers) to 19 weight layers in the organization
E (16 conv. furthermore, 3 FC layers). The width of conv. layers (the dadsadquantity of channels) is
fairly little, beginning from 64 in the primary layer and afterward expanding by a factor of 2 after
every maximum pooling layer, until it arrives at 512.


## FIGURE 3. 2 CONFIGURATION OF COVNET

The use case limitations of VGG-16 are:

1. It takes time to train the model.
2. The network design loads themselves are very enormous.

Because of its profundity and number of completely associated hubs, VGG16 is over 533MB. This
makes conveying VGG a tedious task. VGG16 is utilized in numerous profound learning picture order
issues; nonetheless, littler organization models are frequently more alluring, (for example,
SqueezeNet, GoogLeNet, and so forth.). Yet, it is an incredible structure block for learning reason as
it is anything but difficult to actualize.

VGG16 essentially outflanks the past age of models in the ILSVRC-2012 and ILSVRC- 2013
competitions. The VGG16 result is likewise seeking the grouping task victor (GoogLeNet with 6.7%
blunder) and significantly beats the ILSVRC-2013 winning accommodation Clarifai, which
accomplished 11.2% with outside preparing information and 11.7% without it. Concerning the single-


net execution, VGG16 engineering accomplishes the best outcome (7.0% test mistake), beating a
solitary GoogLeNet by 0.9%.

## 3.4.3 FINE-TUNING VGG16

We tried different types of pooling operation to experiment at the top model. We have used Global
Average Pooling (GAP) Finally. Because It Reduces the total number of parameters more than
flattening , speeds up the training which results in less chance of overfitting.GAP layers are used to
reduce the spatial dimensions of a three-dimensional tensor.GAP layers perform a more extreme type
of dimensionality reduction, where a tensor with dimensions h×w×d is reduced in size to have
dimensions 1×1×d. By doing a global average we make the convolution invariant to where the object
of interest is and this acts as a data augmentation of moving the object around to different regions.
This prevents overfitting of the fc layers. We have used fixed feature extractor which is modified for
recognizing hand gestures only. The last classifier part is removed from the model and we have given
a classifier of our own.


## FIGURE 3. 3 OUTPUT AFTER FINE TUNING THE MODEL.

We have also fine-tuned some of the last layers so that it can extract the high-level features properly.
For our network, we used a rectified linear unit, or ReLU.

## FIGURE 3. 4 RELU ACTIVATION

The above graph shows that the ReLU will output 0 when the input is negative, but will not change
the input otherwise. The outputs from the ReLU will serve as the inputs to the next hidden layer in the
network.

## 3.4.4 REGULARIZATION

Regularization is one of the basic and most important concepts in the world of Machine Learning.

This is a form of regression, that constrains/ regularizes or shrinks the coefficient estimates towards
zero. In other words, this technique discourages learning a more complex or flexible model, so as to
avoid the risk of overfitting. So, Regularizations are techniques used to reduce the error by fitting a
function appropriately on the given training set and avoid overfitting.

There are only two ways to regularize deep neural networks today.

1. Dropouts. 2. Weight Decay.

VGG-Net uses both the methods. Weight decay is a L2 penalty multiplier similar to L2
regularization possible in most Machine Learning algorithms. VGG-Net uses weight decay of 5*10^-

4. And then there is dropouts in the first two layers with a probability of 0.5. Dropouts are equivalent
to just turning off some neurons of the network at random with the defined probability.


After fine tuning the model we experienced overfitting and we have used Regularization that is early
stopping. early stopping is a form of regularization used to avoid overfitting when training a learner
with an iterative method. Such methods update the learner so as to make it better fit the training data
with each iteration. Early stopping rules provide guidance as to how many iterations can be run
before the learner begins to over-fit. Keras supports the early stopping of training via a call-back
called Early Stopping. This call-back allows you to specify the performance measure to monitor, the
trigger, and once triggered, it will stop the training process.

## FIGURE 3. 5 CODE FOR EARLYSTOPPING

We have monitored validation loss and delayed the trigger to 10 epochs.

When we started our training from 42 number epochs our validation loss stopped improving. So
according to our code above if our validation loss does not improve for 10 consecutive times then to
avoid overfitting our model is going to early stop automatically. So, at epoch number 51 it triggered
early stopping and helped our model from getting over fit.

## FIGURE 3. 6 EARLY STOPPING AFTER 51 EPOCHS

## 3.4.5 DATA AUGMENTATION

We have used 'ImageDataGenerator' for real-time data augmentation.


## FIGURE 3. 7 CODE FOR DATA AUGMENTATION

Rescale is a value by which we will multiply the data before any other processing. Our original
images consist in RGB coefficients in the 0-255, but such values would be too high for our models to
process (given a typical learning rate), so we target values between 0 and 1 instead by scaling with a
1/255. Factor.

## 3.5 HYPER - PARAMETER

```
Hyper parameters are all the training variables set manually with a pre-determined value before
starting the training. Basically, it is like a knob that we can turn. We have explored two of the
Hyper-parameters they are
```
1. Learning rate
2. Batch size
- The amount that the weights are updated during training is referred to as the step size or the
“learning rate.” It often ranges between 0.0 and 1.0.
- One of the most important hyper parameters is the batch size, which is the number of images
used to train a single forward and backward pass or every epoch.

## FIGURE 3. 8 CODE FOR LEARNING RATE REDUCTION

There is a high correlation between the learning rate and the batch size, when the learning rates are
high, the large batch size performs better than with small learning rates. we have set leaning rate =
0.0001.


## 3.6 SUMMARY

In this chapter, the theoretical part of our project has been described. We have tried to explain how
speech recognition works in detail, how we have trained our model and the algorithm in details.

## CHAPTER 4 DATASET

## 4.1 INTRODUCTION

A dataset is a collection of data in which data is arranged in some order. To work with machine
learning projects, we need a huge amount of data, because, without the data, one cannot train ML/AI
models.

## 4.2 OUR DATASET

Collecting and preparing the dataset is one of the most crucial parts while creating an ML/AI project.

The technology applied behind any ML projects cannot work properly if the dataset is not well
prepared and pre-processed.

During the development of the ML project, the developers completely rely on the datasets. In
building ML applications, datasets are divided into two parts:

```
o Training dataset:
o Test Dataset
```
In any machine learning project dataset is the most crucial and the most important part. Our
dataset contains pictures of signs for 26 alphabets (A – Z) and a Space (). We have altogether
managed to capture 20,250 images for our dataset.


## FIGURE 4. 1 FOLDER STRUCTURE OF THE TRAINING DATASET

To make our dataset more versatile and larger we took the pictures of the sign gestures from several
persons. We did this because not everyone's skin colour and the way of showing the sign is same. So,
taking different persons’ hand gesture gave our dataset much more versatility and it broadens the
possibility of our model recognizing the gesture with much more accuracy. Some examples from our
datasets are given below.

## FIGURE 4. 2 EXAMPLES OF DATASET (A – Z AND SPACE)

Link for the dataset = https://github.com/mushfiqurrb/Communicator-for-Deaf-and-Dumb--
Dataset-

## 4.3 SUMMARY

Dataset in our project is unique and important. A lot of time and effort was given in the process of
making this dataset.


## CHAPTER 5 STRUCTURE OF THE SYSTEM

## 5.1 INTRODUCTION

The structure of how the system works is discussed in this chapter. We have developed an
application for computer which will give us a platform to make communication easy and efficient
between a normal and a deaf person.

## 5.2 SYSTEM DESIGN AND PROCEDURE

Here we can see a design of our system. We can see normal people is speaking and his speech is
being converted to text and a deaf person is able to see the text. After that the deaf person can
communicate sign language or hand gesture and it will be converted into on screen text too. So, it is
basically a two-way communication platform.

## FIGURE 5. 1 DIAGRAM OF HOW OUR PROJECT IS GOING TO WORK.

## 5.2.1 SPEECH TO TEXT

The speech recognizer will recognize the speech of the speaker and translate it into text.

This text will be shown into a screen which will help the deaf to understand what the speaker is
trying to say.


## FIGURE 5. 2 DIAGRAM OF HOW SPEECH TO TEXT IS GOING TO WORK.

## 5.2.2 SIGN LANGUAGE TO TEXT

This section describes the conversion of sign language to text. We have divided this section into two
part.

```
▪ Training the machine
At first, we had to train a model with a large scale of dataset. For this we have capture
image via camera then feed the dataset to the model and trained the model.
```
## FIGURE 5. 3 HOW WE COLLECTED THE DATASET FOR TRAINING.

```
▪ Recognize sign language
In this part, a user needs to show a sign from the alphabet A to Z in front of a computer
camera. Then the application will recognize the alphabet and show it as on-screen text to
the user.
```
## FIGURE 5. 4 HOW THE MACHINE WILL DETECT THE SIGN LANGUAGE.


## 5.3 SUMMARY

In this chapter, we have described how the system works. The sequence of events resulting in a
speech is being recognized, converted to on screen text and also how sign language is converted into
text.

## CHAPTER 6 USER INTERFACE

To create our app, we have used PyQt5. Qt is set of cross-platform C++ libraries that implement
high-level APIs for accessing many aspects of modern desktop and mobile systems. PyQt5 is a
comprehensive set of Python bindings for Qt v5. It is implemented as more than 35 extension
modules and enables Python to be used as an alternative application development language. So, our
desktop application is built with PyQt5.

We have created just a simple app consisting two buttons and a text box.

## FIGURE 6. 1 LAYOUT OF OUR APPLICATION.


The bottom left button converts speech to text and the bottom right one converts sign language to
text.

## 6.1 SIGN TO TEXT

The bottom left button in our app labeled as “Speech to Text” is used to convert a person's speech
into text. The goal here is that a person will press the button “Speech to Text” and then say whatever
he/she likes and that speech will be converted into text. The converted text will be shown in the text
box.

## FIGURE 6. 2 RECOGNIZED SPEECH SHOWN AS TEXT IN THE TEXT BOX.

## 6.2 SIGN LANGUAGE TO TEXT

The bottom left button in our app labeled as “Sign to Text” is used to convert sign gestures into text.
The goal here is that a deaf/dumb person will press the button “Sign to Text” and then a pop-up
screen will appear. In that screen with the help of the camera they have to show the sign gestures
according to what they want to express. Our model will recognize the gestures and then convert it
into text.


## FIGURE 6. 3 RECOGNIZED SIGN SHOWN IN OUR APPLICATION.............................................................................................................

## 6.3 SUMMARY

Our application is a simple one with only the things we need. In our future work, we will try to
make it much more elegant and fancier looking.

## CHAPTER 7 DEVICE AND SOFTWARE

For both sign language recognition and speech recognition we have used python. To be exact Python
3.7.9 version. To properly work we needed a lot of python modules.

## 7.1 MODULES USED FOR SPEECH RECOGNITION

For our speech recognition to work properly we have used two python modules.

- PyAudio 0.2.11
PyAudio provides Python bindings for PortAudio, the cross-platform audio I/O library. With
PyAudio, you can easily use Python to play and record audio on a variety of platforms.


- SpeechRecognition 3.8.1

Library for performing speech recognition, with support for several engines and APIs, online and
offline.

## 7.2 MODULES USED FOR SIGH LANGUAGE RECOGNITION

- TensorFlow 2.3.0

TensorFlow is an open-sourced library that’s available on GitHub. It is one of the more famous
libraries when it comes to dealing with Deep Neural Networks. TensorFlow excels at numerical
computing, which is critical for deep learning. It provides APIs in most major languages and
environments needed for deep learning projects: Python, C, C++, Rust, Haskell, Go, Java,
Android, IoS, Mac OS, Windows, Linux, and Raspberry Pi. Moreover, TensorFlow was created
keeping the processing power limitations in mind. Implying, we can run this library on all kinds
of computers, irrespective of their processing powers.


- Keras 2.4.3

Keras is a high-level library that’s built on top of Theano or TensorFlow. Developers can use
Keras to quickly build neural networks without worrying about the mathematical aspects of
tensor algebra, numerical techniques, and optimization methods.

The key idea behind the development of Keras is to facilitate experimentations by fast
prototyping. The ability to go from an idea to result with the least possible delay is key to good
research. This offers a huge advantage for scientists and beginner developers alike because they
can dive right into Deep Learning without getting their hands dirty with low-level computations.

- Pandas 1.1.2

Pandas has been one of the most popular and favourite data science tools used in Python
programming language for data wrangling and analysis.

- Pillow 7.2.0

Pillow is a Python Imaging Library (PIL), which adds support for opening, manipulating, and
saving images. The current version identifies and reads a large number of formats.

- Numpy 1.18.5

NumPy is an open-source numerical Python library. NumPy contains a multi-dimensional array
and matrix data structures. It can be utilised to perform a number of mathematical operations on
arrays such as trigonometric, statistical, and algebraic routines. Therefore, the library contains a
large number of mathematical, algebraic, and transformation functions. NumPy is an extension of
Numeric and Numarray. It also contains random number generators.

- matplotlib

Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations
in Python. Matplotlib produces publication-quality figures in a variety of hardcopy formats and
interactive environments across platforms. Matplotlib can be used in Python scripts, the Python
and IPython shell, web application servers, and various graphical user interface toolkits.


## CHAPTER 8 RESULTS AND DISCUSSION

## 8.1 INTRODUCTION

```
The results for our machine learning training is given below. We faced a lot of problems while
training our model with our own dataset. Gradually we had to increase the size of our dataset and
also add hyper-parameters in our model to achieve our expectation.
```
## 8.2 TRAINING RESULT

## 8.2.1 FIRST TRAINING SESSION

First training session was all about learning the model throughout. We created a very small dataset
and trained our model with it to find out what kind of problem we are going to face. We also figured
out what kind of hyper-parameters we need to implement for absolute result.

## 8.2.2 SECOND TRAINING SESSION

In our second training session, we had 5220 images for training and 1300 images for testing. Our
model only ran 13 epochs and then it stopped.

## FIGURE 8. 1 NUMBER OF IMAGES AND PARAMETERS IN OUR PROJECT FROM SECOND TRAINING SESSION.


## FIGURE 8. 2 NUMBER OF EPOCHS RAN IN SECOND TRAINING..............................................................................................................

From the plot for loss and accuracy you can see that the training loss and the testing loss are far away
from each other. Same goes for the accuracy also. This eventually menas that our model could not
learn anything from our datasets and it also could not detect any single alphabets.

## FIGURE 8. 3 LOSS AND ACCURACY CURVE FROM SECOND TRAINING.

## 8.2. 3 THIRD TRAINING SESSION

In our third training session, we completely removed the dataset used for second training session. We
took new 5200 images for training and 1300 images for testing. This time our model only ran 30
epochs.


## FIGURE 8. 4 NUMBER OF IMAGES, PARAMETERS AND EPOCHS RAN IN OUR PROJECT FROM SECOND TRAINING SESSION.

From the plot for loss and accuracy you can see that the training loss and the testing loss are a lot
closer than before. The training accuracy and the testing accuracy curve are also a lot closer. This
time our model actually could recognize some of the alphabets. But not everyone of them.

## FIGURE 8. 5 LOSS AND ACCURACY CURVE FROM THIRD TRAINING.

## 8.2.4 FINAL TRAINING SESSION

Before our final session, we did a lot of research to figure out our actual problem. After a lot of
findings, we came to a conclusion that we need much larger dataset. So, we basically tripled our
dataset. In our final training session, we completely removed the dataset used for second training
session. We took new 16200 images for training and 4050 images for testing. This time our model
only ran 51 epochs.


## FIGURE 8. 6 NUMBER OF IMAGES AND PARAMETERS IN OUR PROJECT FROM FINAL TRAINING SESSION.

## FIGURE 8. 7 NUMBER OF EPOCHS RAN IN FINAL TRAINING.

From the plot for loss and accuracy both the training and testing curves are very close to each other
this time. Our model recognized every alphabets properly this time except P,R and S.

## FIGURE 8. 8 LOSS AND ACCURACY CURVE FROM FINAL TRAINING.


## 8.3 DISCUSSION

Speech to text was easy part of the project as we just have used google speech API. Main and
difficult part was the sign language to text conversion part. We had to learn a lot and face so many
new things to solve this part. First, we tried with existing dataset to learn and modify our model.
After that we have created our own dataset and procced to training. In our first 2 training the results
were not that good or up to the mark. Eventually we update our dataset and made it a lot larger than
before. The use of hyper-parameter in our project and our updated dataset has given us the training
result we wanted from the beginning.

## CHAPTER 9 FUTURE WORK

Our project is to convert sign language to speech. We built a desktop application that converts the
sign language to text and also the speech to text. As we have discussed in the earlier section that
there are few works related to our project but it has many future opportunities too. For the time being
the project can be implemented only in the education sector. In the modern world, we can see that
the use of mobile phones is increasing. So, in future if a mobile application that will increase the
usage opportunity of the system in our daily life. Again, we have used VGG-16 convolutional
network for our training purpose; this CNN model can also be used to train ASL, ISL, Thai sign
languages and many other sign languages.



