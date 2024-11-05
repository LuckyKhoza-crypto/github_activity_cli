import sys
import json
import urllib.request


def fetch_user_events(username: str):
  try:
    url = f'https://api.github.com/users/{username}/events'
    response = urllib.request.urlopen(url)
    data = json.loads(response.read().decode())
    return data

  except urllib.error.HTTPError as e:
    print(
        f'Failed to fetch data for user {username}. HTTP Error code: {e.code}')
    sys.exit(1)

  except urllib.error.URLError as e:
    print(f'Failed to fetch data. Reason: {e.reason}')
    sys.exit(1)

def parse_event(event):
  current_event_type = event['type']
  event_repo = event['repo']['name']
  output = f'{current_event_type} in {event_repo}'

  if current_event_type == 'PushEvent':
    output = f'Pushed to {event_repo}'

  elif current_event_type == 'WatchEvent':
    output = f'Watched {event_repo}'

  elif current_event_type == 'ForkEvent':
    output = f'Forked {event_repo}'

  elif current_event_type == 'IssueCommentEvent':
    action = event['payload']['action']
    issue = event['payload']['issue']['title']
    print(f'User {action} issue: {issue} in repository: {event_repo}')

  return output

def print_events(username: str, events, event_type = None):

  if not events:
    print(f'No events founder for user {username}')

  event_count = 0

  print(f'Recent events by {username}:')

  for event in events:
    if event_type is None or event['type'] == event_type:
      event_count+=1
      print(parse_event(event))
      print('\n-+-+-+-+-+-+-\n')

  print(f'Finished fetching events for user {username}')

def main():
  
  if len(sys.argv) < 2:
    print('Usage: main.py <username> [event_type]')
    sys.exit(1)

  username = sys.argv[1]
  event_type = sys.argv[2] if len(sys.argv) > 2 else None
  events = fetch_user_events(username)
  print_events(username, events, event_type)

if __name__ == '__main__':
  main()