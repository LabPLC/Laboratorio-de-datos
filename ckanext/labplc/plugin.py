import logging
import ckan.plugins as plugins
import ckan.plugins.toolkit as tk

class labplcPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IRoutes, inherit=True)

    def update_config(self, config):

        # Add this plugin's templates dir to CKAN's extra_template_paths, so
        # that CKAN will use this plugin's custom templates.
        tk.add_template_directory(config, 'templates')

        # Add this plugin's templates dir to CKAN's extra_template_paths, so
        # that CKAN will use this plugin's custom templates.
        tk.add_public_directory(config, 'public')

        # Add this plugin's fanstatic dir.
        tk.add_resource('fanstatic', 'ckanext-labplc')


    def before_map(self, map):
        labplc_controller = 'ckanext.labplc.controller:LabplcController'
        map.connect('home_api','/apis', controller=labplc_controller,
		 action='api')
        map.connect('tutorials','/tutoriales', controller=labplc_controller,
		 action='tutorials')
        map.connect('about','/acerca', controller=labplc_controller,
         action='about')
        return map
