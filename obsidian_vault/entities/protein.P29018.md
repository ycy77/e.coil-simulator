---
entity_id: "protein.P29018"
entity_type: "protein"
name: "cydD"
source_database: "UniProt"
source_id: "P29018"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15470119, ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15470119}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "cydD htrD b0887 JW0870"
---

# cydD

`protein.P29018`

## Static

- Type: `protein`
- Source: `UniProt:P29018`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15470119, ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15470119}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex CydDC that exports the reduced low-molecular-weight thiols cysteine and glutathione to the periplasm (PubMed:12393891, PubMed:16040611). Export of these thiol-containing redox-active molecules may be crucial for redox homeostasis in the periplasm, permitting correct assembly of various respiratory complexes and formation of correct disulfide bonds in periplasmic and secreted proteins (Probable). CydD contains transmembrane domains (TMD), which form a pore in the inner membrane, and an ATP-binding domain (NBD), which is responsible for energy generation (PubMed:24958725). Required for the assembly of functional cytochrome bd-type quinol oxidases and periplasmic c-type cytochromes (PubMed:15470119, PubMed:7934832, PubMed:8181727). Overexpression of CydDC under anaerobic conditions also results in the formation of a heme biosynthesis-derived pigment, P-574 (PubMed:12375104). CydDC binds heme b, but heme is probably not transported by the complex and instead has a role in regulating ATPase activity (PubMed:24958725). {ECO:0000269|PubMed:12375104, ECO:0000269|PubMed:12393891, ECO:0000269|PubMed:15470119, ECO:0000269|PubMed:16040611, ECO:0000269|PubMed:24958725, ECO:0000269|PubMed:7934832, ECO:0000269|PubMed:8181727, ECO:0000305|PubMed:12393891, ECO:0000305|PubMed:16040611, ECO:0000305|PubMed:31279084}...

## Biological Role

Component of heme ABC transporter CydDC (complex.ecocyc.ABC-6-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex CydDC that exports the reduced low-molecular-weight thiols cysteine and glutathione to the periplasm (PubMed:12393891, PubMed:16040611). Export of these thiol-containing redox-active molecules may be crucial for redox homeostasis in the periplasm, permitting correct assembly of various respiratory complexes and formation of correct disulfide bonds in periplasmic and secreted proteins (Probable). CydD contains transmembrane domains (TMD), which form a pore in the inner membrane, and an ATP-binding domain (NBD), which is responsible for energy generation (PubMed:24958725). Required for the assembly of functional cytochrome bd-type quinol oxidases and periplasmic c-type cytochromes (PubMed:15470119, PubMed:7934832, PubMed:8181727). Overexpression of CydDC under anaerobic conditions also results in the formation of a heme biosynthesis-derived pigment, P-574 (PubMed:12375104). CydDC binds heme b, but heme is probably not transported by the complex and instead has a role in regulating ATPase activity (PubMed:24958725). {ECO:0000269|PubMed:12375104, ECO:0000269|PubMed:12393891, ECO:0000269|PubMed:15470119, ECO:0000269|PubMed:16040611, ECO:0000269|PubMed:24958725, ECO:0000269|PubMed:7934832, ECO:0000269|PubMed:8181727, ECO:0000305|PubMed:12393891, ECO:0000305|PubMed:16040611, ECO:0000305|PubMed:31279084}.; FUNCTION: Conversely, a more recent study suggests an alternative function of CydDC: authors suggest that CydDC does not mediate the export of L-cysteine but rather reduces cytoplasmic L-cystine to L-cysteine (PubMed:32900959). The principle function of CydDC would be to maintain the reduced state of cytoplasmic L-cysteine, thereby providing an important connection between sulfur metabolism, oxidative stress and resistance to antibiotics (PubMed:32900959). {ECO:0000269|PubMed:32900959}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-6-CPLX|complex.ecocyc.ABC-6-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b0887|gene.b0887]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P29018`
- `KEGG:ecj:JW0870;eco:b0887;ecoc:C3026_05500;`
- `GeneID:949052;`
- `GO:GO:0005524; GO:0005886; GO:0015439; GO:0016887; GO:0033228; GO:0034040; GO:0034775; GO:0035351; GO:0043190; GO:0045454; GO:0055051; GO:0055085; GO:1903605`
- `EC:7.4.2.-`

## Notes

Glutathione/L-cysteine transport system ATP-binding/permease protein CydD (EC 7.4.2.-)
