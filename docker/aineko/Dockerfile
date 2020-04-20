From bigjust/helga:latest

WORKDIR /code
ADD settings-aineko.py /aineko-settings.py
RUN pip install helga-yelling
#RUN ls /code
RUN pip install /code

ENTRYPOINT ["/usr/local/bin/helga"]
CMD ["--settings=/aineko-settings.py"]
