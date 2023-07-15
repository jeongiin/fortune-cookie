FROM python:3.9
LABEL maintainer "jeongin <jeongin@naver.com>"

WORKDIR /app
COPY app/utils.py .
COPY app/cookie_maker.py .
ENV LOGPATH='/data'
ENV DATAPATH='/data'
ENTRYPOINT ["python3"]
CMD ["cookie_maker.py"]