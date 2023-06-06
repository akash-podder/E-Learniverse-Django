class TravelloRouterClass:
    """
        A router to control all database operations on models in the
        log related applications.
    """
    APP_LABELS = {'app1'}
    DB = 'travello_db_2'

    def db_for_read(self, model, **hints):
        """
            Return the database alias to use for read operations.
        """
        if model._meta.app_label in self.APP_LABELS:
            return self.DB
        return None

    def db_for_write(self, model, **hints):
        """
            Return the database alias to use for write operations.
        """
        if model._meta.app_label in self.APP_LABELS:
            return self.DB
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
            Return True if a relation between obj1 and obj2 should be allowed.
        """
        if (
                obj1._meta.app_label in self.APP_LABELS
                or obj2._meta.app_label in self.APP_LABELS
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
            Return True if the migration operation should be applied to the specified database.
        """
        if app_label in self.APP_LABELS:
            return db == self.DB
        return None