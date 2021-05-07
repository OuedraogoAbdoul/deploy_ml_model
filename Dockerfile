FROM python:3.6.4

WORKDIR /usr/src/ml_app/

ADD . /usr/src/ml_app/

RUN pip install --upgrade pip
RUN  python3.6 -m pip install --upgrade pip

RUN pip install -r /usr/src/ml_app/regression_model/requirement.txt
RUN pip install notebook

EXPOSE 5000

CMD ["jupyter", "notebook", "--port=8888", "--no-browser", "--ip=0.0.0.0", "--allow-root", "bash"]
