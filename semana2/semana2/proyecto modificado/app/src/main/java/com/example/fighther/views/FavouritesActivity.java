package com.example.proyecto_firebase.views;

import android.content.Intent;
import android.os.Bundle;
import androidx.appcompat.app.AppCompatActivity;
import androidx.databinding.DataBindingUtil;
import androidx.lifecycle.ViewModelProvider;
import androidx.recyclerview.widget.LinearLayoutManager;
import android.view.View;
import android.widget.Toast;

import com.example.proyecto_firebase.R;
import com.example.proyecto_firebase.adapters.PeliculaAdapter;
import com.example.proyecto_firebase.databinding.ActivityFavouritesBinding;
import com.example.proyecto_firebase.models.Pelicula;
import com.example.proyecto_firebase.viewmodels.FavouritesViewModel;

import java.util.ArrayList;

public class FavouritesActivity extends AppCompatActivity implements
        PeliculaAdapter.OnPeliculaClickListener,
        PeliculaAdapter.OnFavoritoClickListener {  // Agregar esta interfaz

    private ActivityFavouritesBinding binding;
    private FavouritesViewModel viewModel;
    private PeliculaAdapter peliculaAdapter;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        binding = DataBindingUtil.setContentView(this, R.layout.activity_favourites);

        setupToolbar();
        setupRecyclerView();
        setupViewModel();
        observeErrors();
    }

    private void setupToolbar() {
        binding.toolbar.setNavigationOnClickListener(v -> finish());
        binding.toolbar.setTitle("Mis Favoritos");
    }

    private void setupRecyclerView() {
        peliculaAdapter = new PeliculaAdapter(new ArrayList<>(), this, this); // Agregar this para el listener de favoritos
        binding.recyclerViewFavoritos.setLayoutManager(new LinearLayoutManager(this));
        binding.recyclerViewFavoritos.setAdapter(peliculaAdapter);
    }

    private void setupViewModel() {
        viewModel = new ViewModelProvider(this).get(FavouritesViewModel.class);

        viewModel.getFavoritos().observe(this, peliculas -> {
            peliculaAdapter.setPeliculas(peliculas);
            updateEmptyState(peliculas.isEmpty());
        });

        viewModel.getError().observe(this, error -> {
            if (error != null && !error.isEmpty()) {
                Toast.makeText(this, error, Toast.LENGTH_SHORT).show();
            }
        });

        viewModel.cargarFavoritos();
    }

    private void updateEmptyState(boolean isEmpty) {
        binding.textViewEmpty.setVisibility(isEmpty ? View.VISIBLE : View.GONE);
        binding.recyclerViewFavoritos.setVisibility(isEmpty ? View.GONE : View.VISIBLE);

        if (isEmpty) {
            binding.textViewEmpty.setText("No tienes películas favoritas");
        }
    }

    private void observeErrors() {
        viewModel.getError().observe(this, error -> {
            if (error != null && !error.isEmpty()) {
                Toast.makeText(this, error, Toast.LENGTH_SHORT).show();
            }
        });
    }

    @Override
    public void onPeliculaClick(Pelicula pelicula) {
        Intent intent = new Intent(this, DetailActivity.class);
        intent.putExtra("id", pelicula.getId());
        intent.putExtra("titulo", pelicula.getTitulo());
        intent.putExtra("descripcion", pelicula.getDescripcion());
        intent.putExtra("imagen", pelicula.getImagen());
        startActivity(intent);
    }

    @Override
    public void onFavoritoClick(Pelicula pelicula) {
        viewModel.toggleFavorito(pelicula);
    }

    @Override
    protected void onResume() {
        super.onResume();
        viewModel.cargarFavoritos(); // Recargar favoritos al volver a la actividad
    }
}