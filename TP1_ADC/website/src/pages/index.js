import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import Heading from '@theme/Heading';
import styles from './index.module.css';

function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <header className={clsx('hero hero--primary', styles.heroBanner)}>
      <div className="container">
        <Heading as="h1" className="hero__title">
          TP1 ADC: Aplicação de Gestão
        </Heading>
        <p className="hero__subtitle">Faça a gestão completa dos seus Clientes, Produtos e Vendas de forma eficiente e segura pelo terminal.</p>
        <div className={styles.buttons}>
          <Link
            className="button button--secondary button--lg"
            to="/docs/intro">
            Comece a usar ⏱️
          </Link>
        </div>
      </div>
    </header>
  );
}

export default function Home() {
  return (
    <Layout
      title={`Gestão Fácil`}
      description="Site da Aplicação de Gestão desenvolvida para TP1 ADC.">
      <HomepageHeader />
      <main>
        <section style={{padding: '4rem 0', textAlign: 'center'}}>
          <h2>O seu parceiro de negócio</h2>
          <p>
            Desenvolvida de forma robusta e persistente, esta ferramenta ajuda-o a controlar 
            totalmente a sua faturação, verificar os seus relatórios e acompanhar o stock em tempo real.
          </p>
        </section>
      </main>
    </Layout>
  );
}
