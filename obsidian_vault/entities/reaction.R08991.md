---
entity_id: "reaction.R08991"
entity_type: "reaction"
name: "cyclic bis(3->5')diguanylate 3-guanylylhydrolase"
source_database: "KEGG"
source_id: "R08991"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R08991"
---

# cyclic bis(3->5')diguanylate 3-guanylylhydrolase

`reaction.R08991`

## Static

- Type: `reaction`
- Source: `KEGG:R08991`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

3',5'-Cyclic diGMP + H2O 5'-Phosphoguanylyl(3'->5')guanosine

## Biological Role

Catalyzed by pdeL (protein.P21514), pdeA (protein.P23842), pdeC (protein.P32701), pdeH (protein.P37646), pdeK (protein.P37649), pdeI (protein.P75800), pdeG (protein.P75995), dosP (protein.P76129), and 5 more. Substrates: H2O (molecule.C00001), 3',5'-Cyclic diGMP (molecule.C16463).

## Annotation

3',5'-Cyclic diGMP + H2O <=> 5'-Phosphoguanylyl(3'->5')guanosine

## Outgoing Edges (0)

_None._

## Incoming Edges (15)

- `catalyzes` <-- [[protein.P21514|protein.P21514]] `KEGG` `database` - via EC:3.1.4.52
- `catalyzes` <-- [[protein.P23842|protein.P23842]] `KEGG` `database` - via EC:3.1.4.52
- `catalyzes` <-- [[protein.P32701|protein.P32701]] `KEGG` `database` - via EC:3.1.4.52
- `catalyzes` <-- [[protein.P37646|protein.P37646]] `KEGG` `database` - via EC:3.1.4.52
- `catalyzes` <-- [[protein.P37649|protein.P37649]] `KEGG` `database` - via EC:3.1.4.52
- `catalyzes` <-- [[protein.P75800|protein.P75800]] `KEGG` `database` - via EC:3.1.4.52
- `catalyzes` <-- [[protein.P75995|protein.P75995]] `KEGG` `database` - via EC:3.1.4.52
- `catalyzes` <-- [[protein.P76129|protein.P76129]] `KEGG` `database` - via EC:3.1.4.52
- `catalyzes` <-- [[protein.P76261|protein.P76261]] `KEGG` `database` - via EC:3.1.4.52
- `catalyzes` <-- [[protein.P76446|protein.P76446]] `KEGG` `database` - via EC:3.1.4.52
- `catalyzes` <-- [[protein.P77172|protein.P77172]] `KEGG` `database` - via EC:3.1.4.52
- `catalyzes` <-- [[protein.P77334|protein.P77334]] `KEGG` `database` - via EC:3.1.4.52
- `catalyzes` <-- [[protein.P77473|protein.P77473]] `KEGG` `database` - via EC:3.1.4.52
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C16463 + C00001 <=> C18076
- `is_substrate_of` <-- [[molecule.C16463|molecule.C16463]] `KEGG` `database` - C16463 + C00001 <=> C18076

## External IDs

- `KEGG:R08991`

## Notes

EQUATION: C16463 + C00001 <=> C18076
