# Python SSR Autumn Starter Template

[Autumn](https://useautumn.com) is an open-source layer between Stripe and your application, allowing you to create any pricing model and embed it with a few lines of code.

This template demonstrates how you can set up pricing for a simple AI chatbot application using a Python Backend.

View the example app here: https://nextjs-autumn-template.vercel.app/

## Getting Started

1. Clone the repository:

```bash
git clone https://github.com/useautumn/react-python-autumn-template.git

# Backend
uv add . --dev
```

> [!NOTE]
> Python 3.9+ is required.


2. Create an account at [app.useautumn.com](https://app.useautumn.com)

3. Get your Autumn secret key from the [sandbox environment](https://app.useautumn.com/sandbox/dev) and add it to your environment variables:

```bash
export AUTUMN_SECRET_KEY=am_sk_test_OAFUOL0meFCjpMMmFeU13gHnrEOGAHWp2YTLECyY7k
```
*or add it to a `.env` file.*

1. Connect your Stripe account in the [integrations page](https://app.useautumn.com/sandbox/integrations/stripe)

2. Run the backend server:

```bash
uv run --env-file=.env uvicorn app:app --port 8000
```

## Understanding the Implementation

This template implements a simple AI chat message app where users can:

- Send messages (with usage limits)
- Upgrade to a pro or ultra plan
- View their usage and subscription details

<!-- ### Additional Features

The template also includes `getOrCreateCustomer` to fetch customer details, entitlements, and subscription status, which is used in the customer details card in the UI:

```typescript
const customer = await getOrCreateCustomer(CUSTOMER_ID);
// Returns: customer details, product subscriptions, and feature entitlements
``` -->

## Learn More

- [Autumn Documentation](https://docs.useautumn.com)
- [React Router Documentation](https://reactrouter.com/docs)
- [Autumn JS](https://github.com/useautumn/autumn-js)
- [Autumn Py](https://github.com/useautumn/autumn-py)