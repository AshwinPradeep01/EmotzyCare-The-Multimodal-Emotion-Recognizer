# EmotzyCare-The-Multimodal-Emotion-Recognizer

EmotzyCare: A Multimodal Emotion Recognition System for Patients

#Introduction


 EmotzyCare is a multimodal emotion recognition system that utilizes both visual and audio-to-text modalities to accurately recognize emotions in individuals. It is designed to assist in monitoring the emotional state of patients, providing valuable insights for healthcare professionals to make informed treatment decisions.


#Features


 Multimodal Emotion Recognition: EmotzyCare employs a combination of facial expression recognition and audio-to-text sentiment analysis to achieve comprehensive emotion recognition.


 Real-time Monitoring: The system operates in real-time, continuously monitoring and analyzing the patient's emotional state, providing up-to-date information for healthcare providers.


 Personalized Insights: EmotzyCare generates personalized emotion profiles for each patient, allowing for tailored treatment interventions.


#Benefits


 Enhanced Patient Care: EmotzyCare enables healthcare professionals to better understand and respond to the emotional needs of their patients, leading to improved patient care outcomes.


 Early Intervention: The system's real-time monitoring capabilities facilitate early detection of emotional distress, enabling prompt intervention and preventing potential crises.


 Personalized Treatment: Personalized emotion profiles guide healthcare providers in developing individualized treatment plans that address the specific emotional needs of each patient.



#Technologies Used

Visual Recognition:
-mediapipe
-ML classifier(gradient boost classifier,logistic regression,ridge classifier,naive bayes classifier)

Audio-to-Text Analysis:

-Assembly AI(transcriber)

-BERT(text classification)




#modules:

transcriber:

        -transcriber.py

        
text classification using BERT:

        -EmotionDetectionUsingBert.ipynb
        
        -text_classification.py


Visual_emotion_classification:

        -FER_MP.ipynb
        
        -emotion.pkl
        
        -RealtimeEmotion.py





accuracy for visual_emotion_classification: 57

accuracy for audio_to_text_classification: 50(average)

![image](https://github.com/AshwinPradeep01/EmotzyCare-The-Multimodal-Emotion-Recognizer/assets/60032466/3a4233f5-6124-4a18-91aa-9e4fe829de82)

