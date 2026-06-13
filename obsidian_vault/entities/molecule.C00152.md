---
entity_id: "molecule.C00152"
entity_type: "small_molecule"
name: "L-Asparagine"
source_database: "KEGG"
source_id: "C00152"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "L-Asparagine"
  - "2-Aminosuccinamic acid"
---

# L-Asparagine

`molecule.C00152`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00152`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: L-Asparagine; 2-Aminosuccinamic acid ASN "Asparagine" (Asn) is one of the proteinogenic amino acids. It was the first proteinogenic amino acid to be isolated, back in 1806, from asparagus juice, hence its name. The accurate structure of the molecule was reported only in 1888 . Piutti also discovered the existence of CPD-3633 two years earlier .

## Biological Role

Consumed as substrate in 7 reaction(s). Produced in 7 reaction(s).

## Enriched Pathways

- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00460` Cyanoamino acid metabolism (KEGG)
- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Annotation

KEGG compound: L-Asparagine; 2-Aminosuccinamic acid

## Pathways

- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00460` Cyanoamino acid metabolism (KEGG)
- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Outgoing Edges (17)

- `activates` --> [[reaction.ecocyc.ASPARAGHYD-RXN|reaction.ecocyc.ASPARAGHYD-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `is_component_of` --> [[complex.ecocyc.CPLX0-7735|complex.ecocyc.CPLX0-7735]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_product_of` --> [[reaction.R00483|reaction.R00483]] `KEGG` `database` - C00002 + C00049 + C00014 <=> C00020 + C00013 + C00152
- `is_product_of` --> [[reaction.R00578|reaction.R00578]] `KEGG` `database` - C00002 + C00049 + C00064 + C00001 <=> C00020 + C00013 + C00152 + C00025
- `is_product_of` --> [[reaction.ecocyc.ASNSYNA-RXN|reaction.ecocyc.ASNSYNA-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.ASNSYNB-RXN|reaction.ecocyc.ASNSYNB-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-22734|reaction.ecocyc.RXN-22734]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-6982|reaction.ecocyc.RXN0-6982]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-262|reaction.ecocyc.TRANS-RXN-262]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00485|reaction.R00485]] `KEGG` `database` - C00152 + C00001 <=> C00049 + C00014
- `is_substrate_of` --> [[reaction.ecocyc.ASPARAGHYD-RXN|reaction.ecocyc.ASPARAGHYD-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.ASPARAGINE--TRNA-LIGASE-RXN|reaction.ecocyc.ASPARAGINE--TRNA-LIGASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-21104|reaction.ecocyc.RXN-21104]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-23528|reaction.ecocyc.RXN-23528]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5454|reaction.ecocyc.RXN0-5454]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-262|reaction.ecocyc.TRANS-RXN-262]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.ASNSYNA-RXN|reaction.ecocyc.ASNSYNA-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (1)

- `transports` <-- [[protein.P77610|protein.P77610]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00152`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
