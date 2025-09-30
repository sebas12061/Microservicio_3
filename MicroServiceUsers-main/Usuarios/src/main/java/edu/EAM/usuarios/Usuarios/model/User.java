package edu.EAM.usuarios.Usuarios.model;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.Setter;

@Getter @Setter
@AllArgsConstructor
public class User {
    private String id;
    private String name;
    private String gender;
    private String Email;
    private String PhoneNumber;
    private Address address;
}
