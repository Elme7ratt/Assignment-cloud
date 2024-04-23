    FROM python:latest

    WORKDIR /PROGRAM
    
    COPY fff.txt .
    
    RUN pip install ntlk
    
    COPY prog.py .
    
    CMD python prog.py