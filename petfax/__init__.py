from flask import Flask 

# factory
def create_app(): 
    app = Flask(__name__)

    #register pet blueprint
    from . import pet
    app.register_blueprint(pet.bp)

    from . import fact
    app.register_blueprint(fact.bp)

    @app.route('/')
    def hello(): 
        return 'Hello, PetFax!'

    return app
