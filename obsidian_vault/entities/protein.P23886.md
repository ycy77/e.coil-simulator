---
entity_id: "protein.P23886"
entity_type: "protein"
name: "cydC"
source_database: "UniProt"
source_id: "P23886"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15470119, ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15470119}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "cydC mdrA mdrH surB b0886 JW0869"
---

# cydC

`protein.P23886`

## Static

- Type: `protein`
- Source: `UniProt:P23886`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15470119, ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15470119}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex CydDC that exports the reduced low-molecular-weight thiols cysteine and glutathione to the periplasm (PubMed:12393891, PubMed:16040611). Export of these thiol-containing redox-active molecules may be crucial for redox homeostasis in the periplasm, permitting correct assembly of various respiratory complexes and formation of correct disulfide bonds in periplasmic and secreted proteins (Probable). CydC contains transmembrane domains (TMD), which form a pore in the inner membrane, and an ATP-binding domain (NBD), which is responsible for energy generation (PubMed:24958725). Required for the assembly of functional cytochrome bd-type quinol oxidases and periplasmic c-type cytochromes (PubMed:15470119, PubMed:3032907, PubMed:7934832, PubMed:8181727). Overexpression of CydDC under anaerobic conditions also results in the formation of a heme biosynthesis-derived pigment, P-574 (PubMed:12375104). CydDC binds heme b, but heme is probably not transported by the complex and instead has a role in regulating ATPase activity (PubMed:24958725)...

## Biological Role

Component of heme ABC transporter CydDC (complex.ecocyc.ABC-6-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex CydDC that exports the reduced low-molecular-weight thiols cysteine and glutathione to the periplasm (PubMed:12393891, PubMed:16040611). Export of these thiol-containing redox-active molecules may be crucial for redox homeostasis in the periplasm, permitting correct assembly of various respiratory complexes and formation of correct disulfide bonds in periplasmic and secreted proteins (Probable). CydC contains transmembrane domains (TMD), which form a pore in the inner membrane, and an ATP-binding domain (NBD), which is responsible for energy generation (PubMed:24958725). Required for the assembly of functional cytochrome bd-type quinol oxidases and periplasmic c-type cytochromes (PubMed:15470119, PubMed:3032907, PubMed:7934832, PubMed:8181727). Overexpression of CydDC under anaerobic conditions also results in the formation of a heme biosynthesis-derived pigment, P-574 (PubMed:12375104). CydDC binds heme b, but heme is probably not transported by the complex and instead has a role in regulating ATPase activity (PubMed:24958725). {ECO:0000269|PubMed:12375104, ECO:0000269|PubMed:12393891, ECO:0000269|PubMed:15470119, ECO:0000269|PubMed:16040611, ECO:0000269|PubMed:24958725, ECO:0000269|PubMed:3032907, ECO:0000269|PubMed:7934832, ECO:0000269|PubMed:8181727, ECO:0000305|PubMed:12393891, ECO:0000305|PubMed:16040611, ECO:0000305|PubMed:31279084}.; FUNCTION: Conversely, a more recent study suggests an alternative function of CydDC: authors suggest that CydDC does not mediate the export of L-cysteine but rather reduces cytoplasmic L-cystine to L-cysteine (PubMed:32900959). The principle function of CydDC would be to maintain the reduced state of cytoplasmic L-cysteine, thereby providing an important connection between sulfur metabolism, oxidative stress and resistance to antibiotics (PubMed:32900959). {ECO:0000269|PubMed:32900959}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-6-CPLX|complex.ecocyc.ABC-6-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b0886|gene.b0886]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P23886`
- `KEGG:ecj:JW0869;eco:b0886;ecoc:C3026_05495;`
- `GeneID:945504;`
- `GO:GO:0005524; GO:0005886; GO:0015439; GO:0016887; GO:0033228; GO:0034775; GO:0035351; GO:0042626; GO:0043190; GO:0045454; GO:0055051; GO:1903605`
- `EC:7.4.2.-`

## Notes

Glutathione/L-cysteine transport system ATP-binding/permease protein CydC (EC 7.4.2.-)
