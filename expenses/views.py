from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum
from .models import Expense


def expense_list(request):
    expenses = Expense.objects.all().order_by("-date")

    if request.method == "POST":
        title = request.POST.get("title")
        amount = request.POST.get("amount")
        category = request.POST.get("category")
        date = request.POST.get("date")
        description = request.POST.get("description")

        Expense.objects.create(
            title=title,
            amount=amount,
            category=category,
            date=date,
            description=description
        )

        return redirect("expense_list")
    
    total_expenses = Expense.objects.aggregate(
        total=Sum("amount")
    )["total"] or 0

    expense_count = Expense.objects.count()

    return render(
        request,
        "expenses/expense_list.html",
        {
            "expenses": expenses,
            "total_expenses": total_expenses,
            "expense_count": expense_count
        }
    )

def edit_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id)

    if request.method == "POST":
        expense.title = request.POST.get("title")
        expense.amount = request.POST.get("amount")
        expense.category = request.POST.get("category")
        expense.date = request.POST.get("date")
        expense.description = request.POST.get("description")

        expense.save()

        return redirect("expense_list")

    return render(
        request,
        "expenses/edit_expense.html",
        {"expense": expense}
    )



def delete_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id)

    if request.method == "POST":
        expense.delete()
        return redirect("expense_list")

    return render(
        request,
        "expenses/delete_expense.html",
        {"expense": expense}
    )