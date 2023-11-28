from smriprep.workflows.anatomical import init_anat_template_wf
wf = init_anat_template_wf(
    longitudinal=False, omp_nthreads=1, num_files=1, contrast="T1w"
)