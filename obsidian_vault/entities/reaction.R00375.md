---
entity_id: "reaction.R00375"
entity_type: "reaction"
name: "deoxyadenosine 5'-triphosphate:DNA deoxynucleotidyltransferase (DNA-directed)"
source_database: "KEGG"
source_id: "R00375"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00375"
---

# deoxyadenosine 5'-triphosphate:DNA deoxynucleotidyltransferase (DNA-directed)

`reaction.R00375`

## Static

- Type: `reaction`
- Source: `KEGG:R00375`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

dATP + DNA Diphosphate + DNA

## Biological Role

Catalyzed by polA (protein.P00582), dnaQ (protein.P03007), dnaX (protein.P06710), dnaN (protein.P0A988), holE (protein.P0ABS8), dnaE (protein.P10443), polB (protein.P21189), holA (protein.P28630), and 4 more. Substrates: DNA (molecule.C00039), dATP (molecule.C00131). Products: Diphosphate (molecule.C00013), DNA (molecule.C00039).

## Annotation

dATP + DNA <=> Diphosphate + DNA

## Outgoing Edges (0)

_None._

## Incoming Edges (16)

- `catalyzes` <-- [[protein.P00582|protein.P00582]] `KEGG` `database` - via EC:2.7.7.7
- `catalyzes` <-- [[protein.P03007|protein.P03007]] `KEGG` `database` - via EC:2.7.7.7
- `catalyzes` <-- [[protein.P06710|protein.P06710]] `KEGG` `database` - via EC:2.7.7.7
- `catalyzes` <-- [[protein.P0A988|protein.P0A988]] `KEGG` `database` - via EC:2.7.7.7
- `catalyzes` <-- [[protein.P0ABS8|protein.P0ABS8]] `KEGG` `database` - via EC:2.7.7.7
- `catalyzes` <-- [[protein.P10443|protein.P10443]] `KEGG` `database` - via EC:2.7.7.7
- `catalyzes` <-- [[protein.P21189|protein.P21189]] `KEGG` `database` - via EC:2.7.7.7
- `catalyzes` <-- [[protein.P28630|protein.P28630]] `KEGG` `database` - via EC:2.7.7.7
- `catalyzes` <-- [[protein.P28631|protein.P28631]] `KEGG` `database` - via EC:2.7.7.7
- `catalyzes` <-- [[protein.P28632|protein.P28632]] `KEGG` `database` - via EC:2.7.7.7
- `catalyzes` <-- [[protein.P28905|protein.P28905]] `KEGG` `database` - via EC:2.7.7.7
- `catalyzes` <-- [[protein.Q47155|protein.Q47155]] `KEGG` `database` - via EC:2.7.7.7
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `KEGG` `database` - C00131 + C00039 <=> C00013 + C00039
- `is_product_of` <-- [[molecule.C00039|molecule.C00039]] `KEGG` `database` - C00131 + C00039 <=> C00013 + C00039
- `is_substrate_of` <-- [[molecule.C00039|molecule.C00039]] `KEGG` `database` - C00131 + C00039 <=> C00013 + C00039
- `is_substrate_of` <-- [[molecule.C00131|molecule.C00131]] `KEGG` `database` - C00131 + C00039 <=> C00013 + C00039

## External IDs

- `KEGG:R00375`

## Notes

EQUATION: C00131 + C00039 <=> C00013 + C00039
