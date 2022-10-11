import unittest
import os
import json
from patternDetector import PatternDetector
class TestPatternDetector(unittest.TestCase):

    #os.environ["TEXTRACT_S3_OUTPUT_PATH"] = "s3://simpleasyncworkflow-textractsimpleasyncworkflow2d-113764vgh21fm/textract-output/UNDP-GEF Terminal Evaluation of wind renewable energy technology project2022-09-15T14:58:13.674106/UNDP-GEF Terminal Evaluation of wind renewable energy technology project.json"
    os.environ["SKIP_PAGES"] = "CONTENTS, TABLE OF CONTENTS, FOREWORDS, ANNEXES,Table of Contents,ACRONYMS,ABBREVIATIONS"
    def test_PatternDetector(self):
        pattern_detector = PatternDetector()
        result = pattern_detector.regexHeaderOrFooter("HUMAN DEVELOPMENT REPORT 2021/2022")
        print("header/footer :" , result)
        occ={}
        pattern = {}
        occ, pattern = pattern_detector.identifyHeaderFooterPattern( "simpleasyncworkflow-textractsimpleasyncworkflow2d-1v68l1y57cpsn", "textract-temp-output/2e3d2dd009e7250e1eacd1ac8a6d28e51cc820bc484d70cbfcd67364218ad3b8")
        print(occ)
        print(pattern)

if __name__ == '__main__':
    unittest.main()
