# Set up

In your `.zshrc` or equivalent, add your OpenReview login details as environment variables, e.g.

```
export OPENREVIEW_USERNAME='your_username'
export OPENREVIEW_PASSWORD='your password'
```

Create a Conda environment and install dependencies.

```
conda create -n bioc2022openreview python=3.9
conda activate bioc2022openreview
pip install -r requirements.txt
```

# Working environment

```
conda activate bioc2022openreview
```

# Test

```
conda activate bioc2022openreview
python test.py
```

# Setup

Edit the `config.py` script - set the right conference path, define the output 
directory. Also edit the respective scripts to reflect e.g. the fields in 
the submission form that you would like to pull down. 

# Example usage

Pull down the submissions to `_out/submissions.txt`:

```
python tabulate_submissions.py
```

Pull down the reviews to `_out/reviews.txt`:

```
python tabulate_reviews.py
```

# OpenReview API

- [Documentation](https://openreview-py.readthedocs.io/en/latest/)
