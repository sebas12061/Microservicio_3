package edu.EAM.usuarios.Usuarios.model;

import lombok.AllArgsConstructor;
import lombok.Getter;

import lombok.Setter;

@Getter
@Setter
@AllArgsConstructor

public class Address {
    private String street;
    private String number;
    private String neighborhood;  //barrio
    private String city;
    private String postalCode;
}
