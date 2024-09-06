{
    
    'name': 'Student Management',
    'author':'Botspot',
    'version': '1.0',
    'summary': 'Manage student records',
    'technical name':'sms',

    'category': 'Education',
    'depends': ['base'],
    'data': [  
    
        'views/department.xml',
        'views/student_views.xml',
        'security/ir.model.access.csv'
        
    ],
    'installable': True,
    'auto_install': False,
}