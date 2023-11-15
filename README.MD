
# PySpark Data Pipeline

This project implements a scalable data pipeline using PySpark, providing plugable transformation functions and support for reading/writing data in multiple formats.

## Project Structure

- **data_pipeline.py**: Main script for orchestrating the data pipeline.
- **transformations.py**: Module containing plugable transformation functions.
- **connectors.py**: Module containing connector classes for reading and writing data.
- **setup.py**: Package definition file.
- **README.md**: Project documentation.

## Prerequisites

1. Python 3.x installed.
2. PySpark library installed (`pip install pyspark`).
3. Access to a Hadoop environment for testing the pipeline.

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/srihari667/pythonProject.git
   cd your-repo
   ```

2. Install project dependencies:

   ```bash
   pip install -e .
   ```

## Usage

1. Edit the configuration in `data_pipeline.py`:

   - Adjust input/output paths.
   - Modify transformation parameters.

2. Run the data pipeline:

   ```bash
   python data_pipeline.py
   ```

## Connector-based Design

The project follows a connector-based design to handle data input/output. The `connectors.py` module contains classes for reading and writing data from/to Hadoop.

## Supported Data Formats

The pipeline supports reading and writing data in multiple formats, including JSON, Parquet, and Gzip.

## Contributing

If you'd like to contribute to this project, please follow the [contribution guidelines](CONTRIBUTING.md).

## CI/CD Notes

The project is set up for continuous integration and deployment. Refer to the CI/CD configuration file for details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.