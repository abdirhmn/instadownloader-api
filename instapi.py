from fastapi import FastAPI
import instaloader

app = FastAPI()

L = instaloader.Instaloader()


@app.get("/posts-reels-stories-igtv")
async def download_post(link: str = "https://www.instagram.com/p/Cs3leViPf63/?utm_source=ig_web_copy_link&igshid=MzRlODBiNWFlZA"):
    try:
        post = instaloader.Post.from_shortcode(L.context, link.split("/")[-2])
        L.download_post(post, target="./download")
        return {"message": "Post downloaded successfully!"}
    except Exception as e:
        return {"error": str(e)}

