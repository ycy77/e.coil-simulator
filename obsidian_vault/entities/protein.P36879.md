---
entity_id: "protein.P36879"
entity_type: "protein"
name: "yadG"
source_database: "UniProt"
source_id: "P36879"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yadG b0127 JW0123"
---

# yadG

`protein.P36879`

## Static

- Type: `protein`
- Source: `UniProt:P36879`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

Uncharacterized ABC transporter ATP-binding protein YadG YadG is the predicted ATP-binding subunit of a putative ATP-binding cassette (ABC) exporter complex . yadG transcription increases specifically in response to CPD-9138 and its indicator compounds 1,3-DNB, 2,4-DNT, and 2,6-DNT; the response was utilized for construction of an E. coli biosensor strain . A yadG deletion mutant is 2 fold more sensitive to X-radiation than wild type . This minimally characterized enzyme in E. coli was found to interact with the ENOLASE-MONOMER enzyme in glycolysis in a large assessment of protein-protein interactions (PPIs) . This protein was also shown to interact with the enzyme GLUTDECARBOXB-MONOMER in a protein-enzyme interactions (PEIs) study that examined the connection between protein-protein interactions (PPIs) and metabolomics networks studied in 22 different environmental conditions. This PEI may have a metabolic regulatory role in the PWY0-1305 pathway, in part because the PEI is conserved across many other bacterial taxa .

## Biological Role

Component of putative transport complex, ABC superfamily (complex.ecocyc.ABC-21-CPLX).

## Annotation

Uncharacterized ABC transporter ATP-binding protein YadG

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-21-CPLX|complex.ecocyc.ABC-21-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b0127|gene.b0127]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P36879`
- `KEGG:ecj:JW0123;eco:b0127;ecoc:C3026_00540;`
- `GeneID:86862635;944833;`
- `GO:GO:0005524; GO:0005886; GO:0010165; GO:0016887`

## Notes

Uncharacterized ABC transporter ATP-binding protein YadG
