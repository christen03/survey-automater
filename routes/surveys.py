from flask import Blueprint, render_template, request, jsonify
from .mcdonald import survey, isDone
import threading 

surveyResult=[None]

surveys=Blueprint('surveys', __name__)
@surveys.route('/MCDSurveyRunning', methods=["POST"])
def runSurvey():
    surveyCode=[]
    for i in range(1,7):
        if(not request.form.get("code"+str(i))):
            errorMessage="Please enter all form fields!"
            return render_template("failed.html", errorMessage=errorMessage)
        else:
            surveyCode.append(request.form.get("code"+str(i)))
    survey_thread = threading.Thread(target=survey, args=(surveyCode, surveyResult,))
    survey_thread.start()
    return render_template("running.html")
    
@surveys.route('/status')
def survey_status():
    if isDone():
        if(surveyResult[0]!=None):
            return jsonify({"status" : "finished"})
        else:
            return jsonify({"status" : "failed"})
    return jsonify({"status" : "running"})

@surveys.route('/MCDSurveyDone')
def results():
    return render_template("finished.html", code=surveyResult[0], surveyType="MCD")

@surveys.route('/MCDfailed')
def failed():
    errorMessage="Invalid code!"
    return render_template("failed.html", errorMessage=errorMessage)