from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Emp
from .forms import Empform
from django.contrib import messages
from django.core.exceptions import ValidationError
from django .core.paginator import Paginator
# Create your views here.

def index(request):
    employees_=Emp.objects.order_by("-id")
    department=request.GET.get('department')
    role=request.GET.get('role')
    employees_=Emp.objects.all()
    # Apply filters if search parameters are provided
    if department:
        employees_ = employees_.filter(department__icontains=department)
    if role:
        employees_ = employees_.filter(role__icontains=role)

    #Paginator
    paginator=Paginator(employees_,10)
    page=request.GET.get('page')
    employees_=paginator.get_page(page)    
    
    return render(request,"employees/index.html",{'employees_':employees_})

def add(request):
    if request.method == "POST":
        try:
            # Extract data from POST request
            Name = request.POST.get('name')
            Email = request.POST.get('email')
            Department = request.POST.get('department')
            Role = request.POST.get('role')

            # Validate required fields
            if not Name or not Email or not Department or not Role:
                messages.error(request, 'Missing required fields.')
                return redirect('Employees:add')  # Redirect back to the form page

            # Create and save employee in the database
            Emp_info = Emp.objects.create(
                name=Name,
                email=Email,
                department=Department,
                role=Role
            )
            Emp_info.save()

            # Add success message and redirect
            messages.success(request, 'Employee successfully created!')
            return redirect('Employees:index')

        except ValidationError as e:
            # Handle validation errors
            messages.error(request, f'Validation error: {str(e)}')
            return redirect('Employees:add')  # Redirect back to the form page

    return render(request, "employees/createform.html")

def update(request,emp_id):
    employee_ = get_object_or_404(Emp, id=emp_id)
    
    if request.method == "POST":
        # Initialize the form with POST data, bound to the client instance
        form = Empform(request.POST, instance=employee_)
        print(f"Form data: {request.POST}")  # Debugging POST data
        if form.is_valid():
            # Save the form and update the client instance
            form.save()
            return redirect("Employees:index")
        else:
            print("Form is not valid.", form.errors)  # Debugging form errors
    else:
        # If GET request, display the form with current client data
        form = Empform(instance=employee_)
    
    # Render the form template with the form context
    return render(request, "employees/editform.html", {"form": form, "employee_": employee_})


def read(request,emp_id):
    if request.method == "POST":
        employee_ = Emp.objects.get(id=emp_id)
        form = Empform(request.POST, instance=employee_)
        if form.is_valid():
            form.save()
        return redirect("Employees:index")
    else:
        employee_ = Emp.objects.get(id=emp_id)
        form = Empform(instance=employee_)

    return render(request, "employees/viewform.html", {"form": form, "employee_": employee_})

def delete(request,emp_id):
    employee_ = get_object_or_404(Emp, id=emp_id) 
    if request.method == 'POST':
       employee_.delete()
       return redirect("Employees:index")
    return render(request,"employees/deleteform.html",{"employee_":employee_})
       

