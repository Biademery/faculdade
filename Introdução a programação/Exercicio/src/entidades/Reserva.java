package entidades;


import usuario.Hospede;

import java.util.Date;

public class Reserva {
    private Lista_propriedades listaPropriedades;
    private Hospede hospede;
    private double precoTotal;
    private Date checkin;
    private Date checkout;

    public Reserva(Lista_propriedades listaPropriedades, Hospede hospede, double precoTotal, Date checkin, Date checkout) {
        this.listaPropriedades = listaPropriedades;
        this.hospede = hospede;
        this.precoTotal = precoTotal;
        this.checkin = checkin;
        this.checkout = checkout;
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

    public double getPrecoTotal() {
        return precoTotal;
    }

    public void setPrecoTotal(double precoTotal) {
        this.precoTotal = precoTotal;
    }

    public Date getCheckin() {
        return checkin;
    }

    public void setCheckin(Date checkin) {
        this.checkin = checkin;
    }

    public Date getCheckout() {
        return checkout;
    }

    public void setCheckout(Date checkout) {
        this.checkout = checkout;
    }
}
