from dotenv import load_dotenv
import os
from googleapiclient.discovery import build

load_dotenv()
API_KEY = os.getenv('YOUTUBE_API_KEY')
CHANNEL_ID = os.getenv('YOUTUBE_CHANNEL_ID')


def get_channel_videos():
    try:
        youtube = build('youtube', 'v3', developerKey=API_KEY)

        # Get all videos from channel
        videos = []
        next_page_token = None

        while True:
            # Get videos page by page
            request = youtube.search().list(
                part='snippet',
                channelId=CHANNEL_ID,
                maxResults=50,  # Maximum allowed per request
                type='video',  # Only get videos
                pageToken=next_page_token
            )
            response = request.execute()

            # Extract video URLs
            for item in response['items']:
                video_id = item['id']['videoId']
                title = item['snippet']['title']
                url = f"https://www.youtube.com/watch?v={video_id}"
                videos.append({'title': title, 'url': url})

            # Check if there are more pages
            next_page_token = response.get('nextPageToken')
            if not next_page_token:
                break

        print(f"Found {len(videos)} videos")
        for i, video in enumerate(videos, 1):
            print(f"{i}. {video['title']}")
            print(f"   {video['url']}\n")

        return videos

    except Exception as e:
        print(f"Error fetching videos: {str(e)}")
        return None


import webbrowser
import time


# def play_videos_in_batches(urls, batch_size=10, wait_time_minutes=10):
#     # Splitting the URLs into batches of size `batch_size`
#     for i in range(0, len(urls), batch_size):
#         batch = urls[i:i + batch_size]
#         print(f"Playing batch {i // batch_size + 1}:")
#
#         # Open each video in the batch
#         for url in batch:
#             print(f"Opening: {url}")
#             webbrowser.open(url)
#
#         # Wait for the specified time before playing the next batch
#         if i + batch_size < len(urls):  # No need to wait after the last batch
#             print(f"Waiting for {wait_time_minutes} minutes before the next batch...\n")
#             time.sleep(wait_time_minutes * 60)  # Convert minutes to seconds


def play_videos_in_batches(urls, batch_size=10, wait_time_minutes=10):
    # Splitting the URLs into batches of size `batch_size`
    for i in range(0, len(urls), batch_size):
        batch = urls[i:i + batch_size]
        print(f"Playing batch {i // batch_size + 1}:")

        # Open each video in the batch
        for url in batch:
            print(f"Opening: {url}")
            webbrowser.open(url)

        # Wait for the specified time before closing the browser
        print(f"Waiting for {wait_time_minutes} minutes...")
        time.sleep(wait_time_minutes * 60)  # Convert minutes to seconds

        # Close all browser windows/tabs
        print("Closing all browser tabs/windows...")
        if os.name == 'nt':  # For Windows
            os.system("taskkill /im chrome.exe /f")  # Replace "chrome.exe" with your browser's process name
        elif os.name == 'posix':  # For macOS/Linux
            os.system("pkill -f 'Google Chrome'")  # Replace "Google Chrome" with your browser's process name

        print("Browser closed.\n")


def play_videos_in_parallel(urls, batch_size=10, wait_time_minutes=10):
 # Splitting the URLs into batches of size `batch_size`
 for i in range(0, len(urls), batch_size):
  batch = urls[i:i + batch_size]
  print(f"Playing batch {i // batch_size + 1} with {len(batch)} videos:")

  # Open all videos in the batch in parallel
  for url in batch:
   print(f"Opening: {url}")
   webbrowser.open(url)

  # Wait for the specified time while videos play in parallel
  print(f"Waiting for {wait_time_minutes} minutes for videos to play...")
  time.sleep(wait_time_minutes * 60)  # Convert minutes to seconds

  # Close all browser windows/tabs after the wait time
  print("Closing all browser tabs/windows...")
  if os.name == 'nt':  # For Windows
   os.system("taskkill /im chrome.exe /f")  # Replace "chrome.exe" with your browser's process name
  elif os.name == 'posix':  # For macOS/Linux
   os.system("pkill -f 'Google Chrome'")  # Replace "Google Chrome" with your browser's process name
  print("Browser closed.\n")
# Call the function to play videos in batches
if __name__ == "__main__":
    # video = get_channel_videos()
    # print(video)
    video_data=[{'title': 'What Is Apache Spark?', 'url': 'https://www.youtube.com/watch?v=G1XYo3QtxaI'},
     {'title': 'AWS Application Integration #queues #aws #clouds',
      'url': 'https://www.youtube.com/watch?v=3PFP_L-QVys'},
     {'title': 'MongMongoDB:Using MongoDB with Node.js, Express and Angular',
      'url': 'https://www.youtube.com/watch?v=8y33khlQCHQ'},
     {'title': 'Spark API #spark #dataengineering', 'url': 'https://www.youtube.com/watch?v=BpnF8Zmbu8E'},
     {'title': 'Introduction to the Databricks Lakehouse platform',
      'url': 'https://www.youtube.com/watch?v=F3L-XXZPuo8'},
     {'title': 'Big-data Batch vs streaming', 'url': 'https://www.youtube.com/watch?v=9OUD2CVcoOg'},
     {'title': 'Messaging Patterns: RealTime #apachekafka', 'url': 'https://www.youtube.com/watch?v=1lxG-tTigdg'},
     {'title': 'Airflow : How to create an operator', 'url': 'https://www.youtube.com/watch?v=mmvJOVXyxps'},
     {'title': 'Data Engineering Interview Experience at Airwallex 💼',
      'url': 'https://www.youtube.com/watch?v=94stOgHZ0kM'},
     {'title': 'A comprehensive comparison of AWS, GCP, Azure, and Alibaba Cloud',
      'url': 'https://www.youtube.com/watch?v=M0S1hdnwz5g'},
     {'title': 'Introduction to Greenplum: A High-Performance Analytical Database',
      'url': 'https://www.youtube.com/watch?v=fWKL1ChB15I'},
     {'title': 'Optimizing Hive SQL Query Performance: Best Practices and Techniques #aws #bigdata #hive #sql',
      'url': 'https://www.youtube.com/watch?v=afBMW3TJFSc'},
     {'title': 'GCP-Stackdriver Workspaces Cloud Operations', 'url': 'https://www.youtube.com/watch?v=xLLZipkilVY'},
     {'title': 'CGP : Cloud SQL and Cloud datastore', 'url': 'https://www.youtube.com/watch?v=2jTGekDNzao'},
     {'title': '13 RomanTo Int #LeetCode #python # coding Interview',
      'url': 'https://www.youtube.com/watch?v=yC6FCNn2O1M'},
     {'title': '2 02 scala val var def', 'url': 'https://www.youtube.com/watch?v=usRRQhrInmg'},
     {'title': 'Python The Collections Module Counter', 'url': 'https://www.youtube.com/watch?v=FK4YhICNBvs'},
     {'title': 'Apache Kafka vs Amazon Kinesis vs Apache Spark: Which is Right for You?',
      'url': 'https://www.youtube.com/watch?v=_I43ivfQzVw'},
     {'title': 'Python:ChainMap Collections Module in Python', 'url': 'https://www.youtube.com/watch?v=4g1-kCn4jdc'},
     {'title': '680. valid palindrome ii python', 'url': 'https://www.youtube.com/watch?v=DFHA5Pgvqq4'},
     {'title': 'Data Engineering Interview: Top 3 Questions Answered by Lead Engineer',
      'url': 'https://www.youtube.com/watch?v=OwK5LBLryX8'},
     {'title': 'Looker ML Guides for Beginners #data', 'url': 'https://www.youtube.com/watch?v=Q6XHqDgveR0'},
     {'title': 'Work through an example to learn how to read and write Spark DataFrames',
      'url': 'https://www.youtube.com/watch?v=tbK78j5xv5E'},
     {'title': 'what is data engineer for GCP #gcp #data', 'url': 'https://www.youtube.com/watch?v=WTgrLZiNph8'},
     {'title': 'Google Cloud Composer-Airflow in 10 min #gcp #airflow #clouds #architecture',
      'url': 'https://www.youtube.com/watch?v=k7l0P-86nI4'},
     {'title': 'Spark Datasets', 'url': 'https://www.youtube.com/watch?v=fz-t4MGSoyw'},
     {'title': '02 Scala Principle of Uniform Access', 'url': 'https://www.youtube.com/watch?v=FNRw7Jt91UU'},
     {'title': 'MongoDB:High Availability and High-Throughput Configurations',
      'url': 'https://www.youtube.com/watch?v=n3gbss9BgIk'},
     {'title': 'Commit Log :Apache Kafka  #log #commitlog #apachekafka #confluent #cloudwala',
      'url': 'https://www.youtube.com/watch?v=Mvm5_uyjWRw'},
     {'title': 'Python Multiprocessing Tutorial: Parallel Programming Made Easy',
      'url': 'https://www.youtube.com/watch?v=yGCdtAR_7nk'},
     {'title': 'Introduction to Secondary Indexes In DynamoDB', 'url': 'https://www.youtube.com/watch?v=uq8Xxm90FvM'},
     {'title': 'Data Engineering Product :Amazon Web Services (AWS)',
      'url': 'https://www.youtube.com/watch?v=B2mf3Ouj_PE'},
     {'title': 'Mastering Parallel and Distributed Computing with Dask in Python',
      'url': 'https://www.youtube.com/watch?v=X8HZUpHEUp8'},
     {'title': 'Choosing the Right Database for Your Needs: PostgreSQL, MySQL, Hive, and HBase',
      'url': 'https://www.youtube.com/watch?v=1crWXWYAkKM'},
     {'title': '04 scala sbt install :Scala Tutorials - Installing SBT',
      'url': 'https://www.youtube.com/watch?v=yB_96ikbIzY'},
     {'title': '03 scala install', 'url': 'https://www.youtube.com/watch?v=xj8HGacSTDM'},
     {'title': '07 Dynamo DB Monitoring  using cloudwatch', 'url': 'https://www.youtube.com/watch?v=XzZomSkQBfo'},
     {'title': 'data build tool Getting Started with DBT: A Beginner&#39;s Guide',
      'url': 'https://www.youtube.com/watch?v=geTXCRFyfXI'},
     {'title': 'Data Ingestion Done Right: Streamline Your Workflow with Databricks &amp; Delta Lake',
      'url': 'https://www.youtube.com/watch?v=Uz-mQde1G04'},
     {'title': 'GCP BigTable in 10 minute #gcp #dataengineer #bigdata',
      'url': 'https://www.youtube.com/watch?v=n-jM0U2p7Ww'},
     {'title': 'Spark SQL Engine', 'url': 'https://www.youtube.com/watch?v=Ews3x3tchvo'},
     {'title': 'Python: Interactively Learn Advanced Concepts in Python 3',
      'url': 'https://www.youtube.com/watch?v=On3HwFbi_48'},
     {'title': '01 Flink Streaming overview | Introduction to Apache Flink| Flink',
      'url': 'https://www.youtube.com/watch?v=QRvLAmdwWYQ'},
     {'title': '23  Merge k Sorted Lists', 'url': 'https://www.youtube.com/watch?v=25zp0tEk6FQ'},
     {'title': 'Kafka Partitions and partition rebalance', 'url': 'https://www.youtube.com/watch?v=JCNLBfOmsFI'},
     {'title': 'Feature Hashing: Efficient Categorical Data Encoding for Large-Scale ML Systems',
      'url': 'https://www.youtube.com/watch?v=VPHgSUHx6AE'},
     {'title': 'Apache Airflow Architecture', 'url': 'https://www.youtube.com/watch?v=Iod9wkIUR9A'},
     {'title': 'AWS: Full Course 2023 | AWS Tutorial For Beginners 2023 | AWS Training For Beginners #aws',
      'url': 'https://www.youtube.com/watch?v=pTxXFnb22qk'},
     {'title': 'scala course agenda', 'url': 'https://www.youtube.com/watch?v=gk3vYG9Wns8'},
     {'title': 'Core MongoDB\xa0Concepts MongoDB Compass #mongodb',
      'url': 'https://www.youtube.com/watch?v=UcY7g0C1Chc'},
     {'title': 'Apache Spark DataFrames, Schema, data type', 'url': 'https://www.youtube.com/watch?v=bQhrXrgipzY'},
     {'title': 'linked-list  inpython', 'url': 'https://www.youtube.com/watch?v=6_nFwtslZfA'},
     {'title': 'Top Apache Flink Questions', 'url': 'https://www.youtube.com/watch?v=OUpOjPU1uUg'},
     {'title': 'Best Time to Buy and Sell Stock- leetcode', 'url': 'https://www.youtube.com/watch?v=8KEeq2mA19g'},
     {'title': '189  Rotate Array', 'url': 'https://www.youtube.com/watch?v=czNA9m4W6ZM'},
     {'title': 'Apache Spark overview Tutorial Spark With Python 3 | Spark Filter',
      'url': 'https://www.youtube.com/watch?v=GEQbJ3zutLs'},
     {'title': '04 flink programming model', 'url': 'https://www.youtube.com/watch?v=T9zk2oEe6bM'},
     {'title': 'Introduction of System Design', 'url': 'https://www.youtube.com/watch?v=ikuPUMcijPI'},
     {'title': 'Python :NamedTuple', 'url': 'https://www.youtube.com/watch?v=AGbtPplqjlc'},
     {'title': 'Google Phone Interview Problem Lyrics and Keyword',
      'url': 'https://www.youtube.com/watch?v=gswT8wjWe-0'},
     {'title': 'Fundamental Building Blocks of AWS An Overview of AWSSecurity, Identity &amp; Compliance #computer #pv',
      'url': 'https://www.youtube.com/watch?v=i86E2FMcLf4'},
     {'title': 'Data Warehouse Case study questions:data warehouse for a large e-commerce company',
      'url': 'https://www.youtube.com/watch?v=YNAw0GKnuUg'},
     {'title': '06 flink architecture', 'url': 'https://www.youtube.com/watch?v=aqy6jFbHN4U'},
     {'title': 'Data Engineer Databricks Architecture and Services',
      'url': 'https://www.youtube.com/watch?v=W-ndFro_VCw'},
     {'title': 'Consecutive Numbers leetcode SQL', 'url': 'https://www.youtube.com/watch?v=Gzb9-QG9v30'},
     {'title': 'Understanding I/O Bound vs CPU Bound in Data Engineering',
      'url': 'https://www.youtube.com/watch?v=HebwgnDdPDw'},
     {'title': '535  Encode and Decode TinyURL', 'url': 'https://www.youtube.com/watch?v=q6me4m0mxkQ'},
     {'title': 'Execution of a Spark Application #dataengineering #spark',
      'url': 'https://www.youtube.com/watch?v=jPCqRGm2KaE'},
     {'title': 'Cracking the Google Associate Cloud Engineer Certification',
      'url': 'https://www.youtube.com/watch?v=vdoZA98epKE'},
     {'title': 'A Database Model for a Taxi Service', 'url': 'https://www.youtube.com/watch?v=BiH2iNxjigo'},
     {'title': 'Understanding Generative AI and Diffusion Models',
      'url': 'https://www.youtube.com/watch?v=knNbokuQ9uo'},
     {'title': 'graph traversal dfs', 'url': 'https://www.youtube.com/watch?v=bmyP86Sj3ec'},
     {'title': '06 scala method-notation', 'url': 'https://www.youtube.com/watch?v=gSrJt904nEg'},
     {'title': 'Kafka Internals:Replication', 'url': 'https://www.youtube.com/watch?v=dPXizhGvB4c'},
     {'title': 'Spark SQL Views and Tables', 'url': 'https://www.youtube.com/watch?v=IAhl2YcUaBM'},
     {'title': 'LeetCode 153. Find Minimum in Rotated Sorted Array',
      'url': 'https://www.youtube.com/watch?v=MBGnqJI6B3w'},
     {'title': '04 Introduction to Machine Learning with MLlib', 'url': 'https://www.youtube.com/watch?v=n5bU11xr5tw'},
     {'title': '283  Move Zeroes', 'url': 'https://www.youtube.com/watch?v=wvPITJrau0w'},
     {'title': 'The Definitive Guide to MongoDB #nosql #dbd', 'url': 'https://www.youtube.com/watch?v=GqhFst4G4LM'},
     {'title': '09 DynamoDB Best Practices', 'url': 'https://www.youtube.com/watch?v=JyDZfmxSlDc'},
     {'title': 'sign-of-the-product-of-an-array-1822 sign-of-the-product-of-an-array #leetcode',
      'url': 'https://www.youtube.com/watch?v=xILt_2NHldg'},
     {'title': 'Head Of Data :Mastery in Data and Analytics', 'url': 'https://www.youtube.com/watch?v=ZUufMgHEOY4'},
     {'title': 'Spark SQL  An Example-scala', 'url': 'https://www.youtube.com/watch?v=fLC6Ib9OIEM'},
     {'title': '146 LRU Cache', 'url': 'https://www.youtube.com/watch?v=fH3nLYz0Y6U'},
     {'title': '07 flink simple program', 'url': 'https://www.youtube.com/watch?v=Z3OdtQPYvIM'},
     {'title': 'Deep Learning Frameworks: Tensorflow, PyTorch, and Keras',
      'url': 'https://www.youtube.com/watch?v=X4VZ9G2VT2w'},
     {'title': 'GCP Dataproc in 10 minute #dataprocessing #gcp #dataengineer #clouds',
      'url': 'https://www.youtube.com/watch?v=9zhtwwTZnNA'},
     {'title': 'GCP Google Cloud CLI', 'url': 'https://www.youtube.com/watch?v=1p1veIFsA48'},
     {'title': 'Amazon Interview: Design a OLTP System for RedBus',
      'url': 'https://www.youtube.com/watch?v=-PM64xeiihw'},
     {'title': 'Databricks:Version and Optimize Delta Tables', 'url': 'https://www.youtube.com/watch?v=yLtJS4DcNy0'},
     {'title': 'Storage: S3 #aws #s3 #cloudvala #storage', 'url': 'https://www.youtube.com/watch?v=I4wj8QKPw0k'},
     {'title': 'Validate IP Address', 'url': 'https://www.youtube.com/watch?v=YnSiNZqWsN8'},
     {'title': 'Databricks The Medallion Architecture', 'url': 'https://www.youtube.com/watch?v=w4NKBV7blzU'},
     {'title': '&quot;Introduction to Hive ORC File Format: Optimizing Hive Queries for Big Data Processing&quot;',
      'url': 'https://www.youtube.com/watch?v=27g-crkpHOc'},
     {'title': '05 logistic regression theory', 'url': 'https://www.youtube.com/watch?v=MwyPASeNEIs'},
     {'title': '02 02 GCP Creating Projects Hands', 'url': 'https://www.youtube.com/watch?v=qZhNl893TLU'},
     {'title': '02 01 creating Projects and IAM Resource Structure and Inheritance',
      'url': 'https://www.youtube.com/watch?v=GMcH4sMohPM'},
     {'title': 'Databricks Data Objects in the Lakehouse', 'url': 'https://www.youtube.com/watch?v=Jz0CbRuE1wo'},
     {'title': 'Unleashing the Power of Data: How Applied Data Science is Revolutionizing Industries',
      'url': 'https://www.youtube.com/watch?v=bVN_4UMVGRc'},
     {'title': 'move-zeroes || data engineer interview question ||',
      'url': 'https://www.youtube.com/watch?v=NF9H6gYNxtM'},
     {'title': 'Mastering One-Hot Encoding: Simple Guide for ML', 'url': 'https://www.youtube.com/watch?v=lNevDVlwE8Y'},
     {'title': 'Add two Linklist using python leetcode  #coding #datastructures #leetcode',
      'url': 'https://www.youtube.com/watch?v=7NLWM-hXY6Q'},
     {'title': 'Find the average length of letters to words', 'url': 'https://www.youtube.com/watch?v=4D8y_Fvu9Pk'},
     {'title': '2 04 scala AbstractProperties', 'url': 'https://www.youtube.com/watch?v=ioFeIkBvFs0'},
     {'title': 'Introduction to Amazon EMR: Simplify Big Data Processing on AWS',
      'url': 'https://www.youtube.com/watch?v=6pE0JilbQ4U'},
     {'title': 'Amazon Onsite Interview :Read a Python file and find the maximum time repeated word',
      'url': 'https://www.youtube.com/watch?v=YAc5AvcGDgI'},
     {'title': 'Simplify Data Transfer- Google BigQuery to Amazon S3 using Amazon AppFlow',
      'url': 'https://www.youtube.com/watch?v=lq5dLqa6ErE'},
     {'title': 'Compute: Lambda compute lambda function#aws #lambdaexpression  #compute #clouds #dataengineer',
      'url': 'https://www.youtube.com/watch?v=pUexfTj7seA'},
     {'title': 'Scala Programming Tutorial Functional Programming Principles in Scala.mov',
      'url': 'https://www.youtube.com/watch?v=9QGD43c7a00'},
     {'title': 'AWS Media Service Kinesis', 'url': 'https://www.youtube.com/watch?v=mS_zTmU_W1Y'},
     {'title': '896  Monotonic Array #code #python', 'url': 'https://www.youtube.com/watch?v=aBaYKI_acRE'},
     {'title': 'Data Governance with Unity Catalog using Databricks',
      'url': 'https://www.youtube.com/watch?v=wqk0pzgfGao'},
     {'title': 'Scalability And Costs In The Cloud #aws #bigdata #cost #clouds',
      'url': 'https://www.youtube.com/watch?v=c54CUR0u0sY'},
     {'title': 'Editing Unveiling Deep Learning The Future of AI Innovation',
      'url': 'https://www.youtube.com/watch?v=hDBsRGkb-4k'},
     {'title': 'HBASE interview question #hbase #bigdata', 'url': 'https://www.youtube.com/watch?v=3aP-Mgn-wk4'},
     {'title': 'Apache Airflow Hello World Example in 5 min', 'url': 'https://www.youtube.com/watch?v=gR3SAh3y9cs'},
     {'title': 'Introduction of Apache Kafka: Apache Kafka', 'url': 'https://www.youtube.com/watch?v=EDRc8NGoAt0'},
     {'title': '48  Rotate Image', 'url': 'https://www.youtube.com/watch?v=CFMl8WLW2Ak'},
     {'title': 'graph traversal bfs', 'url': 'https://www.youtube.com/watch?v=VcPGXG1glgQ'},
     {'title': '88.  Mergeed sorted Array #coding #java #awscloud #python',
      'url': 'https://www.youtube.com/watch?v=790PSUYkoeM'},
     {'title': '06 scala objects#scala', 'url': 'https://www.youtube.com/watch?v=IQN_Wr_IcYY'},
     {'title': 'Stream Processing Pipeline - Using Pub/Sub #realtime #stream',
      'url': 'https://www.youtube.com/watch?v=aGENySKZ1XY'},
     {'title': 'scala', 'url': 'https://www.youtube.com/watch?v=VwAxEi00C3Q'},
     {'title': 'Coding Interview Data Engineer Find Duplicate Number in given List leetcode',
      'url': 'https://www.youtube.com/watch?v=8ZrSWYXYoUo'},
     {'title': 'Spark Application   An Example', 'url': 'https://www.youtube.com/watch?v=cx_lEBWhb-s'},
     {'title': 'Understanding Modern Data Warehousing and Data Lake',
      'url': 'https://www.youtube.com/watch?v=SPX73_-4JfY'},
     {'title': 'google cloud datastore', 'url': 'https://www.youtube.com/watch?v=95HKM2_vL6U'},
     {'title': 'Scala Operating with Operators #Scala', 'url': 'https://www.youtube.com/watch?v=Qw_K3VUSKSw'},
     {'title': 'Unlocking Data Power: Coding for Data Engineers with Databricks Notebooks',
      'url': 'https://www.youtube.com/watch?v=Enn_z1250b0'},
     {'title': '1826  Faulty Sensor #leecode', 'url': 'https://www.youtube.com/watch?v=PBcnF4jpRTA'},
     {'title': '06 scala basic #scala #scalalearning', 'url': 'https://www.youtube.com/watch?v=Y-fyqH1cMSg'},
     {'title': 'Distributed systems for stream processing : Apache Kafka #apachekafka #freedata',
      'url': 'https://www.youtube.com/watch?v=IfRKriBif-4'},
     {'title': 'AWS  : Introduction for compute', 'url': 'https://www.youtube.com/watch?v=3A5KD-8zGQs'},
     {'title': 'GCP How to Select a Compute Service|| data engineer',
      'url': 'https://www.youtube.com/watch?v=BxO6d8pYrno'},
     {'title': 'Cloud Practical Getting Started with Amazon ECS', 'url': 'https://www.youtube.com/watch?v=wQJJrdLJKWY'},
     {'title': 'Spark Operations with DataFrame', 'url': 'https://www.youtube.com/watch?v=s2WQgVNsPW4'},
     {'title': 'Getting started with App Engine', 'url': 'https://www.youtube.com/watch?v=cDxsmt93G8k'},
     {'title': 'python regular expressions for advanced', 'url': 'https://www.youtube.com/watch?v=VSS3FsZ7DlM'},
     {'title': 'Deque in Python #python', 'url': 'https://www.youtube.com/watch?v=ggU8xgQbkag'},
     {'title': '10 ways To Make Over $400 With No-Code', 'url': 'https://www.youtube.com/watch?v=CCT806d6nQk'},
     {'title': 'The Evolution of Deep Learning Key Milestones and Breakthroughs | NextGenAI',
      'url': 'https://www.youtube.com/watch?v=_mSwa7OOivs'},
     {'title': '228  Summary Ranges', 'url': 'https://www.youtube.com/watch?v=2plCVNgDmlQ'},
     {'title': 'designing a data model for a hotel room booking system youtube',
      'url': 'https://www.youtube.com/watch?v=MWmuxMS66cg'},
     {'title': 'DS-Binary tree- leetcode binary tree', 'url': 'https://www.youtube.com/watch?v=g9H56G4DStI'},
     {'title': '415 Add Strings leetcode python #coding #leetcode #data #python',
      'url': 'https://www.youtube.com/watch?v=cz_BGqAWqx0'},
     {'title': 'Building Blocks of Airflow', 'url': 'https://www.youtube.com/watch?v=su201S_yDBs'},
     {'title': 'Resilient Distributed Datasets', 'url': 'https://www.youtube.com/watch?v=jF6Zy0nJS6E'},
     {'title': 'Dense rank SQL  || leetcode -178  Rank Scores || Meta interview | Facebook Interview',
      'url': 'https://www.youtube.com/watch?v=g0KYp_hIfUo'},
     {'title': 'Stack using list python #stack #datastructures', 'url': 'https://www.youtube.com/watch?v=-hkf-cS4fQw'},
     {'title': 'Dive into the Science of Recommendation Systems!',
      'url': 'https://www.youtube.com/watch?v=yXjxfl98ECI'},
     {'title': '543  Diameter of Binary Tree #coding #python', 'url': 'https://www.youtube.com/watch?v=1kbME7CeqIw'},
     {'title': '04-DynamoDB write-Creating Items using put, batch api and CLI',
      'url': 'https://www.youtube.com/watch?v=IIzzkrj1ByQ'},
     {'title': 'Find Palindrom Leet code', 'url': 'https://www.youtube.com/watch?v=9I7QyH8ZN1E'},
     {'title': 'GCP Decision Chart Compute service decision', 'url': 'https://www.youtube.com/watch?v=6C35EJThMm0'},
     {'title': '01 03 Characteristics and Types of Clouds', 'url': 'https://www.youtube.com/watch?v=ciqhXdFLJcY'},
     {'title': '02 scala java install', 'url': 'https://www.youtube.com/watch?v=juY1ZzJSkIE'},
     {'title': 'A Data Model for an Online Musical Equipment Shop : data engineer',
      'url': 'https://www.youtube.com/watch?v=8jmCWOyFyIc'},
     {'title': '896. Monotonic Array || data engineer interview  leet code',
      'url': 'https://www.youtube.com/watch?v=vG2DTxK0HdI'},
     {'title': '577  Employee Bonus', 'url': 'https://www.youtube.com/watch?v=-avvkufFOBA'},
     {'title': 'Bytedance SQL interview questions DE', 'url': 'https://www.youtube.com/watch?v=2L0nRut8eus'},
     {'title': 'GCP Load Balancer DNS', 'url': 'https://www.youtube.com/watch?v=avYri-eT5Vo'},
     {'title': 'Google Cloud Data Studio : Data Visualization', 'url': 'https://www.youtube.com/watch?v=TtvlFAcWku4'},
     {'title': 'Senior Data Engineer SCB Digital Bank Test', 'url': 'https://www.youtube.com/watch?v=lGLrRK-RazM'},
     {'title': 'Google coding interview String #faang #coding #google',
      'url': 'https://www.youtube.com/watch?v=Y-wmjosQPYU'},
     {'title': '01 DynamoDB Deep Dive|DynamoDB Deep Dive||| free Aws NOSQL || Dynamo DB || Big data',
      'url': 'https://www.youtube.com/watch?v=cwXA6iuDsC4'},
     {'title': 'IELTS speaking pattern', 'url': 'https://www.youtube.com/watch?v=MxzGrE40ddk'},
     {'title': 'Spark SQL Data Source Format  #batch #realtime #dataengineering #funlearning #bigdata #pvdata',
      'url': 'https://www.youtube.com/watch?v=LmE0wEKKFNc'},
     {'title': 'Unlock Limitless Computing Power with AWS EC2 - The Future of Cloud Computing is Here!',
      'url': 'https://www.youtube.com/watch?v=ZNvw5ggTdRg'},
     {'title': 'An Introduction to Apache Spark Course', 'url': 'https://www.youtube.com/watch?v=On0Pqjg4cQs'},
     {'title': 'Leetcode Permutations', 'url': 'https://www.youtube.com/watch?v=ClEhA95kJsQ'},
     {'title': '05 scala intelliJ install', 'url': 'https://www.youtube.com/watch?v=CEmmPGba3QI'},
     {'title': '04 linear regression example', 'url': 'https://www.youtube.com/watch?v=jQwehTix9QA'},
     {'title': '182  Duplicate Emails| data engineer |  facebook interview question | meta interview question',
      'url': 'https://www.youtube.com/watch?v=Q9H_ko_GAiQ'},
     {'title': 'twoSum #leetcode #python # two sum leetcode', 'url': 'https://www.youtube.com/watch?v=RvjVWL1Zzto'},
     {'title': '03 flink stream processing', 'url': 'https://www.youtube.com/watch?v=ajqfq5MIuKs'},
     {'title': '287  Find the Duplicate Number', 'url': 'https://www.youtube.com/watch?v=0sMQxI2dIR0'},
     {'title': '05 flink installl #flink #alicloud#realtime', 'url': 'https://www.youtube.com/watch?v=LBPyzZjhbnw'},
     {'title': '268  Missing Number', 'url': 'https://www.youtube.com/watch?v=uoJWqDlSXMY'},
     {'title': 'Machine Learning Primer: Building Robust Training Pipelines',
      'url': 'https://www.youtube.com/watch?v=ANpuJhEHiCU'},
     {'title': '01 06 Getting Started with GCP', 'url': 'https://www.youtube.com/watch?v=NsQ_ROqOE2E'},
     {'title': '03 spark drop and  fill values', 'url': 'https://www.youtube.com/watch?v=zxzF89vwxrQ'},
     {'title': 'GCP Enabling APIs || GCP Enabling APIs || data engineer',
      'url': 'https://www.youtube.com/watch?v=HK9tkAE8nQA'},
     {'title': 'Apache Spark difference with  Storm, Apache Impala, Apache Drill, Apache Mahout, and Apache Giraph',
      'url': 'https://www.youtube.com/watch?v=DH_8DMEV08o'},
     {'title': 'Why Google Cloud Platform GCP', 'url': 'https://www.youtube.com/watch?v=gG9hG6refBw'},
     {'title': 'Leetcode  data engineer coding  Maximum Sub Array',
      'url': 'https://www.youtube.com/watch?v=TGYoEGECJjA'},
     {'title': '1832  Check if the Sentence Is Pangram', 'url': 'https://www.youtube.com/watch?v=8AD8ZtZe0w0'},
     {'title': 'Apache kafka: The power of big data with Apache kafka',
      'url': 'https://www.youtube.com/watch?v=9US6u9BBYfw'},
     {'title': 'GCP Creating Compute Engine VMs', 'url': 'https://www.youtube.com/watch?v=-w_2JB7-0W8'},
     {'title': 'IELTS speaking do and don&#39;ts  #IELTS', 'url': 'https://www.youtube.com/watch?v=Bw79ZxA9NXQ'},
     {'title': 'IELTS speaking guide #IELTS #writing#SG $china #USA',
      'url': 'https://www.youtube.com/watch?v=j0Hdke3CL7A'},
     {'title': 'Databricks Clusters Resources: Setup and Explained in 5 Minutes (Easy Guide)',
      'url': 'https://www.youtube.com/watch?v=KtkBZuW22wI'},
     {'title': 'GCP Virtual Private Cloud VPC', 'url': 'https://www.youtube.com/watch?v=H_wqWSU0f-g'},
     {'title': '08 Access Management DynamoDB Identity and Access Management (IAM) #aws #dynamodb',
      'url': 'https://www.youtube.com/watch?v=1DrUm90PR_0'},
     {'title': 'Data Warehousing: Star Schema and Snowflake Schema , Onsite interview',
      'url': 'https://www.youtube.com/watch?v=NixHWxP8nsU'},
     {'title': 'Spark Application Lifecycle', 'url': 'https://www.youtube.com/watch?v=cdDUcccVa_4'},
     {'title': 'Valid Parentheses Python', 'url': 'https://www.youtube.com/watch?v=itSgXwlqHZc'},
     {'title': '01 04 Cracking the Google Associate Networking Fundamentals',
      'url': 'https://www.youtube.com/watch?v=KmtE3mG0nWs'},
     {'title': 'GCP BIG Query #gcp #bigquery #dataengineering #bigdata #cloudcomputing #freelearning #software',
      'url': 'https://www.youtube.com/watch?v=IdxGpsVBtLM'},
     {'title': 'google cloud  Storage Decision Chart', 'url': 'https://www.youtube.com/watch?v=IBEqwSJ0fu8'},
     {'title': '02-What is DynamoDB?||NoSQL Databases||Salient Features of DynamoDB||AWS Value-added Services',
      'url': 'https://www.youtube.com/watch?v=msvNfGYU98U'},
     {'title': 'GCP Cloud SQL', 'url': 'https://www.youtube.com/watch?v=bgxePg3Efvw'},
     {'title': 'Coding Interview for Data Engineer: find two max number in given array',
      'url': 'https://www.youtube.com/watch?v=qraeHZCHJtU'},
     {'title': 'Spark SQL Views and Tables', 'url': 'https://www.youtube.com/watch?v=oni83geLZvQ'},
     {'title': '01  02 Cracking the Google Associate Cloud Engineer Cloud Fundamentals',
      'url': 'https://www.youtube.com/watch?v=DTbQlfheZbk'},
     {'title': 'yoga music', 'url': 'https://www.youtube.com/watch?v=BHgebTsOAZ8'},
     {'title': '03-DynamoDB Creating Table and DynamoDB Data ModelDynamoDB Creating Table and DynamoDB Data Model',
      'url': 'https://www.youtube.com/watch?v=SNTnP0NAxm0'},
     {'title': 'Google Cloud Machine Learning', 'url': 'https://www.youtube.com/watch?v=jvKGJkWRSIE'},
     {'title': 'GCP Google Kubernetes Engine', 'url': 'https://www.youtube.com/watch?v=SRxX6EqcrYs'},
     {'title': 'Apache Spark DataFrames Columns', 'url': 'https://www.youtube.com/watch?v=YYm73C_wEwY'},
     {'title': '02 03 IAM Roles and Permissions IAM Members and Policies',
      'url': 'https://www.youtube.com/watch?v=Pg1ucr0a-Z0'},
     {'title': '88 merge array leetcode', 'url': 'https://www.youtube.com/watch?v=sRXHc8efslw'},
     {'title': 'Google Stock Is A Better Buy', 'url': 'https://www.youtube.com/watch?v=ANYEkqL-CFo'},
     {'title': 'Coding :string to alphabet python code youtube tags Facebook interview',
      'url': 'https://www.youtube.com/watch?v=MvaxLbESgc4'},
     {'title': '05 DynamoDB read -Querying and Scanning', 'url': 'https://www.youtube.com/watch?v=nte0KgIVKEo'},
     {'title': 'Makro Data Engineer Assignment  #dataengineer', 'url': 'https://www.youtube.com/watch?v=zV1Gn7g_zFQ'},
     {'title': '175 Combination of Two Tables Data Engineer SQL', 'url': 'https://www.youtube.com/watch?v=lP8DzKI6JG4'},
     {'title': 'Google Cloud Cloud Operations Logging', 'url': 'https://www.youtube.com/watch?v=TSdfm1x4v6E'},
     {'title': 'GCP IAM Hands On', 'url': 'https://www.youtube.com/watch?v=XBYSJVguZg8'},
     {'title': 'What is cloud', 'url': 'https://www.youtube.com/watch?v=kucnYbHHOKE'},
     {'title': 'Meta Data Engineering Friend Requests II: Who Has the Most Friends',
      'url': 'https://www.youtube.com/watch?v=3VREJnsx6X4'},
     {'title': 'Morning  Challenge to Change Your Mindset #mindset',
      'url': 'https://www.youtube.com/watch?v=vqH8bqhZqec'},
     {'title': 'Apache Spark overview Tutorial Spark With Python 3 | spark agg and order by and number format',
      'url': 'https://www.youtube.com/watch?v=JCB3et4jUmA'},
     {'title': '01  01 Cracking the Google Associate Cloud Engineer CertificationCloud Computing Inception',
      'url': 'https://www.youtube.com/watch?v=zKTIvAL3XSA'},
     {'title': 'GCP Cloud Storage', 'url': 'https://www.youtube.com/watch?v=q05DfpMYMxQ'},
     {'title': 'Scala : Variable type and Type cast', 'url': 'https://www.youtube.com/watch?v=VK_hvuJa7MM'},
     {'title': '88 merge array leetcode', 'url': 'https://www.youtube.com/watch?v=VwaCjXnceLI'},
     {'title': 'Event Driven Services Cloud Functions', 'url': 'https://www.youtube.com/watch?v=5vRjuY-FE1w'},
     {'title': 'Apache Spark DataFrames row', 'url': 'https://www.youtube.com/watch?v=Pfp3qhh711g'},
     {'title': 'spark date timestamps 03| Spark tutorial', 'url': 'https://www.youtube.com/watch?v=xkp3V66VStE'},
     {'title': '197  Rising Temperature || Meta SQL || Facebook data engineer',
      'url': 'https://www.youtube.com/watch?v=FDzKVruf1aI'},
     {'title': '181 Employees Earning More Than Their Managers', 'url': 'https://www.youtube.com/watch?v=R3MUcDjbqG0'},
     {'title': '176  Second Highest Salary|| data Engineer SQL', 'url': 'https://www.youtube.com/watch?v=l6fIhg-9Ry8'},
     {'title': 'GCP what is dataflow in GCP #dataflow #bigdata #gcp',
      'url': 'https://www.youtube.com/watch?v=yagafVgsr0k'},
     {'title': '884. Uncommon Words from Two Sentences | data engineer coding interview',
      'url': 'https://www.youtube.com/watch?v=5eUBrJ4u1a4'},
     {'title': 'GCP Preemptive VMs and Custom VMs', 'url': 'https://www.youtube.com/watch?v=ypbaNL9nuGU'},
     {'title': 'graph algorithum', 'url': 'https://www.youtube.com/watch?v=-ZUb-PtiRzU'},
     {'title': 'Mastering Apache Spark: Core APIs, Streaming, ML, and More!  | Big Data &amp; Analytics Guide',
      'url': 'https://www.youtube.com/watch?v=sp-HT5mobb8'},
     {'title': 'great learn my final capstone nlp project', 'url': 'https://www.youtube.com/watch?v=-3MNXxCIhSI'},
     {'title': 'GCP Cloud Spanner', 'url': 'https://www.youtube.com/watch?v=i1rgsB5e-Vw'},
     {'title': '597.Friend Requests Overall Acceptance Rate', 'url': 'https://www.youtube.com/watch?v=cXvUxPJKZGo'},
     {'title': 'Understanding Tensors, Vectors &amp; Matrices: The Foundation of Deep Learning &amp; AI',
      'url': 'https://www.youtube.com/watch?v=tvoECZk4bMg'},
     {'title': 'Delta Lake Fundamentals - Your Data Lakehouse Foundation',
      'url': 'https://www.youtube.com/watch?v=kiizhmYaVjM'},
     {'title': 'Apache Spark overview introduction', 'url': 'https://www.youtube.com/watch?v=vJcbqW6ekCI'},
     {'title': 'SQL vs NoSQL and Polyglot Persistence #mongodb #nosql  #hbase #dataengineer',
      'url': 'https://www.youtube.com/watch?v=rNAW9cY3GJQ'},
     {'title': 'Cloud Operations   Other Services trace  log error',
      'url': 'https://www.youtube.com/watch?v=9XNJ7mCe28A'},
     {'title': 'Anatomy of a Spark Application #DAG #data #dataengineering #it #spark #jobs',
      'url': 'https://www.youtube.com/watch?v=DsmuTnbaUA8'},
     {'title': 'Mastering Valid Parentheses Coding | Data Engineer Leet Code',
      'url': 'https://www.youtube.com/watch?v=I9cf1Swr09M'},
     {'title': 'Apache Spark Architecture: A Deep Dive into Big Data Processing',
      'url': 'https://www.youtube.com/watch?v=MdHXj21KkbM'},
     {'title': 'DBT vs. Manual Coding: Why You Should Use DBT for Data Pipelines',
      'url': 'https://www.youtube.com/watch?v=H_XbXDsVSzk'},
     {'title': 'MongoDB:Using MongoDB in C# and .Net Core #mongodb',
      'url': 'https://www.youtube.com/watch?v=KZ8re-z869A'},
     {'title': 'How to use Spark :Joins, Unions, and Window Functions',
      'url': 'https://www.youtube.com/watch?v=rsN3FoLnwNM'},
     {'title': 'Positive Soul Music , Meditation music', 'url': 'https://www.youtube.com/watch?v=q_CjxanRoCg'},
     {'title': '07 Scala case class', 'url': 'https://www.youtube.com/watch?v=TwDnb0Widp8'},
     {'title': 'LeetCode 152 | Maximum Product Subarray', 'url': 'https://www.youtube.com/watch?v=reHEY01TjOo'},
     {'title': 'Introduction Airflow', 'url': 'https://www.youtube.com/watch?v=Bct_cXtptqA'},
     {'title': 'Building a Machine Learning Pipeline to Predict Customer Churn',
      'url': 'https://www.youtube.com/watch?v=qUuDe96KVmk'},
     {'title': 'Python: OrderedDict', 'url': 'https://www.youtube.com/watch?v=SwZV9OCODlk'},
     {'title': 'AWS Security, Identity &amp; Compliance', 'url': 'https://www.youtube.com/watch?v=b8IG_t6YvZQ'},
     {'title': 'GCP Billing Management', 'url': 'https://www.youtube.com/watch?v=gLNnBkT0yCk'},
     {'title': 'Apache Spark: How to Use Higher Order Functions', 'url': 'https://www.youtube.com/watch?v=3Jn7FG1dTnI'},
     {'title': 'Introduction to the Databricks Lakehouse Platform #data  #dataengineering',
      'url': 'https://www.youtube.com/watch?v=DtWzOM3oJDk'},
     {'title': 'Spark User Defined Functions', 'url': 'https://www.youtube.com/watch?v=5mtA44vRG0I'},
     {'title': 'Apache Spark Architecture#data', 'url': 'https://www.youtube.com/watch?v=stJW8K_FOkg'},
     {'title': 'Modern data Architecture for Emerging Infrastructure',
      'url': 'https://www.youtube.com/watch?v=hdGeCqbF7Co'},
     {'title': 'Into vishnoi-prem', 'url': 'https://www.youtube.com/watch?v=vW4vSvDTKZ4'},
     {'title': 'Google Cloud BigQuery in 10 Min #bigquery #gcp #aws #dataengineer #love',
      'url': 'https://www.youtube.com/watch?v=wz-A54ZIkJg'},
     {'title': 'Google Cloud  Pub Sub Cloud Pub/Sub Overview', 'url': 'https://www.youtube.com/watch?v=lYtKDw64GMw'},
     {'title': 'GCP Introduction to Cloud Run', 'url': 'https://www.youtube.com/watch?v=3N84vj6qddI'},
     {'title': 'GCP Cloud Spanner for  Big Data', 'url': 'https://www.youtube.com/watch?v=IAnctFOveUs'},
     {'title': 'Customers Who Never Order meta data Engineer interview question #sql',
      'url': 'https://www.youtube.com/watch?v=noOxDdPJzSY'},
     {'title': 'Interview Preparation and SQL Skills Discussion', 'url': 'https://www.youtube.com/watch?v=0GdHazY_YNQ'},
     {'title': 'GCP Cloud Bigtable #bigtable #gcp #freelearning', 'url': 'https://www.youtube.com/watch?v=eA5bAaqXSyQ'},
     {'title': 'River valley Singapore Mantra Of morning meditation',
      'url': 'https://www.youtube.com/watch?v=U_U2h4QyzFk'},
     {'title': 'Finding User Purchases Find Active Users in SQL || Asked by Amazon',
      'url': 'https://www.youtube.com/watch?v=fZTZ1s1MtT0'},
     {'title': 'Understanding Artificial Neurons: The Core of Deep Learning',
      'url': 'https://www.youtube.com/watch?v=OBXgHowNm18'},
     {'title': 'Quantum black onsite interview tech round 2 case study #casestudy  #mckinsey   #dataengineer',
      'url': 'https://www.youtube.com/watch?v=sFevJVguxGM'},
     {'title': 'Facebook onsite interview for DE', 'url': 'https://www.youtube.com/watch?v=5laibOG22nk'},
     {'title': 'Kafka vs Other Messaging Systems #pubsub #realtime #kafka #sns運用 #apachekafka #bigdata',
      'url': 'https://www.youtube.com/watch?v=EkY8-_K3u9M'},
     {'title': 'meta data engineer interview onsite', 'url': 'https://www.youtube.com/watch?v=w1Ql_4skH3U'},
     {'title': 'DeepSeek vs ChatGPT vs Claude Comparison', 'url': 'https://www.youtube.com/watch?v=J1CIQ3JvmPY'},
     {'title': 'Amazon DATA  engineer :SQL  query to calculate the total time spent by each employee on each day',
      'url': 'https://www.youtube.com/watch?v=y0kh2iJvlew'},
     {'title': 'Exploring Hive&#39;s Supported File Formats: Which One Is Best for Your Big Data Needs',
      'url': 'https://www.youtube.com/watch?v=whjrjGPB1ek'},
     {'title': 'Creating Powerful SQL UDFs in Databricks for Data Manipulation',
      'url': 'https://www.youtube.com/watch?v=PV2ja_mCt24'},
     {'title': 'GCP Cost Planning and Estimation Using Pricing Calculator',
      'url': 'https://www.youtube.com/watch?v=7ERvyQzclpg'},
     {'title': 'Agoda : two sum coding interview', 'url': 'https://www.youtube.com/watch?v=wt8iNxPXEA0'},
     {'title': 'Sea Corporate Lab Online Assessment   Data Engineer',
      'url': 'https://www.youtube.com/watch?v=UdQL6EE-RNc'}]

    print('prem')
    video_urls = [item['url'] for item in video_data]
    print(video_urls)
    # play_videos_in_batches(video_urls)
    play_videos_in_parallel(video_urls, batch_size=5, wait_time_minutes=10)