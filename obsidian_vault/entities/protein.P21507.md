---
entity_id: "protein.P21507"
entity_type: "protein"
name: "srmB"
source_database: "UniProt"
source_id: "P21507"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00967}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "srmB rbaB rhlA b2576 JW2560"
---

# srmB

`protein.P21507`

## Static

- Type: `protein`
- Source: `UniProt:P21507`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00967}.

## Enriched Summary

FUNCTION: DEAD-box RNA helicase involved in the assembly of the 50S ribosomal subunit at low temperature. Exhibits RNA-stimulated ATP hydrolysis and RNA unwinding activity. Acts before DeaD. {ECO:0000255|HAMAP-Rule:MF_00967, ECO:0000269|PubMed:12787353, ECO:0000269|PubMed:15148362, ECO:0000269|PubMed:15196029}. SrmB is a DEAD-box protein with RNA helicase activity that facilitates an early step in the assembly of the 50S subunit of the ribosome . Recent data suggest that SrmB facilitates ribosome assembly by acting both as an RNA chaperone to resolve misfolded and trapped RNA structures and by stabilizing early ribosomal protein and rRNA binding events . The SrmB protein was found to be associated with a pre-50S ribosomal particle and forms a complex with ribosomal proteins L4, L24, and the region of 23S rRNA that interacts with L4 and L24 . The site of SrmB action is different from its binding site; models for SrmB activity during 50S ribosomal subunit assembly are presented . SrmB positively regulates expression of the ribosomal proteins EG10874-MONOMER L13 and EG10908-MONOMER S9 by preventing premature transcription termination; thus, the role of SrmB in ribosome assembly may be to ensure the synthesis of adequate levels of L13 and S9 . SrmB activates expression of the CSRB-RNA by promoting normal binding of UvrY to csrB...

## Biological Role

Catalyzes RXN-24178 (reaction.ecocyc.RXN-24178).

## Annotation

FUNCTION: DEAD-box RNA helicase involved in the assembly of the 50S ribosomal subunit at low temperature. Exhibits RNA-stimulated ATP hydrolysis and RNA unwinding activity. Acts before DeaD. {ECO:0000255|HAMAP-Rule:MF_00967, ECO:0000269|PubMed:12787353, ECO:0000269|PubMed:15148362, ECO:0000269|PubMed:15196029}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-24178|reaction.ecocyc.RXN-24178]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2576|gene.b2576]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P21507`
- `KEGG:ecj:JW2560;eco:b2576;ecoc:C3026_14270;`
- `GeneID:947055;`
- `GO:GO:0000027; GO:0003724; GO:0005524; GO:0005829; GO:0008143; GO:0008186; GO:0016887; GO:0031555; GO:0033592`
- `EC:3.6.4.13`

## Notes

ATP-dependent RNA helicase SrmB (EC 3.6.4.13)
