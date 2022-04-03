import openreview
import pandas
import os

import config

c = openreview.Client(
    baseurl="https://api.openreview.net", username=config.username, password=config.password
)

notes = c.get_notes(invitation=config.conference + "/-/Submission")

# Reformat content into single value fields

title = [note.content["title"] for note in notes]

number = ["Paper" + str(note.number) for note in notes]

authorids = [",".join(note.content["authorids"]) for note in notes]

authors = [",".join(note.content["authors"]) for note in notes]

keywords = [",".join(note.content["keywords"]) for note in notes]

abstract = [note.content["abstract"] for note in notes]

affiliation = [note.content["affiliation"] for note in notes]

contact_email = [note.content["contact_email"] for note in notes]

orcid = [note.content["orcid"] if "orcid" in note.content.keys() else "" for note in notes]

social_media_handle = [note.content["social_media_handle"] if "social_media_handle" in note.content.keys() else "" for note in notes]

pronoun = [note.content["preferred pronoun"] if "preferred pronoun" in note.content.keys() else "" for note in notes]

bioconductor_package_maintenance = [note.content["bioconductor_package_maintenance"] if "bioconductor_package_maintenance" in note.content.keys() else "" for note in notes]

associated_packages = [note.content["associated_packages"] for note in notes]

short_talk = ["Short talk" in note.content["submission_type"] for note in notes]
package_demo = ["Package demo" in note.content["submission_type"] for note in notes]
birds_of_a_feather = ["Birds-of-a-feather session" in note.content["submission_type"] for note in notes]
workshop = ["Workshop" in note.content["submission_type"] for note in notes]
poster = ["Poster" in note.content["submission_type"] for note in notes]

preferred_format = [note.content["preferred format"] for note in notes]

submission_is_not_registration = [note.content["submission_is_not_registration"] for note in notes]

code_of_conduct = [note.content["code_of_conduct"] for note in notes]

paperhash = [note.content["paperhash"] for note in notes]

submissions_table = pandas.DataFrame(data = {
    "number": number,
    "title": title,
    "authorids": authorids,
    "authors": authors,
    "keywords": keywords,
    "abstract": abstract,
    "affiliation": affiliation,
    "contact_email": contact_email,
    "orcid": orcid,
    "social_media_handle": social_media_handle,
    "pronoun": pronoun,
    "bioconductor_package_maintenance": bioconductor_package_maintenance,
    "associated_packages": associated_packages,
    "short_talk": short_talk,
    "package_demo": package_demo,
    "birds_of_a_feather": birds_of_a_feather,
    "workshop": workshop,
    "poster": poster,
    "preferred_format": preferred_format,
    "submission_is_not_registration": submission_is_not_registration,
    "code_of_conduct": code_of_conduct,
    "paperhash": paperhash,
})

submissions_table.to_csv(os.path.join(config.output_dir, "submissions.txt"),
    sep = "\t",
    index = False)
