import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="FatCat AI | LLM Mention Scorer", layout="wide")

st.markdown("""
    <style>
        .stApp {
            background-color: #1e1e2e;
        }
        [data-testid="stHeader"] {
            background-color: transparent;
        }
        [data-testid="stMetricValue"] {
            color: #89dceb !important;
            font-family: 'Courier New', Courier, monospace;
            font-weight: bold;
        }
        [data-testid="stMetricLabel"] {
            color: #f38ba8 !important;
            font-family: 'Courier New', Courier, monospace;
            font-size: 1.2rem !important;
        }
        h1, h2, h3 {
            color: #f5c2e7 !important;
            font-family: 'Courier New', Courier, monospace;
        }
    </style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    try:
        df = pd.read_csv("LLM_GEO_AISEO_Checklist_Mention_Scorer.csv")
        
        # Ensure LLM columns are treated as booleans for summing
        bool_cols = ['Google AI', 'Perplexity', 'ChatGPT', 'Claude']
        for col in bool_cols:
            if col in df.columns:
                df[col] = df[col].astype(bool)
                
        return df
    except FileNotFoundError:
        return None

def main():
    st.title("FatCat AI : Generative Engine Share-of-Voice")

    df = load_data()

    if df is None:
        st.warning("⚠️ CSV file 'LLM_GEO_AISEO_Checklist_Mention_Scorer.csv' not found. Please ensure it is placed in the root directory.")
        st.stop()

    total_assets = len(df)
    total_points = int(df['Total Points'].sum()) if 'Total Points' in df.columns else 0
    chatgpt_citations = int(df['ChatGPT'].sum()) if 'ChatGPT' in df.columns else 0
    perplexity_citations = int(df['Perplexity'].sum()) if 'Perplexity' in df.columns else 0

    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Tracked Assets", total_assets)
    with col2:
        st.metric("Total Visibility Points", total_points)
    with col3:
        st.metric("ChatGPT Citations", chatgpt_citations)
    with col4:
        st.metric("Perplexity Citations", perplexity_citations)

    st.markdown("---")

    st.subheader("Citation Comparison Across LLMs")
    
    llm_cols = ['Google AI', 'Perplexity', 'ChatGPT', 'Claude']
    llm_counts = {col: int(df[col].sum()) for col in llm_cols if col in df.columns}
    
    chart_df = pd.DataFrame(list(llm_counts.items()), columns=['LLM', 'Total Citations'])
    
    fig = px.bar(
        chart_df, 
        x='LLM', 
        y='Total Citations', 
        text='Total Citations',
        template='plotly_dark',
        color='LLM',
        color_discrete_sequence=['#f38ba8', '#89dceb', '#f9e2af', '#a6e3a1']
    )
    fig.update_traces(textposition='outside', textfont_size=14)
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        showlegend=False,
        yaxis_title="Total Direct Mentions",
        xaxis_title=""
    )
    
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    st.subheader("Raw Mention Data")
    st.dataframe(df, use_container_width=True, hide_index=True)

if __name__ == "__main__":
    main()