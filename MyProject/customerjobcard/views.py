from django.shortcuts import render, redirect, get_object_or_404
from .models import JobCard
from .forms import JobCardForm
# Create your views here.

# Read
def jobcard_list(request):
    jobcards = JobCard.objects.all().select_related('PropertieID', 'CustomerID', 'RoleID', 'RegionID')
    return render(request, 'customerjobcard/jobcard_list.html', {'jobcards': jobcards})

# CREATE
def create_jobcard(request):
    if request.method == 'POST':
        form = JobCardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('jobcard_list')
    else:
        form = JobCardForm()
    return render(request, 'customerjobcard/jobcard_form.html', {'form': form, 'title': 'Create JobCard'})

# UPDATE
def update_jobcard(request, pk):
    jobcard = get_object_or_404(JobCard, pk=pk)
    if request.method == 'POST':
        form = JobCardForm(request.POST, instance=jobcard)
        if form.is_valid():
            form.save()
            return redirect('jobcard_list')
    else:
        form = JobCardForm(instance=jobcard)
    return render(request, 'customerjobcard/jobcard_form.html', {'form': form, 'title': 'Update JobCard'})


# DELETE
def delete_jobcard(request, pk):
    jobcard = get_object_or_404(JobCard, pk=pk)
    if request.method == 'POST':
        jobcard.delete()
        return redirect('jobcard_list')
    return render(request, 'customerjobcard/jobcard_confirm_delete.html')


