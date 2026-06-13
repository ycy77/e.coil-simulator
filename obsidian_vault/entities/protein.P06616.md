---
entity_id: "protein.P06616"
entity_type: "protein"
name: "era"
source_database: "UniProt"
source_id: "P06616"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:8282709}. Cell inner membrane {ECO:0000269|PubMed:8282709}; Peripheral membrane protein {ECO:0000269|PubMed:8282709}; Cytoplasmic side {ECO:0000269|PubMed:8282709}. Note=Binding is GDP or GTP-dependent, slightly more protein is bound in the presence of GTP than GDP."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "era rbaA sdgE b2566 JW2550"
---

# era

`protein.P06616`

## Static

- Type: `protein`
- Source: `UniProt:P06616`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:8282709}. Cell inner membrane {ECO:0000269|PubMed:8282709}; Peripheral membrane protein {ECO:0000269|PubMed:8282709}; Cytoplasmic side {ECO:0000269|PubMed:8282709}. Note=Binding is GDP or GTP-dependent, slightly more protein is bound in the presence of GTP than GDP.

## Enriched Summary

FUNCTION: An essential GTPase that binds both GDP and GTP, with nucleotide exchange occurring on the order of seconds whereas hydrolysis occurs on the order of minutes. Plays a role in numerous processes, including cell cycle regulation, energy metabolism, as a chaperone for 16S rRNA processing and 30S ribosomal subunit biogenesis. One of at least 4 proteins (Era, RbfA, RimM and RsgA/YjeQ) that assist in the late assembly stage of the 30S ribosomal subunit. Its presence in the 30S subunit may prevent translation initiation. Seems to be critical for maintaining cell growth and cell divison rates; a dramatic reduction in Era protein levels temporarily arrests cell growth just before cytokinesis (at the predivisional two-cell stage) and delays cell division. Era mutant era1 suppresses some temperature-sensitive mutations that affect DNA replication and chromosome partitioning and segregation. The dominant-negative Era-de mutant which is missing residues in a putative effector region, is unable to complement the disruption mutant; upon overproduction it shows a significant decrease in cell viability and a synthetic lethal phenotype in the presence of acetate. Era function probably overlaps RbfA (PubMed:16825789). Binds to the pre-30S ribosomal subunit through several stages of protein assembly (PubMed:20188109)...

## Biological Role

Catalyzes RXN0-5462 (reaction.ecocyc.RXN0-5462).

## Annotation

FUNCTION: An essential GTPase that binds both GDP and GTP, with nucleotide exchange occurring on the order of seconds whereas hydrolysis occurs on the order of minutes. Plays a role in numerous processes, including cell cycle regulation, energy metabolism, as a chaperone for 16S rRNA processing and 30S ribosomal subunit biogenesis. One of at least 4 proteins (Era, RbfA, RimM and RsgA/YjeQ) that assist in the late assembly stage of the 30S ribosomal subunit. Its presence in the 30S subunit may prevent translation initiation. Seems to be critical for maintaining cell growth and cell divison rates; a dramatic reduction in Era protein levels temporarily arrests cell growth just before cytokinesis (at the predivisional two-cell stage) and delays cell division. Era mutant era1 suppresses some temperature-sensitive mutations that affect DNA replication and chromosome partitioning and segregation. The dominant-negative Era-de mutant which is missing residues in a putative effector region, is unable to complement the disruption mutant; upon overproduction it shows a significant decrease in cell viability and a synthetic lethal phenotype in the presence of acetate. Era function probably overlaps RbfA (PubMed:16825789). Binds to the pre-30S ribosomal subunit through several stages of protein assembly (PubMed:20188109). {ECO:0000269|PubMed:12753192, ECO:0000269|PubMed:16825789, ECO:0000269|PubMed:20188109, ECO:0000269|PubMed:9515700}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5462|reaction.ecocyc.RXN0-5462]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2566|gene.b2566]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P06616`
- `KEGG:ecj:JW2550;eco:b2566;ecoc:C3026_14215;`
- `GeneID:75172680;947036;`
- `GO:GO:0000028; GO:0003723; GO:0003924; GO:0005525; GO:0005737; GO:0005829; GO:0005886; GO:0006468; GO:0019843; GO:0042274; GO:0043024; GO:0070181; GO:0097216`

## Notes

GTPase Era (ERA) (GTP-binding protein Era)
