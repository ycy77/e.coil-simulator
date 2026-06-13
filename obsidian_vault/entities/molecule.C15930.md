---
entity_id: "molecule.C15930"
entity_type: "small_molecule"
name: "L-Galactonate"
source_database: "KEGG"
source_id: "C15930"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "L-Galactonate"
  - "L-Galactonic acid"
---

# L-Galactonate

`molecule.C15930`

## Static

- Type: `small_molecule`
- Source: `KEGG:C15930`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: L-Galactonate; L-Galactonic acid

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00053` Ascorbate and aldarate metabolism (KEGG)

## Annotation

KEGG compound: L-Galactonate; L-Galactonic acid

## Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00053` Ascorbate and aldarate metabolism (KEGG)

## Outgoing Edges (5)

- `is_product_of` --> [[reaction.ecocyc.RXN-11152|reaction.ecocyc.RXN-11152]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-227|reaction.ecocyc.TRANS-RXN0-227]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R12146|reaction.R12146]] `KEGG` `database` - C15930 + C00003 <=> C00558 + C00004 + C00080
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5229|reaction.ecocyc.RXN0-5229]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-227|reaction.ecocyc.TRANS-RXN0-227]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (1)

- `transports` <-- [[protein.P39398|protein.P39398]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C15930`
- `EcoCyc:CPD0-1083`
- `HMDB:HMDB0253886`
- `ZINC:ZINC000001532586`
- `SEED:cpd14659`
- `METANETX:MNXM636`
- `BIGG:galctn__L`
- `CHEBI:53071`
- `PUBCHEM:44229140`
- `LIGAND-CPD:c15930`
- `canonicalized_from:molecule.ecocyc.CPD0-1083`

## Notes

Included because it appears in at least one E. coli KEGG pathway. | molecule.ecocyc.CPD0-1083: EcoCyc:CPD0-1083
