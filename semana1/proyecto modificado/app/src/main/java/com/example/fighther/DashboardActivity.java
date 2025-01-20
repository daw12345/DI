package com.example.fighther;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;
import androidx.appcompat.app.AppCompatActivity;
import com.bumptech.glide.Glide;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.FirebaseUser;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;
import com.example.fighther.databinding.ActivityDashboardBinding;

public class DashboardActivity extends AppCompatActivity {
    Button btnCerrarSesion;
    FirebaseAuth firebaseAuth;
    FirebaseUser firebaseUser;
    // Añadir referencia a la base de datos
    DatabaseReference databaseReference;
    TextView tvTitulo, tvDescripcion;
    ImageView ivContenido;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_dashboard);

        // Inicializar Firebase
        firebaseAuth = FirebaseAuth.getInstance();
        firebaseUser = firebaseAuth.getCurrentUser();
        databaseReference = FirebaseDatabase.getInstance().getReference("idolos/1");



        // Inicializar vistas
        btnCerrarSesion = findViewById(R.id.btnCerrarSesion);
        tvTitulo = findViewById(R.id.tvTitulo);
        tvDescripcion = findViewById(R.id.tvDescripcion);
        ivContenido = findViewById(R.id.ivUrl);

        // Cargar datos desde Firebase
        cargarDatosFirebase();

        // Configurar botón de cerrar sesión
        btnCerrarSesion.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                cierreSesion();
            }
        });
    }

    private void cargarDatosFirebase() {



        // Obtener el primer elemento
        databaseReference.addListenerForSingleValueEvent(new ValueEventListener() {
            @Override
            public void onDataChange(DataSnapshot dataSnapshot) {
                if (dataSnapshot.exists()){
                    // Obtener los datos del item
                    String titulo = dataSnapshot.child("titulo").getValue(String.class);
                    String descripcion =  dataSnapshot.child("descripcion").getValue(String.class);
                    String imageUrl = dataSnapshot.child("url").getValue(String.class);

                    // Mostrar los datos en la UI
                    tvTitulo.setText(titulo);
                    tvDescripcion.setText(descripcion);

                    // Cargar imagen usando Glide
                    Glide.with(DashboardActivity.this)
                            .load(imageUrl)
                            .into(ivContenido);


                }
            }

            @Override
            public void onCancelled(DatabaseError databaseError) {
                Toast.makeText(DashboardActivity.this,
                        "Error al cargar datos: " + databaseError.getMessage(),
                        Toast.LENGTH_SHORT).show();
            }
        });
    }

    private void cierreSesion() {
        firebaseAuth.signOut();
        startActivity(new Intent(DashboardActivity.this, MainActivity.class));
        Toast.makeText(this, "Cerraste Sesion Exitosamente", Toast.LENGTH_SHORT).show();
        finish();
    }
}