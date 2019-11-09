import unittest
from final_assignment import *

class test_me(unittest.TestCase):
    def test_sort_me(self):
#sortingby first name
        window=Toplevel()
        fr7=frame7(window)
        list=[('sjsh', 'gghjg', 6868768, 'Bsc.Multimedia', 8687),
              ('syuyu', 's', 7697987, 'Bsc.Multimedia', 8787), ('a', 'hi', 8999, 'Bsc.Ethical Hacking', 99)]
        expected=[('a', 'hi', 8999, 'Bsc.Ethical Hacking', 99),('sjsh', 'gghjg', 6868768, 'Bsc.Multimedia', 8687)
            ,('syuyu', 's', 7697987, 'Bsc.Multimedia', 8787)]

        fr7.sortcombo.set(' First Name')
        fr7.quick_sort(list,0,len(list)-1)
        self.assertEqual(list,expected)
#sorting by last name
        expected_1=[('sjsh', 'gghjg', 6868768, 'Bsc.Multimedia', 8687),
                    ('a', 'hi', 8999, 'Bsc.Ethical Hacking', 99),
                    ('syuyu', 's', 7697987, 'Bsc.Multimedia', 8787)]
        fr7.sortcombo.set('Last Name')
        fr7.quick_sort(list,0,len(list)-1)
        print(list)
        self.assertEqual(list,expected_1)
#sorting by contact
        expected_2=[('a', 'hi', 8999, 'Bsc.Ethical Hacking', 99),
                    ('sjsh', 'gghjg', 6868768, 'Bsc.Multimedia', 8687),
                    ('syuyu', 's', 7697987, 'Bsc.Multimedia', 8787)]
        fr7.sortcombo.set('Contact')
        fr7.quick_sort(list,0,len(list)-1)

        self.assertEqual(list,expected_2)
#sorting by course
        expected_3=[('a', 'hi', 8999, 'Bsc.Ethical Hacking', 99),
                    ('sjsh', 'gghjg', 6868768, 'Bsc.Multimedia', 8687),
                    ('syuyu', 's', 7697987, 'Bsc.Multimedia', 8787)
                    ]
        fr7.sortcombo.set("Course")
        fr7.quick_sort(list,0,len(list)-1)
        print(list)
        self.assertEqual(list,expected_3)
#sortingby student id
        expected_4=[('a', 'hi', 8999, 'Bsc.Ethical Hacking', 99),
                    ('sjsh', 'gghjg', 6868768, 'Bsc.Multimedia', 8687),
                    ('syuyu', 's', 7697987, 'Bsc.Multimedia', 8787)]
        fr7.sortcombo.set("Student Id")
        fr7.quick_sort(list,0,len(list)-1)
        print(list)
        self.assertEqual(list,expected_4)

if __name__=="__main__":
    unittest.main()
