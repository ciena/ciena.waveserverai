# ciena.waveserverai

## Development

Build the modules using Ansible RMB:

```bash
PATH_TO_ANSIBLE_COLLECTIONS_DIR=/home/$USER/src/ansible_collections/ciena/waveserverai
ansible-playbook -e rm_dest=$PATH_TO_ANSIBLE_COLLECTIONS_DIR \
                 -e structure=collection \
                 -e collection_org=ciena \
                 -e collection_name=waveserverai \
                 -e model=$PATH_TO_ANSIBLE_COLLECTIONS_DIR/resource_module_models/xcvr/waveserverai_xcvr.yml \
                 -e transport=netconf \
                 site.yml
```
