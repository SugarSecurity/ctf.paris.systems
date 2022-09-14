import type { NextPage } from 'next'
import { useRouter } from "next/router"

import Head from 'next/head'
import Image from 'next/image'
import styles from '../styles/Home.module.css'

const Home: NextPage = () => {

  const router = useRouter();
  const { locale } = router;

  const switchLanguage = (e: { target: { value: any } }) => {
    const locale = e.target.value;
    router.push('/','/', { locale });
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
                  Welcome to Paris!
        </h1>

        <p className={styles.description}>
          select language:
          <select
            onChange={switchLanguage}
            defaultValue={locale}
          >
            <option value="en">EN</option>
            <option value="es">ES</option>
          </select>
        </p>
      </main>

      <footer className={styles.footer}>
        
      </footer>
    </div>
  )
}

export default Home
