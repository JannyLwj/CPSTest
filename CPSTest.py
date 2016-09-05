import os, time
path_to_watch = "\\10.193.236.88\dropfolder\RM2.0CI_CDC"
before = dict ([(f, None) for f in os.listdir (path_to_watch)]) ##使用dict，不使用list
while 1:
  time.sleep (3)
  after = dict ([(f, None) for f in os.listdir (path_to_watch)])
  added = [f for f in after if not f in before]  ##这也是为什么使用dict，而不直接使用list的原因
  removed = [f for f in before if not f in after]
  if added:
      print("Added: ", ", ".join(added))
  if removed:
      print("Removed: ", ", ".join (removed))
  before = after
