# orglog

The Rust and Servo projects enjoy giving credit to those who contribute to
their GitHub repos, and congratulating new contributors when they land their
first commits. 

The [gitstat](https://github.com/youknowone/gitstat) tool turns `git log`
output into pretty graphs and statistics about new contributors and
contribution types. 

`orglog` is designed to concatenate the git logs of all source repositories
(not forks) in a given organization.

## Usage

Copy `credentials.py.example` to `credentials.py`, and edit it to contain the
GitHub username and password of an account without 2-factor auth. 

Then run `python orglog.py orgname` and the log will be created. 

## Contributing

Look for `#TODO` in orglog.py. Pull requests welcome.

