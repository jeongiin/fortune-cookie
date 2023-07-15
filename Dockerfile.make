FROM bitnami/pytorch:latest
LABEL maintainer "jeongin <jeongin@naver.com>"

WORKDIR /app
COPY app/utils.py .
COPY app/cookie_maker.py .
ENV LOGPATH='/data'
ENV DATAPAHT='/data'
ENTRYPOINT ["python3"]
CMD ["python" "cookie_maker.py"]