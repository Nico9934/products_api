![Portada](https://github.com/Nico9934/products_api/blob/master/public/portada.png)

# API de Productos

Una simple API para gestionar productos.
### La misma te permite realizar las operaciones CRUD, para gestionar los productos de tu empresa. 

## Obtener todos los productos

### Ruta
GET /v1/api/products

## Obtener solamente un producto

### Ruta
GET /v1/api/products/<product_id>


## Agregar un producto
### Ruta
POST /v1/api/products

```json
{
  "product": "nombre_del_producto",
  "costPrice": "precio_de_costo",
  "salePrice": "precio_de_venta",
  "category": "Categoria_del_producto"
}

```

## Editar un producto

### Ruta
PUT /v1/api/products/<product_id>
```json
{
  "product": "nombre_del_producto_actualizado",
  "costPrice": "precio_de_costo_actualizado",
  "salePrice": "precio_de_venta_actualizado",
  "category": "Categoria_del_producto_actualizado"
}

```

## Eliminar un producto

### Ruta
PUT /v1/api/products/<product_id>
