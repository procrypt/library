Name:	    ansible-container	
Version:	0.2.0
Release:	1%{?dist}
Summary:	Ansible Container empowers you to orchestrate, build, run, and ship Docker images built from Ansible playbooks.

Group:		Development/Libraries
License:	LGPLv3 (See LICENSE file for terms)
URL:		  https://github.com/ansible/ansible-container
Source0:	ansible-container-%{version}.tar.gz
 
Requires: docker-compose >= 1.7.0
Requires: python-jinja2 >= 2.8
Requires: PyYAML >= 3.11


BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot 


%description
Ansible Container enables you to build Docker images and orchestrate containers using only Ansible playbooks. Describe your application in a Docker Compose-like format and, rather than using a Dockerfile, provide a playbook with tasks for building images. Ansible Container will take it from there.

%global debug_package %{nil}

%prep
%setup -n ansible-container-%{version} 

%build
python setup.py build

%install
python setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)

