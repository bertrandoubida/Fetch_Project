# Fetch_Project
This is a Health Checker written in Python to utilize the provided HTTP Endpoints to yield cumulative results.
Results are logged every 15 seconds, showing the cumulative availability percentages for each monitored domain.

## Docker

To access the results, you can use Docker for a simple and seamless experience.
To quickly run this, if you have docker installed on your system, all that is needed is to
1. Pull the Docker Image with '''docker pull bertrandoubida/fetch_health_checker:2025'''
2. Run the Docker container interactively to see the results with '''docker run -it bertrandoubida/fetch_health_checker:2025'''
3. To exit or stop the container, press '''Ctrl+C'''.


## Local build and run

If you're not using docker, and instead are using your local environment to build all that is needed and run this, here are the steps
1. Install Python if not already on your system.
2. Check that "Pip" is installed as well when python is done. You'll need to install "requests and pyyaml", ("pip install requests pyyaml" should do the trick).
3. After all is installed, simply run "python main.py config.yml"
4. To stop the script, press '''Ctrl+C'''.

## Output
'''
fetch.com has 67% availability percentage
www.fetchrewards.com has 100% availability percentage
'''
The output should look something like the example above.
