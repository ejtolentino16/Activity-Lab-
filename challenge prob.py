
weight = float(input("Weight (lbs): "))
destination = input("Destination (domestic/international): ").lower()
membership = input("Membership (standard/premium): ").lower()

base_shipping_cost = 20
total_cost = base_shipping_cost

if weight > 30:
    total_cost += 10

is_premium = membership == "premium"
is_international = destination == "international"

if is_international and not is_premium:
    total_cost *= 2

if is_premium:
    discount = 0.2 * total_cost
    total_cost -= discount

print(f"Final Shipping Cost: ${total_cost:.2f}")

details = f"(Details: Base ${base_shipping_cost}"
if weight > 30:
    details += " + Overweight $5"
if is_premium:
    details += f", Premium 20% discount applied"
if is_international and not is_premium:
    details += ", International fee applied"
details += ")"

print(details)
