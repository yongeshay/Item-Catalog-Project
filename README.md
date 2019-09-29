---


---

<h1 id="project-overview">Project Overview</h1>
<p>In this project I developed an application that provides a list of items within a variety of categories as well as provide a user registration and authentication system. Registered users have the ability to post, edit and delete their own items.</p>
<h2 id="why-this-project">Why This Project?</h2>
<p>Modern web applications perform a variety of functions and provide amazing features and utilities to their users; but deep down, it’s really all just creating, reading, updating and deleting data. In this project, I combine my knowledge of building dynamic websites with persistent data storage to create a web application that provides a compelling service to users.</p>
<h2 id="what-have-i-learnt">What Have I Learnt?</h2>
<p>I have learnt how to develop a RESTful web application using the Python framework Flask along with implementing third-party OAuth authentication. I then learnt when to properly use the various available HTTP methods and how these methods relate to CRUD (create, read, update and delete) operations.</p>
<h2 id="how-does-this-help-my-career">How Does This Help My Career?</h2>
<ul>
<li>Efficiently interacting with data is the backbone upon which performant web applications are built</li>
<li>Properly implementing authentication mechanisms and appropriately mapping HTTP methods to CRUD operations are core features of a properly secured web application</li>
</ul>
<h2 id="how-to-run-this-project">How To Run This Project</h2>
<p>Here’s what you should do:</p>
<ol>
<li>Install Vagrant and VirtualBox</li>
<li>Clone this GitHub repo</li>
<li>Launch the Vagrant VM <code>vagrant up</code></li>
<li>Unzip and place this application locally in the vagrant/catalog directory (which will automatically be synced to /vagrant/catalog within the VM).</li>
<li>Login into the Vagrant VM <code>vagrant ssh</code></li>
<li>Change directory in the Vagrant VM <code>cd /vagrant</code></li>
<li>Initialize the database with the VM <code>python database_setup.py</code></li>
<li>Populate the database with the VM <code>python db_populator.py</code></li>
<li>Run this application within the VM <code>python application.py</code></li>
<li>Access and test your application by visiting  <a href="http://localhost:8000/">http://localhost:8000</a>  locally</li>
</ol>
<p>You can find the link to the fullstack-nanodegree-vm  <a href="http://github.com/udacity/fullstack-nanodegree-vm">here</a>.</p>

