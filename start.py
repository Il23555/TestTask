from app import app
import settings

if __name__ == "__main__":
    app.run(host=settings.HOST, port=settings.PORT, debug=True)
