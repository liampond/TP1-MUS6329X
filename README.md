# Projet (TP1) pour MUS6329X: Projects en informatique musicale à l'Université de Montréal avec Prof. Dominic Thibault.
### Project (TP1) for MUS6329X: Projects in Computer Music at the University of Montréal with Prof. Dominic Thibault.

---

This project pulls real-time weather data from the [tomorrow.io](tomorrow.io) API. A small database was manually created that maps temperature, humidity, and wind speed to six parameters of a mono synthesizer. Machine learning was then used to interpolate these values in real-time based on the weather data provided by the API.

In order to use the API, you will need to get an API key. Go to [tomorrow.io](tomorrow.io), select Products -> Weather API -> Sign up/Login (verified as of May 2025). Your API key should be displayed at the top of the webpage. Do not share this with anyone. Then, modify the .env file by replacing 'YOUR_API_KEY_HERE' with your API key from tomorrow.io. The default location is set to Montréal. 
