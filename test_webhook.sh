#!/usr/bin/env bash
curl -H "Content-Type: application/json" -X POST -d '{
  "created": 1326853478,
  "livemode": false,
  "id": "evt_17GnWlEUTFmWlhCT1p9nkyvv",
  "type": "invoice.payment_succeeded",
  "object": "event",
  "request": null,
  "pending_webhooks": 1,
  "api_version": "2015-07-28",
  "data": {
    "object": {
      "date": 1416423390,
      "id": "in_00000000000000",
      "period_start": 1416423390,
      "period_end": 1416423390,
      "lines": {
        "data": [
          {
            "id": "sub_6lnNWRmcL4VemY",
            "object": "line_item",
            "type": "subscription",
            "livemode": true,
            "amount": 999,
            "currency": "gbp",
            "proration": false,
            "period": {
              "start": 1441889624,
              "end": 1444481624
            },
            "subscription": null,
            "quantity": 1,
            "plan": {
              "interval": "month",
              "name": "Monthly Subscription",
              "created": 1439209438,
              "amount": 999,
              "currency": "gbp",
              "id": "REG_MONTHLY",
              "object": "plan",
              "livemode": false,
              "interval_count": 1,
              "trial_period_days": null,
              "metadata": {},
              "statement_descriptor": "Monthly Subscription"
            },
            "description": null,
            "discountable": true,
            "metadata": {}
          }
        ],
        "total_count": 1,
        "object": "list",
        "url": "/v1/invoices/in_150dcw2mCJVDQcrEZCuOB251/lines"
      },
      "subtotal": 988,
      "total": 988,
      "customer": "cus_7VpBHcejAlItVy",
      "object": "invoice",
      "attempted": true,
      "closed": true,
      "forgiven": false,
      "paid": true,
      "livemode": false,
      "attempt_count": 1,
      "amount_due": 988,
      "currency": "gbp",
      "starting_balance": 0,
      "ending_balance": 0,
      "next_payment_attempt": null,
      "webhooks_delivered_at": 1416423390,
      "charge": "_00000000000000",
      "discount": null,
      "application_fee": null,
      "subscription": "sub_00000000000000",
      "tax_percent": null,
      "tax": null,
      "metadata": {},
      "statement_descriptor": null,
      "description": null,
      "receipt_number": null
    }
  }
}' http://localhost:8000/accounts/subscriptions/
