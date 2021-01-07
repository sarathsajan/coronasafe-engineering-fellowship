# CoronaSafe Engineering Fellowship
[<img src="https://ci3.googleusercontent.com/proxy/S72SkV5dy1K9-jb7umRtbCKnE6WtBnsqxGfhRxe4csTjeKnEpUye969Dy_IvdrXPPXML6L-YD1NKloq7TDMmq_AwCUMFNPFDwzv3ps-njZfspe7O95Y1KYPFfLsGy0eb7cGDjOjJcFJdbPDmDAQPMt8eDf4shgehumD6FBtY1JQ=s0-d-e1-ft#https://apply.pupilfirst.org/assets/logo-594a33db1581ddba4c61558ec794b6c7244c88828896e4af3d15c74c85f21ab4.png" height=50>](https://fullstack.pupilfirst.org/) <img src="https://fullstack.pupilfirst.org/logos/aicte-logo.png" height=50> <img src="https://fullstack.pupilfirst.org/logos/NSTEDB-logo.svg" height=50>


## Requirements

### Build a todo-list app with CLI
```
$ ./todo help
Usage :-
$ ./todo add "todo item"  # Add a new todo
$ ./todo ls               # Show remaining todos
$ ./todo del NUMBER       # Delete a todo
$ ./todo done NUMBER      # Complete a todo
$ ./todo help             # Show usage
$ ./todo report           # Statistics
```
### How it should work when done [VIDEO]
[![Todo-CLI](https://res.cloudinary.com/sv-co/image/upload/v1607935139/fullstack-CEF/Todo-CLI/play-video-demo_fp50wp.png)](https://vimeo.com/490621534)


## Development Log

### 2021/01/02
* codebase can be upload only after the end of judgement.
* unit tests --> total: 16, passed: 10, failed: 6
<img src="https://raw.githubusercontent.com/sarathsajan/coronasafe-engineering-fellowship/main/unit_test.png" width=75%>

* most of the tests that failed were because of the [newline UTF encoding issues](https://github.com/nseadlc-2020/package-todo-cli-task/issues/12).
* couldn't achieve argument parsing without dashes as shown above in the requirements video. ie. had to do ```todo --add "task1"``` instead of ```todo add "task1"```
* optionally requires installation of [WSL](https://en.wikipedia.org/wiki/Windows_Subsystem_for_Linux) for proper testing; due to limitations of time this step was skipped
* finished remaining features : '--done' and '--report'
* implemented yesterday's 3 features in a different logic with better error handling and reusability
* removed yesterday's full code

### 2021/01/01
* complications while implementing '--done' logic
* completed the '--add', '--ls', '--del' features of the project
* difficulty in fulfilling a feature in the project
  * [Issue filed regarding using of 'del' keyword](https://github.com/nseadlc-2020/package-todo-cli-task/issues/51)
  * [ISSUE SOLVED] [Project requires 'del' keyword to be used as variable, which unfortuntely raises syntax error](https://stackoverflow.com/questions/65517801/python-del-syntax-error-when-used-as-a-variable-name)
* installed nodejs for unit testing
* completed the pre-requirements (symlinks, nodejs, node_modules etc) for the project

### 2020/12/30
* received problem statement
* applied for the course
