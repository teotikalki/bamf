from huey.contrib.djhuey import task

from .utils.comicimporter import ComicImporter


@task()
def import_comic_files_task():
    ci = ComicImporter()
    ci.import_comic_files()

    return


@task()
def refresh_issue_task(cvid):
    ci = ComicImporter()
    success = ci.refreshIssueData(cvid)

    return success


@task()
def refresh_series_task(cvid):
    ci = ComicImporter()
    success = ci.refreshSeriesData(cvid)

    return success


@task()
def refresh_publisher_task(cvid):
    ci = ComicImporter()
    success = ci.refreshPublisherData(cvid)

    return success


@task()
def refresh_character_task(cvid):
    ci = ComicImporter()
    success = ci.refreshCharacterData(cvid)

    return success


@task()
def refresh_creator_task(cvid):
    ci = ComicImporter()
    success = ci.refreshCreatorData(cvid)

    return success


@task()
def refresh_team_task(cvid):
    ci = ComicImporter()
    success = ci.refreshTeamData(cvid)

    return success


@task()
def refresh_arc_task(cvid):
    ci = ComicImporter()
    success = ci.refreshArcData(cvid)

    return success
