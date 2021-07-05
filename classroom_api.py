
import pytest
import logging

logging.basicConfig(
    format="Date-Time : %(asctime)s : Line No. : %(lineno)d - %(message)s",
    level=logging.DEBUG,
    filename="classroomtest.log",
    filemode="w"  )

logging.info("creating class object")
object = Classroom(main())
ids = object.list_courses_id()

###create###
def test_create_courses():
    logging.info("Testing create method")
    logging.info(
        "from test_classroom_api.py controller go to quickstart.py where it return a data of get method."
    )
    res = course_get('359741470739')
    self.assertEqual('359741470739', res['id'])
    self.assertEqual(dict,type(res))

def test_for_negative_get():
    res = courses_get('359744147039')
    self.assertFalse(len(res)!=dict,info)
    info = 'Negative test case'
    logging.debug("create method is pass")

##update##
 
def test_update_courses():
    logging.info("Testing update method")
    logging.info(
        "from test_classroom.py controller go to quickstart.py where it return a data of get method."
    )
    val1 = courses_get(self.course_id)
    val2 = update_course(self.course_id)
    self.assertTrue(val1['name']==val2)

def test_for_negative_update():
    val1 = courses_get('359741470739')
    val2 = update_course('359741470739')
    self.assertTrue(val1['name']==val2)
    logging.debug("update method is pass")

##list#
 
def test_list_courses_id():
    logging.info("Testing list method")
    logging.info(
        "from test_classroom.py controller go to quickstart.py where it return a data of get method."
    )
    var = object.list_courses()
    logging.debug("List method is pass")
    res = course_list()
    self.assertEqual(dict,type(res))

def list_negative_test():
    res = course_list()
    self.assertEqual(type(res)!=dict)
     logging.debug("list method is pass")

###get###
def test_get_courses():
    var = object.get_course(str(ids[0]))
    logging.info("Testing get method")
    logging.info(
        "from test_classroom.py controller go to quickstart.py where it return a data of get method."
    )
    res = course_get('359741470739')
    self.assertTrue(len(res)==16)

def test_for_negative_get():
    val1 = courses_get('359741470739')
    val2 = update_course('359741470739')
    self.assertTrue(val1['name']==val2)
    logging.debug("get method is pass")

##patch##

def test_patch_courses():
    logging.info("Testing Patch method")
    logging.info(
        "from test_classroom.py controller go to quickstart.py where it return a data of get method."
    )
    val1 = courses_get()
    val2 = patch_update()
    self.assertFalse(val1==val2)
    logging.debug("Patch method is pass")

############################################# Script Details ################

# Script name               :       classroom_api.py
# Script version            :       1.0
# Prepared By               :       supriya.jakkamputi@infinite.com
# Create Date               :       09/06/2021
# Last Modification Date    :       14/06/2021

###############################################################################


    