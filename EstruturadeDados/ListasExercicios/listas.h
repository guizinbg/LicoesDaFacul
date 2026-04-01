#ifndef LISTAS_H
#define LISTAS_H

#include <stdio.h>
#include <stdlib.h>

#define MAX 10

typedef int tipoLista;


typedef struct {
    tipoLista itens[MAX];
    int N;
} Lista;


int isFull(Lista L);
int isEmpty(Lista L);
void iniciarLista(Lista *L);
tipoLista inserir(Lista *L, tipoLista x, int k);
int AlterarLista(Lista *L, tipoLista x, int k);
int ConsultarLista(Lista L, tipoLista *x, int k);
int ConcatenarListas(Lista *L1, Lista L2);
int contarLista(Lista L);
int localizarLista(Lista L, int k);
void imprimirLista(Lista L);
tipoLista inserirEmOrdemLista(Lista *L, tipoLista x);

#endif
