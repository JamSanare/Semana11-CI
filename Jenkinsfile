pipeline {
  agent any
  options { timestamps() }
  triggers { pollSCM('H/2 * * * *') }
  environment {
    PATH = "/usr/local/bin:/opt/homebrew/bin:/Applications/Docker.app/Contents/Resources/bin:${env.PATH}"
    SOAK_DURATION = '1m'
    PASO = '10'
    TL_URL = 'http://localhost:8082/lib/api/xmlrpc/v1/xmlrpc.php'
    PIPELINE_ID = "jenkins-${env.BUILD_NUMBER}"
    REPORT_URL = "${env.BUILD_URL}"
  }
  stages {
    stage('Checkout') { steps { checkout scm; sh 'rm -rf reports && mkdir -p reports' } }
    stage('Build') { steps { sh 'mkdir -p reports && docker compose --profile tests build' } }
    stage('Environment') { steps { sh 'docker compose up -d --wait tiendademo' } }
    stage('Unit Tests') { steps { sh 'echo "Sin pruebas unitarias en el proyecto"' } }
    stage('Selenium') {
      steps { catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') { sh 'docker compose --profile tests run --rm -T selenium-runner' } }
    }
    stage('Playwright') {
      steps { catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') { sh 'docker compose --profile tests run --rm -T playwright-runner' } }
    }
    stage('Functional') {
      steps { catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') { sh 'docker compose --profile tests run --rm -T aulanova-runner' } }
    }
    stage('Performance') {
      steps { catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') { sh '''
        set -o pipefail
        docker compose --profile tests run --rm -T aulanova-runner bash pruebas/scripts/ejecutar.sh rendimiento | tee reports/rendimiento.log
        bash scripts/gate_k6.sh reports/rendimiento.log rendimiento
      ''' } }
    }
    stage('Stress') {
      steps { catchError(buildResult: 'UNSTABLE', stageResult: 'UNSTABLE') { sh '''
        set -o pipefail
        docker compose --profile tests run --rm -T aulanova-runner bash pruebas/scripts/ejecutar.sh estres | tee reports/estres.log
        bash scripts/gate_k6.sh reports/estres.log estres
      ''' } }
    }
    stage('Security') {
      steps { catchError(buildResult: 'UNSTABLE', stageResult: 'UNSTABLE') { sh '''
        set -o pipefail
        docker compose --profile tests run --rm -T aulanova-runner bash pruebas/scripts/ejecutar.sh seguridad | tee reports/seguridad.log
        bash scripts/gate_k6.sh reports/seguridad.log seguridad
      ''' } }
    }
    stage('TestLink') {
      steps {
        withCredentials([string(credentialsId: 'TL_API_KEY', variable: 'TL_API_KEY'), string(credentialsId: 'TL_PLAN_ID', variable: 'TL_PLAN_ID')]) {
          sh 'python3 scripts/tl_create_build.py; python3 scripts/k6_to_csv.py && python3 scripts/testlink_reporter.py'
        }
      }
    }
  }
  post {
    always {
      archiveArtifacts artifacts: 'reports/**, evidencias/**, evidencias-playwright/**', allowEmptyArchive: true
      junit testResults: 'reports/**/*.xml', allowEmptyResults: true
      sh 'docker compose --profile tests down -v --remove-orphans || true'
    }
  }
}
