from django import template


register = template.Library()


@register.filter
def highlight_current(value):

	if value == 'app/contacts.html':
		return '''
		  <nav class="row">
			<div class="nav-wrapper col s12">
			  <a href="{% url 'home' %}" class="brand-logo">
			  Компьютеры</a>
			  <ul class="right hide-on-med-and-down">
				<li><a href="{% url 'examples' %}">Примеры</a></li>
				<li class="active"><a href="{% url 'contacts' %}">Контакты</a></li>
				<li><a href="{% url 'about' %}">О проекте</a></li>
			  </ul>
			</div>
		  </nav>
		'''
	elif value == 'app/about.html':
		return '''
		  <nav class="row">
			<div class="nav-wrapper col s12">
			  <a href="{% url 'home' %}" class="brand-logo">
			  Компьютеры</a>
			  <ul class="right hide-on-med-and-down">
				<li><a href="{% url 'examples' %}">Примеры</a></li>
				<li><a href="{% url 'contacts' %}">Контакты</a></li>
				<li class="active"><a href="{% url 'about' %}">О проекте</a></li>
			  </ul>
			</div>
		  </nav>
		'''
	elif value == 'app/examples.html':
		return '''
		  <nav class="row">
			<div class="nav-wrapper col s12">
			  <a href="{% url 'home' %}" class="brand-logo">
			  Компьютеры</a>
			  <ul class="right hide-on-med-and-down">
				<li class="active"><a href="{% url 'examples' %}">Примеры</a></li>
				<li><a href="{% url 'contacts' %}">Контакты</a></li>
				<li><a href="{% url 'about' %}">О проекте</a></li>
			  </ul>
			</div>
		  </nav>
				'''
	elif value == 'app/home.html':
		return '''
		  <nav class="row">
			<div class="nav-wrapper col s12">
			  <a href="{% url 'home' %}" class="brand-logo">
			  Компьютеры</a>
			  <ul class="right hide-on-med-and-down">
				<li><a href="{% url 'examples' %}">Примеры</a></li>
				<li><a href="{% url 'contacts' %}">Контакты</a></li>
				<li><a href="{% url 'about' %}">О проекте</a></li>
			  </ul>
			</div>
		  </nav>
		'''