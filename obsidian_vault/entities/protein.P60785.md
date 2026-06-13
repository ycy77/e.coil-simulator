---
entity_id: "protein.P60785"
entity_type: "protein"
name: "lepA"
source_database: "UniProt"
source_id: "P60785"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305|PubMed:2999765}; Peripheral membrane protein {ECO:0000305|PubMed:2999765}; Cytoplasmic side {ECO:0000305|PubMed:2999765}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "lepA b2569 JW2553"
---

# lepA

`protein.P60785`

## Static

- Type: `protein`
- Source: `UniProt:P60785`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305|PubMed:2999765}; Peripheral membrane protein {ECO:0000305|PubMed:2999765}; Cytoplasmic side {ECO:0000305|PubMed:2999765}.

## Enriched Summary

FUNCTION: Required for accurate and efficient protein synthesis under certain stress conditions. May act as a fidelity factor of the translation reaction, by catalyzing a one-codon backward translocation of tRNAs on improperly translocated ribosomes. Back-translocation proceeds from a post-translocation (POST) complex to a pre-translocation (PRE) complex, thus giving elongation factor G a second chance to translocate the tRNAs correctly. Binds to ribosomes in a GTP-dependent manner. {ECO:0000255|HAMAP-Rule:MF_00071, ECO:0000269|PubMed:17110332, ECO:0000269|PubMed:20045415}. EF4 (LepA) is a highly conserved protein whose function in translation is still controversial. The most recent results indicate that LepA functions in 30S ribosomal subunit biogenesis . Various experimental results that suggested functions in translation initiation or elongation are summarized below. EF4 competes with EF-G for binding to the ribosome and forms a complex that is an intermediate between the PRE and POST complexes, thus sequestering a catalytically active ribosome . EF4 induces back-translocation of the ribosome and prevents peptide bond formation exclusively in the post-translocation (POST) state of the ribosome. A kinetic model of back-translocation has been proposed...

## Biological Role

Catalyzes RXN0-5462 (reaction.ecocyc.RXN0-5462).

## Annotation

FUNCTION: Required for accurate and efficient protein synthesis under certain stress conditions. May act as a fidelity factor of the translation reaction, by catalyzing a one-codon backward translocation of tRNAs on improperly translocated ribosomes. Back-translocation proceeds from a post-translocation (POST) complex to a pre-translocation (PRE) complex, thus giving elongation factor G a second chance to translocate the tRNAs correctly. Binds to ribosomes in a GTP-dependent manner. {ECO:0000255|HAMAP-Rule:MF_00071, ECO:0000269|PubMed:17110332, ECO:0000269|PubMed:20045415}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5462|reaction.ecocyc.RXN0-5462]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2569|gene.b2569]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P60785`
- `KEGG:ecj:JW2553;eco:b2569;ecoc:C3026_14230;`
- `GeneID:93774522;947051;`
- `GO:GO:0003746; GO:0003924; GO:0005525; GO:0005829; GO:0005886; GO:0009268; GO:0009409; GO:0009651; GO:0042274; GO:0042802; GO:0043022; GO:0043023; GO:0043024; GO:0045727; GO:0097216`
- `EC:3.6.5.n1`

## Notes

Elongation factor 4 (EF-4) (EC 3.6.5.n1) (Ribosomal back-translocase LepA)
