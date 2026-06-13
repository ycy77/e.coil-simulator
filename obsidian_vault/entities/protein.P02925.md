---
entity_id: "protein.P02925"
entity_type: "protein"
name: "rbsB"
source_database: "UniProt"
source_id: "P02925"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:1583688}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rbsB prlB rbsP b3751 JW3730"
---

# rbsB

`protein.P02925`

## Static

- Type: `protein`
- Source: `UniProt:P02925`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:1583688}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex RbsABC involved in ribose import. Binds ribose. Also serves as the primary chemoreceptor for chemotaxis. {ECO:0000269|PubMed:25533465, ECO:0000269|PubMed:4608146, ECO:0000269|PubMed:6327617, ECO:0000269|PubMed:7982928}. RbsB is the periplasmic ribose binding protein of an ATP-dependent ribose uptake system; ligand bound RbsB also interacts with the EG11018 "Trg" sensory protein to mediate taxis to ribose. The ribose binding protein is required for chemotaxis towards ribose; mutants lacking this protein do not demonstrate ribose mediated taxis . The RbsB molecule consists of two similar structured domains linked by a hinge region consisting of three short peptide stretches; bound β-D-ribopyranose is completely enclosed in a cleft between the domains . Non-liganded (open) structures of RbsB have also been obtained and conformational changes that the molecule undergoes during ligand binding and release are proposed . Regions/residues of RbsB involved in interaction with RbsC and with the chemosensory receptor have been identified RbsB has been used in the development of a TNT bioreporter . rbsB was found to be downregulated in a MG1655 lysogen carrying the Stx2a phage PA8 .

## Biological Role

Component of ribose ABC transporter (complex.ecocyc.ABC-28-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)
- `eco02030` Bacterial chemotaxis (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex RbsABC involved in ribose import. Binds ribose. Also serves as the primary chemoreceptor for chemotaxis. {ECO:0000269|PubMed:25533465, ECO:0000269|PubMed:4608146, ECO:0000269|PubMed:6327617, ECO:0000269|PubMed:7982928}.

## Pathways

- `eco02010` ABC transporters (KEGG)
- `eco02030` Bacterial chemotaxis (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-28-CPLX|complex.ecocyc.ABC-28-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b3751|gene.b3751]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P02925`
- `KEGG:ecj:JW3730;eco:b3751;ecoc:C3026_20320;`
- `GeneID:948261;`
- `GO:GO:0015752; GO:0016020; GO:0030288; GO:0048029; GO:0050918; GO:0055052; GO:0055085`

## Notes

Ribose import binding protein RbsB
