from django.shortcuts import get_object_or_404
from paypal.standard.models import ST_PP_COMPLETED
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
import weasyprint
from io import BytesIO
from paypal.standard.ipn.signals import valid_ipn_received
from orders.models import Order

def payment_notification(sender, **kwargs):
	ipn_obj = sender
	if ipn_obj.payment_status == ST_PP_COMPLETED:
		order = get_object_or_404(Order, id=ipn_obj.invoice)

		order.paid = True
		order.save()

		subject = 'My Shop - Invoice nr. {}'.format(order.id)
		message = 'Please, find attached the invoice for your recent purchase.'
		email = EmailMessage(subject, message, 'sistemamonitoria@gmail.com', [order.email])

		html = render_to_string('orders/order/pdf.html', {'order': order})
		out = BytesIO()
		stylesheets = [weasyprint.CSS(settings.STATIC_ROOT + 'css/pdf.css')]
		weasyprint.HTML(string=html).write_pdf(out, stylesheets=stylesheets)

		email.attach('order_{}.pdf'.format(order.id), out.getvalue(), 'application/pdf')
		email.send()


valid_ipn_received.connect(payment_notification)