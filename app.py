try:
    from flask import Flask, request,render_template
    from azure.storage.blob import BlockBlobService
    import time
    import json
    from azure.common.credentials import ServicePrincipalCredentials
    from azure.mgmt.resource import ResourceManagementClient
    from azure.mgmt.resource.resources.models import DeploymentMode
    from azure.storage.blob import BlockBlobService
    from io import BytesIO
    app = Flask(__name__)
    def dynamicArmGenerator():

        return "success"

    class Deployer(object):
        def __init__(self,resource_group,subscription_id,azure_client_id,azure_client_secret,azure_tenant_id):
            self.subscription_id = subscription_id
            self.resource_group = resource_group
            self.credentials = ServicePrincipalCredentials(
                client_id = azure_client_id,
                secret = azure_client_secret,
                tenant = azure_tenant_id
            )
            print(azure_client_secret)
            self.client = ResourceManagementClient(self.credentials, self.subscription_id)

        def deploy(self,arm,parms,connectstring):
            self.client.resource_groups.create_or_update(
            self.resource_group,
            {
            'location':'centralus'
            }
            )
            self.arm = arm
            self.parms = parms
            block_blob_service = BlockBlobService(connection_string = connectstring)
            print(block_blob_service)
            template = block_blob_service.get_blob_to_text(container_name = 'marketplacecodes', blob_name = self.arm,encoding = "utf-8-sig")
            template = json.loads(template.content)
                        #template_path = "/home/mohit/Downloads/azured
            block_blob_service = BlockBlobService(connection_string = connectstring)
            parameters = block_blob_service.get_blob_to_text(container_name = 'marketplacecodes', blob_name =self.parms,encoding = "utf-8-sig")
            parameters = json.loads(parameters.content)
            parameters = parameters["parameters"]
            deployment_properties = {
            'mode': DeploymentMode.incremental,
            'template': template,
            'parameters': parameters
            }
            file1 = open("FinalParameters.json","w")
            file1.write(json.dumps(deployment_properties))
            file1.close()
            print("hello")
            deployment_async_operation = self.client.deployments.create_or_update(
            self.resource_group,
            'azure-sample',
            deployment_properties
            )
            print("bye")
            deployment_async_operation.wait()
            return "success!"

    @app.route('/testpy', methods=['GET'])
    def result():
        appservicename = request.args.get("appservicename")# should display 'bar' # response to your request.
        print(appservicename)
        appurl = request.args.get("appurl")
        datafactoryname = request.args.get("datafactoryname")
        accountname = request.args.get("accountname")
        accesskey = request.args.get("accesskey")
        accesskey = accesskey.replace(" ","+")
        connectstring = request.args.get("connectstring")
        connectstring = connectstring.replace(" ","+")
        servername = request.args.get("servername")
        sqlusername = request.args.get("sqlusername")
        sqlpass = request.args.get("sqlpass")
        sqlcon = request.args.get("sqlcon")
        dbname = request.args.get("dbname")
        databricksname = request.args.get("databricksname")
        accesstoken = request.args.get("accesstoken")
        workspaceurl = request.args.get("workspaceurl")
        powerbiname = request.args.get("powerbiname")
        powerbiadmin = request.args.get("powerbiadmin")
        keyvaultname = request.args.get("keyvaultname")
        subid = request.args.get("subid")
        tenid = request.args.get("tenid")
        clientid = request.args.get("clientid")
        clientsecret = request.args.get("clientsecret")
        resourcegroup = request.args.get("resourcegroup")
        rglocation=request.args.get("rglocation")
        dflocation=request.args.get("dflocation")
        azurefunction=request.args.get("azurefunction")
        keyvaultlocation=request.args.get("keyvaultlocation")
        rglocation=request.args.get("rglocation")
        sources = request.args.get("sources")
        bqproject = request.args.get("bqproject")
        bqclient = request.args.get("bqclient")
        bqsecret = request.args.get("bqsecret")
        bqtoken = request.args.get("bqtoken")
        bqschema = request.args.get("bqschema")
        bqtables = request.args.get("bqtables")
        oracleport = request.args.get("oracleport")
        oraclesid = request.args.get("oraclesid")
        oracleuser = request.args.get("oracleuser")
        oraclepassword = request.args.get("oraclepassword")
        oracleschema = request.args.get("oracleschema")
        oracletable = request.args.get("oracletable")
        sapserver = request.args.get("sapserver")
        sapusername = request.args.get("sapusername")
        sappassword = request.args.get("sapschema")
        saptable = request.args.get("saptable")
        sapschema = request.args.get("sapschema")
        salesforceuser = request.args.get("salesforceuser")
        salesforcepass = request.args.get("salesforcepass")
        salesforcetoken = request.args.get("salesforcetoken")
        salesforceschema = request.args.get("salesforceschema")
        salesforcetables = request.args.get("salesforcetables")
        resource_group = resourcegroup
        subscription_id = subid
        azure_client_id = clientid
        azure_client_secret = clientsecret
        azure_tenant_id = tenid

        print(accesskey)
        print(rglocation)
        #ADF parameters
        li_salesforce =  []
        li_sap =  []
        if salesforceuser != "":
            schema_list = salesforceschema.split(",")
            table_list = salesforcetables.split(",")
            for i in range(len(schema_list)):
                li_salesforce.append({"objects_label":schema_list[i],"objects_name":table_list[i]})
        elif sapserver!= "":
            schema_list = sapschema.split(",")
            table_list = saptable.split(",")
            for i in range(len(schema_list)):
                li_sap.append({"table_schema":schema_list[i],"table_name":table_list[i]})




        dic = {}
        dic['$schema']='https://schema.management.azure.com/schemas/2015-01-01/deploymentParameters.json#'
        dic['contentVersion'] = '1.0.0.0'
        dic['parameters']={}
        dic['parameters']['DataFactoryName']={}
        dic['parameters']['DataFactoryName']['value']=datafactoryname
        dic['parameters']['DataFactoryLocation']={}
        dic['parameters']['DataFactoryLocation']['value']=dflocation
        # dic['parameters']['StorageAccountName']={}
        # dic['parameters']['StorageAccountName']['value']=accountname
        # dic['parameters']['StorageAccessKey']={}
        # dic['parameters']['StorageAccessKey']['value']=accesskey
        dic['parameters']['StorageConnectionString']={}
        dic['parameters']['StorageConnectionString']['value']=connectstring
        # dic['parameters']['SQLServerName']={}
        # dic['parameters']['SQLServerName']['value']=servername
        # dic['parameters']['SQLUsername']={}
        # dic['parameters']['SQLUsername']['value']=sqlusername
        # dic['parameters']['SQLPassword']={}
        # dic['parameters']['SQLPassword']['value']=sqlpass
        dic['parameters']['SQLConnectionString']={}
        dic['parameters']['SQLConnectionString']['value']=sqlcon
        # dic['parameters']['SQLDatabaseName']={}
        # dic['parameters']['SQLDatabaseName']['value']=dbname
        dic['parameters']['AzureFunctionURL']={}
        dic['parameters']['AzureFunctionURL']['value']=azurefunction
        dic['parameters']['Sources']={}
        dic['parameters']['Sources']['value']=sources
        if len(li_salesforce)!=0:
            dic['parameters']['SalesForceUsername']={}
            dic['parameters']['SalesForceUsername']['value']=salesforceuser
            dic['parameters']['SalesForcePassword']={}
            dic['parameters']['SalesForcePassword']['value']=salesforcepass
            dic['parameters']['SalesForceToken']={}
            dic['parameters']['SalesForceToken']['value']=salesforcetoken
            dic['parameters']['SalesForceTables']={}
            dic['parameters']['SalesForceTables']['value']=li_salesforce
        if len(li_sap)!=0:
            dic['parameters']['SAPServer']={}
            dic['parameters']['SAPServer']['value']=sapserver
            dic['parameters']['SAPUsername']={}
            dic['parameters']['SAPUsername']['value']=sapusername
            dic['parameters']['SAPPassword']={}
            dic['parameters']['SAPPassword']['value']=sappassword
            dic['parameters']['SAPTables']={}
            dic['parameters']['SAPTables']['value']=li_sap
        li = []
        for key in dic['parameters']:
            li.append(key)
        for i in li:
            value = dic['parameters'][i]['value']
            if value == None :
                del dic['parameters'][i]
        dic = json.dumps(dic)
        file1 = open("ADFParameters.json","w")
        file1.write(dic)
        file1.close()
        # dic['parameters']['DatabaseName']={}
        # dic['parameters']['DatabaseName']['value']=dbname
        # dic['parameters']['DatabricksName']={}
        # dic['parameters']['DatabricksName']['value']=databricksname
        # dic['parameters']['DataBricksWorkspaceURL']={}
        # dic['parameters']['DataBricksWorkspaceURL']['value']=workspaceurl
        # dic['parameters']['DataBricksToken']={}
        # dic['parameters']['DataBricksToken']['value']=accesstoken
        # dic['parameters']['PowerBIEmbeddedName']={}
        # dic['parameters']['PowerBIEmbeddedName']['value']=powerbiname
        # dic['parameters']['PowerBIEmbeddedAdmin']={}
        # dic['parameters']['PowerBIEmbeddedAdmin']['value']=powerbiadmin
        # dic['parameters']['AppServiceName']={}
        # dic['parameters']['AppServiceName']['value']=appservicename
        # dic['parameters']['AppServiceURL']={}
        # dic['parameters']['AppServiceURL']['value']=appurl
        dic2 = {}
        dic2['$schema']='https://schema.management.azure.com/schemas/2015-01-01/deploymentParameters.json#'
        dic2['contentVersion'] = '1.0.0.0'
        dic2['parameters']={}
        dic2['parameters']['SubscriptionID']={}
        dic2['parameters']['SubscriptionID']['value']=str(subid)
        dic2['parameters']['TenantID']={}
        dic2['parameters']['TenantID']['value']=tenid
        dic2['parameters']['ClientID']={}
        dic2['parameters']['ClientID']['value']=clientid
        dic2['parameters']['CientSecret']={}
        dic2['parameters']['CientSecret']['value']=clientsecret
        dic2['parameters']['DataFactoryName']={}
        dic2['parameters']['DataFactoryName']['value']=datafactoryname
        dic2['parameters']['StorageAccountName']={}
        dic2['parameters']['StorageAccountName']['value']=accountname
        dic2['parameters']['StorageAccessKey']={}
        dic2['parameters']['StorageAccessKey']['value']=accesskey
        dic2['parameters']['StorageConnectionString']={}
        dic2['parameters']['StorageConnectionString']['value']=connectstring
        dic2['parameters']['SQLServerName']={}
        dic2['parameters']['SQLServerName']['value']=servername
        dic2['parameters']['SQLUsername']={}
        dic2['parameters']['SQLUsername']['value']=sqlusername
        dic2['parameters']['SQLPassword']={}
        dic2['parameters']['SQLPassword']['value']=sqlpass
        dic2['parameters']['SQLConnectionString']={}
        dic2['parameters']['SQLConnectionString']['value']=sqlcon
        dic2['parameters']['SQLDatabaseName']={}
        dic2['parameters']['SQLDatabaseName']['value']=dbname
        dic2['parameters']['DatabricksName']={}
        dic2['parameters']['DatabricksName']['value']=databricksname
        dic2['parameters']['DataBricksWorkspaceURL']={}
        dic2['parameters']['DataBricksWorkspaceURL']['value']=workspaceurl
        dic2['parameters']['DataBricksToken']={}
        dic2['parameters']['DataBricksToken']['value']=accesstoken
        dic2['parameters']['PowerBIEmbeddedName']={}
        dic2['parameters']['PowerBIEmbeddedName']['value']=powerbiname
        dic2['parameters']['PowerBIEmbeddedAdmin']={}
        dic2['parameters']['PowerBIEmbeddedAdmin']['value']=powerbiadmin
        dic2['parameters']['AppServiceName']={}
        dic2['parameters']['AppServiceName']['value']=appservicename
        dic2['parameters']['AppServiceURL']={}
        dic2['parameters']['AppServiceURL']['value']=appurl
        dic2['parameters']['AzureFunctionURL']={}
        dic2['parameters']['AzureFunctionURL']['value']=azurefunction
        dic2['parameters']['KeyVaultName']={}
        dic2['parameters']['KeyVaultName']['value']=keyvaultname
        dic2['parameters']['KeyVaultLocation']={}
        dic2['parameters']['KeyVaultLocation']['value']=keyvaultlocation
        dic2['parameters']['ResourceGroupName']={}
        dic2['parameters']['ResourceGroupName']['value']=resourcegroup
        dic2['parameters']['ResourceGroupLocation']={}
        dic2['parameters']['ResourceGroupLocation']['value']=rglocation
        dic2 = json.dumps(dic2)
        file1 = open("KeyVaultParameters.json","w")
        file1.write(dic2)
        file1.close()
        container_name = 'marketplacecodes'
        blob_name = 'ADFParameters.json'
        blob_client = BlockBlobService(connection_string=connectstring)
        resp = blob_client.create_blob_from_path(container_name=container_name,blob_name=blob_name,file_path='ADFParameters.json')
        print(resp)
        blob_name = 'KeyVaultParameters.json'
        print(clientsecret)
        resp = blob_client.create_blob_from_path(container_name=container_name,blob_name=blob_name,file_path='KeyVaultParameters.json')
        print(resp)
        obj = Deployer(resource_group,subscription_id,azure_client_id,azure_client_secret,azure_tenant_id)
        print(obj.deploy("DataFactoryDeployment.json","ADFParameters.json",connectstring))
        print(obj.deploy("KeyVaultDeployment.json","KeyVaultParameters.json",connectstring))
        # blob_client.delete_container("marketplacecodes")
        return "rec"

        # return "Modified on: "+str(resp.last_modified)

    @app.route('/')
    def home():
        return render_template('loggedinpagee.html')
    if __name__ == '__main__':
        app.run(debug ="true")

except Exception as e:
    file1 = open("Erros.txt","w")
    file1.write(str(e))
    file1.close()
