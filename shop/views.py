from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Cart, CartItem
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.conf import settings
from openai import OpenAI

client = OpenAI(api_key=settings.OPENAI_API_KEY)

def product_list(request):
    products = Product.objects.all()
    return render(request, "shop/product_list.html", {"products": products})

def product_details(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, "shop/product_details.html", {"product": product})

@login_required
def cart(request):
    cart = request.user.cart
    items = cart.items.all()
    total = cart.total_price()

    return render(request, "shop/cart.html", {"cart": cart, "items": items, "total": total})

@login_required
def add_to_cart(request, slug):
    product = get_object_or_404(Product, slug=slug)
    cart = request.user.cart
    
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product, defaults={"quantity": 1})

    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    return redirect("product_details", slug=product.slug)

@login_required
def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, cart=request.user.cart)
    item.delete()
    
    return redirect("cart")

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("product_list")
    else:
        form = UserCreationForm()

    return render(request, "registration/signup.html", {"form": form})

@login_required
def ai_recipe(request):
    cart = request.user.cart
    items = cart.items.all()

    # Build a comma-separated list: "Apples (2), Bananas (1), Bread (1)"
    item_list = ", ".join([f"{item.product.name} ({item.quantity})" for item in items])

    # The prompt you send to GPT
    prompt = f"""
    Here is the list of items in a user's shopping cart:

    {item_list}

    Suggest a few meal ideas or recipes the user could make with these items.
    Make it friendly, helpful, and short (1-2 sentences).
    """

    # Call OpenAI GPT-4o Mini
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    ai_text = response.choices[0].message.content

    return render(request, "shop/cart.html", {
        "cart": cart,
        "items": items,
        "total": cart.total_price(),
        "ai_response": ai_text,
    })