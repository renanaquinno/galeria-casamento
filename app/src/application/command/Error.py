from flask import Flask, render_template
def Error(nome):
    return render_template("error.html")