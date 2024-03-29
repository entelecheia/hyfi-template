# HyFI Template

[![pypi-image]][pypi-url]
[![version-image]][release-url]
[![release-date-image]][release-url]
[![license-image]][license-url]
[![codecov][codecov-image]][codecov-url]
[![jupyter-book-image]][docs-url]

<!-- Links: -->

[codecov-image]: https://codecov.io/gh/entelecheia/hyfi-template/branch/main/graph/badge.svg?token=CEUCMPZM9F
[codecov-url]: https://codecov.io/gh/entelecheia/hyfi-template
[pypi-image]: https://img.shields.io/pypi/v/hyfi-template
[license-image]: https://img.shields.io/github/license/entelecheia/hyfi-template
[license-url]: https://github.com/entelecheia/hyfi-template/blob/main/LICENSE
[version-image]: https://img.shields.io/github/v/release/entelecheia/hyfi-template?sort=semver
[release-date-image]: https://img.shields.io/github/release-date/entelecheia/hyfi-template
[release-url]: https://github.com/entelecheia/hyfi-template/releases
[jupyter-book-image]: https://jupyterbook.org/en/stable/_images/badge.svg
[repo-url]: https://github.com/entelecheia/hyfi-template
[pypi-url]: https://pypi.org/project/hyfi-template
[docs-url]: https://hyfi-template.entelecheia.ai
[changelog]: https://github.com/entelecheia/hyfi-template/blob/main/CHANGELOG.md
[contributing guidelines]: https://github.com/entelecheia/hyfi-template/blob/main/CONTRIBUTING.md

<!-- Links: -->

A GitHub Template Repository for HyFI-based Projects

- Documentation: [https://hyfi-template.entelecheia.ai][docs-url]
- GitHub: [https://github.com/entelecheia/hyfi-template][repo-url]
- PyPI: [https://pypi.org/project/hyfi-template][pypi-url]

HyFI-Template is a ready-to-use GitHub template repository designed to streamline the process of initializing new projects based on HyFI, a robust framework for building interfaces for Python applications. HyFI leverages the power of the Hydra configuration system and the Pydantic data validation library, offering a comprehensive set of tools to create flexible and adaptable interfaces for various Python projects.

## Features

HyFI-Template provides an ideal starting point for developers looking to build projects using the HyFI framework, with key features including:

- **Pre-configured structure**: The template repository comes with a pre-defined project structure, ensuring a consistent and organized layout for HyFI-based applications.

- **Quick project initialization**: With the `make init-project` command, developers can easily initialize a new project, automatically setting up the necessary files, directories, and configurations.

- **Hydra integration**: The template repository is built around the Hydra configuration system, providing a flexible and powerful foundation for managing configurations in HyFI-based projects.

- **Pydantic integration**: HyFI-Template incorporates the Pydantic data validation library, allowing developers to easily define and validate data structures for their application interfaces.

- **Best practices**: The template repository follows industry best practices for Python project organization and structure, ensuring that developers have a solid starting point for building high-quality applications.

- **Customizable**: Developers can easily customize the template repository to suit their specific requirements and preferences, tailoring it to the needs of their projects.

- **Documentation**: The template repository includes clear instructions and guidelines for getting started with a HyFI-based project, helping developers quickly familiarize themselves with the framework and its features.

### Getting Started

To begin using HyFI-Template for your project, simply follow these steps:

1. Click the "Use this template" button on the [HyFI-Template GitHub repository](https://github.com/entelecheia/hyfi-template) to create a new repository based on the template.
2. Clone the newly created repository to your local machine.
3. Run `make init-project` to initialize the project with the necessary files and configurations.
4. Follow the provided documentation and guidelines to start building your HyFI-based application.

Or you can inject the template into an existing repository:

1. From the root of your repository, run the following command:

   ```bash
   copier copy --trust --data 'code_template_source=gh:entelecheia/hyfi-template' --answers-file .copier-config.yaml gh:entelecheia/hyperfast-python-template .
   ```

2. Follow the provided documentation and guidelines to start building your HyFI-based application.

By using HyFI-Template as the foundation for your project, you'll be well on your way to creating powerful and adaptable interfaces for your Python applications.

## Managing Actions Secrets and Variables in Your Project

When using the HyFI-Template for your project, there are several GitHub Actions secrets and variables that you need to add to ensure proper functioning of the release action and optional JupyterBook deployment.

### Adding PYPI_API_TOKEN and TEST_PYPI_API_TOKEN

To automate the release process of your project to PyPI, you need to provide two tokens: `PYPI_API_TOKEN` and `TEST_PYPI_API_TOKEN`. These tokens will be used by the GitHub Actions workflow to authenticate with PyPI and TestPyPI, respectively.

1. Generate an API token for your PyPI account by following the instructions in the [official PyPI documentation](https://pypi.org/manage/account/token/).
2. Generate an API token for your TestPyPI account by following the instructions in the [official TestPyPI documentation](https://test.pypi.org/manage/account/token/).
3. In your GitHub repository, go to the "Settings" tab and click on "Secrets" in the left sidebar.
4. Click the "New repository secret" button.
5. Add the `PYPI_API_TOKEN` secret with the value set to the token generated for your PyPI account.
6. Add the `TEST_PYPI_API_TOKEN` secret with the value set to the token generated for your TestPyPI account.

By providing these tokens, your project's release action will have the necessary permissions to publish your package to PyPI and TestPyPI.

### Optionally Adding CNAME for JupyterBook Deployment

If you plan to deploy the JupyterBook documentation to a custom domain, you'll need to add a `CNAME` variable to your GitHub repository.

1. In your GitHub repository, go to the "Settings" tab and click on "Pages" in the left sidebar.
2. Follow the instructions to configure your custom domain.
3. In your GitHub repository, go to the "Settings" tab and click on "Repository Variables" in the left sidebar.
4. Click the "New repository variable" button.
5. Add a new variable with the key `CNAME` and set the value to your custom domain (e.g., `your-custom-domain.com`).

By adding the `CNAME` variable, the GitHub Pages action in your `deploy-docs.yaml` workflow will properly configure the deployment to use your custom domain.

With the `CNAME` repository variable properly configured, your project will be set up to handle JupyterBook deployment to your custom domain effectively.

## Changelog

See the [CHANGELOG] for more information.

## Contributing

Contributions are welcome! Please see the [contributing guidelines] for more information.

## License

This project is released under the [MIT License][license-url].
