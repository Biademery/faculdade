package entidades;

public abstract class Lista_propriedades {
    private String endereco;
    private int numbQuartos;
    private double preco;

    public Lista_propriedades( String endereco, int numbQuartos, double preco) {
        this.endereco = endereco;
        this.numbQuartos = numbQuartos;
        this.preco = preco;
    }

    public String getEndereco() {
        return endereco;
    }

    public void setEndereco(String endereco) {
        this.endereco = endereco;
    }

    public int getNumbQuartos() {
        return numbQuartos;
    }

    public void setNumbQuartos(int numbQuartos) {
        this.numbQuartos = numbQuartos;
    }

    public double getPreco() {
        return preco;
    }

    public void setPreco(double preco) {
        this.preco = preco;
    }

    public abstract String getDescricao();
    public abstract String[] getFotos();
    public abstract String[] getComodidade();
}
