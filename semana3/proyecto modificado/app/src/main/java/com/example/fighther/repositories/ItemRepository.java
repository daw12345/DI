package com.example.fighther.repositories;

import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;

public class ItemRepository {
    private DatabaseReference databaseReference;

    public ItemRepository() {
        databaseReference = FirebaseDatabase.getInstance().getReference().child("idolos");
    }

    public void getItem(String itemId, ValueEventListener listener) {
        databaseReference.child(itemId).addListenerForSingleValueEvent(listener);
    }

    public void getAllItems(ValueEventListener listener) {
        databaseReference.addListenerForSingleValueEvent(listener);
    }

    // Método para obtener actualizaciones en tiempo real
    public void observeItems(ValueEventListener listener) {
        databaseReference.addValueEventListener(listener);
    }
}