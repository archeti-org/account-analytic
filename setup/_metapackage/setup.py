import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-oca-account-analytic",
    description="Meta package for oca-account-analytic Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-account_analytic_parent>=15.0dev,<15.1dev',
        'odoo-addon-account_analytic_tag_default>=15.0dev,<15.1dev',
        'odoo-addon-procurement_mto_analytic>=15.0dev,<15.1dev',
        'odoo-addon-product_analytic>=15.0dev,<15.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 15.0',
    ]
)
