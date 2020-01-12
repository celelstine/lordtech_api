## API Documentation


### API V1

`route /api/v1/`

- #### User `user/`
  - **create ['']** : `admin only` route for admin to create a new user
    ```
    request Payload POST
    {
        username: string (required),
        role: string (required [da,gc])
    }

    response 201
    {
        username: string,
        password; string,
        role: string
    }

    ```
  - **Login ['login/']** : `non-proctected` `do not add authorization header`
    ```
    request Payload  POST
    {
        username: string (required),
        paassword: string (required [da,gc])
    }

    response 200
    {
        username: string,
        password; string,
        role: string,
        expired_at: datetime,
        access_token: string,
        refresh_token: string
    }

    ```

    - **logout ['logout/']** : `protected` 
    ```
    request Payload POST
    {
    }

    response 200
    {
    }

    ```

    - **Refrresh Token ['refresh_token/']** : `non-protected`  Get new auth token
    ```
    header
    - Refresh-Token required

    request Payload  POST
    {
    }

    response 200
    {
        expired_at: datetime,
        access_token: string,
        refresh_token: string
    }

    ```
    - **Reset Password ['reset_password/']** : `admin only` reset users password
    ```
    request Payload  POST
    {
        username: string (required)
    }

    response 200
    {
        username: string,
        password; string,
    }

    ```
    - Not allowed or available endpoint
        - patch
        - put
        - delete


- #### Configuration `config/` `protected`
`model fields:`
```
key: string required
value: string required
category: string required [da, gc]
is_active: boolean opt
```
  - **List ['']**
    ```
    request Query String GET
    {
        key: string,
        category: string  [da,gc]
    }

    response 200
    {
        "count": 3,
        "next": null,
        "previous": null,
        "results": [
            {
                "id": "20807cef-69e5-463e-b9ef-58cdf5b93586",
                "create_date": "2019-12-01T15:01:17.487173Z",
                "modify_date": "2019-12-01T15:01:17.487173Z",
                "key": "cost_per_sub",
                "value": "10000",
                "category": "da",
                "is_active": true
            },
            ...
        ]
    }

    ```
- **Create ['']**
    ```
    request Request Payload POST
    {
        key: string (required),
        Value: string (required),
        category: string  [da,gc] (required)
    }

    response 201
    {
        "id": "20807cef-69e5-463e-b9ef-58cdf5b93586",
        "create_date": "2019-12-01T15:01:17.487173Z",
        "modify_date": "2019-12-01T15:01:17.487173Z",
        "key": "cost_per_sub",
        "value": "10000",
        "category": "da",
        "is_active": true
    }

    ```

- **Details Route ['/{id}']**
   - patch
   - put
   - get
   - delete


- #### Sales rep `salesrep/` `protected`
`model fields:`
```
name: string required
category: string required [da, gc]
is_active: boolean opt
cash_balance: decimal optional
airtime_balance: decimal optional
data_balance: decimal optional
```
`unique_together = ('category', 'name')`
  - **List ['']**
    ```
    request Query String GET
    {
        name: string (required),
        category: string  [da,gc]
    }

    response 200
    {
        "count": 3,
        "next": null,
        "previous": null,
        "results": [
            {
            "id": "d67ae125-0a09-4ef3-8e91-b18eb58aaf38",
            "create_date": "2019-12-01T15:15:20.017685Z",
            "modify_date": "2019-12-15T15:10:43.398205Z",
            "name": "sam",
            "category": "da",
            "is_active": true,
            "cash_balance": 0,
            "airtime_balance": 130005,
            "data_balance": 19456000
            },
            ...
        ]
    }

    ```
- **Create ['']**
    ```
    request Request Payload POST
    validation; same as model

    response 201
     {
        "id": "d67ae125-0a09-4ef3-8e91-b18eb58aaf38",
        "create_date": "2019-12-01T15:15:20.017685Z",
        "modify_date": "2019-12-15T15:10:43.398205Z",
        "name": "sam",
        "category": "da",
        "is_active": true,
        "cash_balance": 0,
        "airtime_balance": 130005,
        "data_balance": 19456000
    },

    ```

- **Details Route ['/{id}']**
   - patch
   - put
   - get
   - delete


- #### product `product/` `protected`
`model fields:`
```
name: string required
category: string required [da, gc]
is_active: boolean opt
```
`unique_together = ('category', 'name')`
  - **List ['']**
    ```
    request Query String GET
    {
        name: string (required),
        category: string  [da,gc]
    }

    response 200
    {
        "count": 3,
        "next": null,
        "previous": null,
        "results": [
            {
            "id": "63464d75-dbc4-4307-bc0d-e030bc965768",
            "create_date": "2019-12-01T18:45:13.900083Z",
            "modify_date": "2019-12-01T18:45:13.900083Z",
            "name": "MTN",
            "category": "da",
            "is_active": true
            },
            ...
        ]
    }

    ```
- **Create ['']**
    ```
    request Request Payload POST
    validation; same as model

    response 201
     {
    "id": "63464d75-dbc4-4307-bc0d-e030bc965768",
    "create_date": "2019-12-01T18:45:13.900083Z",
    "modify_date": "2019-12-01T18:45:13.900083Z",
    "name": "MTN",
    "category": "da",
    "is_active": true
    },

    ```

- **Details Route ['/{id}']**
   - patch
   - put
   - get
   - delete


- #### Data Subcription `sub/` `protected`
`model fields:`
```
name: string required
category: string required [da, gc]
is_active: boolean opt
```
`unique_together = ('network', 'name')`
  - **List ['']**
    ```
    request Query String GET
    {
        network: string <product uuid>
    }

    response 200
    {
        "count": 3,
        "next": null,
        "previous": null,
        "results": [
        {
            "id": "ab651525-7464-418b-8e22-d33d5fad9e50",
            "create_date": "2019-12-01T19:30:55.514628Z",
            "modify_date": "2019-12-01T19:30:55.514628Z",
            "mb_per_sub": 10240000,
            "cost_per_sub": 10000,
            "is_active": true,
            "network": {
                "id": "63464d75-dbc4-4307-bc0d-e030bc965768",
                "create_date": "2019-12-01T18:45:13.900083Z",
                "modify_date": "2019-12-01T18:45:13.900083Z",
                "name": "MTN",
                "category": "da",
                "is_active": true
            }
        }
            ...
        ]
    }

    ```
- **Create ['']**
    ```
    request Request Payload POST
    validation; same as model

    response 201
        {
            "id": "ab651525-7464-418b-8e22-d33d5fad9e50",
            "create_date": "2019-12-01T19:30:55.514628Z",
            "modify_date": "2019-12-01T19:30:55.514628Z",
            "mb_per_sub": 10240000,
            "cost_per_sub": 10000,
            "is_active": true,
            "network": {
                "id": "63464d75-dbc4-4307-bc0d-e030bc965768",
                "create_date": "2019-12-01T18:45:13.900083Z",
                "modify_date": "2019-12-01T18:45:13.900083Z",
                "name": "MTN",
                "category": "da",
                "is_active": true
            }
        }

    ```

- **Details Route ['/{id}']**
   - patch
   - put
   - get
   - delete


- #### Data PLan `dataplan/` `protected`
`model fields:`
```
network: string (product uuid)
name: string required
mb: integer required
cost: integer required
```
`unique_together = ('network', 'name')`
  - **List ['']**
    ```
    request Query String GET
    {
        network: string <product uuid>
    }

    response 200
    {
        "count": 3,
        "next": null,
        "previous": null,
        "results": [
        {
            "id": "8afc4887-651d-4c7c-888a-686246fcb4a1",
            "create_date": "2019-12-01T20:39:31.652954Z",
            "modify_date": "2019-12-01T20:39:31.652954Z",
            "name": "1gb",
            "mb": 1024000,
            "cost": 400,
            "is_active": true,
            "network": {
                "id": "63464d75-dbc4-4307-bc0d-e030bc965768",
                "create_date": "2019-12-01T18:45:13.900083Z",
                "modify_date": "2019-12-01T18:45:13.900083Z",
                "name": "MTN",
                "category": "da",
                "is_active": true
            }
        },
            ...
        ]
    }

    ```
- **Create ['']**
    ```
    request Request Payload POST
    validation; same as model

    response 201
        {
            "id": "8afc4887-651d-4c7c-888a-686246fcb4a1",
            "create_date": "2019-12-01T20:39:31.652954Z",
            "modify_date": "2019-12-01T20:39:31.652954Z",
            "name": "1gb",
            "mb": 1024000,
            "cost": 400,
            "is_active": true,
            "network": {
                "id": "63464d75-dbc4-4307-bc0d-e030bc965768",
                "create_date": "2019-12-01T18:45:13.900083Z",
                "modify_date": "2019-12-01T18:45:13.900083Z",
                "name": "MTN",
                "category": "da",
                "is_active": true
            }
        },

    ```

- **Details Route ['/{id}']**
   - patch
   - put
   - get
   - delete


- #### Data Rep Subscription `salesrep-sub/` `protected`
`model fields:`
```
sub: string  required (data sub  uuid)
sales_rep: string  required (sales rep  uuid)
amount: number required (quantity of the sub)
```
  - **List ['']**
    ```
    request Query String GET
    {
        sub: string <data sub uuid>
        sales_rep: string <sales rep uuid>
        create_Date: datetime string
    }

    response 200
    {
        "count": 3,
        "next": null,
        "previous": null,
        "results": [
        {
            "id": "83a0ad5b-1f0f-42da-93c9-ef9429d31289",
            "create_date": "2019-12-02T06:17:30.535854Z",
            "modify_date": "2019-12-02T07:59:52.978501Z",
            "amount": 3,
            "cost": 30000,
            "is_closed": true,
            "sub": "ab651525-7464-418b-8e22-d33d5fad9e50",
            "sales_rep": "d67ae125-0a09-4ef3-8e91-b18eb58aaf38"
        },
            ...
        ]
    }

    ```
- **Create ['']**
    ```
    request Request Payload POST
    validation; same as model

    response 201
    {
        "id": "83a0ad5b-1f0f-42da-93c9-ef9429d31289",
        "create_date": "2019-12-02T06:17:30.535854Z",
        "modify_date": "2019-12-02T07:59:52.978501Z",
        "amount": 3,
        "cost": 30000,
        "is_closed": true,
        "sub": "ab651525-7464-418b-8e22-d33d5fad9e50",
        "sales_rep": "d67ae125-0a09-4ef3-8e91-b18eb58aaf38"
    }

    ```

- **Details Route ['/{id}']** 
   - patch `only for records that are not closed`
   - put `only for records that are not closed`
   - get
   - delete `only for records that are not closed`


- #### Airtime Recieved by data rep `airtime-recieved/` `protected`
`model fields:`
```
sales_rep: string  required (sales rep  uuid)
amount: number required (quantity of the sub)
```
  - **List ['']**
    ```
    request Query String GET
    {
        amount: number
        sales_rep: string <sales rep uuid>
        create_Date: datetime string
        is_closed: boolean
    }

    response 200
    {
        "count": 3,
        "next": null,
        "previous": null,
        "results": [
        {
            "id": "3e69b6de-2d91-4997-b4cb-255ab5182565",
            "create_date": "2019-12-02T09:57:15.584500Z",
            "modify_date": "2019-12-02T10:42:28.053745Z",
            "amount": 80001,
            "is_closed": true,
            "sales_rep": {
                "id": "d67ae125-0a09-4ef3-8e91-b18eb58aaf38",
                "create_date": "2019-12-01T15:15:20.017685Z",
                "modify_date": "2019-12-15T15:10:43.398205Z",
                "name": "sam",
                "category": "da",
                "is_active": true,
                "cash_balance": 0,
                "airtime_balance": 130005,
                "data_balance": 19456000
            }
        },
            ...
        ]
    }

    ```
- **Create ['']**
    ```
    request Request Payload POST
    validation; same as model

    response 201
        {
            "id": "3e69b6de-2d91-4997-b4cb-255ab5182565",
            "create_date": "2019-12-02T09:57:15.584500Z",
            "modify_date": "2019-12-02T10:42:28.053745Z",
            "amount": 80001,
            "is_closed": true,
            "sales_rep": {
                "id": "d67ae125-0a09-4ef3-8e91-b18eb58aaf38",
                "create_date": "2019-12-01T15:15:20.017685Z",
                "modify_date": "2019-12-15T15:10:43.398205Z",
                "name": "sam",
                "category": "da",
                "is_active": true,
                "cash_balance": 0,
                "airtime_balance": 130005,
                "data_balance": 19456000
            }
        },

    ```

- **Details Route ['/{id}']** 
   - patch `only for records that are not closed`
   - put `only for records that are not closed`
   - get
   - delete `only for records that are not closed`



- #### Data sales `datasales/` `protected`
`model fields:`
```
sales_rep: string  required (data sales rep  uuid)
data_plan: string  required (data plan  uuid)
amount: number required (quantity of the sub)
is_direct_sales: boolean (default false)

# auto generate fields
cost: number
total_mb: number
```
  - **List ['']**
    ```
    request Query String GET
        {
            "id": "ceab7d0b-dbe2-4c63-bb73-2bfc19b537fc",
            "create_date": "2019-12-08T10:54:12.911721Z",
            "modify_date": "2019-12-08T10:54:12.911721Z",
            "amount": 5,
            "cost": 2040,
            "total_mb": 10240000,
            "is_direct_sales": false,
            "is_closed": true,
            "data_plan": {
                "id": "e9d1f738-2f8a-44f8-b949-b255b6ee2ab2",
                "create_date": "2019-12-01T20:43:10.185574Z",
                "modify_date": "2019-12-01T20:43:10.185574Z",
                "name": "2gb",
                "mb": 2048000,
                "cost": 408,
                "is_active": true,
                "network": "63464d75-dbc4-4307-bc0d-e030bc965768"
            },
            "sales_rep": {
                "id": "d67ae125-0a09-4ef3-8e91-b18eb58aaf38",
                "create_date": "2019-12-01T15:15:20.017685Z",
                "modify_date": "2019-12-15T15:10:43.398205Z",
                "name": "sam",
                "category": "da",
                "is_active": true,
                "cash_balance": 0,
                "airtime_balance": 130005,
                "data_balance": 19456000
            }
        }

    response 200
    {
        "count": 3,
        "next": null,
        "previous": null,
        "results": [
        {
            "id": "ceab7d0b-dbe2-4c63-bb73-2bfc19b537fc",
            "create_date": "2019-12-08T10:54:12.911721Z",
            "modify_date": "2019-12-08T10:54:12.911721Z",
            "amount": 5,
            "cost": 2040,
            "total_mb": 10240000,
            "is_direct_sales": false,
            "is_closed": true,
            "data_plan": {
                "id": "e9d1f738-2f8a-44f8-b949-b255b6ee2ab2",
                "create_date": "2019-12-01T20:43:10.185574Z",
                "modify_date": "2019-12-01T20:43:10.185574Z",
                "name": "2gb",
                "mb": 2048000,
                "cost": 408,
                "is_active": true,
                "network": "63464d75-dbc4-4307-bc0d-e030bc965768"
            },
            "sales_rep": {
                "id": "d67ae125-0a09-4ef3-8e91-b18eb58aaf38",
                "create_date": "2019-12-01T15:15:20.017685Z",
                "modify_date": "2019-12-15T15:10:43.398205Z",
                "name": "sam",
                "category": "da",
                "is_active": true,
                "cash_balance": 0,
                "airtime_balance": 130005,
                "data_balance": 19456000
            }
        }
            ...
        ]
    }

    ```
- **Create ['']**
    ```
    request Request Payload POST
    validation; same as model

    response 201
    {
        "id": "b00a9279-771b-44f0-8eda-4fffe2312e56",
        "create_date": "2019-12-15T15:07:36.012989Z",
        "modify_date": "2019-12-15T15:07:36.012989Z",
        "amount": 1,
        "cost": 400,
        "total_mb": 1024000,
        "is_direct_sales": false,
        "is_closed": true,
        "data_plan": "8afc4887-651d-4c7c-888a-686246fcb4a1",
        "sales_rep": "d67ae125-0a09-4ef3-8e91-b18eb58aaf38"
    },

    ```

- **Details Route ['/{id}']** 
   - patch `only for records that are not closed`
   - put `only for records that are not closed`
   - get
   - delete `only for records that are not closed`



- #### Dairy Data sales summary `datasales-summary/` `protected`
`model fields:`
```
sales_rep: string  required (data sales rep  uuid)
data_plan: string  required (data plan  uuid)
amount: number required (quantity of the sub)
is_direct_sales: boolean (default false)

# auto generate fields
cost: number
total_mb: number
```
  - **Close Shift  ['/close_shift']**
    ```
    request Payload POST
    {
        actual_airtime: number required
        actual_data_balance: number required
        no_order_treated: number required
        sales_rep: string <sales rep uuid> required
        sales_date: datetime string (default now)
    }

    response 200
    {
        "count": 3,
        "next": null,
        "previous": null,
        "results": [
        {
            "id": "1f80bb81-c1c0-4089-9a6b-5db4b43a5764",
            "create_date": "2019-12-09T13:43:26.757278Z",
            "modify_date": "2019-12-09T13:43:26.757278Z",
            "sales_date": "2019-12-09T13:43:26.720280Z",
            "Start_airtime": "0.00",
            "Start_data": "0.00",
            "total_airtime_recieved": 80004,
            "total_direct_Sales": 0,
            "total_sub_made": 0,
            "expected_airtime": 80004,
            "actual_airtime": 100000,
            "expected_data_balance": -10240000,
            "actual_data_balance": 200,
            "total_data_shared": 10240000,
            "no_order_treated": 5,
            "outstanding": 29996,
            "is_closed": true,
            "sales_rep": {
                "id": "d67ae125-0a09-4ef3-8e91-b18eb58aaf38",
                "create_date": "2019-12-01T15:15:20.017685Z",
                "modify_date": "2019-12-15T15:10:43.398205Z",
                "name": "sam",
                "category": "da",
                "is_active": true,
                "cash_balance": 0,
                "airtime_balance": 130005,
                "data_balance": 19456000
            }
        }
            ...
        ]
    }

    ```
- **Detail ['/${id}']** GET
    ```
    response 200
        {
            "id": "1f80bb81-c1c0-4089-9a6b-5db4b43a5764",
            "create_date": "2019-12-09T13:43:26.757278Z",
            "modify_date": "2019-12-09T13:43:26.757278Z",
            "sales_date": "2019-12-09T13:43:26.720280Z",
            "Start_airtime": "0.00",
            "Start_data": "0.00",
            "total_airtime_recieved": 80004,
            "total_direct_Sales": 0,
            "total_sub_made": 0,
            "expected_airtime": 80004,
            "actual_airtime": 100000,
            "expected_data_balance": -10240000,
            "actual_data_balance": 200,
            "total_data_shared": 10240000,
            "no_order_treated": 5,
            "outstanding": 29996,
            "is_closed": true,
            "sales_rep": {
                "id": "d67ae125-0a09-4ef3-8e91-b18eb58aaf38",
                "create_date": "2019-12-01T15:15:20.017685Z",
                "modify_date": "2019-12-15T15:10:43.398205Z",
                "name": "sam",
                "category": "da",
                "is_active": true,
                "cash_balance": 0,
                "airtime_balance": 130005,
                "data_balance": 19456000
            }
        }

    ```


- #### Cash Recieved `cash-recieved/` `protected`
`model fields:`
```
sales_rep: string (Gift card sales rep uuid)
amount: positive integer required
```
  - **List ['']**
    ```
    request Query String GET
    {
        sales_rep: string <Gift card sales rep uuid>,
        amount: number
    }

    response 200
    {
        "count": 3,
        "next": null,
        "previous": null,
        "results": [
        {
            "id": "a769325a-db22-430e-8ff5-acabb7132a8c",
            "create_date": "2019-12-10T21:17:54.288711Z",
            "modify_date": "2019-12-10T21:17:54.288711Z",
            "amount": 13,
            "is_closed": true,
            "sales_rep": {
                "id": "f8ada025-4776-40af-984d-e8f71c669e3e",
                "create_date": "2019-12-10T21:17:37.528646Z",
                "modify_date": "2020-01-04T15:23:27.121695Z",
                "name": "me",
                "category": "gc",
                "is_active": true,
                "cash_balance": -14731,
                "airtime_balance": 0,
                "data_balance": 0
            }
        }
            ...
        ]
    }

    ```
- **Create ['']**
    ```
    request Request Payload POST
    validation; same as model

    response 201
        {
            "id": "a769325a-db22-430e-8ff5-acabb7132a8c",
            "create_date": "2019-12-10T21:17:54.288711Z",
            "modify_date": "2019-12-10T21:17:54.288711Z",
            "amount": 13,
            "is_closed": true,
            "sales_rep": {
                "id": "f8ada025-4776-40af-984d-e8f71c669e3e",
                "create_date": "2019-12-10T21:17:37.528646Z",
                "modify_date": "2020-01-04T15:23:27.121695Z",
                "name": "me",
                "category": "gc",
                "is_active": true,
                "cash_balance": -14731,
                "airtime_balance": 0,
                "data_balance": 0
            }
        }

    ```

- **Details Route ['/{id}']**
   - patch
   - put
   - get
   - delete


- #### Trade `trade/` `protected`
`model fields:`
```
sales_rep: string (Gift card sales rep uuid)
group: string <group where card was loaded> required
card: string (uuid from giftcard product)
selling_rate: positive decimal (the selling rate in Yaun)
buying_rate: positive decimal (the buying rate in Naira)
amount: positive integer (the worth of the gift cards)
amount_paid: auto generated (amount in Naira paid to customer)
```
  - **List ['']**
    ```
    request Query String GET
    {
        sales_rep: string <data sales rep uuid>,
        amount: number.
        create_date,
        group,
        card: uuid for the giftcard product
    }

    response 200
    {
        "count": 3,
        "next": null,
        "previous": null,
        "results": [
        {
            "id": "39cbf6a6-c450-45a1-b952-546a3d08bf5c",
            "create_date": "2019-12-10T21:57:15.123295Z",
            "modify_date": "2019-12-10T21:57:15.123295Z",
            "group": "g[1",
            "selling_rate": 5,
            "buying_rate": 9,
            "amount": 6,
            "amount_paid": 54,
            "is_closed": true,
            "sales_rep": {
                "id": "f8ada025-4776-40af-984d-e8f71c669e3e",
                "create_date": "2019-12-10T21:17:37.528646Z",
                "modify_date": "2020-01-04T15:23:27.121695Z",
                "name": "me",
                "category": "gc",
                "is_active": true,
                "cash_balance": -14731,
                "airtime_balance": 0,
                "data_balance": 0
            },
            "card": {
                "id": "94813d97-ecf8-4b69-b34c-c44fbedbffdd",
                "create_date": "2019-12-10T21:47:44.612727Z",
                "modify_date": "2019-12-10T21:47:44.612727Z",
                "name": "US itunes",
                "category": "gc",
                "is_active": true
            }
        },
            ...
        ]
    }

    ```
- **Create ['']**
    ```
    request Request Payload POST
    validation; same as model

    response 201
        {
            "id": "39cbf6a6-c450-45a1-b952-546a3d08bf5c",
            "create_date": "2019-12-10T21:57:15.123295Z",
            "modify_date": "2019-12-10T21:57:15.123295Z",
            "group": "g[1",
            "selling_rate": 5,
            "buying_rate": 9,
            "amount": 6,
            "amount_paid": 54,
            "is_closed": true,
            "sales_rep": {
                "id": "f8ada025-4776-40af-984d-e8f71c669e3e",
                "create_date": "2019-12-10T21:17:37.528646Z",
                "modify_date": "2020-01-04T15:23:27.121695Z",
                "name": "me",
                "category": "gc",
                "is_active": true,
                "cash_balance": -14731,
                "airtime_balance": 0,
                "data_balance": 0
            },
            "card": {
                "id": "94813d97-ecf8-4b69-b34c-c44fbedbffdd",
                "create_date": "2019-12-10T21:47:44.612727Z",
                "modify_date": "2019-12-10T21:47:44.612727Z",
                "name": "US itunes",
                "category": "gc",
                "is_active": true
            }
        },

    ```

- **Details Route ['/{id}']**
   - patch
   - put
   - get
   - delete


- #### Trade summary `trade-summary/` `protected`
`model fields:`
```
sales_rep: string  required (gift card sales rep  uuid)

# auto generate fields
total_cash_recieved: number
total_cash_used: number
balance: number
```
  - **Close Shift  ['/close_shift']**
    ```
    request Payload POST
    {
        sales_rep: string <sales rep uuid> required
    }

    response 200
    {
        "count": 3,
        "next": null,
        "previous": null,
        "results": [
        {
            "id": "86bc3807-6518-4ce8-b2b1-8170f6b54201",
            "create_date": "2019-12-10T22:46:31.635974Z",
            "modify_date": "2019-12-10T22:46:31.635974Z",
            "total_cash_recieved": 1313,
            "total_cash_used": 16054,
            "balance": -14731,
            "is_closed": true,
            "sales_rep": {
                "id": "f8ada025-4776-40af-984d-e8f71c669e3e",
                "create_date": "2019-12-10T21:17:37.528646Z",
                "modify_date": "2020-01-04T15:23:27.121695Z",
                "name": "me",
                "category": "gc",
                "is_active": true,
                "cash_balance": -14731,
                "airtime_balance": 0,
                "data_balance": 0
            }
        }
            ...
        ]
    }

    ```
- **Detail ['/${id}']** GET
    ```
        {
            "id": "86bc3807-6518-4ce8-b2b1-8170f6b54201",
            "create_date": "2019-12-10T22:46:31.635974Z",
            "modify_date": "2019-12-10T22:46:31.635974Z",
            "total_cash_recieved": 1313,
            "total_cash_used": 16054,
            "balance": -14731,
            "is_closed": true,
            "sales_rep": {
                "id": "f8ada025-4776-40af-984d-e8f71c669e3e",
                "create_date": "2019-12-10T21:17:37.528646Z",
                "modify_date": "2020-01-04T15:23:27.121695Z",
                "name": "me",
                "category": "gc",
                "is_active": true,
                "cash_balance": -14731,
                "airtime_balance": 0,
                "data_balance": 0
            }
        }

    ```
