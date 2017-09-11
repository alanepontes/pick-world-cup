#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import request, render_template, redirect, url_for, request, flash
from plugins import app

@app.route("/", methods=['GET'])
@app.route("/users", methods=['GET'])
def users_index(): 
    return render_template('commons/base.html')


@app.route("/users/<int:id>", methods=['GET'])
def users_show(id): 
    return render_template('commons/base.html')


@app.route("/users/new", methods=['POST', 'GET'])
def users_new(): 
    return render_template('commons/base.html')


@app.route("/users/edit/<int:id>", methods=['GET', 'UPDATE'])
def users_edit(id): 
    return render_template('commons/base.html')


@app.route("/users/<int:id>", methods=['DELETE'])
def users_destroy(): 
    return render_template('commons/base.html')


@app.route("/users/login", methods=['GET','POST'])
def users_login(): 
    return render_template('users/login.html')