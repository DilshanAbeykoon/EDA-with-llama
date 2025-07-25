import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import subprocess

from eda_utils import generate_eda_prompt

# ---------------------------
def ask_llama(prompt):
    try:
        result = subprocess.run(
            ['ollama', 'run', 'llama2'],
            input=prompt,
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='replace'  # avoids UnicodeDecodeError
        )
        if result.returncode == 0:
            return result.stdout
        else:
            return f"❌ Error calling LLaMA model:\n\n{result.stderr}"
    except Exception as e:
        return f"❌ Unexpected error:\n\n{str(e)}"

# ---------------------------
def show_visualizations(df):
    st.subheader("🔍 Basic Visualizations")

    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
    if len(numeric_cols) == 0:
        st.info("No numeric columns to visualize.")
        return

    col1, col2 = st.columns(2)

    with col1:
        selected_hist = st.selectbox("📊 Select column for Histogram", numeric_cols)
        fig, ax = plt.subplots()
        sns.histplot(df[selected_hist].dropna(), kde=True, ax=ax)
        ax.set_title(f"Histogram of {selected_hist}")
        st.pyplot(fig)

    with col2:
        selected_box = st.selectbox("📦 Select column for Box Plot", numeric_cols)
        fig, ax = plt.subplots()
        sns.boxplot(y=df[selected_box], ax=ax)
        ax.set_title(f"Box Plot of {selected_box}")
        st.pyplot(fig)

    # Correlation heatmap
    if len(numeric_cols) >= 2:
        st.subheader("📌 Correlation Heatmap")
        try:
            corr = df[numeric_cols].corr()
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
            st.pyplot(fig)
        except Exception as e:
            st.warning(f"⚠️ Could not display correlation heatmap: {e}")
    else:
        st.info("ℹ️ Correlation heatmap needs at least two numeric columns.")

# ---------------------------
def main():
    st.set_page_config(page_title="CSV + LLaMA EDA App", layout="wide")
    st.title("📊 CSV EDA with LLaMA")

    uploaded_file = st.file_uploader("📁 Upload a CSV file", type=["csv"])

    if uploaded_file is not None:
        encodings = ['utf-8', 'utf-8-sig', 'latin1', 'ISO-8859-1', 'cp1252']
        df = None

        for enc in encodings:
            try:
                uploaded_file.seek(0)
                df = pd.read_csv(uploaded_file, encoding=enc)
                st.success(f"✅ File successfully read using encoding: `{enc}`")
                break
            except Exception:
                continue

        if df is None:
            st.error("❌ Failed to read the file with supported encodings.")
            return

        st.subheader("🧾 Preview of the Data")
        st.dataframe(df)

        # Visualizations
        show_visualizations(df)

        # EDA Summary Prompt
        st.subheader("🧠 LLaMA-Based EDA Summary")
        eda_prompt = generate_eda_prompt(df)
        st.text_area("📄 Generated Prompt", eda_prompt, height=300)

        if st.button("🔍 Generate LLaMA Summary"):
            with st.spinner("Asking LLaMA..."):
                llama_response = ask_llama(eda_prompt)
            st.subheader("📘 LLaMA's Summary:")
            st.text_area("🦙 Response from LLaMA", llama_response, height=300)

# ---------------------------
if __name__ == "__main__":
    main()
