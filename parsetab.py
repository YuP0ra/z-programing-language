
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftMULTIPLYDIVIDEASSIGN BOOL BOOL COLON COMMA DIVIDE EQUAL FLOAT ID INTEGER LPAREN MINUS MOD MULTIPLY NEWLINE NOTEQUAL PLUS RPAREN R_AND R_DEF R_FOR R_IF R_NOT R_OR R_RETURN R_WHILE STRING\n    parsetree   : program\n    \n    program     : line program\n                |\n    \n    line        : NEWLINE\n                | assignment\n                | declaration\n                | methodcall\n                | returnfunc\n                | decision\n                | loop\n    \n    assignment  : ID ASSIGN idexpr\n                | ID\n    \n    idexpr      : value  mathopt  idexpr\n                | value\n    \n    value       : ID\n                | BOOL\n                | STRING\n                | expression\n                | methodcall\n    \n    declaration : R_DEF  ID  LPAREN  args  RPAREN  COLON  LPAREN  program  RPAREN\n    \n    args        : args  COMMA  args\n                | ID\n                |\n    \n    methodcall  : ID  LPAREN  callargs  RPAREN\n    \n    callargs    : callargs  COMMA  callargs\n                | value\n                |\n    \n    returnfunc  : R_RETURN\n                | R_RETURN value\n    \n    expression  : LPAREN  expression  RPAREN\n                | num  mathopt  expression\n                | num\n    \n    num         : INTEGER\n                | FLOAT\n    \n    mathopt     : PLUS\n                | MINUS\n                | MULTIPLY\n                | DIVIDE\n                | MOD\n    \n    decision    : R_IF  condition  COLON  LPAREN  program  RPAREN\n    \n    loop        : R_WHILE  condition  COLON  LPAREN  program  RPAREN\n    \n    condition   : BOOL\n                | ID  condopt  value\n                | LPAREN  condition  RPAREN\n                | condition  condexpend  condition\n    \n    condopt     : EQUAL\n                | NOTEQUAL\n    \n    condexpend  : R_AND\n                | R_NOT\n                | R_OR\n    '
    
_lr_action_items = {'$end':([0,1,2,3,4,5,6,7,8,9,10,11,13,16,20,21,22,23,24,25,27,28,29,35,36,58,62,63,69,77,78,81,],[-3,0,-1,-3,-4,-5,-6,-7,-8,-9,-10,-12,-28,-2,-29,-15,-16,-17,-18,-19,-32,-33,-34,-11,-14,-24,-30,-31,-13,-40,-41,-20,]),'NEWLINE':([0,3,4,5,6,7,8,9,10,11,13,20,21,22,23,24,25,27,28,29,35,36,58,62,63,64,68,69,77,78,79,81,],[4,4,-4,-5,-6,-7,-8,-9,-10,-12,-28,-29,-15,-16,-17,-18,-19,-32,-33,-34,-11,-14,-24,-30,-31,4,4,-13,-40,-41,4,-20,]),'ID':([0,3,4,5,6,7,8,9,10,11,12,13,14,15,17,18,20,21,22,23,24,25,27,28,29,31,35,36,39,42,43,44,45,46,48,49,50,51,53,54,55,57,58,59,62,63,64,68,69,72,77,78,79,81,],[11,11,-4,-5,-6,-7,-8,-9,-10,-12,19,21,33,33,21,21,-29,-15,-16,-17,-18,-19,-32,-33,-34,33,-11,-14,60,-35,-36,-37,-38,-39,33,-48,-49,-50,21,-46,-47,21,-24,21,-30,-31,11,11,-13,60,-40,-41,11,-20,]),'R_DEF':([0,3,4,5,6,7,8,9,10,11,13,20,21,22,23,24,25,27,28,29,35,36,58,62,63,64,68,69,77,78,79,81,],[12,12,-4,-5,-6,-7,-8,-9,-10,-12,-28,-29,-15,-16,-17,-18,-19,-32,-33,-34,-11,-14,-24,-30,-31,12,12,-13,-40,-41,12,-20,]),'R_RETURN':([0,3,4,5,6,7,8,9,10,11,13,20,21,22,23,24,25,27,28,29,35,36,58,62,63,64,68,69,77,78,79,81,],[13,13,-4,-5,-6,-7,-8,-9,-10,-12,-28,-29,-15,-16,-17,-18,-19,-32,-33,-34,-11,-14,-24,-30,-31,13,13,-13,-40,-41,13,-20,]),'R_IF':([0,3,4,5,6,7,8,9,10,11,13,20,21,22,23,24,25,27,28,29,35,36,58,62,63,64,68,69,77,78,79,81,],[14,14,-4,-5,-6,-7,-8,-9,-10,-12,-28,-29,-15,-16,-17,-18,-19,-32,-33,-34,-11,-14,-24,-30,-31,14,14,-13,-40,-41,14,-20,]),'R_WHILE':([0,3,4,5,6,7,8,9,10,11,13,20,21,22,23,24,25,27,28,29,35,36,58,62,63,64,68,69,77,78,79,81,],[15,15,-4,-5,-6,-7,-8,-9,-10,-12,-28,-29,-15,-16,-17,-18,-19,-32,-33,-34,-11,-14,-24,-30,-31,15,15,-13,-40,-41,15,-20,]),'RPAREN':([3,4,5,6,7,8,9,10,11,13,16,18,20,21,22,23,24,25,27,28,29,32,35,36,37,38,39,40,52,58,59,60,61,62,63,64,65,66,67,68,69,70,72,73,74,76,77,78,79,80,81,],[-3,-4,-5,-6,-7,-8,-9,-10,-12,-28,-2,-27,-29,-15,-16,-17,-18,-19,-32,-33,-34,-42,-11,-14,58,-26,-23,62,66,-24,-27,-22,71,-30,-31,-3,-45,-44,-43,-3,-13,-25,-23,77,78,-21,-40,-41,-3,81,-20,]),'ASSIGN':([11,],[17,]),'LPAREN':([11,13,14,15,17,18,19,21,26,31,41,42,43,44,45,46,47,48,49,50,51,53,54,55,56,57,59,75,],[18,26,31,31,26,26,39,18,26,31,26,-35,-36,-37,-38,-39,64,31,-48,-49,-50,26,-46,-47,68,26,26,79,]),'BOOL':([13,14,15,17,18,31,42,43,44,45,46,48,49,50,51,53,54,55,57,59,],[22,32,32,22,22,32,-35,-36,-37,-38,-39,32,-48,-49,-50,22,-46,-47,22,22,]),'STRING':([13,17,18,42,43,44,45,46,53,54,55,57,59,],[23,23,23,-35,-36,-37,-38,-39,23,-46,-47,23,23,]),'INTEGER':([13,17,18,26,41,42,43,44,45,46,53,54,55,57,59,],[28,28,28,28,28,-35,-36,-37,-38,-39,28,-46,-47,28,28,]),'FLOAT':([13,17,18,26,41,42,43,44,45,46,53,54,55,57,59,],[29,29,29,29,29,-35,-36,-37,-38,-39,29,-46,-47,29,29,]),'COMMA':([18,21,22,23,24,25,27,28,29,37,38,39,58,59,60,61,62,63,70,72,76,],[-27,-15,-16,-17,-18,-19,-32,-33,-34,59,-26,-23,-24,-27,-22,72,-30,-31,59,-23,72,]),'PLUS':([21,22,23,24,25,27,28,29,36,58,62,63,],[-15,-16,-17,-18,-19,42,-33,-34,42,-24,-30,-31,]),'MINUS':([21,22,23,24,25,27,28,29,36,58,62,63,],[-15,-16,-17,-18,-19,43,-33,-34,43,-24,-30,-31,]),'MULTIPLY':([21,22,23,24,25,27,28,29,36,58,62,63,],[-15,-16,-17,-18,-19,44,-33,-34,44,-24,-30,-31,]),'DIVIDE':([21,22,23,24,25,27,28,29,36,58,62,63,],[-15,-16,-17,-18,-19,45,-33,-34,45,-24,-30,-31,]),'MOD':([21,22,23,24,25,27,28,29,36,58,62,63,],[-15,-16,-17,-18,-19,46,-33,-34,46,-24,-30,-31,]),'COLON':([21,22,23,24,25,27,28,29,30,32,34,58,62,63,65,66,67,71,],[-15,-16,-17,-18,-19,-32,-33,-34,47,-42,56,-24,-30,-31,-45,-44,-43,75,]),'R_AND':([21,22,23,24,25,27,28,29,30,32,34,52,58,62,63,65,66,67,],[-15,-16,-17,-18,-19,-32,-33,-34,49,-42,49,49,-24,-30,-31,49,-44,-43,]),'R_NOT':([21,22,23,24,25,27,28,29,30,32,34,52,58,62,63,65,66,67,],[-15,-16,-17,-18,-19,-32,-33,-34,50,-42,50,50,-24,-30,-31,50,-44,-43,]),'R_OR':([21,22,23,24,25,27,28,29,30,32,34,52,58,62,63,65,66,67,],[-15,-16,-17,-18,-19,-32,-33,-34,51,-42,51,51,-24,-30,-31,51,-44,-43,]),'EQUAL':([33,],[54,]),'NOTEQUAL':([33,],[55,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'parsetree':([0,],[1,]),'program':([0,3,64,68,79,],[2,16,73,74,80,]),'line':([0,3,64,68,79,],[3,3,3,3,3,]),'assignment':([0,3,64,68,79,],[5,5,5,5,5,]),'declaration':([0,3,64,68,79,],[6,6,6,6,6,]),'methodcall':([0,3,13,17,18,53,57,59,64,68,79,],[7,7,25,25,25,25,25,25,7,7,7,]),'returnfunc':([0,3,64,68,79,],[8,8,8,8,8,]),'decision':([0,3,64,68,79,],[9,9,9,9,9,]),'loop':([0,3,64,68,79,],[10,10,10,10,10,]),'value':([13,17,18,53,57,59,],[20,36,38,67,36,38,]),'expression':([13,17,18,26,41,53,57,59,],[24,24,24,40,63,24,24,24,]),'num':([13,17,18,26,41,53,57,59,],[27,27,27,27,27,27,27,27,]),'condition':([14,15,31,48,],[30,34,52,65,]),'idexpr':([17,57,],[35,69,]),'callargs':([18,59,],[37,70,]),'mathopt':([27,36,],[41,57,]),'condexpend':([30,34,52,65,],[48,48,48,48,]),'condopt':([33,],[53,]),'args':([39,72,],[61,76,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> parsetree","S'",1,None,None,None),
  ('parsetree -> program','parsetree',1,'p_main','compiler with parse tree.py',79),
  ('program -> line program','program',2,'p_0','compiler with parse tree.py',86),
  ('program -> <empty>','program',0,'p_0','compiler with parse tree.py',87),
  ('line -> NEWLINE','line',1,'p_00','compiler with parse tree.py',100),
  ('line -> assignment','line',1,'p_00','compiler with parse tree.py',101),
  ('line -> declaration','line',1,'p_00','compiler with parse tree.py',102),
  ('line -> methodcall','line',1,'p_00','compiler with parse tree.py',103),
  ('line -> returnfunc','line',1,'p_00','compiler with parse tree.py',104),
  ('line -> decision','line',1,'p_00','compiler with parse tree.py',105),
  ('line -> loop','line',1,'p_00','compiler with parse tree.py',106),
  ('assignment -> ID ASSIGN idexpr','assignment',3,'p_01','compiler with parse tree.py',113),
  ('assignment -> ID','assignment',1,'p_01','compiler with parse tree.py',114),
  ('idexpr -> value mathopt idexpr','idexpr',3,'p_02','compiler with parse tree.py',124),
  ('idexpr -> value','idexpr',1,'p_02','compiler with parse tree.py',125),
  ('value -> ID','value',1,'p_03','compiler with parse tree.py',135),
  ('value -> BOOL','value',1,'p_03','compiler with parse tree.py',136),
  ('value -> STRING','value',1,'p_03','compiler with parse tree.py',137),
  ('value -> expression','value',1,'p_03','compiler with parse tree.py',138),
  ('value -> methodcall','value',1,'p_03','compiler with parse tree.py',139),
  ('declaration -> R_DEF ID LPAREN args RPAREN COLON LPAREN program RPAREN','declaration',9,'p_04','compiler with parse tree.py',146),
  ('args -> args COMMA args','args',3,'p_05','compiler with parse tree.py',153),
  ('args -> ID','args',1,'p_05','compiler with parse tree.py',154),
  ('args -> <empty>','args',0,'p_05','compiler with parse tree.py',155),
  ('methodcall -> ID LPAREN callargs RPAREN','methodcall',4,'p_06','compiler with parse tree.py',168),
  ('callargs -> callargs COMMA callargs','callargs',3,'p_07','compiler with parse tree.py',175),
  ('callargs -> value','callargs',1,'p_07','compiler with parse tree.py',176),
  ('callargs -> <empty>','callargs',0,'p_07','compiler with parse tree.py',177),
  ('returnfunc -> R_RETURN','returnfunc',1,'p_08','compiler with parse tree.py',191),
  ('returnfunc -> R_RETURN value','returnfunc',2,'p_08','compiler with parse tree.py',192),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_09','compiler with parse tree.py',200),
  ('expression -> num mathopt expression','expression',3,'p_09','compiler with parse tree.py',201),
  ('expression -> num','expression',1,'p_09','compiler with parse tree.py',202),
  ('num -> INTEGER','num',1,'p_10','compiler with parse tree.py',215),
  ('num -> FLOAT','num',1,'p_10','compiler with parse tree.py',216),
  ('mathopt -> PLUS','mathopt',1,'p_11','compiler with parse tree.py',223),
  ('mathopt -> MINUS','mathopt',1,'p_11','compiler with parse tree.py',224),
  ('mathopt -> MULTIPLY','mathopt',1,'p_11','compiler with parse tree.py',225),
  ('mathopt -> DIVIDE','mathopt',1,'p_11','compiler with parse tree.py',226),
  ('mathopt -> MOD','mathopt',1,'p_11','compiler with parse tree.py',227),
  ('decision -> R_IF condition COLON LPAREN program RPAREN','decision',6,'p_12','compiler with parse tree.py',234),
  ('loop -> R_WHILE condition COLON LPAREN program RPAREN','loop',6,'p_13','compiler with parse tree.py',240),
  ('condition -> BOOL','condition',1,'p_14','compiler with parse tree.py',246),
  ('condition -> ID condopt value','condition',3,'p_14','compiler with parse tree.py',247),
  ('condition -> LPAREN condition RPAREN','condition',3,'p_14','compiler with parse tree.py',248),
  ('condition -> condition condexpend condition','condition',3,'p_14','compiler with parse tree.py',249),
  ('condopt -> EQUAL','condopt',1,'p_15','compiler with parse tree.py',262),
  ('condopt -> NOTEQUAL','condopt',1,'p_15','compiler with parse tree.py',263),
  ('condexpend -> R_AND','condexpend',1,'p_16','compiler with parse tree.py',270),
  ('condexpend -> R_NOT','condexpend',1,'p_16','compiler with parse tree.py',271),
  ('condexpend -> R_OR','condexpend',1,'p_16','compiler with parse tree.py',272),
]
