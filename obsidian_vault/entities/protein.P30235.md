---
entity_id: "protein.P30235"
entity_type: "protein"
name: "psuK"
source_database: "UniProt"
source_id: "P30235"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "psuK pscK yeiC b2166 JW2153"
---

# psuK

`protein.P30235`

## Static

- Type: `protein`
- Source: `UniProt:P30235`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the phosphorylation of pseudouridine to pseudouridine 5'-phosphate (PsiMP). {ECO:0000269|PubMed:18591240}. E. coli strains B and W were shown to contain a pseudouridine kinase activity and are able to grow on pseudouridine as the sole source of pyrimidine . YeiC from the uropathogenic E. coli UTI89 is a pseudouridine kinase; yeiC is the most highly induced gene when UTI89 is grown on human urine . The crystal structures of apo-PsuK and PsuK complexed with Ψ or N1-methyl-pseudouridine (m1Ψ) were characterized from E. coli strain BL21 (DE3) . PscK: "pseudouridine catabolism, kinase" PsuK: "pseudouridine catabolism, kinase"

## Biological Role

Catalyzes PSEUDOURIDINE-KINASE-RXN (reaction.ecocyc.PSEUDOURIDINE-KINASE-RXN).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalyzes the phosphorylation of pseudouridine to pseudouridine 5'-phosphate (PsiMP). {ECO:0000269|PubMed:18591240}.

## Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.PSEUDOURIDINE-KINASE-RXN|reaction.ecocyc.PSEUDOURIDINE-KINASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2166|gene.b2166]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P30235`
- `KEGG:ecj:JW2153;eco:b2166;ecoc:C3026_12135;`
- `GeneID:946664;`
- `GO:GO:0005524; GO:0050225`
- `EC:2.7.1.83`

## Notes

Pseudouridine kinase (EC 2.7.1.83)
