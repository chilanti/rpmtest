###############################################################################
# Spec file for Knapp
################################################################################
#
Summary: Knapp CLI RPS
Name: knapp
Version: 0.0.1
Release: 1
License: GPL
URL: http://www.ibm.com
Group: System
Packager: Michele Chilanti
Requires: bash
Source0: %{name}
Source1: %{name}-watcher

%description
Knapp CLI

%prep
################################################################################
# Create the build tree and copy the files from the development directories    #
# into the build tree.                                                         #
################################################################################
echo "BUILDROOT = $RPM_BUILD_ROOT"

exit
%build

%install

mkdir -p %{buildroot}/%{_bindir}
install -m 0755 %{SOURCE0} %{buildroot}/%{_bindir}
install -m 0755 %{SOURCE1} %{buildroot}/%{_bindir}


%files
%{_bindir}/%{name}
%{_bindir}/%{name}-watcher

%pre

%post
if [ ! -d "$HOME/.knapp" ]; then
    mkdir $HOME/.knapp
fi
cp %{_bindir}/knapp-watcher $HOME/.knapp

%postun
rm -rf $HOME/.knapp

%clean
rm -rf %{buildroot}/%{_bindir}

%changelog
* Thu May 9 2019 Michele Chilanti <chilantim@us.ibm.com>
  - This is the first release of the knapp RPM package.
