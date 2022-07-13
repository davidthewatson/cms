#  README

# INSTALL

        ~/Github/cms    main wip  python -m venv .venv                 ✔ 
        ~/Github/cms    main wip  source .venv/bin/activate            ✔  38s  
        ~/Github/cms    main wip  echo $VIRTUAL_ENV                    ✔  cms  
     /home/watson/Github/cms/.venv
## Developing 

I develop locally on linux, fish, python3, pip, virtualenv, tmux, and alacritty (terminal). The following instructions rely on that, but they may work for you if you have a similar linux environment.

To run the development environment:

```
cd davidthewatson.github.io
python -m virtualenv .venv
source .venv/bin/activate.fish
pip install -r requirements.txt
tmux
cd docs
python -m http.server
build_local.sh
```

## Deploying

I deploy on github pages.

## My new Github Flow

    # create branch
    git switch -c new-branch
    
    # add changed code
    git add whatever
    
    # commit
    git commit -m 'new stuff'
    
    # push
    git push

    # create the pull request
    gh pr create

    # for others to view diff on a PR
    gh pr diff  
    
    # to view comments on a PR
    gh pr view --comments

    # for others to review your PR
    gh pr review --approve
    
    # for you to merge your PR
    gh pr merge  
