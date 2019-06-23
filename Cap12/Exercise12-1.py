# -*- coding: utf-8 -*-
'''
Created on 21 de jun de 2018

@author: Romulo
'''



def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        inverse.setdefault(val, []).append(key)
    return inverse

def most_frequent(string):
    freq_letters = {}
    total_Letters = 0
    for letter in string:
        lower_Letter = letter.lower()
        if lower_Letter in "abcdefghijklmnopqrstuvwxyz":
            freq_letters.setdefault(lower_Letter, 0)
            freq_letters[lower_Letter] += 1
            total_Letters += 1
    listOfFreqLetters = list(set(freq_letters.values()))
    invertedListOfFreqLetters = invert_dict(freq_letters)
    listOfFreqLetters.sort(reverse = True)
    for freq in listOfFreqLetters: 
        print("%.3f%% ; %s" %(freq/total_Letters*100 ,", ".join(sorted(invertedListOfFreqLetters.get(freq)))))
    return
        
if __name__ == '__main__':
    #most_frequent("aeeaaabbcccr")
    #most_frequent("Vejo esse debate com certa frequência e ja pesquisei um pouco sobre o assunto, e sempre chego na mesma conclus�o. Apesar de ser uma discussao geralmente encaminhada pelo perfil ideol�gico da pessoa, defendendo ou atacando o assunto dependendo se ela for de esquerda ou de direita, tento me afastar dessa ""alineacao"" de achar que devo ter uma determinada opini�o so porque algu�m me chamou de ""de esquerda"" ou ""de direita"". Mas sempre me pareceu muito mais vantajoso a privatiza��o, pelo ponto de vista do consumidor/cidad�o. A concorr�ncia faz com que o produto chegue a um pre�o acess�vel e com uma qualidade boa, nao? Caso contrario, surgira algu�m que faz melhor/mais barato do que voc�, essa e a ideia de concorrencia. Sem falar no poder de escolha da pessoa, que fica livre para decidir o que ela considera melhor. Com a estatizacao, me parece que o governo ganha muito poder, e nao sinto isso como uma coisa boa. Talvez seja um medo so da minha cabe�a, mas faz sentido para mim que quanto mais poder o estado tem, pior. N�o que ele nao tenha que ter poder, so nao extrapolemos. Na estatizacao, se a qualidade e ruim, ou nao e feito do jeito que te agrada, paciencia pois e o unico servi�o disponivel. O argumento mais plausivel para a estatizacao e que ela, teoricamente, protege o cidadao das ""corporacoes mas"". Mas, por ser ""jovem"" e ter me aprofundado pouco no assunto, talvez eu tenha uma visao distorcida tanto da privatiza��o quanto da estatizacao. Por isso, gostaria de saber, e de ser corrigido sobre algo de errado que eu tenha falado tambem claro, porque estatizacao e melhor?")
    most_frequent('''A wonderful serenity has taken possession of my 
    entire soul, like these sweet mornings of spring which I enjoy with my whole heart. I am alone, and feel the charm
     of existence in this spot, which was created for the bliss of souls like mine. I am so happy, my dear friend, 
     so absorbed in the exquisite sense of mere tranquil existence, that I neglect my talents. I should be incapable of 
     drawing a single stroke at the present moment; and yet I feel that I never was a greater artist than now. When, while 
     the lovely valley teems with vapour around me, and the meridian sun strikes the upper surface of the impenetrable 
     foliage of my trees, and but a few stray gleams steal into the inner sanctuary, I throw myself down among the tall grass by
      the trickling stream; and, as I lie close to the earth, a thousand unknown plants are noticed by me: when I hear the buzz of
       the little world among the stalks, and grow familiar with the countless indescribable forms of 
     the insects and flies, then I feel the presence of the Almighty, who formed us in his own image, and the breath of that 
     universal love which bears and sustains us, as it floats around us in an eternity of bliss; and then, my friend, when 
     darkness overspreads my eyes, and heaven and earth seem to dwell in my soul and absorb its power, like the form of a 
     beloved mistress, then I often think with longing, Oh, would I could describe these conceptions, could impress upon 
     paper all that is living so full and warm within me, that it might be the mirror of my soul, as my soul is the mirror 
     of the infinite God! O my friend -- but it is too much for my strength -- I sink under the weight of the splendour of 
     these visions!A wonderful serenity has taken possession of my entire soul, like these sweet mornings of spring which I
      enjoy with my whole heart. I am alone, and feel the charm of existence in this spot, which was created for the bliss of 
      souls like mine. I am so happy, my dear friend, so absorbed in the exquisite sense of mere tranquil existence, that I 
      neglect my talents. I should be incapable of drawing a single stroke at the present moment; and yet I feel that I never 
      was a greater artist than now. When, while the lovely valley teems with vapour around me, and the meridian sun strikes 
      the upper surface of the impenetrable foliage of my trees, and but a few stray gleams steal into the inner sanctuary, 
      I throw myself down among the tall grass by the trickling stream; and, as I lie close to the earth, a thousand unknown 
      plants are noticed by me: when I hear the buzz of the little world among the stalks, and grow familiar with the countless 
      indescribable forms of the insects and flies, then I feel the presence of the Almighty, who formed us in his own image, 
      and the breath of that universal n love which bears and sustains us, as it floats around us in an eternity of bliss; and then,
       my friend, when darkness overspreads my eyes, and heaven and earth seem to dwell in my soul and absorb its power, like the 
       form of a beloved mistress, then I often think with longing, Oh, would I could describe these conceptions, 
    could impress upon paper all that is living so full and warm within me, that it might be the''')
    