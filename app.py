from flask import Flask, render_template, request
import pandas as pd

def crear_app():

    app = Flask(__name__)

    class Activity:
        def __init__(self, name, duration, predecessors):
            self.name = name
            self.duration = int(duration)
            self.predecessors = [p.strip() for p in predecessors.split(',') if p.strip()] if predecessors else []
            self.TIP = 0
            self.TTT = 0
            self.slack = 0

    def calculate_cpm(activities):
        activity_dict = {a.name: a for a in activities}

        # Cálculo hacia adelante (TIP)
        for act in activities:
            if not act.predecessors:
                act.TIP = 0
            else:
                act.TIP = max(activity_dict[p].TIP + activity_dict[p].duration for p in act.predecessors)

        # Cálculo hacia atrás (TTT)
        max_tip = max((a.TIP + a.duration) for a in activities)
        for act in reversed(activities):
            if all(act.name not in a.predecessors for a in activities):
                act.TTT = max_tip - act.duration
            else:
                successors = [a for a in activities if act.name in a.predecessors]
                act.TTT = min(s.TTT - act.duration for s in successors)

        # Holgura
        for act in activities:
            act.slack = act.TTT - act.TIP

        critical_path = [a.name for a in activities if a.slack == 0]
        project_duration = max_tip  # Esta es la duración total del proyecto

        return activities, critical_path, project_duration

    @app.route('/', methods=['GET', 'POST'])
    def index():
        activities = []
        cpm = []
        critical_path = []

        names = request.form.getlist('name') if request.method == 'POST' else []
        durations = request.form.getlist('duration') if request.method == 'POST' else []
        precedences = request.form.getlist('precedence') if request.method == 'POST' else []
        project_duration = 0


        if request.method == 'POST':
            for name, dur, prec in zip(names, durations, precedences):
                if name.strip() and dur.strip():
                    try:
                        activities.append(Activity(name.strip(), dur.strip(), prec.strip()))
                    except ValueError:
                        continue

            if activities:
                cpm, critical_path, project_duration = calculate_cpm(activities)


        # Número de filas a mostrar siempre es igual al número de entradas ingresadas o al menos 3
        num_rows = max(len(names), 3)

        return render_template(
            'index.html',
            activities=cpm,
            critical_path=critical_path,
            names=names,
            durations=durations,
            precedences=precedences,
            num_rows=num_rows,
            project_duration=project_duration
        )
    return app

if __name__ == '__main__':
    app = crear_app()
    app.run(debug=True, host='127.0.0.1', port=5055)

