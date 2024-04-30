class SimulatedCICDPipeline:
    def __init__(self):
        self.docker_images = {}

    def build(self, project_name, version):
        print(f"Building Docker image for {project_name}:{version}...")
        self.docker_images[project_name] = version
        print(f"Docker image for {project_name}:{version} build successfully.")

    def test(self, project_name):
        print(f"Running tests for {project_name}...")
        test_results = 'All tests passed'
        print(f"Test results for {project_name}: {test_results}")

    def deploy(self, project_name, environment):
        print(f"Deploying {project_name} to {environment}...")
        print(f"{project_name} deployed to {environment}")

    def pipeline(self, project_name, version, environment):
        self.build(project_name, version)
        self.test(project_name)
        self.deploy(project_name, environment)


pipeline = SimulatedCICDPipeline()
pipeline.pipeline('my_awesome_app', '1.0.0', 'production')