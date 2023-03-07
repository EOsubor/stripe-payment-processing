# Payment Processing with Stripe and Flask

This is a simple Flask application that demonstrates how to process payments using Stripe's API.

### Getting Started

1. Clone this repository:

```
git clone https://github.com/your_username/stripe-payment-processing.git
```

2. Install the requirements:

```
pip install -r requirements.txt
```

3. Set up environment variables for Stripe API key:

```
export STRIPE_API_KEY=<your_stripe_api_key>
```

4. Run the app:

```
python app.py
```

5. Send a POST request to `/charge` with the following data:

```
amount=1000
currency=usd
description=Test payment
token=<stripe_token>
```

Verify that the payment was successful by checking the Stripe dashboard.


### Code Structure

The code consists of a single Flask app (`app.py`) with a single route (`/charge`). The route expects a POST request with the following parameters:

`amount`: The amount to charge in cents.
`currency`: The currency of the payment (e.g. `usd`).
`description`: A description of the payment.
`token`: A Stripe token representing the payment source (e.g. a credit card).

If the payment is successful, the route returns a JSON response with the message "Payment processed successfully". If the payment fails, the route returns a JSON response with an error message.

The Stripe API key is loaded from an environment variable (`STRIPE_API_KEY`) to keep it secure.


### Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.


### License

[MIT](https://choosealicense.com/licenses/mit/)
