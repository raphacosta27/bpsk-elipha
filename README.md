---
title: Camada Física -  APS 8 - Modulação/DeModulação BPSK
author: Elisa Malzoni e Raphael Costa - elisamm@al.insper.edu.br e raphaelamc1@al.insper.edu.br
date: Outubro - 2017
---
# Modulação/DeModulação BPSK

## Frequência de transmissão e banda ocupada
A frequência de transmissão utilizada pode variar entre 0 e 18.2kHz, sendo o valor ótimo, no nosso caso, em torno de 2.2kHz devido ao falante e microfone utilizados.
Com isso, a banda ocupada pelo sinal é o dobro da frequência, logo 4.4kHz.

## Funcionamento geral do projeto
Para transmissão de texto através de áudio, utilizamos algoritimos em python e GNU Radio.
Primeiro, transformamos a frase em uma sequência de bytes pré-definidos pela modulação do tipo BPSK. Em seguida, o python insere os dados em uma porta através de um socket, para que o GNU Radio tenha acesso a estes dados.
O GNU Radio faz entào a modulação e transmite o audio.

O receptor, pelo GNU Radio, capta e demodula o sinal. Logo após, o GNU disponiliza os dados em outra porta para que o pyhton tenha acesso ao sinal demodulado, já em uma sequência de bytes exibindo os caracteres resultantes.

## Modulação BPSK
A modulação BPSK é um tipo de modulação PSK (Phase-shift keying), que consiste em alterar a fase da portadora, em 180 graus, para cada símbolo.
