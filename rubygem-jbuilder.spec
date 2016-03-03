%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# Generated from jbuilder-1.5.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name jbuilder

%global bootstrap 0

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 2.3.2
Release: 3%{?dist}
Summary: Create JSON structures via a Builder-style DSL
Group: Development/Languages
License: MIT
URL: https://github.com/rails/jbuilder
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires:      %{?scl_prefix_ruby}ruby(release)
Requires:      %{?scl_prefix_ruby}ruby(rubygems)
Requires:      %{?scl_prefix}rubygem(activesupport) >= 3.0.0
Requires:      %{?scl_prefix}rubygem(activesupport) < 5
Requires:      %{?scl_prefix}rubygem(multi_json) => 1.2
Requires:      %{?scl_prefix}rubygem(multi_json) < 2
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby
%if 0%{bootstrap} < 1
BuildRequires: %{?scl_prefix_ruby}rubygem(minitest) >= 5.0.0
BuildRequires: %{?scl_prefix}rubygem(mocha)
BuildRequires: %{?scl_prefix}rubygem(rails)
BuildRequires: %{?scl_prefix}rubygem(multi_json)
%endif
BuildArch:     noarch
Provides:      %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Jbuilder gives you a simple DSL for declaring JSON structures that beats
massaging giant hash structures. This is particularly helpful when
the generation process is fraught with conditionals and loops.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}.

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
%{?scl:scl enable %{scl} - << \EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
%if 0%{bootstrap} < 1
pushd .%{gem_instdir}
# Get rid of Bundler
sed -i -e '1d' test/test_helper.rb
rm Gemfile
%{?scl:scl enable %{scl} - << \EOF}
ruby -rshellwords -Ilib:test -e "Dir.glob './test/*_test.rb', &method(:require)"
%{?scl:EOF}
popd
%endif

%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.travis.yml
%doc %{gem_instdir}/MIT-LICENSE
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/CONTRIBUTING.md
%{gem_instdir}/Gemfile
%{gem_instdir}/%{gem_name}.gemspec
%{gem_instdir}/Rakefile
%{gem_instdir}/test
%{gem_instdir}/gemfiles
%{gem_instdir}/Appraisals

%changelog
* Wed Mar 02 2016 Pavel Valena <pvalena@redhat.com> - 2.3.2-3
- Update to 2.3.2

* Tue Jan 27 2015 Josef Stribny <jstribny@redhat.com> - 2.2.2-1
- Update to 2.2.2

* Thu Oct 17 2013 Josef Stribny <jstribny@redhat.com> - 1.5.0-2
- Convert to scl

* Tue Jul 30 2013 Josef Stribny <jstribny@redhat.com> - 1.5.0-1
- Initial package
