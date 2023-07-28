#!/usr/bin/env python3
from collections import defaultdict

class Beacon:
  def __init__(self, ident, x, y, z):
    self.id = ident
    self.x, self.y, self.z = x, y, z

  # pouzije miesto ==
  def __eq__(self, other):
    return self.x == other.x and self.y == other.y and self.z == other.z

  def __ne__(self, other):
    return not self == other

    # opreator <
  def __lt__(self, other):
    if self.x != other.x:
      return self.x < other.x

    if self.y != other.y:
      return self.y < other.y

    return self.z < other.z

  def coords(self):
    return self.x, self.y, self.z

  def __str__(self):
      return f'{self.x},{self.y},{self.z}'

  def delta(self, other):
    if self > other:
      self, other = other, self
    return other.x - self.x, other.y - self.y, other.z - self.z


class Scanner:
  def __init__(self, ident):
    self.id = ident
    self.beacons = []
    self.rotated = None
    self.distances = defaultdict(list)


  def __str__(self) -> str:
      return f'--- scanner {self.id} ---' + "".join(f"\n{b}" for b in self.beacons)

  def add_beacon(self, beacon):

    for b in self.beacons:
      self.distances[b.delta(beacon)].append(  (b, beacon) if b < beacon else (beacon, b)  )
    self.beacons.append(beacon)

  def rotations(self):

    if self.rotated:
      return self.rotated

    self.rotated = []
    scanner = self
    # ako deepcopy, nech nemodifneme svoje
    beacons = [Beacon(b.id, b.x, b.y, b.z) for b in self.beacons]

    #vsetky mozne rotacie, mozno aj nieco sa zopakuje, nevdi
    for x_rot in range(3):
      for y_rot in range(4):
        for z_rot in range(4):
          self.rotated.append(scanner)
          scanner = Scanner(self.id)

          for b in beacons:
            b.x, b.y = b.y, -b.x
            scanner.add_beacon(Beacon(b.id, b.x, b.y, b.z))

        for b in beacons:
          b.x, b.z = b.z, -b.x

      for b in beacons:
        b.y, b.z = b.z, -b.y

#    for r in self.rotated:
#      print(str(r), [ str(b) for b in r.beacons ])

    return self.rotated

  def find_overlapping(self, other):

    for other_rot_sc in other.rotations():
      matching_beacons = {}
      for (dx, dy, dz) in self.distances.keys():
        if (dx, dy, dz) in other_rot_sc.distances:
          for pair1, pair2 in zip(self.distances[dx, dy, dz], other_rot_sc.distances[dx, dy, dz]):
            if pair1[0].coords() not in matching_beacons:
              matching_beacons[pair1[0].coords()] = (pair1[0], pair2[0])
            if pair1[1].coords() not in matching_beacons:
              matching_beacons[pair1[1].coords()] = (pair1[1], pair2[1])

      if len(matching_beacons) >= 12:
        return list(matching_beacons.values()), other_rot_sc

    return ([], None)


def read_scanners(lines):
  scanners = []
  scanner_indexes = [i for i in range(len(lines)) if lines[i].startswith("--- scanner")]

  for i, index in enumerate(scanner_indexes):
    scanner = Scanner(i)

    for j, line in enumerate(lines[index + 1:]):
      if line == "":
        break
      x, y, z = (int(p) for p in line.split(","))
      scanner.add_beacon(Beacon(j, x, y, z))

    scanners.append(scanner)

  return scanners


lines = [l.strip() for l in open('input19.txt').readlines()]
scanners = read_scanners(lines)
for s in scanners:
    print(str(s))

needs_scan = set(range(len(scanners)))
print(needs_scan)
pending = [0]
relative_pos = {0: (0, 0, 0)}

while len(pending):
  idx = pending.pop()
  if idx not in needs_scan:
    continue

  needs_scan.remove(idx)
  s = scanners[idx]

  for other_idx in needs_scan:
    other = scanners[other_idx]
    beacons, rotated_s = s.find_overlapping(other)
    if beacons:
      scanners[other_idx] = rotated_s
      relative_pos[other_idx] = (
        relative_pos[idx][0] + beacons[0][0].x - beacons[0][1].x,
        relative_pos[idx][1] + beacons[0][0].y - beacons[0][1].y,
        relative_pos[idx][2] + beacons[0][0].z - beacons[0][1].z
      )
      pending.append(other_idx)

beacons = set()
for i, s in enumerate(scanners):
  for b in s.beacons:
    beacons.add((
      relative_pos[i][0] + b.x,
      relative_pos[i][1] + b.y,
      relative_pos[i][2] + b.z
    ))
print('Beacons: ',len(beacons))

for i in relative_pos:
  print(i)

max_distance = 0
for i in range(len(scanners)):
    for j in range(i + 1, len(scanners)):
        distance = (abs(relative_pos[i][0] - relative_pos[j][0])+
         abs(relative_pos[i][1] - relative_pos[j][1])+
         abs(relative_pos[i][2] - relative_pos[j][2]))

        max_distance = max(max_distance, distance)

print('max distance', max_distance)