#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import request, render_template, redirect, url_for, request, flash
from plugins import app

@app.route("/bets", methods=['GET'])
def bets_index(): 
    return render_template('commons/base.html')


@app.route("/bets/<int:id>", methods=['GET'])
def bets_show(id): 
    return render_template('commons/base.html')


@app.route("/bets/new", methods=['GET', 'POST'])
def bets_new(): 
    return render_template('commons/base.html')


@app.route("/bets/edit/<int:id>", methods=['GET', 'UPDATE'])
def bets_edit(id): 
    return render_template('commons/base.html')


@app.route("/bets/<int:id>", methods=['DELETE'])
def bets_destroy(): 
    return render_template('commons/base.html')