package edu.EAM.usuarios.Usuarios.repository;


import edu.EAM.usuarios.Usuarios.model.User;
import org.springframework.stereotype.Repository;

import java.util.*;
import java.util.stream.Collectors;

@Repository
public class UserRepository {

    //base de datos iamginaria
    private final Map<String, User> database = new HashMap<>();

    // guardar
    public User save(User user) {
        database.put(user.getId(), user);
        return user;
    }

    // buscar(por id)
    public User findById(String id) {
        return database.get(id);
    }

    // darme todos
    public List<User> findAll() {
        return new ArrayList<>(database.values());
    }

    // buscar por nombre me da toods los que  tengan ese nombre
    public List<User> findByNameContaining(String name) {
        return database.values().stream()
                .filter(user -> user.getName().toLowerCase().contains(name.toLowerCase()))
                .collect(Collectors.toList());
    }

    // eliminar
    public void deleteById(String id) {
        database.remove(id);
    }

    // actualizar
    public User update(User user) {
        if (database.containsKey(user.getId())) {
            database.put(user.getId(), user);
            return user;
        }
        return null;
    }
}
