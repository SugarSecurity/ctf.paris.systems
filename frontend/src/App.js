import './App.css';
import { useState, useEffect } from 'react';

function App() {

  const [welcome_text, setWelcomeText] = useState('');

  useEffect(() => {
    switchLanguage('en');
  }, []);

  const switchLanguage = async (target_lang) => {
    const translation_api_url = "https://ctf-api.paris.systems/welcome?lang=" + target_lang;
    const api_response = await fetch(translation_api_url);
    const api_response_json = await api_response.json();
    setWelcomeText(await api_response_json.translated_welcome);
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>{welcome_text}</h1>
        <img src="./tower.png" className="App-logo" alt="logo" />
        <p>
        select language:
          <select
            onChange={(event) => {
              switchLanguage(event.target.value)
            }}
            defaultValue="en"
          >
            <option value="en">EN</option>
            <option value="es">ES</option>
            <option value="fr">FR</option>
          </select>
        </p>
      </header>
    </div>
  );
}

export default App;
