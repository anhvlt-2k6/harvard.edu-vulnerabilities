number_of_workflow = input("How many workflows do you want to be created? ").strip()
number_of_workflow = int(number_of_workflow) if number_of_workflow else 1

thread_file_prefix = input("What is your preferred list prefix?: ").strip()
if not thread_file_prefix:
    thread_file_prefix = "list_thread"

try:
    for i in range(1, number_of_workflow + 1):
        f = open(f"workflows/port-scanning-thread-{str(i)}.yml", "w")
        f.write(f"""name: Port Scanning for Harvard University, thread {str(i)}

on:
  workflow_dispatch:

permissions:
  contents: write
  pull-requests: write

jobs:
  nmap-scan-single-linux:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Install Nmap and Python3 for quick runs
        run: |
          sudo apt install -y python3 python3-pip nmap
          sudo pip install psutil
          mkdir port-scanning/results/thread_{str(i)}

      - name: Run the Python file
        run: |
          nohup python3 port-scanning/runner.py port-scanning/{thread_file_prefix}_{str(i)}.txt port-scanning/results/thread_{str(i)} & # Run the script in the background

      - name: Wait for changes and Commit
        run: |
          git config --local user.name \"github-actions[bot]\"
          git config --local user.email \"github-actions[bot]@users.noreply.github.com\"
          while true; do
            git pull
            git add .
            if ! git commit -m \"GitHub Action Bot\"; then
              echo \"No changes to commit\"
            else
              git push --force
            fi
            git pull
            sleep 60
          done
        """)
        f.close()
except NameError:
    print("An error has occurred:\n", NameError)