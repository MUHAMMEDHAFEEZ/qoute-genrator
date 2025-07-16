#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test the API locally before deployment
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'api'))

from api.index import app

if __name__ == '__main__':
    print("Testing the API locally...")
    
    with app.test_client() as client:
        # Test health endpoint
        response = client.get('/health')
        print(f"Health check: {response.status_code}")
        
        # Test quote endpoint
        response = client.get('/api/quote')
        print(f"Quote API: {response.status_code}")
        
        # Test quote image endpoint
        response = client.get('/api/quote/image')
        print(f"Quote Image: {response.status_code}")
        
        # Test personalities endpoint
        response = client.get('/api/personalities')
        print(f"Personalities: {response.status_code}")
        
        if all(r.status_code == 200 for r in [
            client.get('/health'),
            client.get('/api/quote'),
            client.get('/api/quote/image'),
            client.get('/api/personalities')
        ]):
            print("✅ All tests passed! API is ready for deployment.")
        else:
            print("❌ Some tests failed.")
