from flask import Flask, Blueprint

def create_app():

    app = Flask(__name__) 
    app.secret_key = 'Aldovino123'
    
    from Website.Portfolio.login import login_blueprint
    from Website.Portfolio.dashboard import dashboard_blueprint
    from Website.Portfolio.profile import profile_blueprint
    from Website.Portfolio.blog import blog_blueprint
    from Website.Portfolio.crud import crud_blueprint
    from Website.Portfolio.account import account_blueprint
    
    app.register_blueprint(login_blueprint)
    app.register_blueprint(dashboard_blueprint, url_prefix='/dashboard')
    app.register_blueprint(profile_blueprint, url_prefix='/profile')
    app.register_blueprint(blog_blueprint, url_prefix='/blog')
    app.register_blueprint(crud_blueprint)
    app.register_blueprint(account_blueprint, url_prefix='/account')
    
    return app