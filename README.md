=========================================
# Omics Integration and Systems Biology 

[Course homepage](https://uppsala.instructure.com/courses/96642)

Past editions:
- [Online 8 February - 10 February 2023][8]
- [Online 18 March - 22 April 2022, CZI Uppdragsutbilding][6] ([github repo][7])  
- [Online 6 - 10 September 2021, ELIXIR Omics Integration][5]
- [Online 22 - 23 July 2021, as part of the ICMB / ECCB][4]
- [Online 19 - 23 April 2021][3]
- [Lund 5 - 9 October 2020][2]
- [Stockholm 9 - 12 Sep 2019][1]

[8]: https://uppsala.instructure.com/courses/75208
[7]: https://github.com/NBISweden/sms6012_CZIomicsint
[6]: https://uppsala.instructure.com/courses/67276
[5]: https://github.com/NBISweden/workshop_omics_integration/releases/tag/course2109
[4]: https://github.com/NBISweden/workshop_omicsint_ISMBECCB/
[3]: https://github.com/NBISweden/workshop_omics_integration/tree/course2104
[2]: https://github.com/NBISweden/workshop_omics_integration/tree/course2010
[1]: https://github.com/NBISweden/workshop_omics_integration/tree/c60abb4579849bb8a0acd756d1aa9e71125265ac


# Contributions
In this branch we have all different sessions. Each session usually have only one main lab but in some sessions like session_ml we have more than one (main labs are those that we need for the course and should make proper docker for each of them).

In each of these folder we have this pattern:
- lab (folder)
- Dockerfile
- [lab_name]_env.yml
- run.sh
- [lab_name].ipynb or [lab_name].rmd
- slides for the lab

Using the dockerfile you can make the desired docker. It copies all other files inside the docker and makes a conda env inside the docker based on [lab_name]_env.yml file.

## For contribution:


1. First either create an issue or pick one of the currently available issues.
2. Create a branch based on the issue from OMICSINT_H24 brnach.
3. Make your changes on the lab, Dockerfile, [lab_name]_env.yml, [lab_name].ipynb or [lab_name].rmd
4. Make sure that the docker works properly by testing it on your local machine.
5. Make a PR to OMICSINT_H24 brnach and assign it to one of the reviewers.