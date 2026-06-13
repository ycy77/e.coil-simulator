---
entity_id: "protein.P75948"
entity_type: "protein"
name: "thiK"
source_database: "UniProt"
source_id: "P75948"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "thiK ycfN b1106 JW1092"
---

# thiK

`protein.P75948`

## Static

- Type: `protein`
- Source: `UniProt:P75948`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the ATP-dependent phosphorylation of thiamine to thiamine phosphate. Is involved in thiamine salvage. {ECO:0000269|PubMed:15150256}. Thiamine kinase (ThiK) catalyzes the phosphorylation of the hydroxyl group of thiamin. This enzyme is a salvage enzyme and enables the cell to use recycled thiamin as an alternative to its synthesis de novo. The thiK locus was mapped , and the ycfN open reading frame was identified as the structural gene encoding thiamine kinase. The gene was overexpressed as a His10-tagged protein, but the protein was present primarily in inclusion bodies, was unstable, and lost all activity during purification, although assays performed with cell extracts showed significant thiamine kinase activity . The Keio collection thiK mutant is sensitive to lithium (<90% growth at 100mM Li) . Orthologs of ThiK have so far only been found in the γ proteobacteria.

## Biological Role

Catalyzes ATP:thiamine phosphotransferase (reaction.R02134), THIKIN-RXN (reaction.ecocyc.THIKIN-RXN). Bound by Magnesium cation (molecule.C00305).

## Enriched Pathways

- `eco00730` Thiamine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalyzes the ATP-dependent phosphorylation of thiamine to thiamine phosphate. Is involved in thiamine salvage. {ECO:0000269|PubMed:15150256}.

## Pathways

- `eco00730` Thiamine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R02134|reaction.R02134]] `KEGG` `database` - via EC:2.7.1.89
- `catalyzes` --> [[reaction.ecocyc.THIKIN-RXN|reaction.ecocyc.THIKIN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b1106|gene.b1106]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P75948`
- `KEGG:ecj:JW1092;eco:b1106;ecoc:C3026_06675;`
- `GeneID:75203692;948525;`
- `GO:GO:0005524; GO:0006772; GO:0009229; GO:0019165`
- `EC:2.7.1.89`

## Notes

Thiamine kinase (EC 2.7.1.89)
