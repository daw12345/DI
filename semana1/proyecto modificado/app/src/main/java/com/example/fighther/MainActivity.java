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


import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.OnFailureListener;
import com.google.android.gms.tasks.Task;

import com.google.firebase.auth.AuthResult;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.FirebaseUser;

public class MainActivity extends AppCompatActivity {

    private FirebaseAuth firebaseAuth;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        firebaseAuth = FirebaseAuth.getInstance();

        findViewById(R.id.btnIngresarL).setOnClickListener (v -> loginUsuario());

        findViewById(R.id.lblRegistrar).setOnClickListener(v ->
                startActivity(new Intent(MainActivity.this, RegistroActivity.class)));
    }

    private void loginUsuario() {
        String correo = ((EditText) findViewById(R.id.etCorreoL)).getText().toString();
        String contrasena = ((EditText) findViewById(R.id.etContrasenaL)).getText().toString();

        firebaseAuth.signInWithEmailAndPassword(correo, contrasena)
                .addOnCompleteListener(this, task -> {
                    if (task.isSuccessful()) {
                        Toast.makeText(MainActivity.this, "Inicio de sesión exitoso.", Toast.LENGTH_SHORT).show();
                        startActivity(new Intent(MainActivity.this, DashboardActivity.class));
                        finish();
                    } else {
                        Toast.makeText(MainActivity.this, "Error en autenticación.", Toast.LENGTH_SHORT).show();
                    }
                });
    }
}