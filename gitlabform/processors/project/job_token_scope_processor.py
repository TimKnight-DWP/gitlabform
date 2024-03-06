import functools

from typing import List

from gitlabform.gitlab import GitLab
from gitlabform.processors import AbstractProcessor
from cli_ui import warning, debug as verbose

from gitlab.v4.objects import Project, ProjectJobTokenScope


class JobTokenScopeProcessor(AbstractProcessor):
    def __init__(self, gitlab: GitLab):
        super().__init__("job_token_scope", gitlab)

    def _process_configuration(self, project_and_group: str, configuration: dict):
        job_token_config = configuration.get("job_token_scope", {})
        verbose(f"Job Token Scope config: {job_token_config}")

        project = self._get_project(project_and_group)
        job_token_scope = project.job_token_scope.get()

        self._process_limit_access_to_this_project_setting(
            job_token_config, job_token_scope
        )

        job_token_scope.refresh()

        allowlist_config = job_token_config.get("allowlist", {})
        verbose(f"configuration allowlist: {allowlist_config}")

        verbose("Processing Job Token allowlist")

        self._process_groups(job_token_scope, allowlist_config.get("groups", []))

        job_token_scope.refresh()

        self._process_projects(
            project, job_token_scope, allowlist_config.get("projects", [])
        )

        job_token_scope.refresh()

    @staticmethod
    def _process_limit_access_to_this_project_setting(
        configuration: dict, job_token_scope: ProjectJobTokenScope
    ):
        limit_access_to_this_project: bool = configuration.get(
            "limit_access_to_this_project", True
        )
        verbose(f"limit_access_to_this_project: {limit_access_to_this_project}")
        job_token_scope.enabled = limit_access_to_this_project
        job_token_scope.save()

    def _process_projects(
        self,
        project: Project,
        job_token_scope: ProjectJobTokenScope,
        projects_allowlist: List,
    ):
        if not projects_allowlist:
            warning(
                "Process will remove existing projects from allowlist, as none set in configuration"
            )

        existing_allowlist = job_token_scope.allowlist.list()

        project_ids_to_allow = self._get_target_project_ids_from_config(
            projects_allowlist
        )

        if len(project_ids_to_allow) > 0:
            self._add_projects_to_allowlist(
                project, job_token_scope, existing_allowlist, project_ids_to_allow
            )

        self._remove_projects_from_allowlist(
            project, job_token_scope, existing_allowlist, project_ids_to_allow
        )

    def _process_groups(
        self,
        job_token_scope: ProjectJobTokenScope,
        groups_allowlist: List,
    ):
        if not groups_allowlist:
            warning(
                "Process will remove existing groups from allowlist, as none set in configuration"
            )

        existing_allowlist = job_token_scope.groups_allowlist.list()

        group_ids_to_allow = self._get_target_group_ids_from_config(groups_allowlist)

        if len(group_ids_to_allow) > 0:
            self._add_groups_to_allowlist(
                job_token_scope, existing_allowlist, group_ids_to_allow
            )

        self._remove_groups_from_allowlist(
            job_token_scope, existing_allowlist, group_ids_to_allow
        )

    def _remove_groups_from_allowlist(
        self,
        job_token_scope: ProjectJobTokenScope,
        existing_allowlist,
        target_group_ids: List,
    ):
        group_ids_to_remove = self._get_ids_to_remove_from_allowlist(
            existing_allowlist, target_group_ids
        )
        for group_id in group_ids_to_remove:
            job_token_scope.groups_allowlist.delete(group_id)
            verbose("Deleted group %s from allowlist", group_id)
            job_token_scope.save()

    def _add_groups_to_allowlist(
        self, job_token_scope, existing_allowlist, group_ids_to_allow
    ):
        group_ids_to_add = self._get_ids_to_add_to_allowlist(
            existing_allowlist, group_ids_to_allow
        )
        for group_id in group_ids_to_add:
            job_token_scope.groups_allowlist.create({"target_group_id": group_id})
            verbose("Added group %s to allowlist", group_id)
            job_token_scope.save()

    def _add_projects_to_allowlist(
        self, project, job_token_scope, existing_allowlist, project_ids_to_allow
    ):
        project_ids_to_add = self._get_ids_to_add_to_allowlist(
            existing_allowlist, project_ids_to_allow
        )
        for project_id in project_ids_to_add:
            if project_id != project.id:
                job_token_scope.allowlist.create({"target_project_id": project_id})
                verbose("Added project %s to allowlist", project_id)
                job_token_scope.save()

    def _remove_projects_from_allowlist(
        self,
        project: Project,
        job_token_scope: ProjectJobTokenScope,
        existing_allowlist,
        target_project_ids: List,
    ):
        project_ids_to_remove = self._get_ids_to_remove_from_allowlist(
            existing_allowlist, target_project_ids
        )
        for project_id in project_ids_to_remove:
            if project_id != project.id:
                job_token_scope.allowlist.delete(project_id)
                verbose("Deleted project %s from allowlist", project_id)
                job_token_scope.save()

    @staticmethod
    def _get_ids_to_remove_from_allowlist(existing_allowlist, target_ids: List):
        ids_to_remove = []

        for allowed in existing_allowlist:
            if allowed.id not in target_ids:
                ids_to_remove.append(allowed.id)

        return ids_to_remove

    @staticmethod
    def _get_ids_to_add_to_allowlist(existing_allowlist, target_ids: List):
        ids_to_add = []

        for target_id in target_ids:
            if any(allowed.id == target_id for allowed in existing_allowlist):
                # If already in allowlist, do nothing
                pass
            else:
                ids_to_add.append(target_id)

        return ids_to_add

    def _get_target_project_ids_from_config(self, projects_allowlist: List):
        target_project_ids = []

        for target_project_or_id in projects_allowlist:
            target_project = self._get_project(target_project_or_id)
            target_project_ids.append(target_project.id)

        return target_project_ids

    def _get_target_group_ids_from_config(self, groups_allowlist: List):
        target_group_ids = []

        for target_group_or_id in groups_allowlist:
            target_group = self._get_group(target_group_or_id)
            target_group_ids.append(target_group.id)

        return target_group_ids

    # TODO: move into python_gitlab.py once #697 merged in
    @functools.lru_cache()
    def _get_project(self, target_project_or_id):
        return self.gl.projects.get(target_project_or_id)

    @functools.lru_cache()
    def _get_group(self, target_group_or_id):
        return self.gl.groups.get(target_group_or_id)
