import gitlab
# private token or personal token authentication
gl = gitlab.Gitlab('http://localhost:8080', private_token='NFy_LxYyRxrdkC2k29A4', api_version=4)
gl.auth()

project = gl.projects.get('path/to/project')
items = project.repository_tree()

print(items)




- name: Create GitLab Project in group
  community.general.gitlab_project:
    api_url: http://localhost:8080/
    validate_certs: False
    api_token: "wj6oi9dSkFfq56BnkxXw"
    name: repo1
    group: group/group1
    issues_enabled: False
    merge_method: pull
    wiki_enabled: True
    snippets_enabled: True
    import_url: https://github.com/123balu42/my-profile-vuejs.git
    state: present
  delegate_to: localhost
