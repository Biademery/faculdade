package usuario;

import entidades.Usuarios;

public class Proprietário extends Usuarios {
    private String numbPropriedades;

    public Proprietário(String nome, String email, String telefone, String numbPropriedades) {
        super(nome,email, telefone);
        this.numbPropriedades = numbPropriedades;
    }

    public String getNumbPropriedades() {
        return numbPropriedades;
    }

    public void setNumbPropriedades(String numbPropriedades) {
        this.numbPropriedades = numbPropriedades;
    }

    public
}
