# ClapBackBot

Web app that generates comebacks to a roast.

<img src="https://github.com/user-attachments/assets/9338b1e9-0e5f-4caa-907a-f61db9414c5c" width="600"/>

(Frontend WIP)

## Roadmap

- Host docker container to make web app publicly accessible
- Flesh out front end
- Improve quality of AI response

## Deployment

There are two ways to deploy if you want to test the project:
- Local host project manually
- Build and run docker container

Running locally:
- Install python requirements from backend/requirements.txt with `pip install -r backend/requirements.txt`
- Separately install the version of torch best suited to your hardware
- Start the flask server using `python3 backend/server.py`
- Install Node.js dependencies by navigating into the frontend directory then run `npm install`
- Start node server using `npm run dev -- --host`

Running docker container:
- Build docker image using `docker build -t clapbackbot_container .`
- Start docker image using `docker run -p 5173:5173 -p 5000:5000 clapbackbot_container`

**Note:** The backend flask server takes longer to start than the node server due to large python imports. This may result in the webpage being accessable, but a backend error if a request is made too early.
