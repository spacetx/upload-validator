FROM humancellatlas/upload-validator-base-alpine:19
RUN apk --no-cache --update-cache add gcc gfortran python python-dev py-pip build-base wget freetype-dev libpng-dev openblas-dev
RUN apk --no-cache --update-cache add jpeg-dev
COPY requirements.txt /tmp/
RUN pip install matplotlib==2.1.2 'numpy!=1.13.0'
RUN pip install Cython
RUN pip install --requirement /tmp/requirements.txt PyWavelets==1.0.1
ADD myvalidator.py /validator
RUN chmod +x /validator
RUN pip install sqlalchemy  # Somehow removed
RUN pip install dcplib
