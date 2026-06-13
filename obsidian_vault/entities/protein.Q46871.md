---
entity_id: "protein.Q46871"
entity_type: "protein"
name: "yqjH"
source_database: "UniProt"
source_id: "Q46871"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yqjH b3070 JW3041"
---

# yqjH

`protein.Q46871`

## Static

- Type: `protein`
- Source: `UniProt:Q46871`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Plays a role in iron homeostasis under excess nickel conditions. {ECO:0000269|PubMed:21097627}. NfeF is an NADPH-dependent ferric reductase; the enzyme contains FAD that is used as a cofactor rather than a substrate. The enzyme is only weakly active with purified ferric enterobactin ; the hydrolyzed ferric enterobactin complex is the most efficient of the tested substrates . Reports disagree on whether the FAD cofactor is covalently bound to a cysteine sidechain via a thioether bond or not covalently attached . A preliminary report of crystallization and structure analysis of the NfeF protein has appeared. NfeF is structurally related to the NAD(P)H:flavin oxidoreductase superfamily . The reaction mechanism of NfeF has been investigated in detail; a transient flavosemiquinone is involved in the single-electron transfer in a double-displacement (ping-pong)-type reaction. The K55 and R130 residues are required for substrate binding and enzymatic activity. While the enzyme has high affinity for the intact ferric enterobactin, the catalytic turnover rate is much slower than for the hydrolyzed ferric triscatecholate . The slow growth phenotype of a fes deletion mutant is enhanced by deletion of nfeF, supporting a role for NfeF in adaptation to iron starvation. Deletion of nfeF increases the toxicity of nickel...

## Biological Role

Catalyzes RXN0-6555 (reaction.ecocyc.RXN0-6555), RXN0-6941 (reaction.ecocyc.RXN0-6941), RXN0-7313 (reaction.ecocyc.RXN0-7313).

## Annotation

FUNCTION: Plays a role in iron homeostasis under excess nickel conditions. {ECO:0000269|PubMed:21097627}.

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.RXN0-6555|reaction.ecocyc.RXN0-6555]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-6941|reaction.ecocyc.RXN0-6941]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7313|reaction.ecocyc.RXN0-7313]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3070|gene.b3070]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:Q46871`
- `KEGG:ecj:JW3041;eco:b3070;ecoc:C3026_16770;`
- `GeneID:947582;`
- `GO:GO:0005829; GO:0010106; GO:0015891; GO:0033212; GO:0033214; GO:0050660; GO:0052851; GO:0071289; GO:0071949`
- `EC:1.16.1.9`

## Notes

NADPH-dependent ferric-chelate reductase (EC 1.16.1.9) (Ferric siderophore reductase)
