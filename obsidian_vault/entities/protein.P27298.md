---
entity_id: "protein.P27298"
entity_type: "protein"
name: "prlC"
source_database: "UniProt"
source_id: "P27298"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "prlC opdA b3498 JW3465"
---

# prlC

`protein.P27298`

## Static

- Type: `protein`
- Source: `UniProt:P27298`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: May play a specific role in the degradation of signal peptides after they are released from precursor forms of secreted proteins. Can cleave N-acetyl-L-Ala(4). Oligopeptidase A is a cytoplasmic protease with broad specificity. It was originally identified as a suppressor of signal sequence mutants and thus may be involved in degradation of signal peptides . Oligoeptidase A appears shortly before DNA synthesis in at least some strains and may be involved in the onset of DNA replication, as treatment of cells with an inhibitor of Oligopeptidase A prevents cell division . Oligopeptidase A may also be partially reponsible for degradation of signal peptides . Oligopeptidase A catalyzes broad-specificity hydrolysis of peptide bonds. In hydrolysis of bonds in signal sequence peptides, some specificity is seen for cleavage near alanine and glycine .

## Biological Role

Catalyzes 3.4.24.70-RXN (reaction.ecocyc.3.4.24.70-RXN).

## Annotation

FUNCTION: May play a specific role in the degradation of signal peptides after they are released from precursor forms of secreted proteins. Can cleave N-acetyl-L-Ala(4).

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.3.4.24.70-RXN|reaction.ecocyc.3.4.24.70-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3498|gene.b3498]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P27298`
- `KEGG:ecj:JW3465;eco:b3498;ecoc:C3026_18945;`
- `GeneID:948016;`
- `GO:GO:0004222; GO:0005737; GO:0005829; GO:0006260; GO:0006465; GO:0006508; GO:0006518; GO:0008233; GO:0046872`
- `EC:3.4.24.70`

## Notes

Oligopeptidase A (EC 3.4.24.70)
