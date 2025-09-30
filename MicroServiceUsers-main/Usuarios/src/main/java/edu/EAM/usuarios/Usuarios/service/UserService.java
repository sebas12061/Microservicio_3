package edu.EAM.usuarios.Usuarios.service;



import edu.EAM.usuarios.Usuarios.model.Address;
import edu.EAM.usuarios.Usuarios.model.User;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import edu.EAM.usuarios.Usuarios.repository.UserRepository;

import java.util.List;
import java.util.Map;
import java.util.UUID;
@Service
public class UserService {
    private final UserRepository repository;

    @Autowired
    public UserService(UserRepository repository) {
        this.repository = repository;
        initSampleData();
    }

    private void initSampleData() {
        Address addr1 = new Address("Main St", "123", "Downtown", "New York", "10001");
        save(new User(UUID.randomUUID().toString(), "Alice", "Female", "alice@example.com", "123456789", addr1));

        Address addr2 = new Address("Broadway", "456", "Midtown", "New York", "10002");
        save(new User(UUID.randomUUID().toString(), "Bob", "Male", "bob@example.com", "987654321", addr2));
    }

    public User save(User user) {
        if (user.getId() == null) {
            user.setId(UUID.randomUUID().toString());
        }
        return repository.save(user);
    }

    public User findById(String id) {
        return repository.findById(id);
    }

    public List<User> findAll() {
        return repository.findAll();
    }

    public List<User> findByName(String name) {
        return repository.findByNameContaining(name);
    }

    public User update(User user) {
        return repository.update(user);
    }

    public User patch(String id, Map<String, Object> updates) {
        User user = repository.findById(id);
        if (user != null) {
            updates.forEach((key, value) -> {
                switch (key) {
                    case "name" -> {
                        String newName = (String) value;
                        if (newName != null && !newName.trim().isEmpty()) {
                            user.setName(newName);
                        }
                    }
                    case "gender" -> {
                        String newGender = (String) value;
                        if (newGender != null && !newGender.trim().isEmpty()) {
                            user.setGender(newGender);
                        }
                    }
                    case "email" -> {
                        String newEmail = (String) value;
                        if (newEmail != null && !newEmail.trim().isEmpty()) {
                            user.setEmail(newEmail);
                        }
                    }
                    case "phoneNumber" -> {
                        String newPhone = (String) value;
                        if (newPhone != null && !newPhone.trim().isEmpty()) {
                            user.setPhoneNumber(newPhone);
                        }
                    }
                    case "address" -> {

                            if (value instanceof Map<?, ?> addrMap) {

                                Address current = user.getAddress();

                                String street = (String) addrMap.get("street");
                                if (street != null && !street.trim().isEmpty()) {
                                    current.setStreet(street);
                                }

                                String number = (String) addrMap.get("number");
                                if (number != null && !number.trim().isEmpty()) {
                                    current.setNumber(number);
                                }

                                String neighborhood = (String) addrMap.get("neighborhood");
                                if (neighborhood != null && !neighborhood.trim().isEmpty()) {
                                    current.setNeighborhood(neighborhood);
                                }

                                String city = (String) addrMap.get("city");
                                if (city != null && !city.trim().isEmpty()) {
                                    current.setCity(city);
                                }

                                String postalCode = (String) addrMap.get("postalCode");
                                if (postalCode != null && !postalCode.trim().isEmpty()) {
                                    current.setPostalCode(postalCode);
                                }

                                user.setAddress(current);
                            }
                        }


                }
            });
            return repository.update(user);
        }
        return null;
    }


    public void deleteById(String id) {
        repository.deleteById(id);
    }
}
