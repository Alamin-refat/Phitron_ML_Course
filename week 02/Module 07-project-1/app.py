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
    
    selected_option = st.selectbox(
        "Enter the difficulty of your quiz",
        ("Easy", "Medium", "Hard"),
        index=None
    )
    
    
    
    # Generate button
    
    pressed = st.button("Click the button to initiate AI",type="primary")
    
    
    
if pressed:
    if not images:
        st.error("You must upload at least one image to generate the quiz.")
        
    if not selected_option:
        st.error("You must select a difficulty level to generate the quiz.")
        
    if images and selected_option:
        
        # Note
        with st.container(border=True):
            st.subheader("Your Note")
            
            # The portion below will be replace by API call
            st.text("Note will be shown here")
        
        
        # Audio transcription
        with st.container(border=True):
            st.subheader("Audio transcription")
            
            # The portion below will be replace by API call
            st.text("Audio transcription will be shown here")
            
        
        # Quiz
        with st.container(border=True):
            st.subheader(f"Quiz ({selected_option}) Difficulty")
            
            # The portion below will be replace by API call
            st.text("Quiz will be shown here")