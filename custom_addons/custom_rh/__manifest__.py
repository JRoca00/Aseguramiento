{

    'name': 'El tridente',
    'version': '15.0.1.0.0',
    'category': 'Pruebas',
    'summary': 'probando sistema Jorge, joshua y yordi',
    'license': 'AGPL-3',
    'author': 'El tridente',
    'maintainer': 'El tridente',
    'website': '',
    'depends': [
        'hr',
        'hr_holidays',
        ],
    'demo': [],
    'data': [
        'security/ir.model.access.csv',
        'report/hr_employee_report_ingresos.xml',
        'report/hr_employee_report_CLaboral.xml',
        'report/hr_employee_report_ACuenta.xml',
        'report/report_prestaciones.xml',
        'report/hr_employee.xml',
        'views/hr_employee.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
