port quickstart
import logging

logging.basicConfig(filename="quickstart_classroom.log",filemode = 'w', level=logging.INFO,format='%(asctime)s %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
logging.info('Execution starts Here.')

service = quickstart.main()
#Creation of courses
def create_course():
    course = {
        'name': '10th Grade Biology',
        'section': 'Period 2',
        'descriptionHeading': 'Welcome to 10th Grade Biology',
        'description': """We'll be learning about about the
                        structure of living creatures from a
                        combination of textbooks, guest lectures,
                        and lab work. Expect to be excited!""",
        'room': '301',
        'ownerId': 'me',
        'courseState': 'PROVISIONED'
    }
    course = service.courses().create(body=course).execute()
    print('Course created: %s %s %s' % (course.get('name'), course.get('id'),course.get('section'),))
    logging.info('Course created successfully')
    # [END classroom_create_course]
    #return course


#Fetching the data based on course_id
def get_course(course_id):
    try:
        course = service.courses().get(id=course_id).execute()
        print('Course "{%s}" found.' % course.get('name'))
        logging.info('Data fetched successfully')
        #print(course['name'])
        return (course['name'],course['section'],course['room'])
    except errors.HttpError as error:
        print('Course with ID "{%s}" not found.' % course_id) 
        logging.info("course_id is not found")         


#Listing all the course details
def list_courses():
    courses = []
    page_token = None
    lst = []
    while True:
        response = service.courses().list(pageToken=page_token,
                                        pageSize=100).execute()
        courses=response.get('courses', [])
        page_token = response.get('nextPageToken', None)
        if not page_token:
            break

    if not courses:
        print('No courses found.')
        logging.info('No courses found')
    else:
        #print('Courses:')
        for course in courses:
            ids = course['id']
            lst.append(ids)
            print(course.get('name'), course.get('id'), course.get('section'), course.get('room'))
        logging.info('Listing all the course details')
        return lst

#Updating the room no based on course_id
def update_course(course_id):
    course = service.courses().get(id=course_id).execute()
    course['room'] = '304'
    course = service.courses().update(id=course_id, body=course).execute()
    print('Course %s updated.' % course.get('name'))
    logging.info('Updating all the data based on course id')
    return (course['room'])


#Updating the secific field based on course_id
def specific_update_course(course_id):
    course = {
    'section': 'Period 3',
    'room': '302'
    }
    course = service.courses().patch(id=course_id,
                                    updateMask='section,room',
                                    body=course).execute()
    print('Course "%s" updated.' % course.get('name'))
    logging.info("Updating the specific fields")
    return (course['section'],course['room'])

logging.info("Execution ended:")

if __name__ == '__main__':
    main()
    #create_course()
    #get_course(360054595731)
    #list_courses()
    #update_course(360000200991)
    #specific_update_course('360054595731')
    list_courses()
    
################################################################################
############################### Script Details #################################

# Script name               :       methods.py
# Script version            :       1.0
# Prepared By               :       supriya,jakkamputi@infinite.com
# Create Date               :       09/06/2021
# Last Modification Date    :       14/06/2021

################################################################################