#include <stdio.h>
#include <stdlib.h>
#include "listas.h"

void exibirMenu() {
    printf("1. Inserir elemento na posicao K\n");
    printf("2. Inserir elemento em ordem\n");
    printf("3. Alterar elemento na posicao K\n");
    printf("4. Consultar elemento na posicao K\n");
    printf("5. Localizar valor na lista\n");
    printf("6. Contar elementos\n");
    printf("7. Imprimir lista\n");
    printf("8. Testar Concatenacao (Gera Lista 2 automatica)\n");
    printf("0. Sair\n");
    printf("Escolha uma opcao: ");
}

int main() {
    Lista L1;
    iniciarLista(&L1);

    int opcao, k, pos;
    tipoLista x;

    do {
        exibirMenu();
        scanf("%d", &opcao);

        switch(opcao) {
            case 1:
                printf("Digite o valor a ser inserido: ");
                scanf("%d", &x);
                printf("Digite a posicao (K): ");
                scanf("%d", &k);
                if (inserir(&L1, x, k)) {
                    printf("Elemento inserido com sucesso!\n");
                } else {
                    printf("Erro ao inserir. Posicao invalida ou lista cheia.\n");
                }
                break;

            case 2:
                printf("Digite o valor a ser inserido em ordem: ");
                scanf("%d", &x);
                if (inserirEmOrdemLista(&L1, x)) {
                    printf("Elemento inserido em ordem!\n");
                } else {
                    printf("Erro ao inserir.\n");
                }
                break;

            case 3:
                printf("Digite o NOVO valor: ");
                scanf("%d", &x);
                printf("Digite a posicao (K) que deseja alterar: ");
                scanf("%d", &k);
                if (AlterarLista(&L1, x, k)) {
                    printf("Elemento alterado com sucesso!\n");
                } else {
                    printf("Erro: Posicao invalida.\n");
                }
                break;

            case 4:
                printf("Digite a posicao (K) para consulta: ");
                scanf("%d", &k);
                if (ConsultarLista(L1, &x, k)) {
                    printf("O valor na posicao [%d] e: %d\n", k, x);
                } else {
                    printf("Erro: Posicao invalida.\n");
                }
                break;

            case 5:
                printf("Digite o valor que deseja localizar: ");
                scanf("%d", &x);
                pos = localizarLista(L1, x);
                if (pos != -1) {
                    printf("Valor %d encontrado na posicao [%d].\n", x, pos);
                } else {
                    printf("Valor nao encontrado na lista.\n");
                }
                break;

            case 6:
                printf("A lista possui %d elemento(s).\n", contarLista(L1));
                break;

            case 7:
                printf("Conteudo da Lista:\n");
                imprimirLista(L1);
                break;

            case 8: {
                Lista L2;
                iniciarLista(&L2);
                inserir(&L2, 99, 0);
                inserir(&L2, 100, 1);

                printf("Concatenando com a lista [99] [100]...\n");
                if (ConcatenarListas(&L1, L2)) {
                    printf("Listas concatenadas com sucesso!\n");
                } else {
                    printf("Erro: A juncao das listas excede o tamanho MAX.\n");
                }
                break;
            }

            case 0:
                printf("Encerrando o programa...\n");
                break;

            default:
                printf("Opcao invalida. Tente novamente.\n");
        }
    } while(opcao != 0);

    return 0;
}
