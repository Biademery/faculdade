package app;

import entidades.Avaliações;
import entidades.Reserva;
import propriedades.Apartamento;
import usuario.Hospede;
import usuario.Proprietário;

import java.util.*;

public class Main {
    public static void main(String[] args) {
        Proprietário proprietário1 = new Proprietário("Bia", "bia@demery.com", "83987654321", "4");
        Hospede hospede1 = new Hospede("João", "joao@fulano.com", "11987654321");

        Apartamento apartamento1 = new Apartamento("Av. Sem nome, 123",3,1.200,"Belo apartamento de tantos m2","foto1","Café da manhã incluido");
        Reserva reserva = new Reserva(apartamento1, hospede1, 12.333, new Date(), new Date(12345));
        Avaliações avaliacao1 = new Avaliações(apartamento1, hospede1, 5, "Otimo apartamento!");



    }

}
