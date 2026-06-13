---
entity_id: "protein.P0AEJ8"
entity_type: "protein"
name: "eutN"
source_database: "UniProt"
source_id: "P0AEJ8"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Bacterial microcompartment {ECO:0000305|PubMed:17588214, ECO:0000305|PubMed:18292340}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "eutN cchB yffY b2456 JW2440"
---

# eutN

`protein.P0AEJ8`

## Static

- Type: `protein`
- Source: `UniProt:P0AEJ8`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Bacterial microcompartment {ECO:0000305|PubMed:17588214, ECO:0000305|PubMed:18292340}.

## Enriched Summary

FUNCTION: Probably forms vertices in the bacterial microcompartment (BMC) dedicated to ethanolamine degradation (Probable). It may be involved in transporting positively charged molecules into and out of the BMC (Probable). {ECO:0000305|PubMed:17588214, ECO:0000305|PubMed:23456886}. Several genes of the eut operon are involved in the ability to utilize ethanolamine as the sole source of carbon and nitrogen in Salmonella typhimurium; the operon is conserved between Salmonella and E. coli. EutN has not been shown to be involved in ethanolamine utilization in either Salmonella or E. coli . EutN is similar to the carboxysomal shell protein CcmL of Synechococcus sp. strain PCC7942 . A crystal structure of EutN has been solved at 2.4 Å resolution. The protein forms a tight hexamer with a central hole that is predominantly covered by acidic residues, suggesting a pore with a transport function . EutN: "ethanolamine utilization" CchB: "carbon dioxide concentration homolog B"

## Biological Role

Component of putative ethanolamine catabolic microcompartment shell protein EutN (complex.ecocyc.CPLX0-7613).

## Annotation

FUNCTION: Probably forms vertices in the bacterial microcompartment (BMC) dedicated to ethanolamine degradation (Probable). It may be involved in transporting positively charged molecules into and out of the BMC (Probable). {ECO:0000305|PubMed:17588214, ECO:0000305|PubMed:23456886}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7613|complex.ecocyc.CPLX0-7613]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## Incoming Edges (1)

- `encodes` <-- [[gene.b2456|gene.b2456]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AEJ8`
- `KEGG:ecj:JW2440;eco:b2456;ecoc:C3026_13630;`
- `GeneID:86947351;93774684;946945;`
- `GO:GO:0006974; GO:0031469; GO:0034214; GO:0042802; GO:0046336`

## Notes

Bacterial microcompartment shell vertex protein EutN (Ethanolamine catabolic microcompartment shell protein EutN) (Ethanolamine utilization protein EutN)
