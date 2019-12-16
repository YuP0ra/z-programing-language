
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftMULTIPLYDIVIDEASSIGN BOOL BOOL COLON COMMA DIVIDE EQUAL FLOAT ID INTEGER LPAREN MINUS MOD MULTIPLY NEWLINE NOTEQUAL PLUS RPAREN R_AND R_DEF R_FOR R_IF R_NOT R_OR R_RETURN R_WHILE STRING\n    program     : sourcecode program\n                |\n\n    sourcecode  : NEWLINE\n                | assignment\n                | declaration\n                | methodcall\n                | returnfunc\n                | decision\n                | loop\n\n\n    assignment  : ID ASSIGN idexpr\n                | ID\n\n    idexpr      : value  mathopt  idexpr\n                | value\n\n    value       : ID\n                | BOOL\n                | STRING\n                | expression\n                | methodcall\n\n\n\n    declaration : R_DEF  ID  LPAREN  args  RPAREN  COLON\n\n    args        : ID  COMMA  args\n                | ID\n                |\n\n\n\n    methodcall  : ID  LPAREN  callargs  RPAREN\n\n    callargs    : value  COMMA  callargs\n                | value\n                |\n\n\n    returnfunc  : R_RETURN\n                | R_RETURN value\n\n\n\n    expression  : LPAREN  expression  RPAREN\n                | num  mathopt  expression\n                | num\n\n    num         : INTEGER\n                | FLOAT\n\n    mathopt     : PLUS\n                | MINUS\n                | MULTIPLY\n                | DIVIDE\n                | MOD\n\n\n\n    decision    : R_IF  condition  COLON\n\n    loop        : R_WHILE  condition  COLON\n\n    condition   : BOOL\n                | ID  condopt  value\n                | LPAREN  condition  RPAREN\n                | condition  condexpend  condition\n\n    condopt     : EQUAL\n                | NOTEQUAL\n\n    condexpend  : R_AND\n                | R_NOT\n                | R_OR\n    '
    
_lr_action_items = {'$end':([0,1,2,3,4,5,6,7,8,9,10,12,15,19,20,21,22,23,24,26,27,28,34,35,46,55,57,61,62,66,71,],[-2,0,-2,-3,-4,-5,-6,-7,-8,-9,-11,-27,-1,-28,-14,-15,-16,-17,-18,-31,-32,-33,-10,-13,-39,-40,-23,-29,-30,-12,-19,]),'NEWLINE':([0,2,3,4,5,6,7,8,9,10,12,19,20,21,22,23,24,26,27,28,34,35,46,55,57,61,62,66,71,],[3,3,-3,-4,-5,-6,-7,-8,-9,-11,-27,-28,-14,-15,-16,-17,-18,-31,-32,-33,-10,-13,-39,-40,-23,-29,-30,-12,-19,]),'ID':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,19,20,21,22,23,24,26,27,28,32,34,35,38,41,42,43,44,45,46,47,48,49,50,51,52,53,55,56,57,58,61,62,66,68,71,],[10,10,-3,-4,-5,-6,-7,-8,-9,-11,18,20,31,31,20,20,-28,-14,-15,-16,-17,-18,-31,-32,-33,31,-10,-13,59,-34,-35,-36,-37,-38,-39,31,-47,-48,-49,20,-45,-46,-40,20,-23,20,-29,-30,-12,59,-19,]),'R_DEF':([0,2,3,4,5,6,7,8,9,10,12,19,20,21,22,23,24,26,27,28,34,35,46,55,57,61,62,66,71,],[11,11,-3,-4,-5,-6,-7,-8,-9,-11,-27,-28,-14,-15,-16,-17,-18,-31,-32,-33,-10,-13,-39,-40,-23,-29,-30,-12,-19,]),'R_RETURN':([0,2,3,4,5,6,7,8,9,10,12,19,20,21,22,23,24,26,27,28,34,35,46,55,57,61,62,66,71,],[12,12,-3,-4,-5,-6,-7,-8,-9,-11,-27,-28,-14,-15,-16,-17,-18,-31,-32,-33,-10,-13,-39,-40,-23,-29,-30,-12,-19,]),'R_IF':([0,2,3,4,5,6,7,8,9,10,12,19,20,21,22,23,24,26,27,28,34,35,46,55,57,61,62,66,71,],[13,13,-3,-4,-5,-6,-7,-8,-9,-11,-27,-28,-14,-15,-16,-17,-18,-31,-32,-33,-10,-13,-39,-40,-23,-29,-30,-12,-19,]),'R_WHILE':([0,2,3,4,5,6,7,8,9,10,12,19,20,21,22,23,24,26,27,28,34,35,46,55,57,61,62,66,71,],[14,14,-3,-4,-5,-6,-7,-8,-9,-11,-27,-28,-14,-15,-16,-17,-18,-31,-32,-33,-10,-13,-39,-40,-23,-29,-30,-12,-19,]),'ASSIGN':([10,],[16,]),'LPAREN':([10,12,13,14,16,17,18,20,25,32,40,41,42,43,44,45,47,48,49,50,51,52,53,56,58,],[17,25,32,32,25,25,38,17,25,32,25,-34,-35,-36,-37,-38,32,-47,-48,-49,25,-45,-46,25,25,]),'BOOL':([12,13,14,16,17,32,41,42,43,44,45,47,48,49,50,51,52,53,56,58,],[21,30,30,21,21,30,-34,-35,-36,-37,-38,30,-47,-48,-49,21,-45,-46,21,21,]),'STRING':([12,16,17,41,42,43,44,45,51,52,53,56,58,],[22,22,22,-34,-35,-36,-37,-38,22,-45,-46,22,22,]),'INTEGER':([12,16,17,25,40,41,42,43,44,45,51,52,53,56,58,],[27,27,27,27,27,-34,-35,-36,-37,-38,27,-45,-46,27,27,]),'FLOAT':([12,16,17,25,40,41,42,43,44,45,51,52,53,56,58,],[28,28,28,28,28,-34,-35,-36,-37,-38,28,-45,-46,28,28,]),'RPAREN':([17,20,21,22,23,24,26,27,28,30,36,37,38,39,54,57,58,59,60,61,62,63,64,65,67,68,70,],[-26,-14,-15,-16,-17,-18,-31,-32,-33,-41,57,-25,-22,61,65,-23,-26,-21,69,-29,-30,-44,-42,-43,-24,-22,-20,]),'PLUS':([20,21,22,23,24,26,27,28,35,57,61,62,],[-14,-15,-16,-17,-18,41,-32,-33,41,-23,-29,-30,]),'MINUS':([20,21,22,23,24,26,27,28,35,57,61,62,],[-14,-15,-16,-17,-18,42,-32,-33,42,-23,-29,-30,]),'MULTIPLY':([20,21,22,23,24,26,27,28,35,57,61,62,],[-14,-15,-16,-17,-18,43,-32,-33,43,-23,-29,-30,]),'DIVIDE':([20,21,22,23,24,26,27,28,35,57,61,62,],[-14,-15,-16,-17,-18,44,-32,-33,44,-23,-29,-30,]),'MOD':([20,21,22,23,24,26,27,28,35,57,61,62,],[-14,-15,-16,-17,-18,45,-32,-33,45,-23,-29,-30,]),'COMMA':([20,21,22,23,24,26,27,28,37,57,59,61,62,],[-14,-15,-16,-17,-18,-31,-32,-33,58,-23,68,-29,-30,]),'COLON':([20,21,22,23,24,26,27,28,29,30,33,57,61,62,63,64,65,69,],[-14,-15,-16,-17,-18,-31,-32,-33,46,-41,55,-23,-29,-30,-44,-42,-43,71,]),'R_AND':([20,21,22,23,24,26,27,28,29,30,33,54,57,61,62,63,64,65,],[-14,-15,-16,-17,-18,-31,-32,-33,48,-41,48,48,-23,-29,-30,48,-42,-43,]),'R_NOT':([20,21,22,23,24,26,27,28,29,30,33,54,57,61,62,63,64,65,],[-14,-15,-16,-17,-18,-31,-32,-33,49,-41,49,49,-23,-29,-30,49,-42,-43,]),'R_OR':([20,21,22,23,24,26,27,28,29,30,33,54,57,61,62,63,64,65,],[-14,-15,-16,-17,-18,-31,-32,-33,50,-41,50,50,-23,-29,-30,50,-42,-43,]),'EQUAL':([31,],[52,]),'NOTEQUAL':([31,],[53,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,2,],[1,15,]),'sourcecode':([0,2,],[2,2,]),'assignment':([0,2,],[4,4,]),'declaration':([0,2,],[5,5,]),'methodcall':([0,2,12,16,17,51,56,58,],[6,6,24,24,24,24,24,24,]),'returnfunc':([0,2,],[7,7,]),'decision':([0,2,],[8,8,]),'loop':([0,2,],[9,9,]),'value':([12,16,17,51,56,58,],[19,35,37,64,35,37,]),'expression':([12,16,17,25,40,51,56,58,],[23,23,23,39,62,23,23,23,]),'num':([12,16,17,25,40,51,56,58,],[26,26,26,26,26,26,26,26,]),'condition':([13,14,32,47,],[29,33,54,63,]),'idexpr':([16,56,],[34,66,]),'callargs':([17,58,],[36,67,]),'mathopt':([26,35,],[40,56,]),'condexpend':([29,33,54,63,],[47,47,47,47,]),'condopt':([31,],[51,]),'args':([38,68,],[60,70,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> sourcecode program','program',2,'p_z','compiler.py',80),
  ('program -> <empty>','program',0,'p_z','compiler.py',81),
  ('sourcecode -> NEWLINE','sourcecode',1,'p_z','compiler.py',83),
  ('sourcecode -> assignment','sourcecode',1,'p_z','compiler.py',84),
  ('sourcecode -> declaration','sourcecode',1,'p_z','compiler.py',85),
  ('sourcecode -> methodcall','sourcecode',1,'p_z','compiler.py',86),
  ('sourcecode -> returnfunc','sourcecode',1,'p_z','compiler.py',87),
  ('sourcecode -> decision','sourcecode',1,'p_z','compiler.py',88),
  ('sourcecode -> loop','sourcecode',1,'p_z','compiler.py',89),
  ('assignment -> ID ASSIGN idexpr','assignment',3,'p_z','compiler.py',92),
  ('assignment -> ID','assignment',1,'p_z','compiler.py',93),
  ('idexpr -> value mathopt idexpr','idexpr',3,'p_z','compiler.py',95),
  ('idexpr -> value','idexpr',1,'p_z','compiler.py',96),
  ('value -> ID','value',1,'p_z','compiler.py',98),
  ('value -> BOOL','value',1,'p_z','compiler.py',99),
  ('value -> STRING','value',1,'p_z','compiler.py',100),
  ('value -> expression','value',1,'p_z','compiler.py',101),
  ('value -> methodcall','value',1,'p_z','compiler.py',102),
  ('declaration -> R_DEF ID LPAREN args RPAREN COLON','declaration',6,'p_z','compiler.py',106),
  ('args -> ID COMMA args','args',3,'p_z','compiler.py',108),
  ('args -> ID','args',1,'p_z','compiler.py',109),
  ('args -> <empty>','args',0,'p_z','compiler.py',110),
  ('methodcall -> ID LPAREN callargs RPAREN','methodcall',4,'p_z','compiler.py',114),
  ('callargs -> value COMMA callargs','callargs',3,'p_z','compiler.py',116),
  ('callargs -> value','callargs',1,'p_z','compiler.py',117),
  ('callargs -> <empty>','callargs',0,'p_z','compiler.py',118),
  ('returnfunc -> R_RETURN','returnfunc',1,'p_z','compiler.py',121),
  ('returnfunc -> R_RETURN value','returnfunc',2,'p_z','compiler.py',122),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_z','compiler.py',126),
  ('expression -> num mathopt expression','expression',3,'p_z','compiler.py',127),
  ('expression -> num','expression',1,'p_z','compiler.py',128),
  ('num -> INTEGER','num',1,'p_z','compiler.py',130),
  ('num -> FLOAT','num',1,'p_z','compiler.py',131),
  ('mathopt -> PLUS','mathopt',1,'p_z','compiler.py',133),
  ('mathopt -> MINUS','mathopt',1,'p_z','compiler.py',134),
  ('mathopt -> MULTIPLY','mathopt',1,'p_z','compiler.py',135),
  ('mathopt -> DIVIDE','mathopt',1,'p_z','compiler.py',136),
  ('mathopt -> MOD','mathopt',1,'p_z','compiler.py',137),
  ('decision -> R_IF condition COLON','decision',3,'p_z','compiler.py',141),
  ('loop -> R_WHILE condition COLON','loop',3,'p_z','compiler.py',143),
  ('condition -> BOOL','condition',1,'p_z','compiler.py',145),
  ('condition -> ID condopt value','condition',3,'p_z','compiler.py',146),
  ('condition -> LPAREN condition RPAREN','condition',3,'p_z','compiler.py',147),
  ('condition -> condition condexpend condition','condition',3,'p_z','compiler.py',148),
  ('condopt -> EQUAL','condopt',1,'p_z','compiler.py',150),
  ('condopt -> NOTEQUAL','condopt',1,'p_z','compiler.py',151),
  ('condexpend -> R_AND','condexpend',1,'p_z','compiler.py',153),
  ('condexpend -> R_NOT','condexpend',1,'p_z','compiler.py',154),
  ('condexpend -> R_OR','condexpend',1,'p_z','compiler.py',155),
]
