from django.db import models ##import models from django.db


class Modules(models.Model):                        ##declare class which is a table
    ModuleCode = models.CharField(max_length=10)    ##Column Name: ModuleCode char(10)
    ModuleTitle = models.CharField(max_length=40)   ##Column Name: ModuleCode char(10)
    ModuleTutor = models.CharField(max_length=40)   ##Column Name: ModuleCode char(10)

    def __str__(self): ##declare function
        return self.ModuleCode ##return row


class Student(models.Model):                            ##declare class which is a table
    StudentID = models.IntegerField()                   ##Column Name: ModuleCode char(10)
    StudentFirstName = models.CharField(max_length=20)  ##Column Name: ModuleCode char(10)
    StudentLastName = models.CharField(max_length=20)   ##Column Name: ModuleCode char(10)
    Address = models.CharField(max_length=100)          ##Column Name: ModuleCode char(10)
    Postcode = models.CharField(max_length=7)           ##Column Name: ModuleCode char(10)

    def __str__(self): ##declare function
        return str(self.StudentID) ##return row


class Marks(models.Model):                                              ##declare class which is a table
    StudentID = models.ForeignKey('Student', on_delete=models.CASCADE)  ##Column Name: StudentID foreign key from Student table, delete if module deleted from Student table
    ModuleCode = models.ForeignKey('Modules', on_delete=models.CASCADE) ##Column Name: ModuleCode foreign key from Modules table, delete if module deleted from Modules table
    ModuleMark = models.IntegerField()                                  ##Column Name: ModuleMark integer field
    SubmittedDate = models.DateTimeField()                              ##Column Name: SubmittedDate date field

    def __str__(self): ##declare function
        return str(self.StudentID) + ' ' + str(self.ModuleCode) + ' ' + str(self.ModuleMark) + ' ' + str(self.SubmittedDate) ##return row


class Coursework(models.Model):                                         ##declare class which is a table
    ModuleCode = models.ForeignKey('Modules', on_delete=models.CASCADE) ##Column Name: ModuleCode foreign key from Modules table, delete if module deleted from Modules table
    CourseworkNo = models.CharField(max_length=10)                      ##Column Name: CourseworkNo string max length 10
    CourseworkTitle = models.CharField(max_length=50)                   ##Column Name: CourseworkTitle string max length 50
    AssessmentType = models.CharField(max_length=50)                    ##Column Name: AssessmentType string max length 50
    IssueDate = models.DateField()                                      ##Column Name: IssueDate date field
    DueDateTime = models.DateTimeField()                                ##Column Name: DueDateTime date field


class Login(models.Model):                      ##declare class which is a table
    UserName = models.CharField(max_length=50)  ##Column Name: UserName string max length 50


class Password(models.Model):                   ##declare class which is a table
    Password = models.CharField(max_length=50)  ##Column Name: Password string max length 50

