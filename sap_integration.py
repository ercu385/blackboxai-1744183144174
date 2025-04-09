import os
from dotenv import load_dotenv

load_dotenv()

class SAPConnection:
    def __init__(self):
        print("SAP entegrasyonu devre dışı - Mock modunda çalışıyor")
        self.conn = None
    
    def connect(self):
        """Mock SAP bağlantısı"""
        print("Mock SAP bağlantısı oluşturuldu")
    
    def get_materials(self):
        """Mock malzeme listesi döndürür"""
        return [
            {"MATNR": "MOCK001", "MAKTX": "Mock Malzeme 1"},
            {"MATNR": "MOCK002", "MAKTX": "Mock Malzeme 2"}
        ]
    
    def create_production_order(self, order_data):
        """Mock üretim emri oluşturur"""
        print(f"Mock üretim emri oluşturuldu: {order_data}")
        return "MOCK_ORDER_123"
    
    def close(self):
        """Mock bağlantı kapatma"""
        print("Mock SAP bağlantısı kapatıldı")
