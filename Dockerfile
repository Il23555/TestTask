FROM python:3.9
WORKDIR /sticker_predict
COPY requirements.txt /sticker_predict
RUN pip3 install --upgrade pip -r requirements.txt
COPY . /sticker_predict
EXPOSE 5000
CMD python start.py
