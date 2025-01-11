# **GraphQL Task**

This project is a Django application designed for KPI management and data processing. It includes a **GraphQL API** for creating, retrieving, updating, and deleting KPIs, as well as linking assets to KPIs.

---

## **Table of Contents**
- [Overview](#overview)
- [Features](#features)
- [Setup](#setup)
- [GraphQL API](#graphql-api)
  - [1. List All KPIs (Query)](#1-list-all-kpis-query)
  - [2. Delete a Specific KPI (Mutation)](#2-delete-a-specific-kpi-mutation)
  - [3. Create a New KPI (Mutation)](#3-create-a-new-kpi-mutation)
  - [4. Update Current KPI Fields (Mutation)](#4-update-current-kpi-fields-mutation)
  - [5. Link an Asset to a KPI (Mutation)](#5-link-an-asset-to-a-kpi-mutation)
  - [6. Fetch All AssetKPIs (Query)](#6-fetch-all-assetkpis-query)
- [Testing](#testing)

---

## **Overview**

This project reads data from sensors, processes it using user-defined equations, and stores the results in a database. The **GraphQL API** serves as the primary interface for managing KPIs and their relationships with assets.

---

## **Features**

- **GraphQL API** for KPI management and asset linking.
- Real-time data ingestion from sensor files.
- Support for arithmetic and regex-based data processing.
- Automated testing for models and GraphQL queries/mutations.

---

## **Setup**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/ziadwaelai/SW.git
   cd swTask
   ```

2. **Create and Activate a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```

6. **Access the GraphQL API**:
   Visit [http://127.0.0.1:8000/graphql/](http://127.0.0.1:8000/graphql/) to interact with the GraphQL API.

---

## **GraphQL API**

### **1. List All KPIs (Query)**

**Description**: Fetch all KPIs with their details.

**GraphQL Query**:
```graphql
query {
  allKpis {
    id
    name
    expression
    description
  }
}
```

**Expected Response**:
```json
{
  "data": {
    "allKpis": [
      {
        "id": "1",
        "name": "Revenue KPI",
        "expression": "ATTR + 100",
        "description": "Tracks revenue growth"
      },
      {
        "id": "2",
        "name": "Cost KPI",
        "expression": "ATTR - 50",
        "description": "Tracks cost reduction"
      }
    ]
  }
}
```

---

### **2. Delete a Specific KPI (Mutation)**

**Description**: Delete a KPI by its ID.

**GraphQL Mutation**:
```graphql
mutation {
  deleteKpi(kpiId: 1) {
    success
  }
}
```

**Expected Response**:
```json
{
  "data": {
    "deleteKpi": {
      "success": true
    }
  }
}
```

---

### **3. Create a New KPI (Mutation)**

**Description**: Create a new KPI with a name, expression, and optional description.

**GraphQL Mutation**:
```graphql
mutation {
  createKpi(name: "Efficiency KPI", expression: "ATTR * 0.8", description: "Tracks efficiency improvement") {
    kpi {
      id
      name
      expression
      description
    }
  }
}
```

**Expected Response**:
```json
{
  "data": {
    "createKpi": {
      "kpi": {
        "id": "3",
        "name": "Efficiency KPI",
        "expression": "ATTR * 0.8",
        "description": "Tracks efficiency improvement"
      }
    }
  }
}
```

---

### **4. Update Current KPI Fields (Mutation)**

**Description**: Update specific fields of an existing KPI.

**GraphQL Mutation**:
```graphql
mutation {
  updateKpi(kpiId: 3, name: "Updated Efficiency KPI", expression: "ATTR * 0.9") {
    kpi {
      id
      name
      expression
      description
    }
  }
}
```

**Expected Response**:
```json
{
  "data": {
    "updateKpi": {
      "kpi": {
        "id": "3",
        "name": "Updated Efficiency KPI",
        "expression": "ATTR * 0.9",
        "description": "Tracks efficiency improvement"
      }
    }
  }
}
```

---

### **5. Link an Asset to a KPI (Mutation)**

**Description**: Link an asset to an existing KPI.

**GraphQL Mutation**:
```graphql
mutation {
  linkAssetToKpi(assetId: "Asset-101", kpiId: 2, value: "120.5") {
    assetKpi {
      id
      assetId
      value
      kpi {
        id
        name
      }
    }
  }
}
```

**Expected Response**:
```json
{
  "data": {
    "linkAssetToKpi": {
      "assetKpi": {
        "id": "1",
        "assetId": "Asset-101",
        "value": "120.5",
        "kpi": {
          "id": "2",
          "name": "Cost KPI"
        }
      }
    }
  }
}
```

---

### **6. Fetch All AssetKPIs (Query)**

**Description**: Fetch all linked AssetKPIs with their associated KPI details.

**GraphQL Query**:
```graphql
query {
  allAssetKpis {
    id
    assetId
    value
    kpi {
      id
      name
    }
  }
}
```

**Expected Response**:
```json
{
  "data": {
    "allAssetKpis": [
      {
        "id": "1",
        "assetId": "Asset-101",
        "value": "120.5",
        "kpi": {
          "id": "2",
          "name": "Cost KPI"
        }
      }
    ]
  }
}
```

---

## **Testing**

To validate the API, run the following command:
```bash
python manage.py test KPI
```

The tests cover:
- **Model Testing**: Ensures proper creation and linking of KPIs and AssetKPIs.
- **GraphQL API Testing**: Validates KPI creation, retrieval, updating, deletion, and asset linking.

