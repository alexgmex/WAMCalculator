from pypdf import PdfReader 


def extract_pdf(pdf_name):
    # Extract text from transscipt
    reader = PdfReader(pdf_name) 
    page = reader.pages[0] 
    raw = page.extract_text().split("\n")

    # Placeholders for important variables
    name = ""
    sid = ""
    start = 0
    end = 0

    # Extract and delete junk from raw data
    for i in range(len(raw)):
        if raw[i] == "Student name":
            name = raw[i+1]
        if raw[i] == "Student ID":
            sid = raw[i+1]
        if raw[i] == "Credit points":
            start = i+1
        if raw[i] == "Credit points gained":
            end = i
    raw = raw[start:end]

    return raw, name, sid


def create_course_list(raw):
    # Add in missing marks for any non-marked subjects
    course = []
    for x in raw:
        if x == "SR" or x == "FR":
            course.append("0.0")
        course.append(x)

    # Split into 2d array
    course = [course[i:i + 7] for i in range(0, len(course), 7)]

    return course


def calculate_wam(course):
    # Calculate WAM
    num = 0
    den = 0
    wi = 0
    cpi = 0
    mi = 0

    for subject in course:
        # Difficulty weighting
        if subject[2][4] == "1":
            wi = 0
        else:
            wi = int(subject[2][4])
        
        # Credit points
        cpi = int(subject[6])

        # Mark
        mi = float(subject[4])

        # Append to fraction
        num += wi*cpi*mi
        den += wi*cpi
    
    return round(num/den, 2)