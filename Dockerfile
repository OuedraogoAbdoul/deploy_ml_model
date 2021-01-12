FROM python:3.9.1

WORKDIR /usr/src/ml_app/

ADD . /usr/src/ml_app/

RUN pip install --upgrade pip
RUN pip install -r /usr/src/ml_app/regression_model/requirement.txt

EXPOSE 5000

CMD ["bash"]
