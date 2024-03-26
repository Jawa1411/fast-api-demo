FROM python:3.10

WORKDIR /code

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        cmake \
        libgdal-dev \
        gdal-bin \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install QGIS dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        --fix-missing \
        qgis \
        qgis-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./src /code/app

RUN pip install scipy scikit-image scikit-learn opencv-python-headless

# To fix the ImportError: cannot import name '_gdal_array' from 'osgeo' on ReadAsArray()
RUN pip install --no-cache-dir --force-reinstall 'GDAL[numpy]==3.6.2' 

# EXPOSE 80

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80"]
# CMD [ "gunicorn", "app.main:app" ]