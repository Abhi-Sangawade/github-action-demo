const buildInfo = {
  environment: import.meta.env.VITE_ENV || 'production',
  build_commit: import.meta.env.VITE_BUILD_COMMIT || 'unknown',
  build_time: import.meta.env.VITE_BUILD_TIME || 'not available',
  build_image: import.meta.env.VITE_BUILD_IMAGE || 'local',
  deploy_host: import.meta.env.VITE_DEPLOY_HOST || 'AWS EC2',
  app_url: window.location.origin,
};

const examples = {
  react: `// React example - simple portfolio card
// Docs: https://reactjs.org/docs/getting-started.html
import React from 'react';

function PortfolioCard() {
  return <div className="card">React portfolio powered by modern UI.</div>;
}

export default PortfolioCard;`,
  angular: `// Angular example - minimal component
// Docs: https://angular.io/docs
import { Component } from '@angular/core';

@Component({
  selector: 'app-portfolio',
  template: '<div class="card">Angular portfolio component</div>'
})
export class PortfolioComponent {}`,
  javascript: `// Plain JavaScript example - add interactivity
// Reference: https://developer.mozilla.org/en-US/docs/Web/JavaScript
const cards = document.querySelectorAll('.card');

cards.forEach(card => {
  card.addEventListener('click', () => {
    console.log('Portfolio card clicked');
    card.classList.toggle('active');
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
          <span className="badge">DevOps Engineer — Your Name</span>
          <h1>Your Name — DevOps Engineer</h1>
          <p>
            I build reliable CI/CD pipelines, automate cloud infrastructure, and create developer-facing dashboards. This portfolio highlights projects and practical command snippets for core DevOps tools.
          </p>
          <p>
            Contact: <a href="mailto:you@example.com">you@example.com</a> · <a href="https://github.com/your-username" target="_blank" rel="noreferrer">GitHub</a>
          </p>
        </div>
        <div className="summary-card">
          <strong>Profile</strong>
          <p>Infrastructure, CI/CD, Monitoring</p>
        </div>
      </header>

      <section className="grid-overview">
        <article className="feature-card">
          <strong>Projects</strong>
          <p>CI/CD pipelines, infra-as-code, observability</p>
        </article>
        <article className="feature-card">
          <strong>Tools</strong>
          <p>Docker, Kubernetes, Terraform, AWS</p>
        </article>
        <article className="feature-card">
          <strong>Monitoring</strong>
          <p>Prometheus, Grafana, Alerting</p>
        </article>
        <article className="feature-card">
          <strong>SRE</strong>
          <p>Incident response & runbooks</p>
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
        <h2>Selected Projects</h2>
        <div className="code-grid">
          <div className="code-section">
            <h3>CI/CD Pipeline (GitLab + Kubernetes)</h3>
            <p>Automated build, test, and deploy using GitLab CI, Docker images, and a K8s cluster with rolling updates.</p>
            <a href="#">Repository / Docs (replace with link)</a>
          </div>
          <div className="code-section">
            <h3>Infrastructure as Code</h3>
            <p>Modular Terraform code for VPC, EKS, RDS with remote state and CI validation.</p>
            <a href="#">Terraform modules (replace with link)</a>
          </div>
          <div className="code-section">
            <h3>Monitoring & Alerts</h3>
            <p>Prometheus scraping, Grafana dashboards, and Alertmanager for on-call alerts.</p>
            <a href="#">Dashboards (replace with link)</a>
          </div>
        </div>
      </section>

      <section className="content-section">
        <h2>DevOps Tools Cheat Sheet</h2>
        <div className="code-grid">
          <CodeBlock title="Linux (SSH & system)" code={`ssh -i ~/.ssh/id_rsa ec2-user@1.2.3.4\nsudo journalctl -u my-service -f\nss -tuln`} />
          <CodeBlock title="Docker" code={`docker build -t my-app:latest .\ndocker run -d --name my-app -p 5000:5000 my-app:latest\ndocker logs -f my-app`} />
          <CodeBlock title="Terraform" code={`terraform init\nterraform plan -out=tfplan\nterraform apply tfplan`} />
          <CodeBlock title="Kubernetes (kubectl)" code={`kubectl get pods -A\nkubectl rollout status deployment/my-app\nkubectl logs -f deployment/my-app`} />
          <CodeBlock title="AWS CLI" code={`aws s3 ls\naws ec2 describe-instances --region us-east-1`} />
          <CodeBlock title="Jenkins / GitLab CI" code={`# Jenkins: java -jar jenkins-cli.jar -s http://jenkins:8080 build my-job\n# GitLab CI: use .gitlab-ci.yml to define pipelines`} />
        </div>
      </section>

      <section className="notes">
        <h2>Personalize this portfolio</h2>
        <p>
          Replace "Your Name", contact info, and project links above with your real details. Tell me what to insert and I will update the page for you.
        </p>
      </section>
    </div>
  );
}

export default App;
