import streamlit as st

st.set_page_config(
    page_title="Data Scientist Portfolio | Chakravarthi",
    layout="centered", # 'wide' or 'centered'
    initial_sidebar_state="expanded", # 'auto', 'expanded', or 'collapsed'
)

with st.sidebar:
    # Profile image (replace with your own)
    # Option 1: From local file
    col1, col2, col3 = st.columns([1,2,1])
    with col2:

        try:
            profile_img = Image.open("LOGO.jpeg")
            st.image(profile_img, width=150)
        except:
        # Option 2: Placeholder if no image available
            st.image("LOGO.jpeg", width=150)
    
    # Name and title
    st.markdown("""
    <div style="text-align: center;">
        <h1>P.N.S.S.Chakravarthi </h1>
        <h4>Data Scientist | Machine Learning Engineer</h3>
    </div>
    """, unsafe_allow_html=True)
    # Contact information
    st.markdown("---")
    st.markdown("### 📞 Contact Info")
    st.markdown("""
    - ✉ *Email:* [chakravarthy.pothureddy@gmail.com](mailto:chakravarthy.pothureddy@gmail.com)
    - 📱 *Phone:* ‪+91 6302867927‬
    - 🩸 *Blood Group:* A+
    - :globe_with_meridians: *Languages Known:* Telugu, English
    - 📍 *Adress:* Vegeswarapuram, Tallapudi, Andhra Pradesh
    """)
    


# --- SIDEBAR ---
#st.sidebar.header("Contact Information")
st.header("Portfolio")
home_tab, about_me_tab, education_tab, internships_tab, skills_tab, projects_tab, certificates_tab, contact_tab = st.tabs([
    "Home", "About Me", "Education", "Internships", "Skills", "Projects", "Certificates", "Contact"
])

with home_tab:
    st.header("🏠Home")
    st.title("👋 Hi, I'm Naga Sairam Srinivasa Chakravarthi Pothureddy")
    st.subheader("Aspiring Data Scientist | Machine Learning Engineer | Data Analyst")

    st.write("""
I'm passionate about building data-driven solutions and machine learning models.  
With hands-on experience in Python, data analysis, and visualization tools, I'm looking for exciting opportunities in data and AI domains.
""")

# ---- RESUME DOWNLOAD ----
    st.header("📄Resume")
    with open("srinivasa_chakravarthi_datascience_fresher_lyros.docx", "rb") as pdf_file:
        PDFbyte = pdf_file.read()

    st.download_button(label="📄 Download Resume", 
                    data=PDFbyte, 
                    file_name="srinivas_resume", 
                    mime='application/octet-stream')

# ---- SOCIAL MEDIA LINKS ----
    st.markdown("### 🔗 Social Networks")

    social_cols = st.columns(4)

    with social_cols[0]:
        st.markdown("[![LinkedIn](https://img.shields.io/badge/-LinkedIn-blue?logo=linkedin&style=flat-square)](https://www.linkedin.com/in/chakravarthipothureddy/)")

    with social_cols[1]:
        st.markdown("[![GitHub](https://img.shields.io/badge/-GitHub-black?logo=github&style=flat-square)](https://github.com/chakravarthipothureddy)")

    with social_cols[2]:
        st.markdown("[![kaggle](https://img.shields.io/badge/-kaggle-1DA1F2?logo=kaggle&style=flat-square)](https://www.kaggle.com/pothureddychakri)")

    with social_cols[3]:
        st.markdown("[![Gmail](https://img.shields.io/badge/-Email-D14836?logo=gmail&style=flat-square)](mailto:chakravarthy.pothureddy@gmail.com)")


with about_me_tab:
    st.header("🙋‍♂ About Me")
    st.write("Hello! I’m Naga Sairam Srinivasa Chakravarthi Pothureddy, a detail-oriented and highly motivated Data Science professional with a passion for transforming raw data into actionable insights. My fascination with predictive analytics and machine learning drives me to solve complex problems and deliver data-driven solutions.")
    st.write("I possess a strong foundation in Python (NumPy, Pandas, Scikit-learn), SQL, and Power BI, along with expertise in machine learning, statistical modeling, and data visualization. My problem-solving skills and collaborative mindset enable me to contribute effectively to data-centric projects.")
    st.write("I hold a B.Tech in Electrical and Electronics Engineering from BVC Engineering College and further honed my skills through a Post Graduate Program in Computational Data Science from INSOFE and Case Western Reserve University. Additionally, I’ve earned certifications in Power BI and Python, strengthening my analytical and technical capabilities.")
    st.write("During my internships at Turingminds.AI (Data Scientist Intern) and 360DigiTMG (Data Analyst Intern), I gained hands-on experience in data preprocessing, model development, and insight generation. My projects, such as Fraud Detection in Auto Insurance Claims and K-Means Clustering with PySpark, reflect my ability to apply theoretical knowledge to real-world challenges.")
    st.write("I’m eager to leverage my skills in an entry-level Data Scientist role, where I can contribute to innovative projects, continuously learn, and help organizations make data-driven decisions. My analytical rigor, proactive attitude, and enthusiasm for tackling new challenges make me a valuable addition to any data-focused team.")

with education_tab:
    st.header("🎓 Education & Course Work")
    st.markdown("---")
    
    # Education Timeline with Columns
    col1, col2 = st.columns([1, 4])
    
    with col1:
        st.markdown("#### 2022-2023")
        st.markdown("#### 2018-2022")
        
    with col2:
        # Education Entry 1
        with st.expander("*Post Graduate Program in Computational Data Science*", expanded=True):
            st.markdown("""
            - 🏛*Institute:* INSOFE & Case Western Reserve University
            - 📅*Duration:* 2022 - 2023
            - *Key Subjects:* Machine Learning, Data Analytics, Data Science, Statistical Modeling
            - *GPA:* 3.8/4.0""")
            with open("5129_PothureddyNSairamSrinivasaChakravarthi_PGP - Copy.pdf", "rb") as pdf_file:
                PDFbyte = pdf_file.read()

            st.download_button(label="📄 Download Certificate", 
                    data=PDFbyte, 
                    file_name="INSOFE", 
                    mime='application/octet-stream')
               
        # Education Entry 2
        with st.expander("*B.Tech in Electrical and Electronics Engineering*", expanded=True):
            st.markdown("""
            - 🏛*Institute:* BVC Engineering College 🏫Affiliated by JNTUK University
            - 📅*Duration:* 2018 - 2022
            - *Key Subjects:* Python, SQL, Power Systems, Control Systems
            - *GPA:* 6.5/10
            """)
    
    st.markdown("---")
    
    # Additional Learning Section
    st.subheader("📚 Continuous Self Learning")
    
    # Create cards for additional courses
    course1, course2, course3 = st.columns(3)
    
    with course1:
        with st.container(border=True):
            st.markdown("#### Python for Data Science")
            st.markdown("- udemy")
            st.markdown("- 2024")
            st.markdown("[View Certificate](#)")
    
    with course2:
        with st.container(border=True):
            st.markdown("#### Power BI Certification")
            st.markdown("- Microsoft")
            st.markdown("- 2024")
            st.markdown("[View Certificate](#)")
    
    with course3:
        with st.container(border=True):
            st.markdown("#### Machine Learning")
            st.markdown("- Online")
            st.markdown("- 2024")
            st.markdown("[View Certificate](#)")

with internships_tab:
    st.header(" 👨‍💻 Internships")
    st.subheader("Turingminds.AI, Hyderabad (2022 May – 2023 April)")
    st.write("Data Scientist Intern")
    st.write("• Assisted senior Data scientists in Cleaning and Processing and building models on Datasets.")
    st.write("• Collaborated with the team to analyze data to find Insights.")
    st.write("• Gained experience in Data science and Machine learning Algorithms.")

    st.subheader("360DigiTMG, Hyderabad (2023 July – 2023 September)")
    st.write("Data Analyst Intern")
    st.write("• Assisted Data Analyst how to clean the data and how to discover new insight and patterns from raw data.")
    st.write("• To Learn Clean the data from various Languages and Tools like Python, SQL, and Power BI.")

with skills_tab:
    st.markdown("### 🛠 Skills")
    skills = {
        "Languages": "Python, SQL, HTML, CSS, C#(basic)",
        "Data Analysis": "Data Cleaning, Data Preprocessing, Exploratery Data Analysis, Text Mining",
        "Data Science & Machine Learning": "Data Science, Machine Learning, Data Analysis, Deep Learning, NLP",
        "Libraries": "Pandas, NumPy, Keras, NLTK",
        "Visualization": "Matplotlib, Seaborn, Power BI",
        "ML & Stats": "Scikit-learn, Regression, Classification, Clustering",
        "Cloud " : "Microsoft Azure(basics)",
        "Tools & Frame Works": "Jupyter, VS Code, Git, Github, Streamlit, Flask, Docker, Excel, Colab, spider",
        "Soft Skills": "Problem Solving, Communication Skills"
    }
    for category, tools in skills.items():
        st.markdown(f"- *{category}:* {tools}")

with projects_tab:
    st.header("Projects")
    st.subheader("🔍Predict 🛡Fraud Detection in Auto Insurance Claims")
    st.write("• Developed a predictive model using logistic regression to identify fraudulent auto insurance claims from a real-world dataset. ")
    st.write("• The project encompassed comprehensive data preprocessing, including null value handling, redundant column removal, missing value imputation, dummy variable creation, and data scaling.")
    st.write("• The dataset was split into 70% training and 30% testing sets.")
    st.write("• Model performance was rigorously evaluated using a confusion matrix, achieving impressive F1-scores of 0.92 and 0.89 on the training and testing datasets, respectively, demonstrating a robust and accurate fraud detection capability.")
    st.write("🐙 GitHub: [Project](https://github.com/chakravarthipothureddy/insurance-fraudster-capstone-project.git)")

    st.subheader("📊 HR Attrition Analysis and Visualization (Microsoft Power BI)")
    st.write("- Conducted a comprehensive analysis of HR attrition data using Microsoft Power BI to identify key drivers and trends. ")
    st.write("- The project involved connecting to diverse data sources, transforming and cleaning the data to ensure compatibility with Power BI, and creating custom measures and calculated columns.")
    st.write("- Interactive visualizations, including attrition rate by department, employee distribution by age group, attrition rate by gender, and job satisfaction levels, were developed and compiled into a dynamic dashboard to provide actionable insights into employee attrition patterns.")
    st.write("🐙 GitHub: [Project](https://github.com/chakravarthipothureddy/power_BI_HRdata)")

with certificates_tab:
    certifications = [
    {
        "title": "Microsoft Certified: Power BI Data Analyst Associate",
        "issuer": "Microsoft",
        "date": "2024-Dec",
        "credential_link": "https://learn.microsoft.com/api/credentials/share/en-us/POTHUREDDYNSAIRAMSRINIVASACHAKRAVA-4223/E578D36132F4916A?sharingId=3F593004AB35673B",
    },
    {
        "title": "Post Graduate Program in Computational Data Science",
        "issuer": "INSOFE & Case Western Reserve University",
        "date": "2023-May",
        "credential_link": "5129_PothureddyNSairamSrinivasaChakravarthi_PGP - Copy.pdf",
    },
    {
        "title": "Python",
        "issuer": "Codetantra",
        "date": "2021",
        "credential_link": "https://bvcce.codetantra.com/cert/certificate.jsp?certId=CT332-rcaMV81-cfz",
    },
    {
        "title": "Python for Data Science",
        "issuer": "Udemy",
        "date": "2024-July",
        "credential_link": "https://www.udemy.com/certificate/UC-29bb01df-9a09-456f-8095-9055ae3f5bb8/",
    }
]
    
    st.header("📜 My Certifications")
    
    for cert in certifications:
        st.subheader(f"🎖 {cert['title']}")
        st.write(f"🏛 *Issuer:* {cert['issuer']}")
        st.write(f"📅 *Date:* {cert['date']}")
        st.write(f"🔗 [View Credential]({cert['credential_link']})")
        st.markdown("---")

    st.markdown("### 🚀 Career Goals")
    st.markdown("""My goal is to become a data scientist who can build scalable models, deliver insights from data, and contribute to impactful business decisions. I'm also interested in exploring NLP, Computer Vision, and Generative AI.""")

with contact_tab:
    import streamlit as st
    from PIL import Image

# Configure page


# --- Contact Me Tab ---
    st.title("📬 Contact Me")
    st.markdown("""
    <style>
    .contact-card {
        padding: 20px;
        border-radius: 10px;
        background-color: #f8f9fa;
        margin-bottom: 20px;
        border-left: 5px solid #4e73df;
    }
    </style>
    """, unsafe_allow_html=True)

# Two-column layout
    col1, col2 = st.columns(2)

    with col1:
    # --- Direct Contact Card ---
        st.markdown('<div class="contact-card">', unsafe_allow_html=True)
        st.subheader("📌 Direct Contact")
        st.markdown("""
        *📍 Location:*  
        Hyderabad, India  
    
        *✉ Email:*  
        [chakravarthy.pothureddy@gmail.com](mailto:chakravarthy.pothureddy@gmail.com)  
    
        *📱 Phone:*  
        +91 6302867927  
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # --- Social Media Card ---
        st.markdown('<div class="contact-card">', unsafe_allow_html=True)
        st.subheader("🌐 Social Connect")
        st.markdown("""
        *🔗 LinkedIn:*  
        [Pothureddy Naga Sairam](https://linkedin.com/in/chakravarthipothureddy)  
    
        *💻 GitHub:*  
        [GitHub](https://github.com/chakravarthipothureddy)  
        """)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        # --- Contact Form ---
        with st.form("contact_form", border=True):
            st.subheader("✍ Send a Message")
            name = st.text_input("Your Name*", placeholder="John Doe")
            email = st.text_input("Your Email*", placeholder="your.email@example.com")
            subject = st.selectbox("Subject", 
                             ["Project Enquiry", "Job Opportunity", "Collaboration", "Other"])
            message = st.text_area("Your Message*", 
                             placeholder="I'd like to discuss...", height=150)
            submitted = st.form_submit_button("Send Message", type="primary")
        
            if submitted:
                if not name or not email or not message:
                    st.error("Please fill all required fields (*)")
                else:
                # --- Email sending logic would go here ---
                # (Use the email sending code from previous examples)
                
                    st.success("✅ Message sent successfully!")
                    st.balloons()
                    st.markdown("""
                    Thank you for reaching out!  
                    I'll respond within 24-48 hours.
                    """)

# --- Map Embed (Optional) ---
    st.markdown("---")
    st.subheader("📍 Find Me On Map")
    st.components.v1.iframe(
        src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3806.7858340056356!2d78.4516723157176!3d17.426950588052835!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bcb9158f201b205%3A0xad3d8b5d7c0f1f9e!2sHyderabad%2C%20Telangana!5e0!3m2!1sen!2sin!4v1620000000000!5m2!1sen!2sin",
        width=700,
        height=450,
        scrolling=False
    )

# --- Footer ---
    st.markdown("---")
    st.caption("© 2025 | @PNSRSC | All Rights Reserved")
            # (Optional: Add email forwarding logic here)
