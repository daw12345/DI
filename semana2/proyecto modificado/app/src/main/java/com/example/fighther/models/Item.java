package com.example.fighther.models;

public class Item {
    private String titulo;
    private String descripcion;
    private String url;

    // Constructor vacío (requerido para Firebase)
    public Item() {
    }

    // Constructor con todos los campos
    public Item(String titulo, String descripcion, String url) {
        this.titulo = titulo;
        this.descripcion = descripcion;
        this.url = url;
    }

    // Getters y Setters
    public String getTitulo() {
        return titulo;
    }

    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }

    public String getDescripcion() {
        return descripcion;
    }

    public void setDescripcion(String descripcion) {
        this.descripcion = descripcion;
    }

    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }
}