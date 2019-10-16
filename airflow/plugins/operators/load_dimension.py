from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults
from helpers import SqlQueries

class LoadDimensionOperator(BaseOperator):

    ui_color = '#80BD9E'
    
    insert_sql = """
        INSERT INTO {}
        {};
        """

    @apply_defaults
    def __init__(self,
                 redshift_conn_id = "",
                 table = "",
                 sql = "",  
                 insert_and_delete = False,
                 *args, **kwargs):

        super(LoadDimensionOperator, self).__init__(*args, **kwargs)
        
        self.redshift_conn_id = redshift_conn_id
        self.table = table
        self.sql = sql
        self.insert_and_delete = insert_and_delete

    def execute(self, context):
        redshift = PostgresHook(postgres_conn_id=self.redshift_conn_id)
       #switch between append and insert-delete functionality
        if self.insert_and_delete:
            self.log.info("Delete dimension table: {}".format(self.table))
            redshift.run("DELETE FROM {}".format(self.table))
            
        self.log.info("Insert data from staging tables into {} dimension table".format(self.table))
        formatted_sql = LoadDimensionOperator.insert_sql.format(
            self.table,
            self.sql
        )
        redshift.run(formatted_sql)     
        
