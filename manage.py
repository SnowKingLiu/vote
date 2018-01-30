# _*_ coding: utf-8 _*_
# by:Snowkingliu
# 2018/1/30 下午5:15
# from flask.ext.script import Manager
#
# from vote import app
#
# manager = Manager(app)
#
#
# @manager.command
# def hello():
#     print "Start"
#
#
# if __name__ == "__main__":
#     manager.run()

from flask_script import Manager, Shell

from vote import app

manager = Manager(app)


def make_shell_context():
    return dict(app=app)


manager.add_command("shell", Shell(make_context=make_shell_context))


@manager.command
def deploy():
    pass


if __name__ == '__main__':
    manager.run()

