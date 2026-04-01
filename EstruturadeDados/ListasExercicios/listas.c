#include "listas.h"

int isFull(Lista L)
{
    return (L.N == MAX);
}

int isEmpty(Lista L)
{
    return (L.N == 0);
}

void iniciarLista(Lista * L)
{
    L->N = 0;
}

tipoLista inserir(Lista * L, tipoLista x, int k)
{
    if(isFull(*L) || k < 0 || k > L->N) return 0;
int i;
for(i = L->N-1;i >= k; i--) L->itens[i+1] = L->itens[i];
L->itens[k] = x;
L->N++;
return 1;}

int AlterarLista(Lista *L, tipoLista x, int k){
    if(k < 0 || k >= L->N) return 0;
    L->itens[k] = x;
    return 1;}

int ConsultarLista(Lista L, tipoLista *x, int k){
if(k < 0 || k >= L.N) return 0;
*x = L.itens[k];
return 1;}

int ConcatenarListas(Lista *L1, Lista L2)
{
    if (L1->N + L2.N > MAX)
    {
        return 0;
    }

    for (int i = 0; i < L2.N; i++)
    {
        L1->itens[L1->N] = L2.itens[i];
        L1->N++;
    }
    return 1;
}

int contarLista(Lista L)
{
    return L.N;
}

int localizarLista(Lista L, int k)
{
    for (int i = 0; i < L.N; i++)
    {
        if (L.itens[i] == k)
        {
            return i;
        }
    }
    return -1;
}

void imprimirLista(Lista L)
{
    for (int i = 0;i < L.N; i++)
    {
        printf("[%d] ", L.itens[i]);
    }
    printf("\n");
}

tipoLista inserirEmOrdemLista(Lista *L, tipoLista x)
{
    if (isFull(*L))
    {
        return 0;
    }
    int maior = 0;
    for (int i = 0; i < L->N; i++)
    {
        if (x > L->itens[i])
        {
            maior = i + 1;
        }
    }

    return inserir(L, x, maior);
}
