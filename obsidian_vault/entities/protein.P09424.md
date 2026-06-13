---
entity_id: "protein.P09424"
entity_type: "protein"
name: "mtlD"
source_database: "UniProt"
source_id: "P09424"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mtlD b3600 JW3574"
---

# mtlD

`protein.P09424`

## Static

- Type: `protein`
- Source: `UniProt:P09424`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

Mannitol-1-phosphate 5-dehydrogenase (EC 1.1.1.17) Mannitol is the most common natural hexitol and can serve as a carbon source for E. coli. After entering the cell via a dedicated PTS transporter, mannitol-1-phosphate 5-dehydrogenase (MtlD) oxidizes mannitol-1-phosphate to fructose-6-phosphate in a reversible reaction . MtlD activity is induced by growth on mannitol. An mtlD mutant does not grow on mannitol as the sole carbon source . MtlD: "mannitol"

## Biological Role

Catalyzes D-mannitol-1-phosphate:NAD+ 5-oxidoreductase (reaction.R00758), MANNPDEHYDROG-RXN (reaction.ecocyc.MANNPDEHYDROG-RXN).

## Enriched Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

Mannitol-1-phosphate 5-dehydrogenase (EC 1.1.1.17)

## Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00758|reaction.R00758]] `KEGG` `database` - via EC:1.1.1.17
- `catalyzes` --> [[reaction.ecocyc.MANNPDEHYDROG-RXN|reaction.ecocyc.MANNPDEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3600|gene.b3600]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P09424`
- `KEGG:ecj:JW3574;eco:b3600;ecoc:C3026_19520;`
- `GeneID:948117;`
- `GO:GO:0005829; GO:0008926; GO:0019592`
- `EC:1.1.1.17`

## Notes

Mannitol-1-phosphate 5-dehydrogenase (EC 1.1.1.17)
