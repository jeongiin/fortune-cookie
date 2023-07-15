FROM bitnami/pytorch:latest
LABEL maintainer "jeongin <jeongin@naver.com>"

WORKDIR /app
COPY app/utils.py .
COPY app/cookie_maker.py .
COPY ./requirements.txt /code/requirements.txt
RUN pip3 install -r /code/requirements.txt
ENV LOGPATH='/data'
ENV DATAPAHT='/data'
ENTRYPOINT ["python3"]
CMD ["cookie_maker.py"]