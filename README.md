## Sentiment classification with GST tweet data on LSTM based on polarity-popularity model


A full scale frameowrk for determining the polarity-popularity occurrence order of words extracted from tweets, based on a large scale economic reform. This research work is one of the most comprehensive approach on a large scale Twitter data, i.e., based on the implementation of GST in India. <br><br>




This is a concise form of the full scale work, providing *only* the main modules. <br><br>



⦁  If you utilize our codes and/or the open datasets provided, or any of our findings, please cite this work as: 

 **Das, S., Das, D. & Kolya, A.K. Sentiment classification with GST tweet data on LSTM 	based on polarity-popularity model. Sādhanā 45, 140 (2020). 	https://doi.org/10.1007/s12046-020-01372-8** <br><br>



⦁  You can also read our paper on: [Springer Nature SharedIt](https://rdcu.be/b4vJw). <br><br>



⦁  **Abstract of the work:**


One of the biggest issues of Indian economy in 2017 was the implementation of Goods and Services Tax (GST), and the social networks witnessed a lot of opinion contrasts and conflicts regarding this new taxation system. Inspired by such a large-scale tax reformation, we developed an experimental approach to analyze the reactions of public sentiment on Twitter based on popular words either directly or indirectly related to GST. We collected a number of almost 200 k tweets solely about GST from June 2017 to December 2017 in two phases. In order to assure the relevance of our crawled tweets with respect to GST, we prepared a topic-sentiment relevance model. Furthermore, we employed several state-of-art lexicons for identifying sentiment words and assigned polarity ratings to each of the tweets. On the other hand, in order to extract the relevant words that are linked with GST implicitly, we propose a new polarity-popularity framework and such popular words were also rated with sentiments. Next, we trained an LSTM model using both types of rated words for predicting sentiment on GST tweets and obtained an overall accuracy of **84.51%**. It was observed that the performance of the system has been started improving while incorporating the knowledge of indirectly related GST words during training. <br><br><br>


<br>

⦁  **Workflow of the project:**

Please follow the mentioned project hierarchy:

	1. Data Collection & Preprocessing,
	
	   2. Feature I - GST-specified word sentiment identification,
		
	      3. GST-implied word identification from POS tagging,

	         4. Feature II: Sentiment rating of tweets,

		    5. LSTM for sentiment accuracy prediction,

		       6. Confusion matrix & classification report.
						     
					     

<br><br><br>
⦁  *Please* open all the txt and CSV files using Notepad++ and MS Excel respectively. Since the tweet data is dense with multiple parameters, traditional notepad may not be able to show it properly. <br><br>



⦁ This project was done with the following experimental setup:

Our experimental setup consisted of an Intel i7 7700k processor, Nvidia 1050Ti (768 Cuda Cores, 4 Gb GDDR5 Frame Buffer), 8 Gb system memory, Nvidia Cuda Toolkit, and Python version 3.6.4 with Nltk, Plotly, Matplotlib, and other relevant packages. We mostly aimed for Unicode, gibberish words, and URL removal, as they generally keep minimum to no impact on the extraction of underlying meaning or opinion of a natural English text. On the other hand, we did not eliminate the emoticons or emojis from their native tweets, as emojis can be a useful key to determine the flavor of a text. Moreover, modern Python libraries such as Textblob handles emojis really well for further processing. <br><br><br><br><br>




-By Sourav Das.
