import unittest
import os
import json
from pdfTextExtractor import lambda_handler
class TestTextractPdfTextExtractor(unittest.TestCase):

    os.environ["TEXTRACT_S3_OUTPUT_PATH"] = "s3://simpleasyncworkflow-textractsimpleasyncworkflow2d-113764vgh21fm/textract-output/UNDP-GEF Terminal Evaluation of wind renewable energy technology project2022-09-15T14:58:13.674106/UNDP-GEF Terminal Evaluation of wind renewable energy technology project.json"

    def test_pdfTextExtractor(self):
        event = '{"jobId": "512dfe4c71ca6e1ef2a50b9220dcb870"}'
        lambda_handler( json.loads(event), "")


if __name__ == '__main__':
    unittest.main()
