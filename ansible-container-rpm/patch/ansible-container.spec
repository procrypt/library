%define name ansible-container
%define version 0.2.0rc0
%define unmangled_version 0.2.0rc0
%define unmangled_version 0.2.0rc0
%define release 1

Summary: Ansible Container empowers you to orchestrate, build, run, and ship Docker images built from Ansible playbooks.
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{unmangled_version}.tar.gz

Patch0: remove-docker-py-and-requests-py.patch 

License: LGPLv3 (See LICENSE file for terms)
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Joshua "jag" Ginsberg, Chris Houseknecht, and others (See AUTHORS file for contributors) <jag@ansible.com>
Url: https://github.com/ansible/ansible-container

%description
Ansible Container enables you to build Docker images and orchestrate containers using only Ansible playbooks. Describe your application in a Docker Compose-like format and, rather than using a Dockerfile, provide a playbook with tasks for building images. Ansible Container will take it from there.

%prep
%setup -n %{name}-%{unmangled_version} -n %{name}-%{unmangled_version}

%patch0 -p1

%build
python setup.py build


%install
python setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
