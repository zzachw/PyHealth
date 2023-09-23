# Sunlab PyHealth Hackathon 2023

## Schedule
| Day	| Activity |
|-----|------|
| Fri (Sep 29)	| Team Formation (1-2) and Problem Statement Discussion (adding new papers) |
| Sat (Sep 30) | Team work and report their progress | 
| Sun (Oct 1)	| Team continue working on the project | 
| Mon (Oct 2)	| Presentation (afternoon group meeting) | 
| Next Mon (Oct 9)	| Vote and iteratively improve PR |

## Team (continuously updated)
| Team Name	| Team Members | Paper |
|-----|------|------|
| Team 1	| Chaoqi Yang | [BIOT: Biosignal Transformer for Cross-data Learning in the Wild](https://openreview.net/forum?id=c2LZyTyddi) |


## How to frame the PR
You will be implementing one research paper. It can be your own recent ICLR, AAAI, WWW papers or previous research papers or one paper from our prepared list (). Each paper may have new dataset, task definition, and AI models, so your PR may involve adding new datasets, new tasks, and new models. 
- Adding new datasets and tasks can refer to these examples:
    - [Example 1: add SHHS datasets and tasks](https://github.com/sunlabuiuc/PyHealth/pull/162)
    - [Example 2: add TUEV, TUAB datasets and tasks](https://github.com/sunlabuiuc/PyHealth/pull/194)
    - [Example 3: add Cardiology datasets and tasks](https://github.com/sunlabuiuc/PyHealth/pull/176)
- Adding new models can refer to these examples
    - [Example 1: add deeper model](https://github.com/sunlabuiuc/PyHealth/pull/61)
    - [Example 2: add image classification models](https://github.com/sunlabuiuc/PyHealth/pull/175)
    - [Example 3: add MoleRec model](https://github.com/sunlabuiuc/PyHealth/pull/122)
- The final PR is pushed to the `230922-sunlab-hackthon` branch, and we will work with you to merge it in.

### Format of the PR
1. **Python class** follows the structure of `SHHSDataset` in `pyhealth/datasets/shhs.py`
    - with detailed docstring
        ```
        Description: xxx

        Args:
            dataset_name: name of the dataset.
            root: root directory of the raw data (should contain many csv files).
            ...

        Attributes:
            task: Optional[str], name of the task (e.g., "sleep staging").
                Default is None.
            ...

        Examples:
            >>> from pyhealth.datasets import SHHSDataset
            >>> dataset = SHHSDataset(
            ...         root="/srv/local/data/SHHS/",
            ...     )
            >>> dataset.stat()
            >>> dataset.info()
        ```
    - with a runnable example at the end of the file, so that we can use `python pyhealth/datasets/shhs.py` for small data test
        ```
        if __name__ == "__main__":
        dataset = SHHSDataset(
            root="/srv/local/data/SHHS/polysomnography",
            dev=True,
            refresh_cache=True,
        )
        ```

2. **Python function** follows the structure of `sleep_staging_shhs_fn` in `pyhealth/tasks/sleep_staging.py`
    - with detailed docstring
        ```
        Descriptions: xxx

        Args:
            ...

        Returns:
            ...

        Examples:
            ...
        ```
    - with a runnable example at the end of the file, so that we can use `python pyhealth/datasets/shhs.py` for small data test
        ```
        if __name__ == "__main__":
            from pyhealth.datasets import SHHSDataset

            dataset = SHHSDataset(
                root="/srv/local/data/SHHS/polysomnography",
                dev=True,
                refresh_cache=True,
            )
            sleep_staging_ds = dataset.set_task(sleep_staging_shhs_fn)
            print(sleep_staging_ds.samples[0])
            print(sleep_staging_ds.input_info)
        ```

3. Every PR must has an `example/xxx.py` for large scale data test. For example, `examples/sleep_staging_shhs_contrawr.py`.


## Resources
- PyHealth Documentation: https://pyhealth.readthedocs.io/en/latest/
- PyHealth GitHub: https://github.com/sunlabuiuc/PyHealth
- PyHealth Tutorial: https://pyhealth.readthedocs.io/en/latest/tutorials.html
- PyHealth Live Videos: https://www.youtube.com/playlist?list=PLR3CNIF8DDHJUl8RLhyOVpX_kT4bxulEV

## Mentors & Judges
- `Chaoqi Yang` is a Ph.D. student in CS @ UIUC. His research is build ML models and systems for time-dependent data in health, e.g., electronic health records (EHR), EEG.
- `Zhenbang Wu` is a Ph.D. student in CS @ UIUC. His research interest is in developing generalizable and adaptable deep learning algorithms to solve important healthcare problems.
- `Patrick Jiang` is an M.S. student in CS @ UIUC. His research interest is healthcare natural language processing.
<!-- - `Zhen Lin` is a Ph.D. student in CS @ UIUC. His research interests include uncertainty quantification in healthcare and biosignal modeling. -->
<!-- - `Benjamin Danek` is an MCS student in CS @ UIUC. His interests are in federated learning and fairness, and synthetic data generation.
- `Junyi Gao` is a Ph.D. student at the University of Edinburgh funded by the HDR UK-Turing Welcome Ph.D. Program. His research interests include spatio-temporal epidemiology prediction and individual-level clinical predictive modeling. -->

## Criteria
- (50%) Votes from lab students (each team or other lab students can vote for no more than 3 teams). In total, N voters here.
- (50%) Votes from judges (Chaoqi, Zhenbang, Patrick can vote for no more than 3 teams). In total, 3 judges here.
- Scores: #other_votes / N * 50% + #judge_votes / 3 * 50%

## Rewards ($2000 total)
- Threshold: score > 50%
    - 1st Prize: 35% of the prize budget ($700)
    - 2nd Prize: 25% of the prize budget ($500)
    - 3rd Prize: 15% of the prize budget ($300)
    - Best new-participant award: 25% of the prize budget ($500 divided by the number of participated new MS/PhD students)