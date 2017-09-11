#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import request, render_template, redirect, url_for, request, flash
from plugins import app

@app.route("/competitions", methods=['GET'])
def competitions_index(): 
    return render_template('commons/base.html')


@app.route("/competitions/<int:id>", methods=['GET'])
def competitions_show(id): 
    return render_template('commons/base.html')


@app.route("/competitions/new", methods=['GET', 'POST'])
def competitions_new(): 
    return render_template('commons/base.html')


@app.route("/competitions/edit/<int:id>", methods=['GET','UPDATE'])
def competitions_edit(id): 
    return render_template('commons/base.html')


@app.route("/competitions/<int:id>", methods=['DELETE'])
def competitions_destroy(): 
    return render_template('commons/base.html')