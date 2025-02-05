package com.example.fighther.views;

import android.content.Intent;
import android.os.Bundle;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.databinding.DataBindingUtil;
import androidx.recyclerview.widget.LinearLayoutManager;

import com.example.fighther.R;
import com.example.fighther.adapters.ItemAdapter;
import com.example.fighther.databinding.ActivityFavoritesBinding;
import com.example.fighther.models.Item;
import com.example.fighther.repositories.FavoritesRepository;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;

import java.util.ArrayList;
import java.util.List;

public class FavoritesActivity extends AppCompatActivity {
    private ActivityFavoritesBinding binding;
    private ItemAdapter adapter;
    private FavoritesRepository favoritesRepository;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        binding = DataBindingUtil.setContentView(this, R.layout.activity_favorites);

        // Ya no necesitamos setupToolbar() porque lo manejaremos directamente aquí
        setSupportActionBar(binding.toolbar);
        if (getSupportActionBar() != null) {
            getSupportActionBar().setDisplayHomeAsUpEnabled(true);
            getSupportActionBar().setDisplayShowHomeEnabled(true);
        }

        setupRecyclerView();
        loadFavorites();
    }

    private void setupRecyclerView() {
        adapter = new ItemAdapter(new ArrayList<>(), item -> {
            Intent intent = new Intent(this, DetailActivity.class);
            intent.putExtra("id", item.getId());
            intent.putExtra("titulo", item.getTitulo());
            intent.putExtra("descripcion", item.getDescripcion());
            intent.putExtra("url", item.getUrl());
            startActivity(intent);
        });

        binding.rvFavorites.setLayoutManager(new LinearLayoutManager(this));
        binding.rvFavorites.setAdapter(adapter);
    }

    private void loadFavorites() {
        favoritesRepository = new FavoritesRepository();
        favoritesRepository.getFavorites(new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot snapshot) {
                List<Item> items = new ArrayList<>();

                if (snapshot.exists() && snapshot.hasChildren()) {
                    for (DataSnapshot favSnapshot : snapshot.getChildren()) {
                        String itemId = favSnapshot.getKey();
                        if (itemId != null) {
                            FirebaseDatabase.getInstance().getReference("idolos")
                                    .child(itemId)
                                    .get()
                                    .addOnSuccessListener(dataSnapshot -> {
                                        if (dataSnapshot.exists()) {
                                            Item item = new Item();
                                            item.setId(itemId);
                                            item.setTitulo(dataSnapshot.child("titulo").getValue(String.class));
                                            item.setDescripcion(dataSnapshot.child("descripcion").getValue(String.class));
                                            item.setUrl(dataSnapshot.child("url").getValue(String.class));
                                            items.add(item);
                                            adapter.setItems(new ArrayList<>(items));
                                        }
                                    })
                                    .addOnFailureListener(e -> {
                                        Toast.makeText(FavoritesActivity.this,
                                                "Error al cargar juego: " + e.getMessage(),
                                                Toast.LENGTH_SHORT).show();
                                    });
                        }
                    }
                } else {
                    adapter.setItems(new ArrayList<>());
                }
            }

            @Override
            public void onCancelled(@NonNull DatabaseError error) {
                Toast.makeText(FavoritesActivity.this,
                        "Error al cargar favoritos: " + error.getMessage(),
                        Toast.LENGTH_SHORT).show();
            }
        });
    }

    @Override
    public boolean onSupportNavigateUp() {
        onBackPressed();
        return true;
    }
}