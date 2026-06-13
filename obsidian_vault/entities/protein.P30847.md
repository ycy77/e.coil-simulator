---
entity_id: "protein.P30847"
entity_type: "protein"
name: "baeS"
source_database: "UniProt"
source_id: "P30847"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "baeS b2078 JW2063"
---

# baeS

`protein.P30847`

## Static

- Type: `protein`
- Source: `UniProt:P30847`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}.

## Enriched Summary

FUNCTION: Member of the two-component regulatory system BaeS/BaeR which responds to envelope stress (PubMed:12354228, PubMed:21317898). Activates expression of periplasmic chaperone spy in response to spheroplast formation, indole and P pili protein PapG overexpression (PubMed:12354228). Activates BaeR by phosphorylation which then activates the mdtABCD (PubMed:12107134) and probably the CRISPR-Cas casABCDE-ygbT-ygbF operons (PubMed:21255106). {ECO:0000269|PubMed:12354228, ECO:0000269|PubMed:15522865, ECO:0000269|PubMed:21255106, ECO:0000269|PubMed:21317898}. BaeS is the sensor histidine kinase of the BaeSR two-component system. BaeS is a predicted integral membrane protein with sequence similarity to the sensor kinase family of proteins including a conserved histidine (His-250) which is presumed to be the site of autophosphorylation; overproduced BaeS autophosphorylates in the presence of ATP and transfers a phosphate to its cognate response regulator, BaeR in vitro; it is also able to phosphorylate purified OmpR with low efficiency (see also ). BaeSR is implicated in the adaption to envelope stress . The baeS1::Tn10cam mutation is a gain-of-function mutation which induces expression of a spy-lacZ transcriptional fusion in a Cpx-independent manner; inactivation of baeS prevents induction of spy expression in response to spheroplasting...

## Biological Role

Catalyzes 2.7.13.3-RXN (reaction.ecocyc.2.7.13.3-RXN).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Member of the two-component regulatory system BaeS/BaeR which responds to envelope stress (PubMed:12354228, PubMed:21317898). Activates expression of periplasmic chaperone spy in response to spheroplast formation, indole and P pili protein PapG overexpression (PubMed:12354228). Activates BaeR by phosphorylation which then activates the mdtABCD (PubMed:12107134) and probably the CRISPR-Cas casABCDE-ygbT-ygbF operons (PubMed:21255106). {ECO:0000269|PubMed:12354228, ECO:0000269|PubMed:15522865, ECO:0000269|PubMed:21255106, ECO:0000269|PubMed:21317898}.

## Pathways

- `eco02020` Two-component system (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.2.7.13.3-RXN|reaction.ecocyc.2.7.13.3-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2078|gene.b2078]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P30847`
- `KEGG:ecj:JW2063;eco:b2078;ecoc:C3026_11685;`
- `GeneID:75205982;946611;`
- `GO:GO:0000155; GO:0005524; GO:0005886; GO:0007165; GO:0016020; GO:0036460`
- `EC:2.7.13.3`

## Notes

Signal transduction histidine-protein kinase BaeS (EC 2.7.13.3)
