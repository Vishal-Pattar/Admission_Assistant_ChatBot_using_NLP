import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Downloading the punkt tokenizer from NLTK
nltk.download('punkt', quiet=True)
# Downloading stopwords from NLTK
nltk.download('stopwords', quiet=True)

class ResponseGenerator:
     def __init__(self):
          # Initializing the ResponseGenerator class with English stopwords
          self.stop_words = set(stopwords.words('english'))

     def extract_words(self, sentence):
          # Tokenizing the input sentence into words and converting them to lowercase
          word_tokens = word_tokenize(sentence.lower())
          # Removing punctuation from the word tokens
          word_tokens = [word for word in word_tokens if word not in string.punctuation]
          # Filtering out stopwords and non-alphanumeric words
          filtered_words = [word for word in word_tokens if word.isalnum() and word not in self.stop_words]
          return filtered_words

class Response:
     def __init__(self):
          # Initializing a dictionary with predefined responses
          self.responses = {
               "hello": "Hello! How can I assist you with your admission inquiries?",
               "hi": "Hi! Welcome to our college admission assistant. How can I help you today?",
               "help": "Sure, I'm here to help! What do you need assistance with?",
               "problem": "I'm sorry to hear that you're having trouble. Please let me know what the issue is, and I'll do my best to assist you.",
               "application_process": "To apply for admission, you need to visit the college's official website and fill out the online application form. Make sure to provide accurate information and submit all required documents.",
               "required_documents": "You will need to submit your high school transcripts, standardized test scores (such as JEE Main or state-level entrance exams), proof of identity, and passport-sized photographs.",
               "eligibility_criteria": "Eligibility criteria vary between colleges, but typically, candidates must have completed their 12th standard (or equivalent) with Physics, Chemistry, and Mathematics as compulsory subjects. Additionally, they need to qualify for entrance exams like JEE Main, JEE Advanced, or state-level engineering entrance exams.",
               "cutoff_scores": "The cutoff scores for engineering colleges vary each year and depend on factors like the number of applicants, available seats, and difficulty level of the entrance exam. It's best to check with the college's official website for the latest cutoff scores.",
               "courses_offered": "Engineering colleges offer a wide range of courses in various disciplines such as Computer Science, Mechanical Engineering, Electrical Engineering, Civil Engineering, and more. You can explore the college's website or brochure for detailed information about the courses offered.",
               "placement_opportunities": "Many engineering colleges in India have dedicated placement cells that assist students in securing internships and job placements. They invite reputed companies for campus recruitment drives, and students have the opportunity to participate in placement activities during their final year.",
               "scholarship_options": "Several scholarships are available for engineering students based on merit, financial need, and other criteria. These scholarships may be offered by the government, private organizations, or the college itself. Students are encouraged to explore scholarship options and apply for them.",
               "fee_structure": "The fee structure for engineering colleges varies depending on factors such as the college's reputation, location, facilities, and course specialization. In addition to tuition fees, students may also need to pay for hostel accommodation, transportation, and other expenses.",
               "admission_deadlines": "Engineering colleges in India typically have specific deadlines for submitting applications and completing admission-related procedures. It's essential to check the college's website or admission brochure for the latest information on admission deadlines.",
               "admission_criteria_for_foreign_students": "Foreign students interested in studying engineering in India may have to fulfill additional admission criteria, such as obtaining a student visa, meeting specific academic requirements, and providing proof of English proficiency. They are advised to contact the college's international admissions office for guidance.",
               "entrance_exam_preparation_tips": "Preparing for engineering entrance exams requires dedication and consistent effort. Students are advised to start their preparation early, practice solving sample papers and previous years' question papers, seek guidance from experienced mentors or coaching institutes, and focus on strengthening their problem-solving and time management skills.",
               "faculty_qualifications": "Engineering colleges in India employ highly qualified faculty members with expertise in various engineering disciplines. Many faculty members hold advanced degrees (such as M.Tech or Ph.D.) from reputed institutions and have industry experience.",
               "campus_facilities": "Engineering colleges typically offer modern campus facilities, including well-equipped laboratories, libraries, computer centers, sports complexes, hostels, and cafeteria. These facilities are designed to enhance students' learning experience and overall well-being.",
               "industry_collaborations": "Many engineering colleges collaborate with industries to provide students with practical exposure to real-world engineering projects, internships, and industry-relevant training programs. These collaborations help students bridge the gap between academic knowledge and industry requirements.",
               "research_opportunities": "Engineering colleges encourage students to engage in research activities and contribute to advancements in their respective fields. They provide support and resources for conducting research projects, publishing papers, and participating in conferences.",
               "internship_programs": "Internship programs are an integral part of the curriculum in engineering colleges. Students have the opportunity to gain hands-on experience, apply theoretical knowledge to real-world problems, and build professional networks. Many colleges have tie-ups with reputed companies for internships.",
               "mentorship_programs": "Engineering colleges often have mentorship programs where senior students or faculty members guide and support junior students in academic, career, and personal development. Mentorship programs help students navigate college life and make informed decisions.",
               "extracurricular_activities": "In addition to academics, engineering colleges offer a variety of extracurricular activities such as clubs, societies, cultural events, technical competitions, and sports. These activities provide students with opportunities to explore their interests, develop leadership skills, and build friendships.",
               "student_support_services": "Engineering colleges provide various support services to assist students in their academic and personal growth journey. These services may include counseling, academic advising, career guidance, disability support, and accommodation assistance.",
               "alumni_network": "Engineering colleges maintain strong alumni networks consisting of successful graduates who provide mentorship, career guidance, and networking opportunities to current students. Alumni networks play a crucial role in fostering lifelong connections and professional growth.",
               "social_outreach_initiatives": "Many engineering colleges engage in social outreach initiatives such as community service projects, environmental conservation efforts, and rural development programs. These initiatives instill a sense of social responsibility and leadership among students.",
               "accreditation_and_rankings": "Accreditation and rankings play a significant role in assessing the quality and reputation of engineering colleges. Students are advised to consider factors such as accreditation status, rankings by reputed agencies, and industry reputation when choosing a college."
          }

     def generate_response(self, input_text):
          words = ResponseGenerator().extract_words(input_text)
          # Mapping input words to predefined responses
          if "hello" in words:
               return self.responses["hello"]
          elif "hi" in words:
               return self.responses["hi"]
          elif "help" in words:
               return self.responses["help"]
          elif "problem" in words:
               return self.responses["problem"]
          elif "admission" in words and "procedure" in words:
               return self.responses["application_process"]
          elif "required" in words and "documents" in words:
               return self.responses["required_documents"]
          elif "eligibility" in words and "criteria" in words:
               return self.responses["eligibility_criteria"]
          elif "cutoff" in words and "scores" in words:
               return self.responses["cutoff_scores"]
          elif "courses" in words and "offered" in words:
               return self.responses["courses_offered"]
          elif "placement" in words and "opportunities" in words:
               return self.responses["placement_opportunities"]
          elif "scholarship" in words and "options" in words:
               return self.responses["scholarship_options"]
          elif "fee" in words and "structure" in words:
               return self.responses["fee_structure"]
          elif "admission" in words and "deadlines" in words:
               return self.responses["admission_deadlines"]
          elif "admission" in words and "criteria" in words and "foreign" in words and "students" in words:
               return self.responses["admission_criteria_for_foreign_students"]
          elif "entrance" in words and "exam" in words and "preparation" in words and "tips" in words:
               return self.responses["entrance_exam_preparation_tips"]
          elif "faculty" in words and "qualifications" in words:
               return self.responses["faculty_qualifications"]
          elif "campus" in words and "facilities" in words:
               return self.responses["campus_facilities"]
          elif "industry" in words and "collaborations" in words:
               return self.responses["industry_collaborations"]
          elif "research" in words and "opportunities" in words:
               return self.responses["research_opportunities"]
          elif "internship" in words and "programs" in words:
               return self.responses["internship_programs"]
          elif "mentorship" in words and "programs" in words:
               return self.responses["mentorship_programs"]
          elif "extracurricular" in words and "activities" in words:
               return self.responses["extracurricular_activities"]
          elif "student" in words and "support" in words and "services" in words:
               return self.responses["student_support_services"]
          elif "alumni" in words and "network" in words:
               return self.responses["alumni_network"]
          elif "social" in words and "outreach" in words and "initiatives" in words:
               return self.responses["social_outreach_initiatives"]
          elif "accreditation" in words and "and" in words and "rankings" in words:
               return self.responses["accreditation_and_rankings"]
          else:
               return "I'm sorry, I didn't understand that. Please ask another question."