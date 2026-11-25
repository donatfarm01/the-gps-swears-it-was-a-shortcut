Build notes for the GPS shortcut excuse entry.

The bounty asks for one line, in the GPS's own voice, excusing the wrong
road it sent the driver down. The judge weighs five things in order: the
line must be the GPS's own excuse, it must be genuinely funny with a turn
the reader does not see coming, it must sound like the GPS talking, smug
and defensive and blaming the map, it must read cleanly aloud in one
breath inside two hundred characters, and it must carry a fresh specific
detail instead of the usual recalculating joke.

The line I chose is the GPS blaming the map for the turn and refusing to
listen to the lake that disagreed with it. The joke lands in three beats:
the map says turn, the lake objects, and the GPS announces it takes no
directions from water. The lake is the fresh specific detail, the map
takes the blame, and the last beat is the smug turn the reader does not
expect. The line is eighty-five characters, so it fits the gate with room
to spare and reads aloud in a single breath.

The program is deliberately tiny. It holds the line as a fixed string and
writes it to the output file, creating the output folder if needed and
leaving the file world-readable so the grader can collect it. There is no
network use, no input, and no randomness, so every run produces the exact
same file. I verified the run locally, counted the characters, and checked
the file hash both with and without a trailing newline. The repository
also carries an MIT license file and a readme built from the bounty
template with all three badges linked to the bounty page.
