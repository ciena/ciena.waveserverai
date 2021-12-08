# Ciena Waveserver Ai Collection

The Ansible Ciena Waveserver Ai collection includes a variety of Ansible content to help automate the management of Ciena Waveserver Ai platforms.

This collection has been tested against 

## Ansible version compatibility

This collection has been tested against following Ansible versions: **>=2.9.10,<2.11**.

### Supported connections

Supports ``netconf`` connections.

## Included content

<!--start collection content-->

### Modules
| Name                                                                                                                           | Description                         |
| ------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------- |
| [ciena.waveserverai.waveserverai_facts](https://github.com/ciena/ciena.waveserverai/blob/master/docs/waveserverai_facts.txt)   | Collect facts from remote devices   |
| [ciena.waveserverai.waveserverai_xcvrs](https://github.com/ciena/ciena.waveserverai/blob/master/docs/waveserverai_command.txt) | Set xcvr settings on remote devices |

<!--end collection content-->
## Installing this collection

Install the collection with the Ansible Galaxy CLI:

```bash
ansible-galaxy collection install ciena.waverserverai
```

You can also include it in a `requirements.yml` file and install it with `ansible-galaxy collection install -r requirements.yml`, using the format:

```yaml
---
collections:
  - name: ciena.waveserverai
```

## Using this collection

This collection includes [network resource modules](https://docs.ansible.com/ansible/latest/network/user_guide/network_resource_modules.html).

### Using modules from the collection in your playbooks

You can call modules by their Fully Qualified Collection Namespace (FQCN), such as `ciena.waveserverai.waveserverai_xcvrs`.

```yaml
---
  - name: Set xcvr mode
    ciena.waveserverai.waveserverai_xcvrs:
      config:
        - xcvr-id: 1-1
          properties:
            mode: 56-400
```

## Development

We welcome community contributions to this collection. If you find problems, please open an issue or create a PR against the [collection repository](https://github.com/ciena/ciena.waveserverai).

Release is done automatically use Github Actions as part of merging to master.

### Documentation generation

```bash
ansible-doc -M ./plugins/modules/ waveserverai_facts | sed -e 's/(\/home.*//g' | sed -e 's/> //g' > docs/waveserverai_facts.txt
ansible-doc -M ./plugins/modules/ waveserverai_xcvrs | sed -e 's/(\/home.*//g' | sed -e 's/> //g' > docs/waveserverai_xcvrs.txt
```

### Resource Module Builder

The modules in this project were built using the resource module builder.

Usage:

```bash
PATH_TO_ANSIBLE_COLLECTIONS_DIR=/home/$USER/src/ansible_collections/ciena/waveserverai
ansible-playbook -e rm_dest=$PATH_TO_ANSIBLE_COLLECTIONS_DIR \
                 -e structure=collection \
                 -e collection_org=ciena \
                 -e collection_name=waveserverai \
                 -e model=$PATH_TO_ANSIBLE_COLLECTIONS_DIR/resource_module_models/xcvrs/waveserverai_xcvrs.yml \
                 -e transport=netconf \
                 site.yml
```

## Changelogs

[CHANGELOG](CHANGELOG.md)

## Licensing

See [LICENSE](LICENSE) to see the full text.
