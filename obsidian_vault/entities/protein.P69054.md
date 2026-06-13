---
entity_id: "protein.P69054"
entity_type: "protein"
name: "sdhC"
source_database: "UniProt"
source_id: "P69054"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "sdhC cybA b0721 JW0711"
---

# sdhC

`protein.P69054`

## Static

- Type: `protein`
- Source: `UniProt:P69054`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: Membrane-anchoring subunit of succinate dehydrogenase (SDH). SdhC is one of two membrane proteins in the four subunit succinate dehydrogenase (SQR) enzyme. SdhC and SdhD are the large and small subunits of cytochrome b556, respectively . The quinone binding (Qp) site resides in the interface between SdhB, SdhC and SdhD . The b556 type heme bridges both membrane subunits . Mutation of key heme binding residues in SdhC and SdhD does not affect proper assembly or physiological function of the complex . Despite similar function, hydrophobicity, and protein size, the SdhC and SdhD subunits of succinate dehydrogenase do not share significant sequence identity with the corresponding membrane-binding subunits of fumarate reductase, FrdC and FrdD .

## Biological Role

Component of succinate:quinone oxidoreductase (complex.ecocyc.CPLX0-8160), succinate:quinone oxidoreductase subcomplex (complex.ecocyc.SUCC-DEHASE).

## Enriched Pathways

- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00190` Oxidative phosphorylation (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

FUNCTION: Membrane-anchoring subunit of succinate dehydrogenase (SDH).

## Pathways

- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00190` Oxidative phosphorylation (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8160|complex.ecocyc.CPLX0-8160]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=3
- `is_component_of` --> [[complex.ecocyc.SUCC-DEHASE|complex.ecocyc.SUCC-DEHASE]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b0721|gene.b0721]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P69054`
- `KEGG:ecj:JW0711;eco:b0721;`
- `GeneID:945316;`
- `GO:GO:0005886; GO:0006099; GO:0008177; GO:0009055; GO:0009060; GO:0016020; GO:0017004; GO:0019646; GO:0020037; GO:0045273; GO:0046872; GO:0048039`

## Notes

Succinate dehydrogenase cytochrome b556 subunit (Cytochrome b-556)
