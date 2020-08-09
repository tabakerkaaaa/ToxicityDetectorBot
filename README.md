# ToxicityDetectorBot (2020)
**ToxicityDetectorBot** is a telegram bot for sentiment analysis of Russian messages in chat and creating warnings about the most negative ones. 

This repository contains a fully functioning code, which you may launch on any cloud computing service. The only thing you should do: create your telegram bot via @BotFather, set it's privacy status to *disabled* to let the bot receive all messages, and enter API-token in the third line of the *main.py* file.

Technology:
The model behind ToxicityDetectorBot, consisting of CountVectorizer, TfidfTransformer, and LogisticRegression with cross-validation, achieved 83% accuracy on a dataset of Russian tweets.
