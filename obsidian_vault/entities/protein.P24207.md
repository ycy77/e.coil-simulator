---
entity_id: "protein.P24207"
entity_type: "protein"
name: "pheP"
source_database: "UniProt"
source_id: "P24207"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:8626334, ECO:0000269|PubMed:9791098}; Multi-pass membrane protein {ECO:0000269|PubMed:8626334}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pheP b0576 JW0565"
---

# pheP

`protein.P24207`

## Static

- Type: `protein`
- Source: `UniProt:P24207`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:8626334, ECO:0000269|PubMed:9791098}; Multi-pass membrane protein {ECO:0000269|PubMed:8626334}.

## Enriched Summary

FUNCTION: Permease that is involved in the active transport across the cytoplasmic membrane of phenylalanine (PubMed:10735864, PubMed:1711024, PubMed:8226700, PubMed:9791098). Can also transport tyrosine, but not tryptophan (PubMed:10735864). {ECO:0000269|PubMed:10735864, ECO:0000269|PubMed:1711024, ECO:0000269|PubMed:8226700, ECO:0000269|PubMed:9791098}. PheP is a phenylalanine transporter that is a member of the Amino Acid-Polyamine-Organocation (APC) Superfamily of transporters . Complementation of a pheP mutant restored phenylalanine-specific transport activity, indicating that PheP is normally responsible for phenylalanine transport . Experiments with oxidative phosphorylation uncouplers and E. coli strains deficient in the F0F1-ATPase suggest that PheP-mediated transport is driven by the proton motive force . PheP probably functions as a phenylalanine/proton symporter. PheP shares sequence similarity with AroP, which is a general aromatic amino acid transport system, responsible for phenylalanine, tyrosine, and tryptophan transport . Hydropathy analysis and PhoA fusion suggests that PheP has a 12 transmembrane segment topology .

## Biological Role

Catalyzes phenylalanine:proton symport (reaction.ecocyc.TRANS-RXN-56).

## Annotation

FUNCTION: Permease that is involved in the active transport across the cytoplasmic membrane of phenylalanine (PubMed:10735864, PubMed:1711024, PubMed:8226700, PubMed:9791098). Can also transport tyrosine, but not tryptophan (PubMed:10735864). {ECO:0000269|PubMed:10735864, ECO:0000269|PubMed:1711024, ECO:0000269|PubMed:8226700, ECO:0000269|PubMed:9791098}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-56|reaction.ecocyc.TRANS-RXN-56]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0576|gene.b0576]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P24207`
- `KEGG:ecj:JW0565;eco:b0576;ecoc:C3026_02860;`
- `GeneID:945199;`
- `GO:GO:0005886; GO:0006865; GO:0015823; GO:0022857`

## Notes

Phenylalanine-specific permease (Phenylalanine:H(+) symporter PheP)
