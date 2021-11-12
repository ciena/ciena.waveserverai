# ciena.waveserverai

```bash
ansible-playbook -e rm_dest=interfaces \
                 -e structure=collection \
                 -e collection_org=ciena \
                 -e collection_name=waveserverai \
                 -e model=/home/<you>/ansible_collections/ciena/waveserverai/resource_module_models/xcvr/waveserverai_xcvr.yml \
                 -e transport=netconf \
                 site.yml
```
