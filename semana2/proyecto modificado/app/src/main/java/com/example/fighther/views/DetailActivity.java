package com.example.fighther.views;

import android.os.Bundle;
import androidx.appcompat.app.AppCompatActivity;
import androidx.databinding.DataBindingUtil;
import com.bumptech.glide.Glide;
import com.example.fighther.R;
import com.example.fighther.databinding.ActivityDetailBinding;
import com.example.fighther.models.Item;

public class DetailActivity extends AppCompatActivity {
    private ActivityDetailBinding binding;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        binding = DataBindingUtil.setContentView(this, R.layout.activity_detail);

        // Obtener datos del Intent
        Item item = new Item();
        item.setTitulo(getIntent().getStringExtra("titulo"));
        item.setDescripcion(getIntent().getStringExtra("descripcion"));
        item.setUrl(getIntent().getStringExtra("url"));

        // Establecer los datos en el binding
        binding.setItem(item);

        // Cargar la imagen con Glide
        Glide.with(this)
                .load(item.getUrl())
                .centerCrop()
                .into(binding.ivItemDetalle);
    }
}