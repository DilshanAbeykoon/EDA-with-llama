# 📊 EDA with LLaMA - Automated Exploratory Data Analysis

An intelligent data analysis application that combines the power of **Streamlit**, **Python data science libraries**, and **LLaMA 2** to provide automated exploratory data analysis (EDA) with natural language insights.

## 🚀 Features

- **CSV File Upload & Processing**: Robust file handling with multiple encoding support
- **Interactive Data Visualization**: 
  - Histograms with KDE
  - Box plots for outlier detection
  - Correlation heatmaps
- **AI-Powered Insights**: Integration with LLaMA 2 for intelligent data analysis and summaries
- **User-Friendly Interface**: Clean, responsive Streamlit web application
- **Data Quality Assessment**: Automatic missing value detection and summary statistics

## 🛠️ Technologies Used

- **Python 3.x**
- **Streamlit** - Web application framework
- **Pandas** - Data manipulation and analysis
- **Matplotlib & Seaborn** - Data visualization
- **LLaMA 2** - Large Language Model for AI insights
- **Ollama** - Local LLM runtime

## 📋 Prerequisites

- Python 3.7+
- Ollama installed locally
- LLaMA 2 model downloaded via Ollama

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/DilshanAbeykoon/EDA-with-llama.git
   cd EDA-with-llama
   ```

2. **Install required packages**
   ```bash
   pip install streamlit pandas matplotlib seaborn
   ```

3. **Install and setup Ollama**
   ```bash
   # Install Ollama (visit https://ollama.ai for platform-specific instructions)
   ollama pull llama2
   ```

## 🚀 Usage

1. **Start the Streamlit application**
   ```bash
   streamlit run app.py
   ```

2. **Upload your CSV file** through the web interface

3. **Explore visualizations** automatically generated from your data

4. **Get AI insights** by clicking "Generate LLaMA Summary"

## 📁 Project Structure

```
EDA-with-llama/
├── app.py              # Main Streamlit application
├── eda_utils.py        # Utility functions for EDA prompt generation
├── README.md           # Project documentation
└── requirements.txt    # Python dependencies (if added)
```

## 🎯 Key Functionalities

### Data Processing
- **Multi-encoding support**: Handles various CSV file encodings (UTF-8, Latin-1, etc.)
- **Data type detection**: Automatic identification of numeric and categorical columns
- **Missing value analysis**: Comprehensive missing data assessment

### Visualizations
- **Distribution Analysis**: Histograms with kernel density estimation
- **Outlier Detection**: Box plots for identifying data anomalies
- **Correlation Analysis**: Heatmaps showing relationships between variables

### AI Integration
- **Automated Prompt Generation**: Creates structured prompts for LLaMA based on data characteristics
- **Natural Language Insights**: Leverages LLaMA 2 for human-readable data analysis summaries
- **Error Handling**: Robust error management for AI model interactions

## 🔍 Technical Highlights

- **Modular Design**: Separation of concerns with utility functions
- **Error Handling**: Comprehensive exception management
- **Performance Optimization**: Efficient data processing for large datasets
- **User Experience**: Intuitive interface with progress indicators

## 🌟 Skills Demonstrated

- **Data Science**: Pandas, statistical analysis, data visualization
- **Web Development**: Streamlit application development
- **AI/ML Integration**: Working with large language models
- **Software Engineering**: Clean code, modular architecture, error handling
- **Problem Solving**: Automated EDA workflow design

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

**Dilshan Abeykoon**
- GitHub: [@DilshanAbeykoon](https://github.com/DilshanAbeykoon)
- Email: dilshanyasantha1999@gmail.com

---

*This project demonstrates proficiency in data science, AI integration, and full-stack application development - perfect for data analyst, data scientist, and ML engineer roles.*