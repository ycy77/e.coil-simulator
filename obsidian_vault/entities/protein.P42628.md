---
entity_id: "protein.P42628"
entity_type: "protein"
name: "dlsT"
source_database: "UniProt"
source_id: "P42628"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dlsT yhaO b3110 JW5519"
---

# dlsT

`protein.P42628`

## Static

- Type: `protein`
- Source: `UniProt:P42628`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: Plays a role in L-cysteine detoxification (PubMed:27435271). May transport both D- and L-serine (By similarity). {ECO:0000250|UniProtKB:Q8XAF5, ECO:0000269|PubMed:27435271}. CyuP is an L-cysteine-specific importer that, together wih G7622-MONOMER, supports anaerobic growth with cysteine as either the sole nitrogen or the sole carbon/energy source . CyuP-mediated [14C]cysteine import can be detected (after cysteine induction) using an engineered strain that lacks other interfering transporters . A ΔcyuP strain has decreased growth in the presence of cysteine and produces significantly less hydrogen sulfide than wild type . A ΔcyuP mutant does not show anaerobic cysteine sensitivity (10 mM cysteine) and does not show cysteine-dependent production of sulfide . cyuP forms an operon with cyuA; expression is activated by G6247-MONOMER "DecR" in the presence of L-cysteine (see further ). In the Transporter Classification Database , CyuP is a member of the Hydroxy/Aromatic Amino Acid Permease (HAAAP) Family within the Amino Acid-Polyamine-Organocation (APC) Superfamily. In enterohaemorrhagic E. coli (EHEC) the CyuP homolog, known as DlsT, is implicated in proton-dependent serine transport cyuP: cysteine utilization permease

## Biological Role

Catalyzes L-cysteine import (reaction.ecocyc.RXN-23966).

## Annotation

FUNCTION: Plays a role in L-cysteine detoxification (PubMed:27435271). May transport both D- and L-serine (By similarity). {ECO:0000250|UniProtKB:Q8XAF5, ECO:0000269|PubMed:27435271}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-23966|reaction.ecocyc.RXN-23966]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3110|gene.b3110]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P42628`
- `KEGG:ecj:JW5519;eco:b3110;ecoc:C3026_16970;`
- `GeneID:75205080;947628;`
- `GO:GO:0005886; GO:0006865; GO:0009093; GO:0022857; GO:0033229; GO:1903712`

## Notes

Probable serine transporter
