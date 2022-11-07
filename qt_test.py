# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 10:25:47 2022

@author: pontu
"""

from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QWidget, QGridLayout, QButtonGroup, QRadioButton
from PyQt5.QtCore import pyqtSignal, pyqtSlot

class SeniorityData:
    def __init__(self, sen_prefs, crew_labels, key_labels):
        self.sen_prefs = sen_prefs
        self.crew_labels = crew_labels
        self.key_labels = key_labels

def get_data():
    num_crew = 6
    num_keys = 10
    
    data = []
    for crew_index in range(num_crew):
        crew_data = []
        for key_index in range(num_keys):
            crew_data.append((crew_index, key_index))
            
        data.append(crew_data)
        
    crew_labels = ['%d' % i for i in range(num_crew)]
    key_labels = ['key_%d' % i for i in range(num_keys)]
        
    return SeniorityData(data, crew_labels, key_labels)

def get_data_2():
    crew_labels = ['001', '002', '003', '004', '005', '006', '007']
    key_labels = ['in_A_jan', 'in_A_feb', 'in_A_mar', 
                  'out_B_in_A_jan', 'out_B_in_A_feb', 'out_B_in_A_mar',
                  'out_C_in_A_jan', 'out_C_in_A_feb', 'out_C_in_A_mar']
    
    data = [
        [(1, 1), (1, 2), (1, 3), (1000, 1000), (1000, 1000), (1000, 1000), (1000, 1000), (1000, 1000), (1000, 1000)],
        [(2, 1), (2, 2), (2, 3), (1000, 1000), (1000, 1000), (1000, 1000), (1000, 1000), (1000, 1000), (1000, 1000)],
        [(3, 1), (3, 2), (3, 3), (1000, 1000), (1000, 1000), (1000, 1000), (1000, 1000), (1000, 1000), (1000, 1000)],
        [(-96, 3), (-96, 2), (-96, 1), (4, 3), (4, 2), (4, 1), (1000, 1000), (1000, 1000), (1000, 1000)],
        [(-95, 3), (-95, 2), (-95, 1), (5, 3), (5, 2), (5, 1), (1000, 1000), (1000, 1000), (1000, 1000)],
        [(-94, 3), (-94, 2), (-94, 1), (1000, 1000), (1000, 1000), (1000, 1000), (6, 3), (6, 2), (6, 1)],
        [(-97, 3), (-97, 2), (-97, 1), (1000, 1000), (1000, 1000), (1000, 1000), (7, 3), (7, 2), (7, 1)],
        ]
        
    return SeniorityData(data, crew_labels, key_labels)

class ZeroOrOneRadioButton(QRadioButton):
    def __init__(self, label, parent):
        super().__init__(label, parent)
 
    def mouseReleaseEvent(self, event):
        if self.isChecked():
            self.group().setExclusive(False)
            super().mouseReleaseEvent(event)
            self.group().setExclusive(True)
      
        else:
            super().mouseReleaseEvent(event)
            
    def enterEvent(self, event):
        self.enter_signal.emit()
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.leave_signal.emit()
        super().leaveEvent(event)

        
    enter_signal = pyqtSignal()
    leave_signal = pyqtSignal()

            
class CrewLabel(QLabel):
    def __init__(self, label, parent):
        super().__init__(label, parent)
        self.assigned = False
        self.update_color()
        
    def toggle_assign(self, state):
        if state:
            self.assigned = True
        else:
            self.assigned = False

        self.update_color()
        
    def update_color(self):
        color = 'white' if self.assigned else 'pink'
        self.setStyleSheet('QLabel { background-color : %s; }' % color);

class CrewColumnWidget(QWidget):
    def __init__(self, crew_index, crew_label, crew_data, layout, parent):
        super().__init__(parent)
        self.crew_data = crew_data
        
        label = CrewLabel(crew_label, self)
        layout.addWidget(label, 0, crew_index + 1)
        button_group = QButtonGroup(self)
        
        for key_index, sen_pref in enumerate(crew_data):
            button = ZeroOrOneRadioButton(str(sen_pref), self)
            layout.addWidget(button, key_index + 1, crew_index + 1)
            button_group.addButton(button)
            button.clicked.connect(label.toggle_assign)
            button.clicked.connect(lambda state, crew_index=crew_index, key_index=key_index: self.toggle_assign(crew_index, key_index, False))
            button.enter_signal.connect(lambda crew_index=crew_index, key_index=key_index: self.toggle_assign(crew_index, key_index, True))
            button.leave_signal.connect(lambda crew_index=crew_index, key_index=key_index: self.clear_hover())
            
        self.violation_label = QLabel('', self)
        self.violation_label.setStyleSheet('QLabel { background-color : green; }');
        layout.addWidget(self.violation_label, len(crew_data) + 2, crew_index + 1)

        self.assigned_pref_label = QLabel('', self)
        layout.addWidget(self.assigned_pref_label, len(crew_data) + 3, crew_index + 1)

        self.implied_label = QLabel('', self)
        layout.addWidget(self.implied_label, len(crew_data) + 4, crew_index + 1)

        self.last_label = QLabel('', self)
        layout.addWidget(self.last_label, len(crew_data) + 5, crew_index + 1)

        self.violation_hover_label = QLabel('', self)
        self.violation_hover_label.setStyleSheet('QLabel { background-color : green; }');
        layout.addWidget(self.violation_hover_label, len(crew_data) + 6, crew_index + 1)

        self.assigned_pref_hover_label = QLabel('', self)
        layout.addWidget(self.assigned_pref_hover_label, len(crew_data) + 7, crew_index + 1)

        self.implied_hover_label = QLabel('', self)
        layout.addWidget(self.implied_hover_label, len(crew_data) + 8, crew_index + 1)

        self.last_hover_label = QLabel('', self)
        layout.addWidget(self.last_hover_label, len(crew_data) + 9, crew_index + 1)

    def toggle_assign(self, *args):
        self.assignment_changed.emit(*args)

    def clear_hover(self):
        self.clear_hover_signal.emit()
        
    def deassign_occured(self):
        self.only_last_label.setText('')
        
    def update(self, assigned_pref, implication, violation, implication_by_only_last, implication_reason_infos):
        assigned_pref_str = str(assigned_pref) if assigned_pref is not None else ''
        implication_str = str(implication) if implication is not None else ''
        implication_by_only_last_str = str(implication_by_only_last) if implication_by_only_last is not None else ''
    
        self.assigned_pref_label.setText(assigned_pref_str)
        self.implied_label.setText(implication_str)
        self.last_label.setText(implication_by_only_last_str)

        headers = ['Preference on junior', 'Junior', 'Junior key', 'Junior seniority', 'Seniority on junior']
        html = '<table>'
        html += '<tr>' + ''.join(['<th>%s</th>' % h for h in headers]) + '</tr>'
        for implication_reason_infos in sorted(implication_reason_infos, key=lambda x: x[3][1])[:10]:
            html += '<tr>'
            html += '<td>' + str(implication_reason_infos[3][1]) + '</td>'
            html += '<td>' + str(implication_reason_infos[4]) + '</td>'
            html += '<td>' + str(implication_reason_infos[5]) + '</td>'
            html += '<td>' + str(implication_reason_infos[6][0]) + '</td>'
            html += '<td>' + str(implication_reason_infos[3][0]) + '</td>'
            html += '</tr>'
            
        if len(implication_reason_infos) > 10:
            html += '<tr>'
            html += '<td>...</td>'
            html += '<td>...</td>'
            html += '<td>...</td>'
            html += '<td>...</td>'
            html += '<td>...</td>'
            html += '</tr>'
            
        html += '</table>'
        
        print(implication_reason_infos)

#        self.implied_label.setToolTip(str(implication_reason_infos))
        self.implied_label.setToolTip(html)

        color = 'red' if violation else 'green'
        self.violation_label.setStyleSheet('QLabel { background-color : %s; }' % color);
    
    def update_hover(self, assigned_pref, implication, violation, implication_by_only_last):
        assigned_pref_str = str(assigned_pref) if assigned_pref is not None else ''
        implication_str = str(implication) if implication is not None else ''
        implication_by_only_last_str = str(implication_by_only_last) if implication_by_only_last is not None else ''
    
        self.assigned_pref_hover_label.setText(assigned_pref_str)
        self.implied_hover_label.setText(implication_str)
        self.last_hover_label.setText(implication_by_only_last_str)
        
        color = 'red' if violation else 'green'
        self.violation_hover_label.setStyleSheet('QLabel { background-color : %s; }' % color);

    def do_clear_hover(self):
        self.update_hover(None, None, False, None)
        
    assignment_changed = pyqtSignal(int, int, bool)
    clear_hover_signal = pyqtSignal()

class MainWidget(QWidget):
    def __init__(self, data, parent):
        super().__init__(parent)
        self.data = data
        
        self.assignments = [None] * len(data.sen_prefs)
        
        layout = QGridLayout(self)
        layout.addWidget(QLabel('key/crew', self), 0, 0)
        
        for key_index, key_label in enumerate(data.key_labels):
            layout.addWidget(QLabel(key_label, self), key_index + 1, 0)
            
        self.crew_widgets = []
        for crew_index in range(len(data.crew_labels)):
            crew_widget = CrewColumnWidget(crew_index, 
                                           data.crew_labels[crew_index],
                                           data.sen_prefs[crew_index],
                                           layout,
                                           self)
            crew_widget.assignment_changed.connect(self.assignment_changed)
            crew_widget.clear_hover_signal.connect(self.clear_hover)
            self.crew_widgets.append(crew_widget)

        layout.addWidget(QLabel('Violation', self), len(data.key_labels) + 2, 0)
        layout.addWidget(QLabel('Assigned pref', self), len(data.key_labels) + 3, 0)
        layout.addWidget(QLabel('Implied by junior', self), len(data.key_labels) + 4, 0)
        layout.addWidget(QLabel('Implied pref by last assign', self), len(data.key_labels) + 5, 0)

        layout.addWidget(QLabel('Violation (hover)', self), len(data.key_labels) + 6, 0)
        layout.addWidget(QLabel('Assigned pref (hover)', self), len(data.key_labels) + 7, 0)
        layout.addWidget(QLabel('Implied by junior (hover)', self), len(data.key_labels) + 8, 0)
        layout.addWidget(QLabel('Implied pref by (hover)', self), len(data.key_labels) + 9, 0)
            
    def compute_data(self, crew_index, key_index, assigned, op_assignments):
        assigned_prefs = []
        implications = []
        implications_by_only_last = []
        violations = []
        implication_reason_infos = []
        for this_crew in range(len(self.data.sen_prefs)):
            assigned_key = op_assignments[this_crew]
            assigned_pref = self.data.sen_prefs[this_crew][assigned_key][1] if assigned_key is not None else None
            
            implication_by_only_last = None
            if assigned:
                other_crew_seniority = self.data.sen_prefs[crew_index][key_index][0]
                this_crew_seniority, this_crew_preference = self.data.sen_prefs[this_crew][key_index]
                if this_crew_seniority < other_crew_seniority:
                    implication_by_only_last = this_crew_preference
            
            implication = None
            implication_reason_info = []
            for other_crew in range(len(op_assignments)):
                if this_crew == other_crew:
                    continue
                
                assigned_key = op_assignments[other_crew]
                if assigned_key is None:
                    continue
                
                other_crew_seniority = self.data.sen_prefs[other_crew][assigned_key][0]
                this_crew_seniority, this_crew_preference = self.data.sen_prefs[this_crew][assigned_key]
                
                if this_crew_seniority > other_crew_seniority:
                    continue
                
                implication_reason_info.append((self.data.crew_labels[this_crew],
                                                self.data.key_labels[assigned_key],
                                                self.data.sen_prefs[this_crew][assigned_key],
                                                self.data.sen_prefs[this_crew][op_assignments[other_crew]],
                                                self.data.crew_labels[other_crew], 
                                                self.data.key_labels[op_assignments[other_crew]],
                                                self.data.sen_prefs[other_crew][op_assignments[other_crew]]))
                
                if implication is None:
                    implication = this_crew_preference
                else:
                    implication = min(implication, this_crew_preference)
            
            violation = assigned_pref > implication if assigned_pref is not None and implication is not None else False
            
            implications.append(implication)
            implications_by_only_last.append(implication_by_only_last)
            assigned_prefs.append(assigned_pref)
            violations.append(violation)
            implication_reason_infos.append(implication_reason_info)
        
        print(op_assignments)
        print(implications)

        return (assigned_prefs,
                implications,
                implications_by_only_last,
                violations,
                implication_reason_infos)
        
    
    def assignment_changed(self, crew_index, key_index, dry_run):
        
        op_assignments = self.assignments[:] if dry_run else self.assignments
        
        print(crew_index, key_index, dry_run)
        if op_assignments[crew_index]:
            if key_index == op_assignments[crew_index]:
                assigned = False
                op_assignments[crew_index] = None
            else:
                assigned = True
                op_assignments[crew_index] = key_index
        else:
            assigned = True
            op_assignments[crew_index] = key_index
        
        (assigned_prefs,
                implications,
                implications_by_only_last,
                violations,
                implication_reason_infos) = self.compute_data(crew_index, key_index, assigned, op_assignments)

        print(implication_reason_infos)

        if dry_run:
            for crew_index, crew_widget in enumerate(self.crew_widgets):
                crew_widget.update_hover(assigned_prefs[crew_index],
                                         implications[crew_index],
                                         violations[crew_index],
                                         implications_by_only_last[crew_index])
        else:
            for crew_index, crew_widget in enumerate(self.crew_widgets):
                crew_widget.update(assigned_prefs[crew_index],
                                   implications[crew_index],
                                   violations[crew_index],
                                   implications_by_only_last[crew_index],
                                   implication_reason_infos[crew_index])
                
    def clear_hover(self):
        for crew_widget in self.crew_widgets:
            crew_widget.do_clear_hover()
    
def do_main():
    data = get_data_2()
    
    app = QApplication([])
    #window = QMainWindow()
    main_widget = MainWidget(data, None)
#    label = QLabel('asdf', window)
    main_widget.show()
    app.exec()
    
    
if __name__ == '__main__':
    do_main()