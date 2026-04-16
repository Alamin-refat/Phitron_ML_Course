import streamlit as st


# Title

st.title("Note Summary and Quiz Generator")
st.markdown("Upload upto 3 images to generate Note summary and Quizzes")
st.divider()

# sidebar

with st.sidebar:
    st.header("Controls")
    
    # Image uploader
    
    images = st.file_uploader(
        "Upload the photos of your note",
        type=["jpg", "jpeg", "png"],
        accept_multiple_files=True,
        
    )
    
    if images:
        if len(images) > 3:
            st.error("Upload at max 3 images")
            
        else:
            
            st.subheader("Uploaded Images")
            
            col = st.columns(len(images))
            
            for i,img in enumerate(images):
                with col[i]:
                    st.image(img)
                    
                    
    # Difficulty level selection
    
    st.selectbox(
        "Enter the difficulty of your quiz",
        ("Easy", "Medium", "Hard"),
        index=None
    )