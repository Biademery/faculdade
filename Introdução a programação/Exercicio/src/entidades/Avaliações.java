package entidades;

import usuario.Hospede;

public class Avaliações {
    private Lista_propriedades listaPropriedades;
    private Hospede hospede;
    private int nota;
    private String comentario;

    public Avaliações(Lista_propriedades listaPropriedades, Hospede hospede, int nota, String comentario){
        this.listaPropriedades = listaPropriedades;
        this.hospede = hospede;
        this.nota = nota;
        this.comentario =comentario;
    }

    public Lista_propriedades getListaPropriedades() {
        return listaPropriedades;
    }

    public void setListaPropriedades(Lista_propriedades listaPropriedades) {
        this.listaPropriedades = listaPropriedades;
    }

    public Hospede getHospede() {
        return hospede;
    }

    public void setHospede(Hospede hospede) {
        this.hospede = hospede;
    }

    public int getNota() {
        return nota;
    }

    public void setNota(int nota) {
        this.nota = nota;
    }

    public String getComentario() {
        return comentario;
    }

    public void setComentario(String comentario) {
        this.comentario = comentario;
    }


}
