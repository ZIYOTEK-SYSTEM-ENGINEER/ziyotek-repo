me: Install and start Apache HTTPD
  hosts: db
  become: yes

  tasks:
    - name: httpd package is present
      yum:
        name: httpd
        state: present

    - name: correct index.html is present
      copy:
        src: files/index.html
        dest: /var/www/html/index.html

    - name: httpd is started
      service:
        name: httpd
        state: started
        enabled: true

    - name: stop firewalld
      service:
        name: firewalld
        state: stopped

    - name: Update httpd.conf
      lineinfile:
        path: /etc/httpd/conf/httpd.conf
        regexp: '^Listen'
        line: 'Listen 8080'
      ignore_errors: yes
      notify: httpd is restarted

  handlers:
    - name: httpd is restarted
      service:
        name: httpd
        state: restarted


