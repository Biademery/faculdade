package propriedades;

import entidades.Lista_propriedades;

public class Apartamento extends Lista_propriedades {
    private String descrição;
    private String[] fotos;
    private String[] comodidades;

    public Apartamento(String endereco, int numbQuartos, double preco, String descrição, String[] fotos, String[] comodidades) {
        super(endereco, numbQuartos, preco);
        this.descrição = descrição;
        this.fotos = fotos;
        this.comodidades = comodidades;
    }

    @Override
    public String getDescricao() {
        return null;
    }

    @Override
    public String[] getFotos() {
        return new String[0];
    }

    @Override
    public String[] getComodidade() {
        return new String[0];
    }

    public String getDescrição() {
        return descrição;
    }

    public void setDescrição(String descrição) {
        this.descrição = descrição;
    }

    public void setFotos(String[] fotos) {
        this.fotos = fotos;
    }

    public String[] getComodidades() {
        return comodidades;
    }

    public void setComodidades(String[] comodidades) {
        this.comodidades = comodidades;
    }
}
