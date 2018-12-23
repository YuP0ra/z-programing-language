
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftMULTIPLYDIVIDEASSIGN DIVIDE ID LPAREN MINUS MOD MULTIPLY NEWLINE NUM PLUS RPAREN R_DEF\n    sourcecode  : NEWLINE\n                | varcall\n                | assignment\n                |\n    \n    assignment  : ID ASSIGN expression\n    \n    varcall     : ID\n    \n    expression  : LPAREN        expression  RPAREN\n                | expression    MOD         expression\n                | expression    PLUS        expression\n                | expression    MINUS       expression\n                | expression    DIVIDE      expression\n                | expression    MULTIPLY    expression\n                | NUM\n                | ID\n    '
    
_lr_action_items = {'NEWLINE':([0,],[2,]),'$end':([0,1,2,3,4,5,7,8,10,17,18,19,20,21,22,],[-4,0,-1,-2,-3,-6,-14,-5,-13,-8,-9,-10,-11,-12,-7,]),'ID':([0,6,9,11,12,13,14,15,],[5,7,7,7,7,7,7,7,]),'ASSIGN':([5,],[6,]),'LPAREN':([6,9,11,12,13,14,15,],[9,9,9,9,9,9,9,]),'NUM':([6,9,11,12,13,14,15,],[10,10,10,10,10,10,10,]),'MOD':([7,8,10,16,17,18,19,20,21,22,],[-14,11,-13,11,11,-9,-10,-11,-12,-7,]),'PLUS':([7,8,10,16,17,18,19,20,21,22,],[-14,12,-13,12,12,-9,-10,-11,-12,-7,]),'MINUS':([7,8,10,16,17,18,19,20,21,22,],[-14,13,-13,13,13,-9,-10,-11,-12,-7,]),'DIVIDE':([7,8,10,16,17,18,19,20,21,22,],[-14,14,-13,14,14,14,14,-11,-12,-7,]),'MULTIPLY':([7,8,10,16,17,18,19,20,21,22,],[-14,15,-13,15,15,15,15,-11,-12,-7,]),'RPAREN':([7,10,16,17,18,19,20,21,22,],[-14,-13,22,-8,-9,-10,-11,-12,-7,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'sourcecode':([0,],[1,]),'varcall':([0,],[3,]),'assignment':([0,],[4,]),'expression':([6,9,11,12,13,14,15,],[8,16,17,18,19,20,21,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> sourcecode","S'",1,None,None,None),
  ('sourcecode -> NEWLINE','sourcecode',1,'p_0','calc_comppiler.py',62),
  ('sourcecode -> varcall','sourcecode',1,'p_0','calc_comppiler.py',63),
  ('sourcecode -> assignment','sourcecode',1,'p_0','calc_comppiler.py',64),
  ('sourcecode -> <empty>','sourcecode',0,'p_0','calc_comppiler.py',65),
  ('assignment -> ID ASSIGN expression','assignment',3,'p_1','calc_comppiler.py',70),
  ('varcall -> ID','varcall',1,'p_2','calc_comppiler.py',80),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_3','calc_comppiler.py',90),
  ('expression -> expression MOD expression','expression',3,'p_3','calc_comppiler.py',91),
  ('expression -> expression PLUS expression','expression',3,'p_3','calc_comppiler.py',92),
  ('expression -> expression MINUS expression','expression',3,'p_3','calc_comppiler.py',93),
  ('expression -> expression DIVIDE expression','expression',3,'p_3','calc_comppiler.py',94),
  ('expression -> expression MULTIPLY expression','expression',3,'p_3','calc_comppiler.py',95),
  ('expression -> NUM','expression',1,'p_3','calc_comppiler.py',96),
  ('expression -> ID','expression',1,'p_3','calc_comppiler.py',97),
]