# student_project_tracker(authentication+crud )
Question:
Create a Django project named student_project_tracker, where students register using a custom
user model based on AbstractUser. After login, students can perform CRUD operations on a model
called ProjectModel.
Project Setup:
• Project Name: student_project_tracker
• App Name: project
• Model: User Model and ProjectModel
User Model:
This is the Django authentication model. Used following fields to register the user:
• username
• email
• password
• student_name
• student_id
Project model:
• project_name
• project_description
• project_status (NotStarted, InProgress, Completed)
• deadline
• assign_to (Relation with the UserModel)
• thumbnail
• created_by (Must be the relationship with the UserModel. Project created user info will be
store into this field)
Templates and Navigation:
Create a master layout using HTML and CSS that includes the following links:
• Home: Display all the Project as Card Style with the fields of (project_name,
project_description, status)
• Register: To register user, used all the fields of the User Model.
• Login
• Logout
• Add Project
• Project List(Here display all the data of the project into the table with the fields of
(project_name, project_description, status, deadline).
**Note: Also create details view page for the every single project.
