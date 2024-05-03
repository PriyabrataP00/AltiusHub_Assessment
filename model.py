from app import db

class Invoice_Header(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    InvoiceNumber=db.Column(db.Integer, unique=True)
    CustomerName= db.Column(db.String(64))
    BillingAddress=db.Column(db.String(64))
    ShippingAddress= db.Column(db.String(128))
    GSTIN=db.Column(db.String(64))
    TotalAmount= db.Column(db.Integer)


class Invoice_Items(db.Model):
    id=db.Column(db.Integer, db.Foreign_key(Invoice_Header.id))
    itemName= db.Column(db.String(64))
    Quantity= db.Column(db.Integer)
    Price= db.Column(db.Integer)
    Amount= db.Column(db.Integer)



class BillSundry(db.Model):
    id= db.Column(db.Integer, db.Foreign_key(Invoice_Header.id))
    billSundryName =db.Column(db.String(64))
    Amount= db.Column(db.Integer)

db.create_all()