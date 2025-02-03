package com.example.fighther.views;

import android.content.Intent;
import android.os.Bundle;
import android.widget.Toast;


import androidx.appcompat.app.AppCompatActivity;
import androidx.databinding.DataBindingUtil;
import androidx.lifecycle.Observer;
import androidx.lifecycle.ViewModelProvider;
import androidx.recyclerview.widget.LinearLayoutManager;

import com.example.fighther.R;
import com.example.fighther.databinding.ActivityDashboardBinding;
import com.example.fighther.adapters.ItemAdapter;
import com.example.fighther.models.Item;
import com.example.fighther.viewmodels.DashboardViewModel;

import java.util.ArrayList;
import java.util.List;

public class DashboardActivity extends AppCompatActivity implements ItemAdapter.OnItemClickListener {
    private ActivityDashboardBinding binding;
    private DashboardViewModel dashboardViewModel;
    private ItemAdapter itemAdapter;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        binding = DataBindingUtil.setContentView(this, R.layout.activity_dashboard);
        binding.setLifecycleOwner(this);

        // Inicializar ViewModel
        dashboardViewModel = new ViewModelProvider(this).get(DashboardViewModel.class);

        // Configurar RecyclerView
        setupRecyclerView();

        // Observar cambios en los datos
        observeViewModel();

        // Configurar listeners
        setupListeners();

        // Cargar datos
        dashboardViewModel.cargarItems();
    }

    private void setupRecyclerView() {
        itemAdapter = new ItemAdapter(new ArrayList<>(), this);
        binding.recyclerViewItems.setLayoutManager(new LinearLayoutManager(this));
        binding.recyclerViewItems.setAdapter(itemAdapter);
    }

    private void observeViewModel() {
        dashboardViewModel.getItems().observe(this, new Observer<List<Item>>() {
            @Override
            public void onChanged(List<Item> items) {
                if (items != null) {
                    itemAdapter.setItems(items);
                }
            }
        });

        dashboardViewModel.getNavigateToLogin().observe(this, shouldNavigate -> {
            if (shouldNavigate) {
                startActivity(new Intent(DashboardActivity.this, MainActivity.class));
                finish();
            }
        });

        dashboardViewModel.getError().observe(this, error -> {
            if (error != null) {
                Toast.makeText(DashboardActivity.this, error, Toast.LENGTH_SHORT).show();
            }
        });
    }

    private void setupListeners() {
        binding.btnCerrarSesion.setOnClickListener(v -> {
            dashboardViewModel.cerrarSesion();
            Toast.makeText(this, "Cerraste Sesión Exitosamente", Toast.LENGTH_SHORT).show();
        });
    }

    @Override
    public void onItemClick(Item item) {
        // Navegar a DetailActivity cuando se hace click en un item
        Intent intent = new Intent(this, DetailActivity.class);
        intent.putExtra("titulo", item.getTitulo());
        intent.putExtra("descripcion", item.getDescripcion());
        intent.putExtra("url", item.getUrl());
        startActivity(intent);
    }
}