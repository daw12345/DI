package com.example.fighther;

import android.app.ProgressDialog;
import android.content.Intent;
import android.os.Bundle;
import android.text.TextUtils;
import android.util.Patterns;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;


import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import com.google.android.gms.tasks.OnFailureListener;
import com.google.android.gms.tasks.OnSuccessListener;
import com.google.firebase.Firebase;
import com.google.firebase.auth.AuthResult;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;

import java.util.HashMap;


public class RegistroActivity extends AppCompatActivity {
    EditText etNombre, etApellido, etCorreo, etContrasena, etConfirmContrasena;
    Button btnRegistrar;


    TextView lblLoginR;
    FirebaseAuth firebaseAuth;
    private ProgressDialog progressDialog;


    String nombre = "", apellido = "", correo = "", contrasena = "", confirmarContrasena = "", telefono = "", direccion = "";


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_registro);

        // Inicializar Firebase Auth
        firebaseAuth = FirebaseAuth.getInstance();

        // Inicializar vistas
        etNombre = findViewById(R.id.etNombre);
        etApellido = findViewById(R.id.etApellido);
        etCorreo = findViewById(R.id.etCorreo);
        etContrasena = findViewById(R.id.etContrasena);
        etConfirmContrasena = findViewById(R.id.etConfirmContrasena);


        // Configurar botón de registro
        findViewById(R.id.btnRgistrar).setOnClickListener(v -> registrarUsuario());

        // Configurar botón de login
        findViewById(R.id.lblLoginR).setOnClickListener(v ->
                startActivity(new Intent(RegistroActivity.this, MainActivity.class)));

    }

    private void registrarUsuario() {

        String correo = etCorreo.getText().toString();
        String contrasena = etContrasena.getText().toString();

        firebaseAuth.createUserWithEmailAndPassword(correo, contrasena)
                .addOnCompleteListener(this, task -> {
                    if (task.isSuccessful()) {
                        // Si el registro es exitoso, guardar datos adicionales
                        guardarDatosUsuario();
                        Toast.makeText(RegistroActivity.this, "Usuario registrado correctamente",
                                Toast.LENGTH_SHORT).show();
                        startActivity(new Intent(RegistroActivity.this, DashboardActivity.class));
                        finish();
                    } else {
                        Toast.makeText(RegistroActivity.this, "Error en el registro: " +
                                task.getException().getMessage(), Toast.LENGTH_SHORT).show();
                    }
                });


    }

    private void guardarDatosUsuario() {
        String uid = firebaseAuth.getUid();
        HashMap<String, String> datosUsuario = new HashMap<>();
        datosUsuario.put("uid", uid);
        datosUsuario.put("nombre", etNombre.getText().toString());
        datosUsuario.put("apellido", etApellido.getText().toString());
        datosUsuario.put("correo", etCorreo.getText().toString());


        FirebaseDatabase.getInstance().getReference("Usuarios")
                .child(uid)
                .setValue(datosUsuario);
    }
    }





