from ipywidgets import *
from functools import partial
from IPython.display import display
import json

def load_style():
    style = HTML("""
<style>
.widget-radio-box{
    display: inline;
}
.widget-radio-box label{
    padding-right: 2em;
}
.answer_labels{
    background: #d2d6ba;
    padding: 7px;
    white-space: break-spaces;
}
h5{
    font-family: "Lucida Sans Unicode, Lucida Grande, sans-serif";
    font-size: 14pt;
}
</stlye>""")
    display(style)
class Quiz():
    def __init__(self, quiz_file):
        fp = open(quiz_file, 'r')
        self.quiz_file = json.load(fp)
        fp.close()

        self.correct_answers = 0
        self.total_questions = 0
        self.answers = {}
        self.answer_key = {}
        self.correct_text = {}
        self.question_output = {}

    def display_questions(self):
        for i, question in enumerate(self.quiz_file):
            display(HTML(f"<h4>Question {i+1    }</h4><h5>{question['question']}</h5>"))

            # get question type from answer key
            read_type = type(question['correct_answer']).__name__

            if read_type == 'int':
                question_type = 'select_one'
            elif read_type == 'list':
                question_type = 'select_multi'
            elif read_type == 'dict':
                question_type = 'match_list'

            
            labels = []
            answers = []
            if question_type == 'select_one':
                for idx, answer in enumerate(question['answers']):
                    answer_key = f'{chr(idx + 65)}'
                    answers.append(answer_key)
                    labels.append(HTML(f"<b>{answer_key}</b>: {answer}"))

                labels =  VBox(labels)
                labels.add_class('answer_labels')

                out = Output()
                options = RadioButtons(options=answers, style={'description_width': '1px'})
                
                self.correct_text[i] = question['answer_text']
                self.answer_key[i] = answers[question['correct_answer']]
                self.answers[i] = options
                self.question_output[i] = out

                display(HBox([options, labels]), out, HTML('<hr>'))

            elif question_type == 'select_multi':
                for idx, answer in enumerate(question['answers']):
                    answer_key = f'{chr(idx + 65)}'
                    answers.append(Checkbox(description=answer_key))
                    labels.append(HTML(f"<b>{answer_key}</b>: {answer}"))
                
                labels =  VBox(labels)
                labels.add_class('answer_labels')

                out = Output()
                options = VBox(answers)

                self.correct_text[i] = question['answer_text']
                self.answer_key[i] = question['correct_answer']
                self.answers[i] = options
                self.question_output[i] = out
                display(HBox([options, labels]), out, HTML('<hr>'))

            elif question_type == 'match_list':
                for idx, answer in enumerate(question['answers']):
                    key = list(answer.items())[0][0]
                    answer_key = f'{chr(idx + 65)}'
                    answers.append(Dropdown(description=key, options=[(xx,ii) for ii, xx in enumerate(answer[key])]))

                out = Output()
                options = VBox(answers)

                self.correct_text[i] = question['answer_text']
                self.answer_key[i] = question['correct_answer']
                self.answers[i] = options
                self.question_output[i] = out
                display(options, out, HTML('<hr>'))

        submit_output = Output()
        button = Button(description= 'Submit Test', button_style='primary')
        button.on_click(partial(self.grade_test, submit_output))
        display(button, submit_output)


    def show_submit(self):
        outp = Output()
        button = Button(description= 'Submit Test', button_style='primary')
        button.on_click(partial(self.grade_test, outp))
        display(button, outp)

    def grade_test(self, outp, btn):
        # btn.is_disabled = True
        self.total_questions = 0
        self.correct_answers = 0
        for idx, item in self.answers.items():
            self.total_questions += 1

            try:
                answer_value = item.value
            except AttributeError:
                if type(item.children[0]).__name__ == 'Checkbox':
                    answer_value = []
                    for i, answer in enumerate(item.children):
                        if answer.value:
                            answer_value.append(i)
                
                elif type(item.children[0]).__name__ == 'Dropdown':
                    answer_value = {}
                    for i, answer in enumerate(item.children):
                        answer_value[answer.description] = answer.value

            expected_value = self.answer_key[idx]

            output = self.question_output[idx]
            with output:
                output.clear_output()
                if answer_value == expected_value:
                    self.correct_answers += 1
                    print(f'✅ Correct. {self.correct_text[idx]}')
                else:
                    print(f'❌ Incorrect.')

        calculated_percent = ( self.correct_answers / self.total_questions * 100)
        
        with outp:
            outp.clear_output()
            print(f"You have correctly solved {round(calculated_percent,2)}% of the questions.")

