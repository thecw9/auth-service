FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10

WORKDIR /app

# Copy the requirements.txt first for better cache on later pushes
COPY ./requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

# Copy the main application
COPY . .

EXPOSE 8000

# Run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]


