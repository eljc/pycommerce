# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
import stripe
stripe.api_key = "sk_test_Ho24N7La5CVDtbmpjc377lJI"

stripe.PaymentIntent.create(amount=500, currency="gbp", payment_method="pm_card_visa")