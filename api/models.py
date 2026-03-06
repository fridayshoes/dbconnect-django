from django.db import models

# The Department model represents a department inside an organisation.
# Each attribute becomes a column in the database table.

class Department(models.Model):
    # AutoField creates an automatically incrementing integer primary key.
    # Setting primary_key=True makes this the table's unique identifier.
    dept_id = models.AutoField(primary_key=True)

    # CharField stores short text. max_length is required.
    dept_name = models.CharField(max_length=100)

    # Location of the department (e.g., "London", "HQ", "Building A").
    location = models.CharField(max_length=100)

    # Name of the person who leads the department.
    head_of_department = models.CharField(max_length=100)

    # __str__ controls how the object appears in Django admin and shell.
    # Returning the department name makes it easy to read.
    def __str__(self):
        return self.dept_name