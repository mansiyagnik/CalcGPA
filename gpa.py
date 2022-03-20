import streamlit as st
from PIL import Image
st.set_page_config(page_title ="CalcGPA",page_icon=None)

def grades (marks):
    if marks >=90:
        grade=10
    elif marks >=75:
        grade =9
    elif marks >=65:
        grade =8  
    elif marks >=55:
        grade =7
    elif marks >=50:
        grade =6
    elif marks >=45:
        grade =5
    elif marks >=40:
        grade =4
    else :
        grade=0
    return grade


def calc (sem):
    subjects={}
    labs ={}
    GPA =0
    flag =0
    credits =0
    col1,col2=st.columns(2)

    if sem ==1:
        subjects = { 'App. Maths-I' : 4, 'App. Physics-I' : 3, 'Manufacturing Processes' : 3, 'Electrical Tech.' : 3, 'Human Values' : 1, 'Fundamentals of Computing' : 2, 'App. Chemistry' : 3 }
        labs = { 'App. Physics Lab-I' : 1, 'Elecrical Tech. Lab' : 1, 'Workshop' : 2, 'Engg. Graphics Lab' : 2, 'FOC Lab' : 1, 'App. Chemistry Lab' : 1 }
        credits = 27  

    elif sem == 2:
        subjects = { 'App. Maths-II' : 4, 'App. Physics-II' : 3, 'Electronic Devices' : 3, 'Intro To Programming' : 3, 'Engineering Mechanics' : 3, 'Communication Skills' : 3, 'Environmental Studies' : 3 }
        labs = { 'App. Physics Lab-II' : 1, 'Programming Lab' : 1, 'Electronic devices Lab' : 1, 'Engineering Mechanics Lab' : 1, 'EVS Lab' : 1 }
        credits = 27   

    elif sem == 3:
        subjects = { 'App. Maths-III' : 4, 'Foundation of CS' : 4, 'Switching Theory & Logic Design' : 4, 'Circuits & Systems' : 4, 'Data Structures' : 4, 'Computer Graphics & Multimedia' : 4, }
        labs = { 'STLD Lab' : 1, 'Data Stucture Lab' : 1, 'Circuits & Systems Lab' : 1, 'CGMM Lab' : 1 }
        credits = 28  

    elif sem == 4:
        subjects = { 'App. Maths-IV' : 4, 'Computer Organisation & Architecture' : 4, 'Theory of Computation' : 4, 'Database Management' : 4, 'Object Oriented Programming' : 3, 'Communication Systems' : 4 }
        labs = { 'App. Maths Lab' : 1, 'COA Lab' : 1, 'DBMS Lab' : 1, 'OOPS Lab' : 1, 'Communication Systems Lab' : 1 }
        credits = 29  

    elif sem == 5:
        subjects = { 'Algo. Design & Analysis' : 4, 'Software Engineering' : 4, 'Java Programming' : 4, 'Industrial Management' : 3, 'Digital Communication ' : 4, 'Communication Skills' : 1 }
        labs = { 'Algo. Design Lab' : 1, 'Software Engineering Lab' : 1, 'Java Programming Lab' : 1, 'In-house Workshop' : 1, 'Digital Communication Lab' : 1, 'Communication Skills Lab' : 1 }
        credits = 26             

    elif sem == 6:
        subjects = { 'Compiler Design' : 4, 'Operating Systems' : 4, 'Computer Networks' : 4, 'Web Technology' : 3, 'Artificial Intelligence' : 4, 'Microprocessors & Microcontrollers' : 4, }
        labs = { 'Operating Systems Lab' : 1, 'Computer Networks Lab' : 1, 'Web Technology Lab' : 1, 'Microprocessor & Microcontroller Lab' : 1 }
        credits = 27   

    elif sem == 7:
        subjects = { 'Information Security' : 4, 'Software Testing and Quality Assurance' : 3, 'Wireless Comunication' : 3,'elective 1' :3,'elective 2 ':3}
        labs = { 'Information Security Lab' : 1, 'Software Testing and QA Lab' : 1, 'Wireless Communication Lab' : 1, 'lab on elevtive' : 1 ,'Summer training/Industrial Workshop /Certification' : 1,'Minor Project' : 3 }
        credits = 24

    elif sem == 8:
        subjects = { 'Mobile Computing ' : 4, 'Machine Learning' : 3, 'Human Value and Profesional Ethics-II' : 1 ,'elective 1':3, 'elective 2':3}
        labs = { 'Mobile Computing Lab' : 1, 'Machine Learning Lab' : 1, 'lab on elective 1' : 1, 'lab on elective 2' : 1 ,'Major Project' : 8 }
        credits = 26  


    with col1:
        with st.expander ("Theory Subjects"):
            for subject in subjects:
                marks=st.number_input("{}:".format(subject),0,100)
                if marks==0:
                    flag =1
                num =grades(marks)
                GPA+=num*subjects[subject]

    with col2:
        with st.expander ("Practical Subjects"):
            for lab in labs:
                marks=st.number_input("{}:".format(lab),0,100)
                if marks==0:
                    flag =1
                num =grades(marks)
                GPA+=num*labs[lab]            
    if flag:
        st.warning("You haven't entered the marks of all subjects !")

    GPA =GPA/credits
    return GPA

with st.container():
    cl1,cl2,cl3,cl4,cl5,cl6,cl7=st.columns(7)
    with cl3:  
        logo=Image.open("logo.png")      
        st.image([logo],width=350)
st.markdown("<h3 style='text-align: center;color :#313131 ;'>Semester GPA Calculator of B.Tech(CSE)</h3>", unsafe_allow_html=True)

with st.container():
    st.markdown("<h4 style= 'text-align: center;color :green;'>-------------------------------------------------------------------</h4> ",unsafe_allow_html=True)
    name = st.text_input("ENTER YOUR NAME")

    if name:
        st.write("Hello {}!".format(name)) 
        sem = st.number_input("ENTER YOUR SEMESTER", 0, 8)
        st.markdown("<h4 style= 'text-align: center;color :green;'>-------------------------------------------------------------------</h4> ",unsafe_allow_html=True)

        if sem:
            st.write("")
            st.write("")
            st.markdown("<h3 style='text-align: center; color:teal; '>Enter Marks!</h3>", unsafe_allow_html=True)

            GPA = calc(sem)

            st.write("")
            st.write("")

            cl1, cl2, cl3, cl4, cl5, cl6, cl7, cl8, cl9 = st.columns(9) 
            with cl5:
                ans = st.button("Submit")
               

              
            if ans:
                msg = "Your GPA: {}".format(str(round(GPA,2)))
                st.markdown(f"<h3 style='text-align: center; color:olivedrab '>{msg}</h3>", unsafe_allow_html=True)
                if GPA >= 8.0 :
                    st.markdown("<h2 style='text-align:center;color:green;'>Amazing</h2>",unsafe_allow_html=True)
                    st.balloons()
                    st.balloons()
                    st.balloons()




