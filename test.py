import unittest
import sys
import mapper
import reducer

class TestMethods(unittest.TestCase):

    def test_mapper(self):
        with open('test/input/file1.txt','r') as in_f:
            with open('test/output_mapper.txt','w') as out_f:
                mapper.main(InputFile = in_f,OutputFile=out_f)     
    def test_reducer(self):
        with open('test/output_mapper.txt','r') as in_f:
            with open('test/output.txt','w') as out_f:
                reducer.main(InputFile = in_f,OutputFile=out_f)
   
    def test_mapper_decoding_and_spliting(self):
        l = 'some tExt with-Mistakes and mоrе русского текста lol\n'
        en_l = l.encode(encoding='utf8',errors='replace')
        d_l = mapper.line_decode(en_l)
        words = mapper.string_processing(d_l)
        self.assertEqual(words,['some','tExt','with','Mistakes','and','m','r','lol'])

    def test_mapper_mlw(self):
        Keys = ['some','tExt','with','Mistakes','and','m','r','lol']
        words=list(mapper.max_length_words(zip(map(lambda x: x.lower(),Keys),map(lambda x: len(x),Keys))))
        self.assertEqual(words,[('mistakes',8)])          
if __name__ == '__main__':
    unittest.main()
         