---
entity_id: "reaction.R07767"
entity_type: "reaction"
name: "[protein]-N6-(octanoyl)-L-lysine:an [Fe-S] cluster scaffold protein carrying a [4Fe-4S]2+ cluster sulfurtransferase"
source_database: "KEGG"
source_id: "R07767"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R07767"
---

# [protein]-N6-(octanoyl)-L-lysine:an [Fe-S] cluster scaffold protein carrying a [4Fe-4S]2+ cluster sulfurtransferase

`reaction.R07767`

## Static

- Type: `reaction`
- Source: `KEGG:R07767`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

[Protein]-N6-(octanoyl)-L-lysine + [Fe-S] cluster scaffold protein carrying a [4Fe-4S]2+ cluster + 2 S-Adenosyl-L-methionine + 2 Reduced [2Fe-2S] ferredoxin + 8 H+ [Protein]-N6-[(R)-dihydrolipoyl]-L-lysine + [Fe-S] cluster scaffold protein + 2 Hydrogen sulfide + 4 Fe2+ + 2 L-Methionine + 2 5'-Deoxyadenosine + 2 Oxidized [2Fe-2S] ferredoxin

## Biological Role

Catalyzed by lipA (protein.P60716). Substrates: S-Adenosyl-L-methionine (molecule.C00019), H+ (molecule.C00080). Products: L-Methionine (molecule.C00073), Hydrogen sulfide (molecule.C00283), Fe2+ (molecule.C14818).

## Annotation

[Protein]-N6-(octanoyl)-L-lysine + [Fe-S] cluster scaffold protein carrying a [4Fe-4S]2+ cluster + 2 S-Adenosyl-L-methionine + 2 Reduced [2Fe-2S] ferredoxin + 8 H+ <=> [Protein]-N6-[(R)-dihydrolipoyl]-L-lysine + [Fe-S] cluster scaffold protein + 2 Hydrogen sulfide + 4 Fe2+ + 2 L-Methionine + 2 5'-Deoxyadenosine + 2 Oxidized [2Fe-2S] ferredoxin

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P60716|protein.P60716]] `KEGG` `database` - via EC:2.8.1.8
- `is_product_of` <-- [[molecule.C00073|molecule.C00073]] `KEGG` `database` - C16236 + C22154 + 2 C00019 + 2 C22150 + 8 C00080 <=> C16832 + C22155 + 2 C00283 + 4 C14818 + 2 C00073 + 2 C05198 + 2 C22151
- `is_product_of` <-- [[molecule.C00283|molecule.C00283]] `KEGG` `database` - C16236 + C22154 + 2 C00019 + 2 C22150 + 8 C00080 <=> C16832 + C22155 + 2 C00283 + 4 C14818 + 2 C00073 + 2 C05198 + 2 C22151
- `is_product_of` <-- [[molecule.C14818|molecule.C14818]] `KEGG` `database` - C16236 + C22154 + 2 C00019 + 2 C22150 + 8 C00080 <=> C16832 + C22155 + 2 C00283 + 4 C14818 + 2 C00073 + 2 C05198 + 2 C22151
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `KEGG` `database` - C16236 + C22154 + 2 C00019 + 2 C22150 + 8 C00080 <=> C16832 + C22155 + 2 C00283 + 4 C14818 + 2 C00073 + 2 C05198 + 2 C22151
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C16236 + C22154 + 2 C00019 + 2 C22150 + 8 C00080 <=> C16832 + C22155 + 2 C00283 + 4 C14818 + 2 C00073 + 2 C05198 + 2 C22151

## External IDs

- `KEGG:R07767`

## Notes

EQUATION: C16236 + C22154 + 2 C00019 + 2 C22150 + 8 C00080 <=> C16832 + C22155 + 2 C00283 + 4 C14818 + 2 C00073 + 2 C05198 + 2 C22151
