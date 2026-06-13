---
entity_id: "protein.P0DM85"
entity_type: "protein"
name: "rdcA"
source_database: "UniProt"
source_id: "P0DM85"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:23994470}. Note=About half the protein co-localizes with beta sliding clamp (DnaN) at midcell, the rest without clamp in quarter-cell positions when chromosomes are condensed during DNA replication. {ECO:0000269|PubMed:23994470}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rdcA crfC yjdA b4109 JW4070"
---

# rdcA

`protein.P0DM85`

## Static

- Type: `protein`
- Source: `UniProt:P0DM85`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:23994470}. Note=About half the protein co-localizes with beta sliding clamp (DnaN) at midcell, the rest without clamp in quarter-cell positions when chromosomes are condensed during DNA replication. {ECO:0000269|PubMed:23994470}.

## Enriched Summary

FUNCTION: Regulatory protein that, together with its partner protein RdcB, activates the diguanylate cyclase E (DgcE) to control CsgD and biofilm matrix production (PubMed:31022167). Binds GTP and shows GTPase activity (PubMed:23994470, PubMed:31022167). The GTPase activity is essential for activation of DgcE (PubMed:31022167). The GTP-bound form of RdcA might be unable to activate DgcE because GTP may act as an allosteric inhibitor (PubMed:31022167). {ECO:0000269|PubMed:23994470, ECO:0000269|PubMed:31022167}.; FUNCTION: Is also proposed to be involved in chromosome segregation (PubMed:23994470). Is important for the colocalization of sister nascent DNA strands after replication fork passage during DNA replication, and for positioning and subsequent partitioning of sister chromosomes (PubMed:23994470). This activity is not affected by the presence or absence of GTP (PubMed:23994470). {ECO:0000269|PubMed:23994470}.

## Biological Role

Component of regulator of diguanylate cyclase RdcA (complex.ecocyc.CPLX0-8536).

## Annotation

FUNCTION: Regulatory protein that, together with its partner protein RdcB, activates the diguanylate cyclase E (DgcE) to control CsgD and biofilm matrix production (PubMed:31022167). Binds GTP and shows GTPase activity (PubMed:23994470, PubMed:31022167). The GTPase activity is essential for activation of DgcE (PubMed:31022167). The GTP-bound form of RdcA might be unable to activate DgcE because GTP may act as an allosteric inhibitor (PubMed:31022167). {ECO:0000269|PubMed:23994470, ECO:0000269|PubMed:31022167}.; FUNCTION: Is also proposed to be involved in chromosome segregation (PubMed:23994470). Is important for the colocalization of sister nascent DNA strands after replication fork passage during DNA replication, and for positioning and subsequent partitioning of sister chromosomes (PubMed:23994470). This activity is not affected by the presence or absence of GTP (PubMed:23994470). {ECO:0000269|PubMed:23994470}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8536|complex.ecocyc.CPLX0-8536]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b4109|gene.b4109]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0DM85`
- `KEGG:ecj:JW4070;eco:b4109;ecoc:C3026_22200;`
- `GeneID:948620;`
- `GO:GO:0003924; GO:0005525; GO:0005737; GO:0006260; GO:0007059; GO:0043022; GO:0043590; GO:1900231`
- `EC:3.6.-.-`

## Notes

Regulator of diguanylate cyclase RdcA (EC 3.6.-.-) (Clamp-binding protein CrfC) (Clamp-binding sister replication fork colocalization protein) (Dynamin-like GTPase RdcA) (Regulator of a diguanylate cyclase A)
