
# Lab 03 - Intro to Visual Studio Code

## Timeline
<table>
  <thead>
      <td style="text-align:left;">Assigned</td>
      <td style="text-align:left;">Monday 16 September 2024</td>
  </thead>
  <tfoot>
      <td style="text-align:left; color: red;">Deadline</td>
      <td style="text-align:left;">Friday 20 September 2024</td>
  </tfoot>
</table>

![Lab 1 Assignment](https://github.com/allegheny-college-cmpsc-104-Fall-2024/lab03/blob/main/graphics/vscode.png)

## Project Goals
- Familiarize yourself with the VSCode interface and basic navigation.
- Explore code editing and debugging features.
- Utilize extensions to enhance development productivity.
- Integrate VSCode with Git for version control.

## Tools
- A computer
- Internet connection for installation and documentation reference
- A GitHub account

## Learning Outcomes
These assignment learning outcomes contribute to the following course learning outcomes described in the course syllabus:

1. Describe and explain processes such as software installation or design for a variety of technical and non-technical audiences ranging from inexperienced to expert.
2. Use professional-grade integrated development environments (IDEs), command-line tools, and version control systems to compose, edit, and deploy well-structured, web-ready documents and industry-standard documentation tools.

## Instructions

### Part 1: Check a VSCode Setting
Please verify that your development environment is correctly set up.

#### 1. Verify VSCode Installation:
- Execute `code --version` in Command Prompt (CMD)/Terminal to confirm your VSCode installation.

#### 2. Check Git Configuration in VSCode:
- Execute `git --version` in Command Prompt (CMD)/Terminal to confirm your Git installation.
- Run `git config --global user.name` and `git config --global user.email` in Command Prompt (CMD)/Terminal to verify your Git username and email are correctly configured.
- Open VSCode, press **Ctrl+Shift+P** (or **Cmd+Shift+P** on macOS) to open the Command Palette, and type `Git: Show Git Output`.

### Part 2: VSCode Commands
- Please complete the TODOs in `writing/VSCode_command.md`.

### Part 3: Code Editing
1. Create a new file named **lab3.py**.
2. In this file, write a simple Python program that prints the message "Hello, VSCode!" to the console. (You can use: `print ("Hello, VSCode!")`)
3. Take a screenshot of VSCode showing the lab3.py file and the output in the Console.
4. Name the screenshot file **lab3.png**.
5. Submit both lab3.py and the screenshot to the `writing/` directory in your project repository.

### Part 4: Debugging
1. Identify and correct errors in `writing/debug.py` using VSCode's debugging features.
3. Upon successfully debugging the script, take a screenshot of your VSCode interface showing the corrected script and no errors present. Name this screenshot debug.png. This will serve as proof of your successful debugging process
2. Submit the corrected debug.py file and the debug.png screenshot.

### Part 5: Write about Visual Studio Code Insights
- Please complete the TODOs in `writing/reflection.md`.
1. **What is Visual Studio Code?** and its purpose in software development.
2. Discuss the key features of VSCode, such as IntelliSense, Debugging, Extensions, and Version Control Integration.

### Part 6: Git Integration and Branching
1. **Modify README.md**:Open the README.md file and Delete the "TODO" here.
2. **Commit Your Changes**:
   - Navigate to the Source Control panel in VSCode.
   - Stage your changes for commit by clicking the `+` next to the `README.md` file.
   - Commit your changes by entering a meaningful commit message in the message box and pressing the checkmark icon or `Ctrl+Enter` (`Cmd+Enter` on macOS).
   - Example commit message: `"Remove TODO items from README."`
3. **Work with Branches**:
   - Create a new branch named `feature/update-readme` by opening the Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P` on macOS), then typing `Git: Create Branch...` and entering the branch name.
   - Switch to your newly created branch by opening the Command Palette again, typing `Git: Checkout to...`, and selecting `feature/update-readme`.
4. **Push Changes and Branch to Remote**:
   - Push your commit along with the new branch to the remote repository. This can be done from the Source Control panel by clicking the `...` button, selecting `Push to...`, choosing your remote, and then selecting your branch.
5. **Documentation**:
   - Take a screenshot showing the successful creation and checkout of the new branch in VSCode, with the Source Control panel visible and displaying your recent commit.
   - Name this screenshot `lab3-branching.png`.
6. **Submission**:
   - Place the screenshot `lab3-branching.png` into the `writing/` directory of your project repository.

### _Notes_: 
- Within `writing/VSCode_command.md` and `writing/reflection.md`, you will find several TODOs awaiting your completion. As you work, please ensure to remove all TODO markers. 
- For this lab, GatorGrader will verify that all TODOs have been eliminated and that your submission includes a minimum of 200 words.
- To complete part 3, first make sure that Python3 is installed by typing `python --version` into the Terminal in VSCode to verify your current version. If Python is not installed, refer to the instructions in the "Gator Grade" section of this assignment for guidance on installation.

## Resources
- Official Visual Studio Code Documentation: https://code.visualstudio.com/docs
- Git Integration with VSCode: https://code.visualstudio.com/docs/editor/versioncontrol

## Deliverables
Please submit your work by pushing it to your GitHub Classroom repository.
- You will modify the files `writing/VSCode_command.md` and `writing/reflection.md` to respond questions in the document.

## Project Assessment
- **Report Quality (20%)**: The quality of the writing in `writing/reflection.md` will be assessed.
    - Clarity and Coherence (5%): Writing clearly expresses ideas and concepts, with logical flow and coherence throughout.
    - Structure and Organization (5%): The report is well-structured. Follows the assignment guidelines accurately.
    - Grammar and Style (5%): Correct use of grammar, punctuation, and academic style. Professional and appropriate language is used.
    - Depth of Reflection (5%): Demonstrates deep understanding and thoughtful reflection on each topics. Includes detailed explanations and insights.
- **VScode Command Proficiency (30%)**: Correctly answer questions related to Git commands in `writing/VSCode_command.md`. Each correct response is worth 3%.
- **Code Editing (10%)**: 
    - Write a Python program that prints "Hello, VSCode!" to the console (5%).
    - Provide a clear screenshot showing the lab3.py file open in VSCode with the visible output in the Console (5%).
- **Debugging (10%)**: 
    - Correctly identify and fix all logical errors in the debug.py file, ensuring that the function group_religions returns accurate categories for each religion type (5%).
    - Provide a clear screenshot (debug.png) showing the corrected debug.py file open in VSCode, with the script successfully executed and displaying the expected output in the Terminal. The screenshot should clearly show the VSCode interface, including the Terminal output demonstrating the script running without errors (5%).
- **Git Integration and Branching (20%)**:
    - Successfully removing the "TODO" from the `README.md` file (5%).
    - Correctly committing changes with an appropriate message (5%).
    - Successfully creating and switching to a new branch within VSCode (10%).
- **Achieve GatorGrader Compliance (10%)**: Successfully meets the criteria set by GatorGrader.

## Gator Grade
### GatorGrade Checks for Immediate Feedback

To provide immediate feedback on your submissions, we're utilizing GatorGrade. Upon submission, if there's a thick red X, it indicates missing components. This X will turn into a green check mark once your submission is complete. For details on what's missing, click on the red X.

To meet the lab assignment's baseline writing and commit requirements, you can use the department's `GatorGrade` tool. Ensure Python3 is installed on your computer (check with `python --version`). If Python is not installed, please follow these guides:

- [Setting Up Python on Windows](https://realpython.com/lessons/python-windows-setup/)
- [Python 3 Installation and Setup Guide](https://realpython.com/installing-python/)
- [Setting Up a Local Programming Environment on Windows 10](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-windows-10)

Installing `GatorGrade`:

- [Install](https://pipx.pypa.io/stable/) [pipx](https://pipx.pypa.io/stable/) if you haven't already (`pip install pipx`).
- Install `GatorGrade` using pipx (`pipx install gatorgrade`).
- Running `GatorGrade`:
 `gatorgrade --config config/gatorgrade.yml`

Good luck!
