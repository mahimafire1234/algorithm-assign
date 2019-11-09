import unittest
from final_assignment import *

class test_me1(unittest.TestCase):
    def test_search_me(self):
        window=Toplevel()
        fr7=frame7(window)
#searchingby first name
        fr7.searchbox.set("First name")
        list=[('sjsh', 'gghjg', 6868768, 'Bsc.Multimedia', 8687),
              ('syuyu', 's', 7697987, 'Bsc.Multimedia', 8787), ('a', 'hi', 8999, 'Bsc.Ethical Hacking', 99)]
        fr7.textentry.delete(0,END)
        fr7.textentry.insert(0,'a')
        list_func=fr7.search_info(list)
        exepcted_1=[('a', 'hi', 8999, 'Bsc.Ethical Hacking', 99)]
        self.assertEqual(list_func,exepcted_1)
#searching by last name
        fr7.searchbox.set("Last name")
        fr7.textentry.delete(0,END)
        fr7.textentry.insert(0,'s')
        list_func=fr7.search_info(list)
        expected_2=[('syuyu', 's', 7697987, 'Bsc.Multimedia', 8787)]
        self.assertEqual(list_func,expected_2)
#searching by contact
        fr7.searchbox.set("Contact")
        fr7.textentry.delete(0,END)
        fr7.textentry.insert(0,'8999')
        list_func1=fr7.search_info(list)
        print(list_func1)
        expected_3=[('a', 'hi', 8999, 'Bsc.Ethical Hacking', 99)]
        self.assertEqual(list_func1,expected_3)
#searching by course
        fr7.searchbox.set('Course')
        fr7.textentry.delete(0,END)
        fr7.textentry.insert(0,"Bsc.Multimedia")
        list_func2=fr7.search_info(list)
        print(list_func2)
        expected_4=[('sjsh', 'gghjg', 6868768, 'Bsc.Multimedia', 8687),
              ('syuyu', 's', 7697987, 'Bsc.Multimedia', 8787)]
        self.assertEqual(list_func2,expected_4)
#searching by student id
        fr7.searchbox.set('Student Id')
        fr7.textentry.delete(0,END)
        fr7.textentry.insert(0,'8687')
        list_func3=fr7.search_info(list)
        expected_5=[('sjsh', 'gghjg', 6868768, 'Bsc.Multimedia', 8687)]
        print(list_func3)
        self.assertEqual(list_func3,expected_5)



if __name__=="__main__":
    unittest.main()