from django.shortcuts import render, redirect
from .models import Tech, Company, Entry
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import time


def index(request):
    context = {
        'languages': Tech.objects.filter(category='languages').order_by('name'),
        'databases': Tech.objects.filter(category='databases').order_by('name'),
        'frameworks': Tech.objects.filter(category='frameworks').order_by('name'),
        'libraries': Tech.objects.filter(category='libraries').order_by('name'),
        'services': Tech.objects.filter(category='services').order_by('name'),
    }

    # Create M2M relationship between tech and company for each data point
    # entries = Entry.objects.all()
    # for entry in entries:
    #     try:
    #         tech = Tech.objects.get(name=entry.tech)
    #         company = Company.objects.get(name=entry.company)
    #         tech.companies_using.add(company)
    #     except Exception as e:
    #         print(f"An error occurred while processing: {str(e)}")
    
    # company = Company.objects.get(id=6)
    # for tech in company.technologies.all():
    #     print(tech)
    
    
    return render(request, 'selection.html', context)



def results(request):
    forum = request.POST.copy()
    del forum['csrfmiddlewaretoken']
    if not forum:
        return redirect('/')
    
    # Sort searched technologies into correct search_boxes index
    search_boxes = [[],[],[],[],[]]
    for tech_name, box_position in forum.items():
        for i in range(len(search_boxes)):
            if i == int(box_position):
                search_boxes[i].append(tech_name)

    # Get companies for all technologies in each search_box and add to company set with corresponding index
    company_sets = []
    for search_box in search_boxes:
        companies_using_tech = []
        for tech_name in search_box:
            tech = Tech.objects.get(name=tech_name)
            companies = tech.companies_using.all()
            for company in companies:
                if company not in companies_using_tech:
                    companies_using_tech.append(company)
        if companies_using_tech:
            company_sets.append(set(companies_using_tech))
    
    # Filter out any company that doesnt appear in all company_sets
    filtered_companies = company_sets[0]
    for company_set in company_sets:
        filtered_companies = filtered_companies.intersection(company_set)
    filtered_companies = list(filtered_companies)

    # Convert Company objects to dictionaries
    serialized_companies = []
    for company in filtered_companies:
        serialized_company = {
            'id': company.id,
            'entity': company.entity,
            'name': company.name,
            'url':company.url,
            'logourl':company.logourl
        }
        serialized_companies.append(serialized_company)

    request.session['companies'] = serialized_companies

    # Create a boolean-search string to display
    search_string = ''
    seperator_or = ' OR '
    for search_box in search_boxes:
        if search_box:
            if not search_string:
                search_string = '(' + seperator_or.join(search_box) + ')'
            else:
                search_string = search_string + ' AND (' + seperator_or.join(search_box) + ')'

    request.session['search_string'] = search_string
    return redirect('results/page/1')


def display_results(request, page):
    companies = request.session.get('companies', [])
    company_count = len(companies)
    search_string = request.session.get('search_string', '')

    paginator = Paginator(companies, 10)

    try:
        companies_page = paginator.page(page)
    except PageNotAnInteger:
        companies_page = paginator.page(1)
    except EmptyPage:
        companies_page = paginator.page(paginator.num_pages)

    context = {
        'companies': companies_page,
        'company_count' : company_count,
        'search_string': search_string,
    }

    return render(request, 'results.html', context)