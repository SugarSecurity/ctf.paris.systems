import type { NextPage } from 'next';
import { useRouter } from "next/router";

import Head from 'next/head'
import Image from 'next/image'
import styles from '../styles/Home.module.css'

export async function getWelcomeText(target_lang: any) {
  if (typeof target_lang === 'undefined') {
    target_lang = "en";
  }
  const translation_api_url = "https://ctf-api.paris.systems/welcome?lang=" + target_lang;
  const api_response = await fetch(translation_api_url);
  const api_response_json = await api_response.json();
  return api_response_json;
}

const welcome_text = getWelcomeText("en");

const Home: NextPage = () => {
  const router = useRouter();

  //const welcome_text = "test"
  //const welcome_text = getWelcomeText("en");

  const switchLanguage = (target_lang: string) => {
    console.log(target_lang);
    const welcome_text = getWelcomeText(target_lang);
    console.log(welcome_text)
    router.push('/', '/', { locale: target_lang});
  }

  return (
    <div className={styles.container}>
      <Head>
        <title>Paris CTF</title>
        <meta name="description" content="by sugarsecurity.com" />
        <link rel="icon" href="/tower.png" />
      </Head>

      <main className={styles.main}>
        <h1 className={styles.title}>
          <span className={styles.logo}>
            <Image src="/tower.png" alt="Eiffel Tower" width={60} height={100}/>
          </span>
        </h1>

        <p className={styles.description}>
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
      </main>

      <footer className={styles.footer}>
        
      </footer>
    </div>
  )
}

export default Home
