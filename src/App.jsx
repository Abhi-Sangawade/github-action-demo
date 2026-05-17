const buildInfo = {
  environment: import.meta.env.VITE_ENV || 'production',
  build_commit: import.meta.env.VITE_BUILD_COMMIT || 'unknown',
  build_time: import.meta.env.VITE_BUILD_TIME || 'not available',
  build_image: import.meta.env.VITE_BUILD_IMAGE || 'local',
  deploy_host: import.meta.env.VITE_DEPLOY_HOST || 'AWS EC2',
  app_url: window.location.origin,
};

const examples = {
  react: `import React from 'react';

function PortfolioCard() {
  return <div className="card">React portfolio powered by modern UI.</div>;
}

export default PortfolioCard;`,
  angular: `import { Component } from '@angular/core';

@Component({
  selector: 'app-portfolio',
  template: '<div class="card">Angular portfolio component</div>'
})
export class PortfolioComponent {}`,
  javascript: `const cards = document.querySelectorAll('.card');

cards.forEach(card => {
  card.addEventListener('click', () => {
    console.log('Portfolio card clicked');
  });
});`,
};

function CodeBlock({ title, code }) {
  return (
    <section className="code-section">
      <h3>{title}</h3>
      <pre>{code}</pre>
    </section>
  );
}

function App() {
  return (
    <div className="app-shell">
      <header className="hero">
        <div>
          <span className="badge">Frontend DevOps Portfolio</span>
          <h1>React, Angular, JavaScript Portfolio</h1>
          <p>
            A frontend-focused portfolio site for a DevOps engineer. This project uses React and Vite to showcase frontend skills, with sample Angular and JavaScript snippets.
          </p>
        </div>
        <div className="summary-card">
          <strong>Portfolio focus</strong>
          <p>Frontend + DevOps</p>
        </div>
      </header>

      <section className="grid-overview">
        <article className="feature-card">
          <strong>React</strong>
          <p>Modern component-driven UI</p>
        </article>
        <article className="feature-card">
          <strong>Angular</strong>
          <p>Enterprise frontend framework</p>
        </article>
        <article className="feature-card">
          <strong>JavaScript</strong>
          <p>Core scripting and automation</p>
        </article>
        <article className="feature-card">
          <strong>DevOps</strong>
          <p>Build, deploy, monitor</p>
        </article>
      </section>

      <section className="metadata-section">
        <h2>Build metadata</h2>
        <div className="metadata-grid">
          <div>
            <span>Host</span>
            <strong>{buildInfo.deploy_host}</strong>
          </div>
          <div>
            <span>Environment</span>
            <strong>{buildInfo.environment}</strong>
          </div>
          <div>
            <span>Commit</span>
            <strong>{buildInfo.build_commit}</strong>
          </div>
          <div>
            <span>Build time</span>
            <strong>{buildInfo.build_time}</strong>
          </div>
        </div>
      </section>

      <section className="content-section">
        <h2>Frontend command cheat sheet</h2>
        <div className="code-grid">
          <CodeBlock title="React sample" code={examples.react} />
          <CodeBlock title="Angular sample" code={examples.angular} />
          <CodeBlock title="JavaScript sample" code={examples.javascript} />
        </div>
      </section>

      <section className="notes">
        <h2>Why frontend?</h2>
        <p>
          Your portfolio should highlight frontend skills for modern web experiences. React and Angular are widely used in developer-facing dashboards, documentation portals, and DevOps UIs.
        </p>
      </section>
    </div>
  );
}

export default App;
