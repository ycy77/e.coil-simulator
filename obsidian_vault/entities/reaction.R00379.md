---
entity_id: "reaction.R00379"
entity_type: "reaction"
name: "deoxynucleoside triphosphate:DNA deoxynucleotidyltransferase"
source_database: "KEGG"
source_id: "R00379"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00379"
---

# deoxynucleoside triphosphate:DNA deoxynucleotidyltransferase

`reaction.R00379`

## Static

- Type: `reaction`
- Source: `KEGG:R00379`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Deoxynucleoside triphosphate + DNA(n) Diphosphate + DNA(n+1)

## Biological Role

Catalyzed by polA (protein.P00582), dnaQ (protein.P03007), dnaX (protein.P06710), dnaN (protein.P0A988), holE (protein.P0ABS8), dnaE (protein.P10443), polB (protein.P21189), holA (protein.P28630), and 4 more. Substrates: DNA (molecule.C00039). Products: Diphosphate (molecule.C00013), DNA (molecule.C00039).

## Annotation

Deoxynucleoside triphosphate + DNA(n) <=> Diphosphate + DNA(n+1)

## Outgoing Edges (0)

_None._

## Incoming Edges (15)

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
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `KEGG` `database` - C00677 + C00039(n) <=> C00013 + C00039(n+1)
- `is_product_of` <-- [[molecule.C00039|molecule.C00039]] `KEGG` `database` - C00677 + C00039(n) <=> C00013 + C00039(n+1)
- `is_substrate_of` <-- [[molecule.C00039|molecule.C00039]] `KEGG` `database` - C00677 + C00039(n) <=> C00013 + C00039(n+1)

## External IDs

- `KEGG:R00379`

## Notes

EQUATION: C00677 + C00039(n) <=> C00013 + C00039(n+1)
