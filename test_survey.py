import unittest
from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    """针对AnonmymousSurvey 类的测试"""
    def test_store_single_response(self):
        """测试单个答案会被妥善地存储"""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn('English', my_survey.responses)


    def test_stor_three_responses(self):
        """测试三个答案都被妥善存储"""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Japanese', 'Cantonese']
        for response in responses:
                my_survey.store_response(response)

        for response in responses:
            self.assertIn(response, my_survey.responses)


if __name__ == '__mian__':
    unittest.main

