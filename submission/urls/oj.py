from django.conf.urls import url

from ..views.oj import SubmissionAPI, SubmissionListAPI, ContestSubmissionListAPI, SubmissionExistsAPI, SubmissionAPI_compile, \
        SubmissionFromUserAPI, SubmissionDateFromUserAPI, SubmissionFromDateAPI

urlpatterns = [
    url(r"^submission/?$", SubmissionAPI.as_view(), name="submission_api"),
    url(r"^submission_compile/?$", SubmissionAPI_compile.as_view(), name="submission_compile_api"),
    url(r"^submissions/?$", SubmissionListAPI.as_view(), name="submission_list_api"),
    url(r"^submission_exists/?$", SubmissionExistsAPI.as_view(), name="submission_exists"),
    url(r"^contest_submissions/?$", ContestSubmissionListAPI.as_view(), name="contest_submission_list_api"),
    url(r"^smbyuser/?$", SubmissionFromUserAPI.as_view(), name="submission_from_user_api"),
    url(r"^submission_date_from_user/?$", SubmissionDateFromUserAPI.as_view(), name="submission_date_from_user_api"),
    url(r"^submission_from_date/?$", SubmissionFromDateAPI.as_view(), name="submission_from_date_api"),
]
