# Changelog

## 0.1.0 (2024-05-15)


### Features

* ability to transfer project between groups or namespaces ([#582](https://github.com/TimKnight-DWP/gitlabform/issues/582)) ([d56ab32](https://github.com/TimKnight-DWP/gitlabform/commit/d56ab32b952a83f846496687ec736dd8ad71c057))
* add `enforce` support for project hooks/webhooks configuration ([#664](https://github.com/TimKnight-DWP/gitlabform/issues/664)) ([aa53356](https://github.com/TimKnight-DWP/gitlabform/commit/aa53356afd500fa6cd14f88da5e3b845d76a6574)), closes [#662](https://github.com/TimKnight-DWP/gitlabform/issues/662)
* add allowed_to_create support for tag protection ([0da9a15](https://github.com/TimKnight-DWP/gitlabform/commit/0da9a15db97d7199c4af3673bb411c3dfb75ff81))
* add enforce config support for pipeline schedules ([4795ad5](https://github.com/TimKnight-DWP/gitlabform/commit/4795ad52e06f891f0bed58c10eb1d3ca94329b03))
* add option to keep bots when enforcing membership ([846de95](https://github.com/TimKnight-DWP/gitlabform/commit/846de95ee5d9f44eafbe3512c90ce3d479f468da)), closes [#454](https://github.com/TimKnight-DWP/gitlabform/issues/454)
* add option to not fail if configured resource group does not exist ([#650](https://github.com/TimKnight-DWP/gitlabform/issues/650)) ([a362d8e](https://github.com/TimKnight-DWP/gitlabform/commit/a362d8e41f9b65d2debd86e529d5939cc023dbbe)), closes [#649](https://github.com/TimKnight-DWP/gitlabform/issues/649)
* add support for Application Settings ([7c4b9fd](https://github.com/TimKnight-DWP/gitlabform/commit/7c4b9fd78c34aa636513475397eb6dffd0182893))
* manage Project and Group Labels via gitlabform ([#751](https://github.com/TimKnight-DWP/gitlabform/issues/751)) ([f1be42b](https://github.com/TimKnight-DWP/gitlabform/commit/f1be42bd245237f512ff61de9dfb30057bdf1700))
* migrate group_members to use python-gitlab ([c9f1dcf](https://github.com/TimKnight-DWP/gitlabform/commit/c9f1dcfabfd38d61c37966507bb868367e7480d4))
* use python lib for group settings ([#746](https://github.com/TimKnight-DWP/gitlabform/issues/746)) ([03ce3fa](https://github.com/TimKnight-DWP/gitlabform/commit/03ce3faf0b01cbda4ff5f9137030a8f2ac159bb0))


### Bug Fixes

* 461 + prepare 3.3.3 release ([cff3f03](https://github.com/TimKnight-DWP/gitlabform/commit/cff3f03abad91229ffc3dc3cd69fcdeb5e6184f1))
* add improved error handling when processing transferred project ([#745](https://github.com/TimKnight-DWP/gitlabform/issues/745)) ([a063b69](https://github.com/TimKnight-DWP/gitlabform/commit/a063b6985dfdf052384e190458f561cace99d55f))
* **ci:** install setuptools in github workflow to fix release process ([b3eb164](https://github.com/TimKnight-DWP/gitlabform/commit/b3eb1648ff18ecd2db799007341986378f0c4d6a))
* don't retry again on GETs with RemoteDisconnected ([6f8aa7f](https://github.com/TimKnight-DWP/gitlabform/commit/6f8aa7f7d9b4bc4ae5fd88d0f18206dd9696b2a9))
* dry run failure when project transfer is configured along with other additional configs ([#726](https://github.com/TimKnight-DWP/gitlabform/issues/726)) ([71070bf](https://github.com/TimKnight-DWP/gitlabform/commit/71070bff075e5c5c4d7994fe5550db5bfc8ce9bc)), closes [#725](https://github.com/TimKnight-DWP/gitlabform/issues/725)
* error when running with --noop and --output-file parameter and config contains project to be transferred ([#729](https://github.com/TimKnight-DWP/gitlabform/issues/729)) ([f91c9f6](https://github.com/TimKnight-DWP/gitlabform/commit/f91c9f67fbb57bac8034817c1b1a38ed1857d3f3))
* hooks processing fails when config includes token ([#693](https://github.com/TimKnight-DWP/gitlabform/issues/693)) ([dd58a7a](https://github.com/TimKnight-DWP/gitlabform/commit/dd58a7a2df60a1a5b8fe6a9cdf127ae1bf79ee5a)), closes [#685](https://github.com/TimKnight-DWP/gitlabform/issues/685)
* ignore keep_bots from users list for group membership ([0bf7d4c](https://github.com/TimKnight-DWP/gitlabform/commit/0bf7d4c62fa3c3d3e21967c3613e2d376d92b616))
* iterates through group members ([b54bbe8](https://github.com/TimKnight-DWP/gitlabform/commit/b54bbe8728681c662b552f3765c1cf2179e6c794))
* **members:** ensure group and project users are case-insensitive ([#556](https://github.com/TimKnight-DWP/gitlabform/issues/556)) ([2381ebe](https://github.com/TimKnight-DWP/gitlabform/commit/2381ebe1201c3321e17ee17be18f79b0339bd0bd))
* process all schedules and not only the first 20 ([625b81f](https://github.com/TimKnight-DWP/gitlabform/commit/625b81faa7aff8b329db7f7445d9c1d83899e5b6))
* transfer project not working when target is ALL or ALL_DEFINED or group or subgroup ([#714](https://github.com/TimKnight-DWP/gitlabform/issues/714)) ([4887326](https://github.com/TimKnight-DWP/gitlabform/commit/4887326b2eb970caa13dea2d397880792ec2609f))
* we need a non-dictionary-words passwords for GitLab users... ([73958a0](https://github.com/TimKnight-DWP/gitlabform/commit/73958a049b91cb89efc7862bc800a7b9df8ab7b8))


### Reverts

* we need auto approve deployment, not auto approve PRs.. ([8008695](https://github.com/TimKnight-DWP/gitlabform/commit/8008695dba70a5ace80263eb1662eabf9dd6b13d))


### Documentation

* add changelog for 3.9.4 ([b3640a1](https://github.com/TimKnight-DWP/gitlabform/commit/b3640a110666461e492117c14e9864a359fbdfc9))
* add changelog for 3.9.5 ([94f0fb9](https://github.com/TimKnight-DWP/gitlabform/commit/94f0fb9dbb33f86ac75955830b2affeff8616918))
* add fixes info into changelog for release 3.10.0 ([96a39ee](https://github.com/TimKnight-DWP/gitlabform/commit/96a39eee118b6c7e00d6dd1d47d845213876ffb3))
* add information about Application Settings ([568cb1b](https://github.com/TimKnight-DWP/gitlabform/commit/568cb1b6f98856dd50e8e97471b0fefdb87cbc6a))
* add schedule enforce documentation ([2be4d9f](https://github.com/TimKnight-DWP/gitlabform/commit/2be4d9fa0bdb1cb734a11bb49e52060968e08457))
* fix branches keyword in MR approval rules ([#710](https://github.com/TimKnight-DWP/gitlabform/issues/710)) ([ae42c2a](https://github.com/TimKnight-DWP/gitlabform/commit/ae42c2abed38fd47f78766cb276972bcfc4fa725))
* fix broken links to references in homepage ([#653](https://github.com/TimKnight-DWP/gitlabform/issues/653)) ([aa26e66](https://github.com/TimKnight-DWP/gitlabform/commit/aa26e66637645ec7d530aa00be53d2bdb57770db))
* fix documentation and test in PRs ([ce4260b](https://github.com/TimKnight-DWP/gitlabform/commit/ce4260bcc2f2c1d7f3c4fbb1fa09baff2f1bed95))
* move commit message guideline ([c0d3f68](https://github.com/TimKnight-DWP/gitlabform/commit/c0d3f68255fb13eb2a769d7df4a6888ffdcc742d))
* remove deprecation warning about delete config ([2f6c4b8](https://github.com/TimKnight-DWP/gitlabform/commit/2f6c4b8d54bb953b8fab8acfdb022ce1fdf0e79e))
* update changelog for 3.9.1 release ([c7f6559](https://github.com/TimKnight-DWP/gitlabform/commit/c7f65599f2ad4a0bd02e9c57bf83347c0642c28e))
* update changelog for 3.9.2 release ([ad4986c](https://github.com/TimKnight-DWP/gitlabform/commit/ad4986c7c19c6f617395abe0b19ee7a4e292e057))
* update changelog for release 3.9.0 ([77710ba](https://github.com/TimKnight-DWP/gitlabform/commit/77710ba291ea044813360a5cc8520c2075e6a8ff))
* update example in homepage to reflect latest config syntax ([be53585](https://github.com/TimKnight-DWP/gitlabform/commit/be53585d4d7ca2d242fd1e7290ba6922e9e086d0))
* update local dev instruction to specify installing setuptools package ([bd31788](https://github.com/TimKnight-DWP/gitlabform/commit/bd317886e894f263e1494fe43f2b2706aee92570))
* update local development instructions for clarity on env setup ([3265792](https://github.com/TimKnight-DWP/gitlabform/commit/3265792dd470988a5231228359c7448b016932b1))
* update release instructions to clarify usage of tbump tool ([c6f3aec](https://github.com/TimKnight-DWP/gitlabform/commit/c6f3aec536962e59fa3467a16aba33daf6db10f3))
* update release process documentation for more clarity ([171fcc8](https://github.com/TimKnight-DWP/gitlabform/commit/171fcc833afd559cdc23074d7b86cb338724ff47))
