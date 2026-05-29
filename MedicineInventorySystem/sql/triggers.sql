USE medicine_inventory_db;

DELIMITER //

CREATE TRIGGER bills_before_insert
BEFORE INSERT ON Bills
FOR EACH ROW
BEGIN
    SET NEW.total = NEW.subtotal + NEW.tax - NEW.discount;
END//

CREATE TRIGGER bills_before_update
BEFORE UPDATE ON Bills
FOR EACH ROW
BEGIN
    SET NEW.total = NEW.subtotal + NEW.tax - NEW.discount;
END//

CREATE TRIGGER prescription_item_after_insert
AFTER INSERT ON Prescription_Items
FOR EACH ROW
BEGIN
    UPDATE Medicines
    SET quantity = quantity - NEW.quantity
    WHERE medicine_id = NEW.medicine_id;
END//

DELIMITER ;
