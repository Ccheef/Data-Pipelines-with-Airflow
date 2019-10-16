from airflow.contrib.hooks.aws_hook import AwsHook
from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class StageToRedshiftOperator(BaseOperator):
    ui_color = '#358140'

    copy_sql = """
        COPY {}
        FROM '{}'
        ACCESS_KEY_ID '{}'
        SECRET_ACCESS_KEY '{}'
        JSON '{}'
        region 'us-west-2';
    """


    @apply_defaults
    def __init__(self,
                 redshift_conn_id="",
                 aws_credentials_id="",
                 table="",
                 data_path="",
                 json_path="",
                 file_type="",
                 *args, **kwargs):

        super(StageToRedshiftOperator, self).__init__(*args, **kwargs)
        self.table = table
        self.redshift_conn_id = redshift_conn_id
        self.data_path = data_path
        self.json_path = json_path
        self.file_type = file_type
        self.aws_credentials_id = aws_credentials_id

    def execute(self, context):
        aws_hook = AwsHook(self.aws_credentials_id)
        credentials = aws_hook.get_credentials()
        redshift = PostgresHook(postgres_conn_id=self.redshift_conn_id)
        self.log.info("Deleting data from destination Redshift table")
        redshift.run("DELETE FROM {}".format(self.table))
        self.log.info("Copying data from S3 to Redshift")
     
        formatted_sql = StageToRedshiftOperator.copy_sql.format(
            self.table,
            self.data_path,
            credentials.access_key,
            credentials.secret_key,
            self.json_path
        )
        redshift.run(formatted_sql)


