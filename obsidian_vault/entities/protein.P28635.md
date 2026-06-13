---
entity_id: "protein.P28635"
entity_type: "protein"
name: "metQ"
source_database: "UniProt"
source_id: "P28635"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell membrane {ECO:0000305}; Lipid-anchor {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "metQ yaeC b0197 JW0193"
---

# metQ

`protein.P28635`

## Static

- Type: `protein`
- Source: `UniProt:P28635`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell membrane {ECO:0000305}; Lipid-anchor {ECO:0000305}.

## Enriched Summary

FUNCTION: This protein is a component of a D-methionine permease, a binding protein-dependent, ATP-driven transport system. {ECO:0000269|PubMed:12169620}. MetQ is the substrate binding protein of a high affinity methionine uptake system. MetQ has a predicted signal sequence and a lipoprotein lipid attachment site . MetQ is a verified lipoprotein according to unpublished data by S. Matsuyama et al. (cited in ). A MetQ mutant (N229A)* with significantly reduced affinity for D-methionine and D-selenomethionine supports the uptake of D-selenomethionine at an increased rate compared to the wild type; a crystal structure of the transporter complex containing the apoMetQ variant (MetNIQN229A) indicates the presence of a substrate access channel through the binding protein to the translocation pathway and suggests that the MetQ binding protein may support the uptake of low-affinity substrates through a non-canonical mechanism whereby substrate binding occurs directly to the MetNIQ complex . * the MetQ mutant characterized by was a soluble variant lacking the lipoprotein signal peptide

## Biological Role

Component of L-methionine/D-methionine ABC transporter (complex.ecocyc.METNIQ-METHIONINE-ABC-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: This protein is a component of a D-methionine permease, a binding protein-dependent, ATP-driven transport system. {ECO:0000269|PubMed:12169620}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.METNIQ-METHIONINE-ABC-CPLX|complex.ecocyc.METNIQ-METHIONINE-ABC-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b0197|gene.b0197]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P28635`
- `KEGG:ecj:JW0193;eco:b0197;ecoc:C3026_00915;`
- `GeneID:86862708;944893;`
- `GO:GO:0005886; GO:0015821; GO:0016020; GO:0030288; GO:0048473; GO:0055052; GO:1903692; GO:1990197`

## Notes

D-methionine-binding lipoprotein MetQ
