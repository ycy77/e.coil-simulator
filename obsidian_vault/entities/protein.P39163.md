---
entity_id: "protein.P39163"
entity_type: "protein"
name: "chaC"
source_database: "UniProt"
source_id: "P39163"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "chaC b1218 JW1209"
---

# chaC

`protein.P39163`

## Static

- Type: `protein`
- Source: `UniProt:P39163`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the cleavage of glutathione into 5-oxo-L-proline and a Cys-Gly dipeptide. Acts specifically on glutathione, but not on other gamma-glutamyl peptides. {ECO:0000269|PubMed:27913623}. ChaC is a γ-glutamylcyclotransferase with relatively low catalytic efficiency . Expression of chaC enables growth on glutathione of a mutant yeast organic sulphur auxotroph that can not utilize glutathione and γ-glu amino acids . A chaC mutant shows a defect in swarming motility, but no significant defect in swimming motility .

## Biological Role

Catalyzes RXN-19024 (reaction.ecocyc.RXN-19024).

## Enriched Pathways

- `eco00480` Glutathione metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalyzes the cleavage of glutathione into 5-oxo-L-proline and a Cys-Gly dipeptide. Acts specifically on glutathione, but not on other gamma-glutamyl peptides. {ECO:0000269|PubMed:27913623}.

## Pathways

- `eco00480` Glutathione metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-19024|reaction.ecocyc.RXN-19024]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1218|gene.b1218]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P39163`
- `KEGG:ecj:JW1209;eco:b1218;ecoc:C3026_07165;`
- `GeneID:945793;`
- `GO:GO:0003839; GO:0005737; GO:0006751; GO:0061928`
- `EC:4.3.2.7`

## Notes

Glutathione-specific gamma-glutamylcyclotransferase (Gamma-GCG) (EC 4.3.2.7) (Cation transport regulatory protein ChaC)
