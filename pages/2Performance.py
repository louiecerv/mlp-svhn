#Input the relevant libraries
import numpy as np
import pandas as pd
import streamlit as st
import altair as alt
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances_argmin
from sklearn.metrics.pairwise import pairwise_distances
from sklearn.metrics import silhouette_score

# Define the Streamlit app
def app():
    st.subheader('Performance of the K-Means Classifier')
    n_clusters = st.session_state.n_clusters
    X = st.session_state.X
    y = st.session_state.y
    
    # WCSS (Within Cluster Sum of Squares) list
    wcss_list = []

    # Silhouette score list
    silhouette_scores = []

    # Try different numbers of clusters
    for k in range(2, 11):
        # Create KMeans object
        kmeans = KMeans(n_clusters=k, random_state=0)

        # Fit the model to the data
        kmeans.fit(X)

        # Calculate WCSS
        wcss = kmeans.inertia_
        wcss_list.append(wcss)

        # Calculate Silhouette score
        silhouette_score_val = silhouette_score(X, kmeans.labels_)
        silhouette_scores.append(silhouette_score_val)

    # WCSS vs Number of Clusters plot
    fig, ax = plt.subplots()
    ax.plot(range(2, 11), wcss_list)
    ax.set_xlabel("Number of Clusters")
    ax.set_ylabel("WCSS")
    ax.set_title("WCSS vs Number of Clusters")
    st.pyplot(fig)

    # Silhouette Score vs Number of Clusters plot
    fig, ax = plt.subplots()
    ax.plot(range(2, 11), silhouette_scores)
    ax.set_xlabel("Number of Clusters")
    ax.set_ylabel("Silhouette Score")
    ax.set_title("Silhouette Score vs Number of Clusters")
    st.pyplot(fig)

#run the app
if __name__ == "__main__":
    app()
