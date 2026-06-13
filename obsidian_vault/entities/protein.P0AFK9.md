---
entity_id: "protein.P0AFK9"
entity_type: "protein"
name: "potD"
source_database: "UniProt"
source_id: "P0AFK9"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:1939142}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "potD b1123 JW1109"
---

# potD

`protein.P0AFK9`

## Static

- Type: `protein`
- Source: `UniProt:P0AFK9`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:1939142}.

## Enriched Summary

FUNCTION: Required for the activity of the bacterial periplasmic transport system of putrescine and spermidine. Polyamine binding protein. {ECO:0000269|PubMed:1939142}. potD encodes the periplasmic binding protein of an ATP dependent spermidine uptake system. PotD binds putrescine and spermidine ; PotD binds spermidine (Kd = 3.2 µM , Kd = 5.8 nM ) but will also bind putrescine with a lower affinity (Kd = 100 µM) . Purified, crystallized PotD is a dimer but the molecule is monomeric in the presence of spermidine; the switch from dimer to monomer may have physiological significance . The PotD monomer consists of two domains connected through a hinge region (two β strands and a short peptide segment); the two domains are divided by a deep cleft which contains the substrate binding site; spermidine interacts directly with aromatic and acidic side chains atoms in the PotD binding site; it also interacts indirectly via a water molecule located in the binding site . PotD or PotD precursor functions as a transcription regulator of the the potABCD operon . PotD regulates biofilm formation through an unknown mechanism .

## Biological Role

Component of spermidine preferential ABC transporter (complex.ecocyc.ABC-24-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Required for the activity of the bacterial periplasmic transport system of putrescine and spermidine. Polyamine binding protein. {ECO:0000269|PubMed:1939142}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-24-CPLX|complex.ecocyc.ABC-24-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1123|gene.b1123]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AFK9`
- `KEGG:ecj:JW1109;eco:b1123;ecoc:C3026_06760;`
- `GeneID:86863622;945682;`
- `GO:GO:0015847; GO:0015848; GO:0016020; GO:0019809; GO:0019810; GO:0030288; GO:1903711`

## Notes

Spermidine/putrescine-binding periplasmic protein (SPBP)
