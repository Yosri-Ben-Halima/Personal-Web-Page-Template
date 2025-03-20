import streamlit as st
from PIL import Image
import requests
from io import BytesIO
from bs4 import BeautifulSoup

# Set page configuration
st.set_page_config(page_title="Yosri Ben Halima | Portfolio", page_icon=":wave:", layout="wide")

# Custom CSS for sophisticated styling
st.markdown("""
    <style>
    /* Global settings */
    body {
        background-color: #ffffff;
        font-family: 'Arial', sans-serif;
    }
    
    h1, h2, h3, h4, h5, h6 {
        color: #333333;
    }

    /* Profile picture */
    .profile-pic {
        border-radius: 50%;
        margin-bottom: 20px;
    }

    /* Title and subtitle */
    .title {
        font-size: 2.5rem;
        font-weight: bold;
        color: #2c3e50;
    }
    .subtitle {
        text-align: center;
        font-size: 1.2rem;
        color: #7f8c8d;
        margin-bottom: -50px;
    }

    /* Summary section */
    .summary {
        font-size: 1.1rem;
        color: #34495e;
        margin-bottom: 20px;
    }

    /* Contact Information box */
    .contact-box {
        width: 800px; /* Set your desired width */
        /* border: 1px solid #ddd; */
        margin: 0 auto; /* Center align */
        padding: 20px;
        margin-top: 30px;
        border-radius: 10px;
        background-color: #F0F8FF;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
    }
    .contact-info {
        font-size: 1rem;
        margin-top: 15px;
    }
    .contact-info a {
        text-decoration: none;
        color: #2980b9;
    }
    .icon {
        margin-right: 10px;
    }

    /* Portfolio section */
    .project-thumbnail {
        border: none;
        width: 100%;
        height: auto;
        border-radius: 15px;
        transition: transform 0.3s ease;
    }
    .project-thumbnail:hover {
        transform: scale(1.05);
    }
    .project-title {
        color: #2c3e50;
        font-size: 1.3rem;
        margin-top: 15px;
    }
    .project-description {
        color: #7f8c8d;
    }

    /* Footer */
    .footer {
        margin-top: 50px;
        text-align: center;
        color: #8e9193c7;
        font-size: 0.9rem;
    }

        /* Sidebar */
    /* Sidebar styling */
        .sidebar {
            position: fixed;
            top: 0;
            left: 0;
            width: 250px;
            height: 100vh;
            background-color: #54CFD4;
            padding: 20px;
            box-shadow: 5px 0 5px rgba(0,0,0,0.1);
            border-right: 1px solid #ddd;
            overflow-y: auto; /* Scroll if content overflows */
        }

         .sidebar .sidebar-content {
            background-color: #ffffff; /* Set your desired secondary background color */
        }   

        /* Sidebar heading */
        .sidebar h2 {
            font-size: 1.5rem;
            color: #ffffff;
            margin-bottom: 20px;
            border-bottom: 2px solid #ffffff;
            padding-bottom: 10px;
        }

        /* Sidebar links */
        .sidebar a {
            display: block;
            margin: 15px 0;
            color: #ffffff;
            text-decoration: none;
            font-size: 1.1rem;
            position: relative;
            transition: color 0.3s ease, transform 0.3s ease; /* Smooth transitions */
        }

        /* Animated underline for sidebar links */
        .sidebar a::after {
            content: '';
            position: absolute;
            left: 0;
            bottom: 0;
            width: 0;
            height: 2px;
            background: #31333F; /* Underline color */
            transition: width 0.3s ease; /* Animate width change */
        }

        /* Hover effects for sidebar links */
        .sidebar a:hover {
            color: #31333F; /* Change text color on hover */
            transform: scale(1.05); /* Slightly enlarge the link */
        }

        .sidebar a:hover::after {
            width: 100%; /* Expand underline on hover */
        }

    </style>
""", unsafe_allow_html=True)

# Sidebar with navigation links
st.sidebar.markdown("""
    <div class="sidebar">
        <h2>Navigation</h2>
        <a href="#contact">About Me</a>
        <a href="#skills">My Skills</a>  
        <a href="#portfolio">My Portfolio</a>
        <a href="#resume">My Resume</a>
        <a href="#interests">My Interests</a>     
    </div>
""", unsafe_allow_html=True)

# Main content with sections

# Profile picture
# Create two columns
cols = st.columns([1, 3],vertical_alignment="center")  # Adjust column widths as needed

# Place image in the first column
with cols[0]:
    st.image("DSC_6406-modified.png", width=200, use_container_width=False, output_format='auto', caption=None, clamp=False, channels="RGB")

# Place title and subtitle in the second column
with cols[1]:
    st.markdown('<h1 class="title">Hi, I am Yosri Ben Halima 👋</h1>', unsafe_allow_html=True)
st.markdown('<h2 class="subtitle">Quantitative Researcher | Data Scientist | Data Analyst | Multidisciplinary Engineering Graduate</h2>', unsafe_allow_html=True)


st.markdown('<div id="contact">', unsafe_allow_html=True)

# Contact Information in a separate box
st.markdown("""
<div class="contact-box">
    <h4>About Me</h4>
    <p class="summary">I am a Quant at [LAEVITAS](https://www.laevitas.ch/) and multidisciplinary engineer with a passion for Data Science, AI, and Quantitative Finance. My academic and professional journey has been centered around turning raw data into meaningful insights and solutions. I am constantly exploring new technologies and methodologies to enhance my skillset and stay at the forefront of the field.</p>
    <div class="contact-info">
        <div class="contact-info-column">
            <p><img src="https://img.icons8.com/ios-filled/50/000000/marker.png" width="25" class="icon"> Tunis, Tunisia</p>
            <p><img src="https://img.icons8.com/ios-filled/50/000000/birthday.png" width="25" class="icon"> 04/07/2000</p>
            <p><img src="https://img.icons8.com/ios-filled/50/000000/phone.png" width="25" class="icon"> +216 27 642 212</p>
        </div>
        <div class="contact-info-column">
            <p><img src="https://img.icons8.com/ios-filled/50/000000/email.png" width="25" class="icon"> <a href="mailto:yosri.benhalima@ept.ucar.tn">yosri.benhalima@ept.ucar.tn</a></p>
            <p><img src="https://img.icons8.com/ios-filled/50/000000/linkedin.png" width="25" class="icon"> <a href="https://www.linkedin.com/in/yosri-ben-halima-3553a9221/">Yosri Ben Halima</a></p>
            <p><img src="https://img.icons8.com/ios-filled/50/000000/github.png" width="25" class="icon"> <a href="https://github.com/Yosri-Ben-Halima">Yosri-Ben-Halima</a></p>
        </div>
    </div>
</div>

<style>
.contact-info {
    display: flex;
    justify-content: space-between;
}

.contact-info-column {
    flex: 1;
    margin: 0 10px;
}

.contact-info p {
    margin: 5px 0;
}

.contact-info a {
    color: #2980b9;
    text-decoration: none;
}
</style>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

#Skills
st.markdown('<div id="skills">', unsafe_allow_html=True)

# List of skills
skills = [
    "Data Science",
    "Data Analysis & Visualization",
    "Databases (MongoDB, Redis, etc)",
    "Machine Learning",
    "Deep Learning",
    "Natural Language Processing",
    "Advanced Python Skills",
    "Quantitative Analysis",
    "Applied Mathematics",
    "Stochastic Modeling",
    "Econometric Modeling",
    "Tutoring (Maths, Physics)",
]

# Custom CSS for styling the skills
st.markdown(
    """
    <style>
    .skills-container {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        margin-top: 20px;
        gap: 20px;
    }
    .skills-column {
        display: flex;
        flex-direction: column;
        gap: 20px; /* Space between skills in the column */
    }
    .skill-box {
        background-color: #f0f2f6;
        color: #2c3e50;
        padding: 15px 25px;
        margin: 10px;
        border-radius: 12px;
        font-size: 1rem;
        font-weight: bold;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
        align-items: center; /* Vertically center the text */
        display: flex;
        justify-content: center;
        transition: background-color 0.3s ease, transform 0.3s ease;
        /*cursor: pointer;*/
    }
    .skill-box:hover {
        background-color: #d6dae0;
        transform: translateY(-5px);
    }
    </style>
    """,
    unsafe_allow_html=True
)
# Display skills in a creative layout
st.markdown("## My Skills")
st.markdown("---")
st.markdown('<div class="skills-container">', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)

# Calculate split indices
third = len(skills) // 3
remainder = len(skills) % 3

# Split the skills list into three parts
skills1 = skills[:third + (1 if remainder > 0 else 0)]
skills2 = skills[third + (1 if remainder > 0 else 0):2 * third + (1 if remainder > 1 else 0)]
skills3 = skills[2 * third + (1 if remainder > 2 else 0):]

# Populate the first column
with col1:
    for skill in skills1:
        st.markdown(f'<div class="skill-box">{skill}</div>', unsafe_allow_html=True)

# Populate the second column
with col2:
    for skill in skills3:
        st.markdown(f'<div class="skill-box">{skill}</div>', unsafe_allow_html=True)

# Populate the third column
with col3:
    for skill in skills2:
        st.markdown(f'<div class="skill-box">{skill}</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
st.markdown("---")

st.markdown('<div id="portfolio">', unsafe_allow_html=True)

# Portfolio
st.markdown("## My Portfolio")
st.markdown("---")
# Function to fetch GitHub project details
def fetch_github_repo_info(repo_url):
    repo_name = repo_url.split('/')[-1]
    user_name = repo_url.split('/')[-2]
    api_url = f"https://api.github.com/repos/{user_name}/{repo_name}"
    response = requests.get(api_url)
    if response.status_code == 200:
        repo_info = response.json()
        return repo_info.get('description', 'No description available')
    else:
        return 'Description not available'

def scrape_pinned_repos(github_username):
    url = f"https://github.com/{github_username}"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        pinned_repos = soup.find_all('span', class_='repo')
        
        repo_links = []
        for repo in pinned_repos:
            repo_name = repo.text.strip()
            repo_url = f"https://github.com/{github_username}/{repo_name}"
            repo_links.append(repo_url)
        
        return repo_links
    else:
        print(f"Failed to retrieve GitHub profile for {github_username}")
        return []

# Example usage
github_username = "Yosri-Ben-Halima"  # Replace with your GitHub username

# Adding a loading spinner
with st.spinner("Loading projects..."):
    projects = scrape_pinned_repos(github_username)

for project in projects:
    description = fetch_github_repo_info(project)
    cols = st.columns([1, 3],vertical_alignment='center')
    
    # Thumbnail image wrapped with hyperlink
    thumbnail_html = f"""
    <a href="{project}" target="_blank">
        <img src="https://opengraph.githubassets.com/1/{project[19:]}" class="project-thumbnail">
    </a>
    """
    cols[0].markdown(thumbnail_html, unsafe_allow_html=True)
    
    # Project title and description
    cols[1].markdown(f'<h3 class="project-title"><a href="{project}" target="_blank">{project.split("/")[-1].replace("-", " ")}</a></h3>', unsafe_allow_html=True)
    cols[1].markdown(f'<p class="project-description">{description}</p>', unsafe_allow_html=True)
    st.markdown("---")

st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div id="resume">', unsafe_allow_html=True)

# Resume
resume_thumbnail_path = "Resume.jpg"
resume_pdf_path = "Resume.pdf"

# Display the resume section
st.markdown("## My Resume")
st.markdown("---")


# Display resume thumbnail and description side by side
col1, col2 = st.columns([1, 3], vertical_alignment="center")

with col1:
    st.image(resume_thumbnail_path, width=150, use_container_width =False)

with col2:
    st.markdown("""
    Feel free to grab a PDF copy of my resume for more details on my professional background, experiences, and skills. 
    Click the button below to download the full resume.
    """)
    st.download_button(
        label="Download Resume",
        data=open(resume_pdf_path, "rb").read(),
        file_name="Yosri_Ben_Halima_Resume.pdf",
        mime="application/pdf"
    )

st.markdown('</div>', unsafe_allow_html=True)

# Interests
st.markdown('<div id="interests">', unsafe_allow_html=True)

# List of interests
interests = [
    "Boxing",
    "Tennis",
    "Cycling",
    "Guitar",
    "Violin",
    "Cooking",
    "Traveling",
    "Cultural Exchange",
    "Reading",
    "Running",
    "Coding",
    "Hiking"
]

# Custom CSS for styling the interests
st.markdown(
    """
    <style>
    .interests-container {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        margin-top: 20px;
        gap: 20px;
    }
    .interests-column {
        display: flex;
        flex-direction: column;
        gap: 20px; /* Space between interests in the column */
    }
    .interest-box {
        background-color: #f0f2f6;
        color: #2c3e50;
        padding: 15px 25px;
        margin: 10px;
        border-radius: 12px;
        font-size: 1rem;
        font-weight: bold;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
        align-items: center; /* Vertically center the text */
        display: flex;
        justify-content: center;
        transition: background-color 0.3s ease, transform 0.3s ease;
    }
    .interest-box:hover {
        background-color: #d6dae0;
        transform: translateY(-5px);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Display interests in four columns
st.markdown("---")
st.markdown("## My Interests")
st.markdown("---")

# Create four columns
col1, col2, col3, col4 = st.columns(4)

# Calculate split indices
quarter = len(interests) // 4
remainder = len(interests) % 4

# Split the interests list into four parts
interests1 = interests[:quarter + (1 if remainder > 0 else 0)]
interests2 = interests[quarter + (1 if remainder > 0 else 0):2 * quarter + (1 if remainder > 1 else 0)]
interests3 = interests[2 * quarter + (1 if remainder > 1 else 0):3 * quarter + (1 if remainder > 2 else 0)]
interests4 = interests[3 * quarter + (1 if remainder > 2 else 0):]

# Populate the first column
with col1:
    for interest in interests1:
        st.markdown(f'<div class="interest-box">{interest}</div>', unsafe_allow_html=True)

# Populate the second column
with col2:
    for interest in interests2:
        st.markdown(f'<div class="interest-box">{interest}</div>', unsafe_allow_html=True)

# Populate the third column
with col3:
    for interest in interests3:
        st.markdown(f'<div class="interest-box">{interest}</div>', unsafe_allow_html=True)

# Populate the fourth column
with col4:
    for interest in interests4:
        st.markdown(f'<div class="interest-box">{interest}</div>', unsafe_allow_html=True)

st.markdown("---")

st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
    © 2025 Yosri Ben Halima. All rights reserved.
</div>
""", unsafe_allow_html=True)
