from flask import jsonify, request
from app import app, db
from app.model import Invoice_Header, Invoice_Items, BillSundry

@app.route("/create", methods=['POST'])
def create():
    data= request.json
    header= data["Invoice_Header"]
    items= data["Invoice_Item"]
    sundry= data["BillSundry"]
    if header:
        if id not in header:
            return jsonify({'msg': "Missing Invoice Id"}), 400
        
        id=header['id']
        if Invoice_Header.query.filter_by(id=id).first():
            return jsonify({'msg':"Invoice Id already exists"}), 400
        
        id=Invoice_Header(id=id)
        invoice_num=Invoice_Header(InvoiceNumber=header.get("InvoiceNumber",-1))
        cust_name=  Invoice_Header(CustomerName=header.get("CustomerName",""))
        bill_Addr=  Invoice_Header(BillingAddress=header.get("BillingAddress",""))
        ship_Addr=  Invoice_Header(ShippingAddress=header.get("ShippingAddress",""))
        gstin=      Invoice_Header(GSTIN=header.get("GSTIN",0))
        total_amt=  Invoice_Header(TotalAmount=header.get("TotalAmount",0))
        
        db.session.add(id)
        db.session.add(invoice_num)
        db.session.add(cust_name)
        db.session.add(bill_Addr)
        db.session.add(ship_Addr)
        db.session.add(gstin)
        db.session.add(total_amt)
    
    if items:
        if id not in items:
            return jsonify({'msg': "Missing Invoice Id"}), 400
        
        id=items['id']
        if Invoice_Items.query.filter_by(id=id).first():
            return jsonify({'msg':"Invoice Id already exists"}), 400
        
        id=Invoice_Items(id=id)
        itemName= Invoice_Items(itemName= items.get("itemName"))
        Quantity= Invoice_Items(Quantity= items.get("Quantity"))
        Price= Invoice_Items(Price= items.get("Price"))
        Amount= Invoice_Items(Amount= items.get("Amount"))

        db.session.add(id)
        db.session.add(itemName)
        db.session.add(Quantity)
        db.session.add(Price)
        db.session.add(Amount)

    if sundry:
        if id not in sundry:
            return jsonify({'msg': "Missing Invoice Id"}), 400
        
        id= sundry['id']
        if Invoice_Header.query.filter_by(id=id).first():
            return jsonify({'msg':"Invoice Id already exists"}), 400
        
        id= BillSundry(id=id)
        billSundry= BillSundry(billSundry= sundry.get("billSundry"))
        Amount= BillSundry(Amount= sundry.get("Amount"))

        db.session.add(id)
        db.session.add(billSundry)
        db.session.add(Amount)

    db.commit()

    return jsonify({'msg':"Successfully Inserted Data"}), 201


@app.route("/update", methods=['POST'])
def update():
    data= request.json
    header= data["Invoice_Header"]
    items= data["Invoice_Item"]
    sundry= data["BillSundry"]
    if header:
        if id not in header:
            return jsonify({'msg': "Missing Invoice Id"}), 400
        
        id=header['id']
        if not Invoice_Header.query.filter_by(id=id).first():
            return jsonify({'msg':"Invoice Id does not exist"}), 400
        
        for i in header:
            db.session.update(i,header[i])
        return jsonify({'msg':"Updated Invoice Header successfully"}), 201
    
    if items:
        if id not in items:
            return jsonify({'msg': "Missing Invoice Id"}), 400
        
        id=items['id']
        if not Invoice_Items.query.filter_by(id=id).first():
            return jsonify({'msg':"Invoice Id does not exist"}), 400
        
        for i in items:
            db.session.update(i,items[i])
        return jsonify({'msg':"Updated Invoice Items successfully"}), 201
    
    if sundry:
        if id not in sundry:
            return jsonify({'msg': "Missing Invoice Id"}), 400
        
        id= sundry['id']
        if not BillSundry.query.filter_by(id=id).first():
            return jsonify({'msg':"Invoice Id does not exist"}), 400
        for i in sundry:
            db.session.update(i,items[i])
        return jsonify({'msg':"Updated Bill Sundry successfully"}), 201

@app.route("/delete", methods=['POST'])
def delete():
    return ("val")

@app.route("/retrieve", methods=['GET'])
def retrieve():
    data= request.json
    header= data["Invoice_Header"]
    items= data["Invoice_Item"]
    sundry= data["BillSundry"]
    if header:
        if id not in header:
            return jsonify({'msg': "Missing Invoice Id"}), 400
        
        id=header['id']
        val=Invoice_Header.query.filter_by(id=id).first()
        return jsonify({'Header':val}),201
    
    if items:
        if id not in items:
            return jsonify({'msg': "Missing Invoice Id"}), 400
        
        id=items['id']
        val= Invoice_Header.query.filter_by(id=id).first()
        return jsonify({'Items':val}),201
    
    if sundry:
        if id not in sundry:
            return jsonify({'msg': "Missing Invoice Id"}), 400
        
        id= sundry['id']
        val= Invoice_Header.query.filter_by(id=id).first()
        return jsonify({'Sundry':val}),201

    return jsonify({"msg":"Invalid filter"}), 400

@app.route("/list", methods=['GET'])
def list():
    data= request.json
    header= data["Invoice_Header"]
    items= data["Invoice_Item"]
    sundry= data["BillSundry"]
    if header:
        if id not in header:
            return jsonify({'msg': "Missing Invoice Id"}), 400
        

        id=header['id']
        val=Invoice_Header.query.filter_by(id=id)
        return jsonify({'Header':val}),201
    
    if items:
        if id not in items:
            return jsonify({'msg': "Missing Invoice Id"}), 400
        
        id=items['id']
        val= Invoice_Header.query.filter_by(id=id)
        return jsonify({'Items':val}),201
    
    if sundry:
        if id not in sundry:
            return jsonify({'msg': "Missing Invoice Id"}), 400
        
        id= sundry['id']
        val= Invoice_Header.query.filter_by(id=id)
        return jsonify({'Sundry':val}),201

    return jsonify({"msg":"Invalid filter"}), 400