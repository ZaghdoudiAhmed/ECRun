from app.extensions import db,fake # Import your db and faker instance instance from your app
from app.models.Client import Client
from app.models.CodeAppointment import CodeAppointment
from app.models.DrivingAppointment import DrivingAppointment
from app.models.Quiz import Quiz
from app.models.Question import Question
from app.models.Response import Response
from main import create_app
import random


app = create_app()

# Generated client data 
client_data= []
for _ in range(20):
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.email()
    phone_number = fake.random_int(min= 20000000, max = 99000000)
    cin_number = fake.random_int(min= 12000000, max = 99999999)
    cin_recto = fake.image_url()
    cin_verso = fake.image_url()
    address = fake.address()
    date_of_birth = fake.date_of_birth(minimum_age=18, maximum_age=65)
    nb_hours_code = fake.random_int(min=1, max= 99)
    nb_hours_driving = fake.random_int(min=1, max= 99)

    client_instance = Client(
        first_name=first_name,
        last_name=last_name,
        email=email,
        phone_number=phone_number,
        cin_number=cin_number,
        cin_recto=cin_recto,
        cin_verso=cin_verso,
        address=address,
        date_of_birth=date_of_birth,
        nb_hours_code=nb_hours_code,
        nb_hours_driving=nb_hours_driving
    )
    client_data.append(client_instance)
    # Add the generated client data to the database 
    with app.app_context():
        db.session.add_all(client_data)
        db.session.commit()

# Generated code appointement data 
with app.app_context():
        clients = Client.query.all() #Fetch all clients from database
        code_appointment_data= []

        for _ in range(10):
            test_date_code= fake.date_of_birth(minimum_age=18, maximum_age=65)
            client = random.choice(clients)
            code_appointment_instance = CodeAppointment(
                test_date_code=test_date_code,
                client_id = client.id
            )
            code_appointment_data.append(code_appointment_instance)
        db.session.add_all(code_appointment_data)
        db.session.commit()


# Generated driving appointement data 
with app.app_context():
    clients = Client.query.all() #Fetch all clients from database
    driving_appointment_data = []

    for _ in range(10):
        test_date_driving= fake.date_of_birth(minimum_age=18, maximum_age=65)
        client = random.choice(clients)
        driving_appointment_instance= DrivingAppointment(
             test_date_driving=test_date_driving,
             client_id =client.id
        )
        driving_appointment_data.append(driving_appointment_instance)
    db.session.add_all(driving_appointment_data)
    db.session.commit()

# Generated Quiz data
with app.app_context():
    code_appointments = CodeAppointment.query.all()
    quiz_data = []
    for _ in range(10):
        uuid = fake.uuid4()
        score = fake.random_int(min=0,max=100)
        code_appointment = random.choice(code_appointments)
        quiz_instance = Quiz(
             uuid=uuid,
             score=score,
             appointment_id= code_appointment.id
        )
        quiz_data.append(quiz_instance)
    db.session.add_all(quiz_data)
    db.session.commit()
    
# Generated Question data
with app.app_context():
    quizes = Quiz.query.all()  #Fetch all quizes from database

    question_data = []
    for _ in range(10):
        text = fake.paragraph()
        quiz = random.choice(quizes)
        question_instance = Question(
            text=text,
            quiz_id = quiz.id
        )
        question_data.append(question_instance)
    db.session.add_all(question_data)
    db.session.commit()

# Generated Response data
with app.app_context():
    questions = Question.query.all()  #Fetch all questions from database

    response_data = []
    for _ in range(10):
        text = fake.paragraph()
        is_correct = fake.boolean()
        question = random.choice(questions)
        response_instance = Response(
            text=text,
            is_correct=is_correct,
            question_id = question.id
        )
        response_data.append(response_instance)
    db.session.add_all(response_data)
    db.session.commit()




