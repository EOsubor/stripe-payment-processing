import os
import stripe
from flask import Flask, jsonify, request

app = Flask(__name__)

stripe.api_key = os.environ.get('STRIPE_API_KEY')

@app.route('/charge', methods=['POST'])
def charge():
    """
    Process a payment through Stripe

    Returns:
        json: A JSON object with a message indicating payment was processed successfully
        or an error message if payment failed
    """
    try:
        amount = int(request.form['amount'])
        currency = request.form['currency']
        description = request.form['description']
        token = request.form['token']

        if amount <= 0:
            raise ValueError('Amount must be greater than zero')

        charge = stripe.Charge.create(
            amount=amount,
            currency=currency,
            description=description,
            source=token
        )

        return jsonify({'message': 'Payment processed successfully'}), 200

    except (KeyError, ValueError) as e:
        error_message = str(e)
        return jsonify({'error': error_message}), 400

    except stripe.error.StripeError as e:
        app.logger.error(f'Stripe error: {str(e)}')
        return jsonify({'error': 'Payment failed'}), 500

if __name__ == '__main__':
    app.run(debug=True)
