from django.db import models



class Contact(models.Model):
    # options
    showing = models.BooleanField(default=True)

    #data
    contact_service_name = models.CharField(max_length=200)
    # icon of the service method of contact
    contact_link = models.URLField(max_length=200, null=True, blank=True)
    contact_email = models.EmailField(max_length=200, null=True, blank=True)
    # TODO: probably should create a custom field for phone
    #contact_phone = models.CharField(max_length=200, null=True, blank=True)



class Education(models.Model):
    # options
    showing = models.BooleanField(default=True)

    # data
    school_name = models.CharField(max_length=200)
    degree_title = models.CharField(max_length=200)
    start_date = models.CharField(max_length=100, null=True, blank=True)
    end_date = models.CharField(max_length=100, null=True, blank=True)
    # TODO: add location

    # details
    details_description = models.TextField(null=True, blank=True)

    # school contacts(optional)
    school_site = models.URLField(max_length=200, null=True, blank=True)



class JobHistory(models.Model):
    class Meta:
        verbose_name = "Job History"
        verbose_name_plural = "Job Histories"

    # options
    showing = models.BooleanField(default=True)

    # data
    position_title = models.CharField(max_length=200)
    employer_name = models.CharField(max_length=200)
    start_date = models.CharField(max_length=100, null=True, blank=True)
    end_date = models.CharField(max_length=100, null=True, blank=True)
    current_job = models.BooleanField(default=False)
    # TODO: add location

    # details
    job_description = models.TextField(null=True, blank=True)


    # employer contacts(optional)
    employer_site = models.URLField(max_length=200, null=True, blank=True)



class JobHistoryInfo(models.Model):
    class Meta:
        verbose_name = "Job History Info"
        verbose_name_plural = "Job Histories Info"

    # options
    showing = models.BooleanField(default=True)

    # data
    job = models.ForeignKey('JobHistory', on_delete=models.CASCADE)

    # details
    job_info = models.TextField()



class Profile(models.Model):
    # data
    name = models.CharField(max_length=200, unique=True)
    about = models.TextField(null=True, blank=True)

    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)



class Project(models.Model):
    # options
    showing = models.BooleanField(default=True)
    showcased = models.BooleanField(default=False)

    # data
    project_title = models.CharField(max_length=200, unique=True)
    project_showcase_link = models.URLField(max_length=200, null=True, blank=True)
    project_sourcecode_link = models.URLField(max_length=200, null=True, blank=True)

    # details
    description = models.TextField(null=True, blank=True)



class Skill(models.Model):
    # options
    showing = models.BooleanField(default=True)
    show_years_exp = models.BooleanField(default=False)

    # data
    skill_name = models.CharField(max_length=200, unique=True)
    rating = models.IntegerField(default=0)
    years_experience = models.IntegerField(default=0)
    # TODO: examples links possibly
    # TODO: maybe create a soft skills section



class Tool(models.Model):
    # options
    showing = models.BooleanField(default=True)
    show_years_exp = models.BooleanField(default=True)

    # data
    tool_name = models.CharField(max_length=200, unique=True)
    rating = models.IntegerField(default=0)
    years_experience = models.IntegerField(default=0)
    # TODO: examples links possibly
