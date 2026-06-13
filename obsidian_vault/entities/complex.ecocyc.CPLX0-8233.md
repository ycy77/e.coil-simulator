---
entity_id: "complex.ecocyc.CPLX0-8233"
entity_type: "complex"
name: "pseudouridine-5'-phosphate glycosidase"
source_database: "EcoCyc"
source_id: "CPLX0-8233"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# pseudouridine-5'-phosphate glycosidase

`complex.ecocyc.CPLX0-8233`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8233`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P33025|protein.P33025]]

## Enriched Summary

PsuG is a pseudouridine-5'-phosphate glycosidase . The activity was first described for YeiN from the uropathogenic E. coli UTI89 . Crystal structures of wild type and mutant forms of PsuG have been solved. Active site residues were identified both within the structure and by site-directed mutagenesis, and a reaction mechanism was proposed . PscG: "pseudouridine catabolism, glycosidase" PsuG: "pseudouridine catabolism, glycosidase" PsuG is a pseudouridine-5'-phosphate glycosidase . The activity was first described for YeiN from the uropathogenic E. coli UTI89 . Crystal structures of wild type and mutant forms of PsuG have been solved. Active site residues were identified both within the structure and by site-directed mutagenesis, and a reaction mechanism was proposed . PscG: "pseudouridine catabolism, glycosidase" PsuG: "pseudouridine catabolism, glycosidase"

## Biological Role

Catalyzes RXN0-5398 (reaction.ecocyc.RXN0-5398). Bound by Mn2+ (molecule.ecocyc.MN_2).

## Annotation

PsuG is a pseudouridine-5'-phosphate glycosidase . The activity was first described for YeiN from the uropathogenic E. coli UTI89 . Crystal structures of wild type and mutant forms of PsuG have been solved. Active site residues were identified both within the structure and by site-directed mutagenesis, and a reaction mechanism was proposed . PscG: "pseudouridine catabolism, glycosidase" PsuG: "pseudouridine catabolism, glycosidase"

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5398|reaction.ecocyc.RXN0-5398]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P33025|protein.P33025]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3

## External IDs

- `EcoCyc:CPLX0-8233`
- `QSPROTEOME:QS00183287`

## Notes

3*protein.P33025
