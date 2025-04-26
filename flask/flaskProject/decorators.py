from functools import wraps
from flask import render_template, g, url_for, redirect


def login_required(func):
    # 保留func信息
    @wraps(func)
    def inner(*args, **kwargs):
        if g.user:
            return func(*args, **kwargs)
        else:
            return redirect(url_for('auth.login'))
    return inner