import oci  # pyright: ignore[reportMissingTypeStubs]
from oci import Response

COMPARTMENT_ID = "ocid1.compartment.oc1..aaaaaaaaqucirsmgdqkohccypfkhx66gckdnlnhdbfprayahqqdmfgroh5za"  # Replace with your compartment OCID

config = oci.config.from_file()  # Load the default OCI config file (~/.oci/config)
oci.config.validate_config(config)

client = oci.object_storage.ObjectStorageClient(config)

namespace: Response = client.get_namespace()

buckets = client.list_buckets(namespace_name=namespace.data, compartment_id=COMPARTMENT_ID)
print(f"Buckets in compartment {COMPARTMENT_ID}:")
for bucket in buckets.data:
    print(bucket.name)
