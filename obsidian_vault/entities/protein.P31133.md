---
entity_id: "protein.P31133"
entity_type: "protein"
name: "potF"
source_database: "UniProt"
source_id: "P31133"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:8416922}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "potF b0854 JW0838"
---

# potF

`protein.P31133`

## Static

- Type: `protein`
- Source: `UniProt:P31133`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:8416922}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex PotFGHI involved in putrescine uptake (PubMed:23719730, PubMed:8416922). Binds putrescine (PubMed:8416922, PubMed:9651355). Imports putrescine for maintenance of the optimal concentration of polyamines necessary for cell growth in the presence of glucose (PubMed:23719730). {ECO:0000269|PubMed:23719730, ECO:0000269|PubMed:8416922, ECO:0000269|PubMed:9651355}. PotF is the periplasmic, putrescine binding protein of an ATP-dependent putrescine uptake system. PotF binds putrescine in a 1:1 ratio; PotF has 35% sequence similarity with POTD-MONOMER PotD - the spermidine preferential binding protein of the PotABCD polyamine uptake system . PotF binds its endogenous ligand, putrescine, with high affinity (Kd=4.8 nM ; Kd=68 nM ). Purified PotF also binds CADAVERINE (Kd=68 nM ) and AGMATHINE (Kd=0.22 µM ), and with less affinity, SPERMIDINE and SPERMINE ). In the crystal structure reported by PotF consists of two globular domains and three interdomain linker segments; the two domains are divided by a deep cleft which contains the substrate binding site; bound putrescine is completely enclosed within the cleft and is held in place through multiple direct and indirect (water-mediated) interactions with PotF residues. Structures of apo-PotF in open and closed conformation and in complex with various polyamine ligands are also available...

## Biological Role

Component of putrescine ABC transporter (complex.ecocyc.ABC-25-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex PotFGHI involved in putrescine uptake (PubMed:23719730, PubMed:8416922). Binds putrescine (PubMed:8416922, PubMed:9651355). Imports putrescine for maintenance of the optimal concentration of polyamines necessary for cell growth in the presence of glucose (PubMed:23719730). {ECO:0000269|PubMed:23719730, ECO:0000269|PubMed:8416922, ECO:0000269|PubMed:9651355}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-25-CPLX|complex.ecocyc.ABC-25-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b0854|gene.b0854]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P31133`
- `KEGG:ecj:JW0838;eco:b0854;ecoc:C3026_05330;`
- `GeneID:945480;`
- `GO:GO:0015847; GO:0016020; GO:0019809; GO:0019810; GO:0030288; GO:0055052`

## Notes

Putrescine-binding periplasmic protein PotF
