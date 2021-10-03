import unittest

from repos import repo


class Testrepos(unittest.TestCase):

    def testInvalidRepo1(self):
        self.assertEqual(repo('richkempinski'),[('csp', 2), ('hellogitworld', 30), ('helloworld', 6), ('Mocks', 10), ('Project1', 2), ('richkempinski.github.io', 9), ('threads-of-life', 1), ('try_nbdev', 2), ('try_nbdev2', 5)])

    def testInvalidRepo2(self):
        self.assertEqual(repo('jaitul25'),[('Cloudflare-Jaitul-Bharodiya', 2), ('CS-561-DBMS', 12), ('GithubRepo', 15), ('HW05-Static-Code-Analyzer', 1), ('jaitul25.github.io', 14), ('kg_jaitul25_2021', 5), ('SSW-567', 2), ('Stevens-Database', 3), ('Stevens-Milee-Project', 30), ('Stevens-Web-Solution', 2), ('Triangle567', 11), ('Voyager_SDET_Hiring_Test', 2)])

    def testInvalidRepo3(self):
        self.assertEqual(repo('nidhi0329'),[('ClubWealthInterview', 2), ('CS-513-Data-Mining-and-Knowledge-Management', 9), ('CS-513_final_project', 1), ('CS-546-web-programming', 11), ('CS-555-Agile-Methods-for-Software-Development', 1), ('CS-555_project', 1), ('CS-561-DBMS', 1), ('CS-570-Data-structure', 7), ('CS-573-Cyber-Security', 1), ('E-Mall-Web-Application', 2), ('Music_Room', 5), ('SSW-810-Special-Topics-in-SSW', 1), ('Student-Repository', 13)])

    def testInvalidRepo4(self):
        self.assertEqual(repo('nidhi'),[('communityengine', 30)])







