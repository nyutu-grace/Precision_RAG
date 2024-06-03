# Precision_RAG
The main of this project is to improve on the three key services of the company.ie: Automatic Prompt Generation, Automatic Evaluation Data Generation, and Prompt Testing and Ranking.

## Project Structure
```
PRECISION_RAG/
├── docs/
│   └── api_documentation.md
├── notebooks/
├── src/
│   ├── evaluation/
│   │   ├── __init__.py
│   │   └── evaluation_data_generator.py
│   ├── frontend/
│   │   ├── node_modules/
│   │   ├── public/
│   │   │   └── ...
│   │   ├── src/
│   │   │   └── ...
│   │   ├── .gitignore
│   │   ├── package-lock.json
│   │   ├── package.json
│   │   └── README.md
│   ├── prompt_generation/
│   │   ├── __init__.py
│   │   └── prompt_generator.py
│   ├── tests/
│   │   └── __init__.py
│   ├── utils/
│   │   └── __init__.py
│   └── main.py
├── venv/
├── .gitignore
├── LICENSE
└── README.md
```


## Getting Started

### Prerequisites

- Python 3.8+
- Node.js

### Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/username/AmharicNLPDataCollection.git
    cd AmharicNLPDataCollection
    ```

2. **Install Python dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

3. **Install Node.js dependencies:**

    ```sh
    cd frontend
    npm install
    cd ..
    ```

## Usage

### Frontend

- **Start the React app:**

    ```sh
    cd frontend
    npm start
    ```

## Contributing

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add your feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

## License

This project is licensed under the APACHE License.

