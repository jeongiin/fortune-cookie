FROM bitnami/pytorch:latest
LABEL maintainer "jeongin <jeongin@naver.com>"

WORKDIR /app
COPY app/utils.py .
COPY app/cookie_maker.py .
RUN pip3 install unittest
ENV LOGPATH='/data'
ENV DATAPAHT='/data'
ENTRYPOINT ["python3"]
CMD ["cookie_maker.py"]