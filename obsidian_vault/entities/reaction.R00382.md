---
entity_id: "reaction.R00382"
entity_type: "reaction"
name: "(deoxyribonucleotide)n:5'-phospho-(deoxyribonucleotide)m ligase (AMP-forming, NMN-forming)"
source_database: "KEGG"
source_id: "R00382"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00382"
---

# (deoxyribonucleotide)n:5'-phospho-(deoxyribonucleotide)m ligase (AMP-forming, NMN-forming)

`reaction.R00382`

## Static

- Type: `reaction`
- Source: `KEGG:R00382`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

NAD+ + DNA(n) + 5'-Phospho-DNA(m) AMP + Nicotinamide D-ribonucleotide + DNA(n+m)

## Biological Role

Catalyzed by ligA (protein.P15042), ligB (protein.P25772). Substrates: NAD+ (molecule.C00003), DNA (molecule.C00039). Products: AMP (molecule.C00020), DNA (molecule.C00039), Nicotinamide D-ribonucleotide (molecule.C00455).

## Annotation

NAD+ + DNA(n) + 5'-Phospho-DNA(m) <=> AMP + Nicotinamide D-ribonucleotide + DNA(n+m)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P15042|protein.P15042]] `KEGG` `database` - via EC:6.5.1.2
- `catalyzes` <-- [[protein.P25772|protein.P25772]] `KEGG` `database` - via EC:6.5.1.2
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `KEGG` `database` - C00003 + C00039(n) + C02128(m) <=> C00020 + C00455 + C00039(n+m)
- `is_product_of` <-- [[molecule.C00039|molecule.C00039]] `KEGG` `database` - C00003 + C00039(n) + C02128(m) <=> C00020 + C00455 + C00039(n+m)
- `is_product_of` <-- [[molecule.C00455|molecule.C00455]] `KEGG` `database` - C00003 + C00039(n) + C02128(m) <=> C00020 + C00455 + C00039(n+m)
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `KEGG` `database` - C00003 + C00039(n) + C02128(m) <=> C00020 + C00455 + C00039(n+m)
- `is_substrate_of` <-- [[molecule.C00039|molecule.C00039]] `KEGG` `database` - C00003 + C00039(n) + C02128(m) <=> C00020 + C00455 + C00039(n+m)

## External IDs

- `KEGG:R00382`

## Notes

EQUATION: C00003 + C00039(n) + C02128(m) <=> C00020 + C00455 + C00039(n+m)
