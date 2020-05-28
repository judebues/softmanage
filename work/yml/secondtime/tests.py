from django.test import TestCase

class TestUpload(TestCase):
    def testUploadsuccess(self):
        text = 'UPload over!'
        client = Client()
        mscode = 411
        url =  '/temp/upload/' 


		#****为正确可用文件路径  


        with open('****', 'rb') as fp:  
            response  = client.post(url, data = {'mscode':mscode,'file':fp})
            json_resp = json.loads(response.content)
            self.assertEqual(text,json_resp)

    def testUploadWrongmscode(self):
        text = 'mscode is error'
        url =  '/temp/upload/'
        client = Client()
        mscode = 0
        response = client.post(url,data = {'mscode':mscode})
        json_resp = json.loads(response.content)
        self.assertEqual(text,json_resp)


    def testUploadWrongFileurl(self):
        text = '没有需要上传的文件'
        url =  '/temp/upload/'
        client = Client()
        mscode = 2
        response  = client.post(url, data = {'mscode':mscode})
        json_resp = json.loads(response.text)
        self.assertEqual(text,json_resp)


    def testUploadWrongFiletype(self):
        url =  '/temp/upload/'
        client = Client()
        mscode = 2

    	#****为错误类型文件路径


        with open('****', 'rb') as fp:
            response  = client.post(url, data = {'mscode':mscode,'file':fp})
            json_resp = json.status_code
            self.assertEqual(json_resp,404)