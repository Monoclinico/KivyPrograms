#!/urb/bin/env python
# _*_ coding: utf-8 _*_

import kivy
kivy.require('1.9.1')
from kivy.config import Config
Config.set('graphics','multisamples','0')
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
def num_exten(n):
  """Retorna uma string do número (n) por extenso. (n) deve ser estar entre 0 e 999999999999999999.\n
  Returns a string of the name of the number (n). (n) must be between 0 and 999999999999999999."""
  u = {'1':'um','2':'dois','3':'três','4':'quatro','5':'cinco','6':'seis','7':'sete','8':'oito','9':'nove'}
  d = {'10':'dez','11':'onze','12':'doze','13':'treze','14':'quatorze','15':'quinze','16':'dezesseis','17':'dezessete',
    '18':'dezoito','19':'dezenove','2':'vinte','3':'trinta','4':'quarenta','5':'cinquenta','6':'sessenta','7':'setenta','8':'oitenta','9':'noventa'}
  c = {'1':'cento','2':'duzentos','3':'trezentos','4':'quatrocentos','5':'quinhentos','6':'seiscentos','7':'setecentos','8':'oitocentos',
    '9':'novecentos'}
  espe = ['mil',['milhão','milhões'],['bilhão','bilhões'],['trilhão','trilhões'],['quadrilhão','quadrilhões']] 

  if n <= 999999999999999999 and n >= 0:
    pass
  else: 
    return None

  n_str = str(n)
  lista_nume = list(n_str)
  lista_tres = []
  nome_nume = []

  lista_nume.reverse()
  tam = len(lista_nume)

  for dd in range(0,tam,3):
    lista_tres.append(lista_nume[dd:dd+3])

  if not((len(lista_nume) == 1) and (lista_nume[0] == '0')):
    for _d in range(len(lista_tres)):
      
      if _d == 1:
        if lista_tres[_d] != ['0','0','0']:
          nome_nume.insert(0,espe[0]) 

      elif _d == 2:
        if lista_tres[_d] != ['0','0','0']:
          if int(''.join(lista_tres[_d][::-1])) > 1:
            nome_nume.insert(0,espe[1][1])
          else:
            nome_nume.insert(0,espe[1][0])
      elif _d == 3:
        if lista_tres[_d] != ['0','0','0']:
          if int(''.join(lista_tres[_d][::-1])) > 1:
            nome_nume.insert(0,espe[2][1])
          else:
            nome_nume.insert(0,espe[2][0])
      elif _d == 4:
        if lista_tres[_d] != ['0','0','0']:
          if int(''.join(lista_tres[_d][::-1])) > 1:
            nome_nume.insert(0,espe[3][1])
          else:
            nome_nume.insert(0,espe[3][0])
      elif _d == 5:
        if lista_tres[_d] != ['0','0','0']:
          if int(''.join(lista_tres[_d][::-1])) > 1:
            nome_nume.insert(0,espe[4][1])
          else:
            nome_nume.insert(0,espe[4][0])


      for _ddd in range(len(lista_tres[_d])):
        
        if _ddd == 0:
          if len(lista_tres[_d]) == 1:
            if _d == 1:
              if lista_tres[_d][_ddd] == '1':
                pass
              else:
                nome_nume.insert(0,u[str(lista_tres[_d][_ddd])])
            else:   
              nome_nume.insert(0,u[str(lista_tres[_d][_ddd])])

          else:
            if lista_tres[_d][_ddd+1] == '1':
              pass
            else:
              if lista_tres[_d][_ddd] == '0':
                pass
              else:  
                nome_nume.insert(0,u[str(lista_tres[_d][_ddd])])
                nome_nume.insert(0,'e')
        if _ddd == 1:
          if lista_tres[_d][_ddd] == '1':
            nome_nume.insert(0,d[str((lista_tres[_d][_ddd])+(lista_tres[_d][_ddd-1]))])

            if len(lista_tres[_d]) == 3:
              nome_nume.insert(0,'e')
            
          elif lista_tres[_d][_ddd] == '0':
            pass
          else:
            nome_nume.insert(0,d[str(lista_tres[_d][_ddd])])

            if len(lista_tres[_d]) == 3:
              nome_nume.insert(0,'e')
        
        if _ddd == 2:
          if lista_tres[_d][_ddd] != '0':
            if (lista_tres[_d][_ddd-1] == '0') and (lista_tres[_d][_ddd-2] == '0') and (lista_tres[_d][_ddd] == '1'):
              nome_nume.insert(0,'cem')
            else:
              nome_nume.insert(0,c[str(lista_tres[_d][_ddd])])
          else:
            pass
  else:
    nome_nume.insert(0,'zero')
  return ' '.join(nome_nume)

class Exte(App):
  def build(self):
  
    layout = FloatLayout()

    label_p = Label()
    label_p.text = '''Conversor de Números Inteiros\nRetorna um texto representando o número por extenso.\n O número deve estar entre 0 e 999999999999999999.'''
    label_p.pos_hint = {'center_x':0.5,'top':0.98}
    label_p.size_hint = (0.7,(1/4))
    label_p.halign = 'center'
    label_p.font_size = 20
    label_p.color = [1,1,1,1]

    texto_area = TextInput()
    texto_area.pos_hint = {'x':0.05,'y':0.40} 
    texto_area.size_hint = (0.6,(1/4))
    texto_area.background_color = [1, 1, 1,1]
    texto_area.input_filter = 'int'
    texto_area.hint_text = "Digite um número natural..."
    texto_area.hint_text_color = (1,0,0,1)
    texto_area.multiline = False
    texto_area.font_size = '23sp'

    texto_area_f = TextInput()
    texto_area_f.pos_hint = {'center_x':0.5,'y':0.03} 
    texto_area_f.size_hint = (0.99,(1/3))
    texto_area_f.background_color = [1, 1, 1,1]
    texto_area_f.readonly = True
    texto_area_f.cursor_blink = False
    texto_area_f.font_size = '20sp'
    texto_area_f.foreground_color = (0,0,0,1)
    
    botao_1 = Button()
    botao_1.text = "CONVERTER"
    botao_1.pos_hint = {'x':0.65,'y':0.40}
    botao_1.size_hint = (0.15,(1/4))
    botao_1.background_color = (0,0,0,1)
    botao_1.background_normal = ''

    botao_copia = Button()
    botao_copia.text = "COPIAR"
    botao_copia.pos_hint = {'x':0.80,'y':0.40}
    botao_copia.size_hint = (0.15,(1/4))
    botao_copia.background_color = (0,0,0,1)
    botao_copia.background_normal = ''



    layout.add_widget(label_p)
    layout.add_widget(texto_area)
    layout.add_widget(texto_area_f)
    layout.add_widget(botao_1)
    layout.add_widget(botao_copia)

    Window.size = (800,300)
    Window.clearcolor = (0.2, 0.8, 1,1)

    def copia_texto():
      texto_area_f.copy(data=texto_area_f.text)

    def ver_num():
      if texto_area.text == "":
        texto_area_f.text = 'Vazio'
      else:
        if int(texto_area.text) >=0 and int(texto_area.text) <= 999999999999999999:
          texto_area_f.text = num_exten(int(texto_area.text))
        else:
          texto_area.text = ""
          texto_area_f.text = ""
    botao_1.on_press = ver_num
    botao_copia.on_press = copia_texto
    return layout
   

if __name__ == '__main__':
  
  e = Exte() 
  e.icon = "icone_exte.ico"
  e.title = "Número por extenso V1.0"
  e.run()
