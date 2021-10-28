import pysftp
import os

s3_location = ''

def main():
	files  = os.listdir('./s3_bucket')
	with pysftp.Connection('hostname', username='me', password='secret') as sftp:
		for file in files:
        	sftp.put(f'/my/local/filename/{file}')  # upload file to public/ on remote

if __name__ == '__main__':
	main()
