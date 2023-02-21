from flask import render_template, url_for, request, redirect
from Models.Products import Product
from Models.Employees import Employee
from Assets import DBConn


def setup(app):

    @app.route("/index")
    def index():
        return render_template("index.html")

    @app.route("/contact")
    def contact():
        return render_template("contact.html")
    
    @app.route("/unosemployees")
    def unosemployees():
        return render_template("addemployee.html")
    
    @app.route("/addemployee",methods=["POST","GET"])
    def addemployee():
        dbSession = DBConn.createSession()
        if request.method == "POST":
            name = request.form.get("name")
            address = request.form.get("address")
            noviZaposlenik = Employee(Name = name, Address = address)
            dbSession.add(noviZaposlenik)
            dbSession.commit()
            return redirect(url_for("employees"))
        else:
            return redirect(url_for("unosemployees"))

    @app.route("/employees")
    def employees():
        dbSession = DBConn.createSession()
        employeesQuery = dbSession.query(Employee).all()
        return render_template("employees.html", employees=employeesQuery)
    
     
    @app.route("/listemployees",methods=["POST","GET"])
    def listemployees():
        dbSession = DBConn.createSession()
        employeeQuery = dbSession.query(Employee).all()
        return render_template("listemployees.html",employees = employeeQuery)
    
    @app.route("/unos")
    def unos():
        return render_template("addProduct.html")

    @app.route("/addproduct",methods=["POST","GET"])
    def addproduct():
        dbSession = DBConn.createSession()
        if request.method == "POST":
            name = request.form.get("name")
            price = request.form.get("price")
            noviProizvod = Product(Name = name, Price = price)
            dbSession.add(noviProizvod)
            dbSession.commit()
            return redirect(url_for("products"))
        else:
            return redirect(url_for("unos"))

    @app.route("/products",methods=["POST","GET"])
    def products():
        dbSession = DBConn.createSession()
        productsQuery = dbSession.query(Product).all()
        return render_template("products.html", products = productsQuery)
    
    @app.route("/listProduct",methods=["POST","GET"])
    def listProduct():
        dbSession = DBConn.createSession()
        productsQuery = dbSession.query(Product).all()
        return render_template("listProduct.html",products = productsQuery)
        
    
            
    @app.route("/login")
    def login():
        return render_template("login.html")
      
    @app.route("/register")
    def register():
        return render_template("register.html")
    
    
    app.add_url_rule("/", "index", index)
    app.run(debug=True)
