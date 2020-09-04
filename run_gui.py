#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 19:02:47 2020

@author: abdullah
"""

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from ui_The_concordancer_gui import Ui_Form 
from Code import *
import time


class Mywidget(QWidget, Ui_Form):
    
    def __init__(self):
        start_time = time.time()
        QWidget.__init__(self)
        self.setupUi(self)
        print ("-- paesing documents--")
        build_all_docs_list("resources")
        print("--Extracting words--")
        self.word_occurances = extract_words()
        print("--opining window--")
        print("--- %s seconds ---" % (time.time() - start_time))
        self.bt_search.clicked.connect(self.search_for_word)
        self.bt_save.clicked.connect(self.save_search_result)
        self.bt_language.clicked.connect(self.change_langauge)
        self.lb_root.setAlignment(Qt.AlignLeft)
        
    def search_for_word(self):
        word = self.le_search.text() 
        result_list = find_part_of_sentence(word)
        
        self.tb_result.setRowCount(0)
        
        for i, result in enumerate(result_list):
            self.tb_result.insertRow(i)
            spcial_cell = QTextBrowser();
            spcial_cell.insertHtml(result[1].replace(word, f"<span style='color:green;'>{word}</span>"))
                
            self.tb_result.setItem(i, 0, QTableWidgetItem(result[0]))
            self.tb_result.setCellWidget(i, 1, spcial_cell)
            
        self.display_Divered(word)
        
    def display_Divered(self, word):
        root, *others_forms = print_other_forms(word)
        self.lw_result.clear()
        self.lw_result.addItems(others_forms)
        self.lb_root.setText(root)
        to_langauge = self.bt_language.text()
        
        if to_langauge != "English":
            self.lb_root.setAlignment(Qt.AlignLeft)
        else:
            
            self.lb_root.setAlignment(Qt.AlignRight)
            
    def save_search_result(self):
        
        
        info = QFileDialog().getSaveFileName(filter = "json file (*.json)")
        
        if info[0] != "":
            result_list = []
            row_count = self.tb_result.rowCount()
            
            for i in range (row_count):
                result_list.append({
                    "domain" : self.tb_result.item(i, 0).text(),
                    "The The concordances" : self.tb_result.item(i, 1).text(),
                    })
                
            with open(info [0], "w", encoding='utf8') as file:
                json.dump(result_list, file, ensure_ascii=False)
                                     
                                             
        print (info)
        
    def change_langauge(self):
        to_langauge = self.bt_language.text()
        
        if to_langauge != "English":
            self.bt_language.setText("English")
            self.bt_search.setText("ابحث")
            self.bt_save.setText("إحفظ النتيجة")
            self.lb_title.setText("أداة التوافق")
            self.lb_word.setText("مشتقات من الكلمة")
            self.lb_root_1.setText("الجذر هو :")
            self.lb_root.setAlignment(Qt.AlignLeft)
            self.tb_result.horizontalHeaderItem(0).setText("المجال")
            self.tb_result.horizontalHeaderItem(1).setText("التوافق")
        else:
            self.bt_language.setText("اللغة العربية")
            self.bt_search.setText("Search")
            self.bt_save.setText("Save the result")
            self.lb_title.setText("The concordancer")
            self.lb_word.setText("Derived words")
            self.lb_root_1.setText("The root")
            self.lb_root.setAlignment(Qt.AlignRight)
            self.tb_result.horizontalHeaderItem(0).setText("The domain")
            self.tb_result.horizontalHeaderItem(1).setText("The concordances")
            
       

        
 
app = QApplication([])
window = Mywidget()
window.show()
app.exec()
