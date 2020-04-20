From bigjust/helga:latest

WORKDIR /code
ADD settings-aineko.py /aineko-settings.py
ADD requirements.txt aineko-requirements.txt
RUN pip install -r aineko-requirements.txt

ENTRYPOINT ["/usr/local/bin/helga"]
CMD ["--settings=/aineko-settings.py"]
