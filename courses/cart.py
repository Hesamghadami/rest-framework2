from .models import Course
class Cart:
    def __init__(self, request):
        """
        Construct a Cart
        """
        self.request = request
        self.session = request.session
        cart = self.session.get('cart')
        if cart is None:
            cart = self.session['cart'] = {}
        self.cart = cart

    def save(self):
        """
        Update the Cart
        """
        self.session.modified = True

    def add_to_cart_some_quantity(self, product, quantity=1):
        """"
        Add a product to the Cart over than 1
        """
        if str(product.id) not in self.cart:
            self.cart[str(product.id)] = {'quantity': quantity}

        else:
            self.cart[str(product.id)]['quantity'] += quantity
        

        self.save()

    def add_to_cart_one_quantity(self, product):
        """"
        Add a product to the Cart just one quantity
        """

        if str(product.id) not in self.cart:
            self.cart[str(product.id)] = {'quantity': 1}

        self.save()

    def delete_from_cart(self,product):
        """
        Delete a product from the
        """

        if str(product.id) in self.cart:
            del self.cart[str(product.id)]
            self.save()

    def __iter__(self):
        """
        Iterate over all products
        """
        product_ids = self.cart.keys()
        products = Course.objects.filter(id__in=product_ids)
        cart = self.cart.copy()#generator empty list . use copy for keep base cart
        for product in products:
            cart[str(product.id)]['product_object'] = product

        for item in cart.values():
            yield item

    def __len__(self):
        """
        Returns the lenght of cart objects
        """
        return len(self.cart.keys())
    
    def clear(self):
        """
        Clear all products
        """
        del self.session['cart']
        self.save()

    def get_total_price_one_quantity(self):
        """
        Calculate total price if quantity for all products is one
        """
        product_ids = self.cart.keys()
        products = Course.objects.filter(id__in=product_ids)
        return sum(product.price for product in products)

    def get_total_price_some_quantity(self):
        """
        Calculate total price if quantity for all products is one
        """
        product_quantity = list(self.cart.values())
        all_quantity = [i['quantity'] for i in product_quantity]
        product_id = list(self.cart.keys())
        products = Course.objects.filter(id__in=product_id)
        price_list = [product.price for product in products]
        return (sum(price_list[i]*all_quantity[i] for i in range(len(all_quantity))))

