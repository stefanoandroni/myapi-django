<h1> Overview </h1>
<a href="https://www.djangoproject.com/" target="_blank">
    <img src="https://static.djangoproject.com/img/logos/django-logo-positive.svg" alt="django" height="50"/>
</a> &nbsp;&nbsp;&nbsp;&nbsp;
<a href="https://www.django-rest-framework.org/" target="_blank">
  <img src="https://www.django-rest-framework.org/img/logo.png" href="https://www.django-rest-framework.org/" alt="django-rest-framework" height="50"/>
</a> &nbsp;&nbsp;&nbsp;&nbsp;
<a href="https://requests.readthedocs.io/" target="_blank">
  <img src="https://requests.readthedocs.io/en/latest/_static/requests-sidebar.png" href="https://requests.readthedocs.io/" alt="requests" height="50"/>
</a>

<p>A simple articles HTTP api built with <b>django + django rest framework</b> (+ requests for client examples).</p>

<h1>Installation</h1>
<ol type="1">
  <li> Clone git repository </li>
  <pre><code>$ git clone https://github.com/stefanoandroni/myapi-django </code></pre>
  <li> <em>(Optional)</em> Create a Python virual environment and activate it (py version in <em>runtime.txt</em>)</li>
  <li>Install requirements</li>
  <pre><code>$ cd myapi-django</code></pre>
  <pre><code>$ pip install -r requirements.txt</code></pre>
  <li>Change directory to myapi</li>
  <pre><code>$ cd src\myapi</code></pre>
  <li>Make migrations and migrate</li>
  <pre><code>$ py manage.py makemigrations</code></pre><pre><code>$ py manage.py migrate</code></pre>
  <li>Run server</li>
  <pre><code>$ py manage.py runserver</code></pre>
</ol>

<h1>API</h1>

<h2>Edpoints</h2>
<p>CRUD views (and endpoints) kept separate for learning purposes.</p>
<br>
<table>
<tbody>
  <tr>
    <td>api/</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td>auth/</td>
    <td></td>
    <td>POST</td>
    <td>authentication</td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td>register/</td>
    <td>POST</td>
    <td>registration</td>
  </tr>
  <tr>
    <td></td>
    <td>articles/</td>
    <td></td>
    <td>GET</td>
    <td>articles list</td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td>create/</td>
    <td>POST</td>
    <td>create article</td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td>&lt;slug:article_slug&gt;/update/</td>
    <td>PUT</td>
    <td>update article</td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td>&lt;slug:article_slug&gt;/delete/</td>
    <td>DELETE</td>
    <td>delete article</td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td>&lt;slug:article_slug&gt;/</td>
    <td>GET</td>
    <td>article detail</td>
  </tr>
  <tr>
    <td></td>
    <td>comments/</td>
    <td></td>
    <td>GET</td>
    <td>all comments list</td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td>&lt;int:id&gt;/delete/</td>
    <td>DELETE</td>
    <td>delete comment</td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td>&lt;int:id&gt;/update</td>
    <td>PUT</td>
    <td>update comment</td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td>&lt;int:id&gt;/</td>
    <td>GET</td>
    <td>comment detail</td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td>&lt;slug:article_slug&gt;/create/</td>
    <td>POST</td>
    <td>comment create</td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td>&lt;slug:article_slug&gt;/</td>
    <td>GET</td>
    <td>article comments list</td>
  </tr>
  <tr>
    <td></td>
    <td>search/</td>
    <td>?q=QUERY&amp;topic=TOPIC&amp;author=AUTHOR</td>
    <td>GET</td>
    <td>search</td>
  </tr>
</tbody>
</table>

<h2>Authentication and Permission </h2>
<h3>DEFAULT_AUTHENTICATION_CLASSES</h3>
<ul>
<li>rest_framework.authentication.SessionAuthentication</li>
<li>api.authentication.TokenAuthentication</li>
<em><b>Example</b> Token Authentication example in src\client\utils.py</em>
</ul>
<h3>DEFAULT_PERMISSION_CLASSES</h3>
<ul>
<li>rest_framework.permissions.IsAuthenticated</li>
<em><b>Note</b> Accessing any API endpoint requires authentication</em>
</ul>
<h3>Custom Permission</h3>
Custom permissions have been implemented for CRUD operations (articles and comments).

<h1>Client Examples</h1>

Client examples in src\client.
<pre><code>$ cd src\client</code></pre>
<pre><code>$ py file_name.py</code></pre>

<h1> TODO </h1>
<ul>
<li>implement Users CRUD</li>
</ul>