from flask import Flask, render_template
import random
app = Flask(__name__)
images = [
 "https://i2.wp.com/www.libraryforsmartinvestors.com/wp-content/uploads/2017/02/aws_logo.jpg?fit=500%2C500&ssl=1",
 "http://australiaday.openstack.org.au/wp-content/uploads/2016/01/openstack_500x500.png",
 "http://isoc.ae/image/cache/catalog/courses/Google%20Cloud%20Compute%20Engine%20Essential%20Training-500x500.jpg",
 "https://static.onthehub.com/production/attachments/9/9cb7d193-f0b7-e611-9423-b8ca3a5db7a1/7d04d71c-c4e0-4df8-8e07-ff33bf12915e.png",
 "https://aptira.com/wp-content/uploads/2016/09/kubernetes_logo.png",
 "https://www.opsview.com/sites/default/files/docker.png"
]
@app.route('/')
def index():
 url = random.choice(images)
 return render_template('index.html', url=url)
if __name__ == "__main__":
 app.run(host="0.0.0.0")
