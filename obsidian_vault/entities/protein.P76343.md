---
entity_id: "protein.P76343"
entity_type: "protein"
name: "msrQ"
source_database: "UniProt"
source_id: "P76343"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_01207, ECO:0000305|PubMed:26641313}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "msrQ yedZ b1972 JW1955"
---

# msrQ

`protein.P76343`

## Static

- Type: `protein`
- Source: `UniProt:P76343`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_01207, ECO:0000305|PubMed:26641313}.

## Enriched Summary

FUNCTION: Part of the MsrPQ system that repairs oxidized periplasmic proteins containing methionine sulfoxide residues (Met-O), using respiratory chain electrons. Thus protects these proteins from oxidative-stress damage caused by reactive species of oxygen and chlorine. MsrPQ is essential for the maintenance of envelope integrity under bleach stress, rescuing a wide series of structurally unrelated periplasmic proteins from methionine oxidation, including the primary periplasmic chaperone SurA and the lipoprotein Pal. MsrQ provides electrons for reduction to the reductase catalytic subunit MsrP, using the quinone pool of the respiratory chain. {ECO:0000269|PubMed:26641313}. MsrQ (formerly YedZ) is a heme-binding, inner membrane quinol dehydrogenase that provides reducing equivalents to MsrP which in turn, reduces oxidized methionine residues of functionally diverse periplasmic proteins. The MsrPQ system protects periplasmic proteins, including SurA and Pal, from oxidative damage . MsrQ is a member of the ferric reductase domain (FRD) superfamily ; MsrQ may also receive electrons from the cytosolic NAD(P)H:flavin reductase FMNREDUCT-MONOMER Fre; purified MsrQ can be efficiently reduced by Fre in the presence of free FMN and NADPH...

## Biological Role

Component of periplasmic protein-L-methionine sulfoxide reducing system (complex.ecocyc.CPLX0-8213).

## Annotation

FUNCTION: Part of the MsrPQ system that repairs oxidized periplasmic proteins containing methionine sulfoxide residues (Met-O), using respiratory chain electrons. Thus protects these proteins from oxidative-stress damage caused by reactive species of oxygen and chlorine. MsrPQ is essential for the maintenance of envelope integrity under bleach stress, rescuing a wide series of structurally unrelated periplasmic proteins from methionine oxidation, including the primary periplasmic chaperone SurA and the lipoprotein Pal. MsrQ provides electrons for reduction to the reductase catalytic subunit MsrP, using the quinone pool of the respiratory chain. {ECO:0000269|PubMed:26641313}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8213|complex.ecocyc.CPLX0-8213]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1972|gene.b1972]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76343`
- `KEGG:ecj:JW1955;eco:b1972;ecoc:C3026_11140;`
- `GeneID:946483;`
- `GO:GO:0005886; GO:0009055; GO:0010181; GO:0016679; GO:0020037; GO:0030091; GO:0046872`

## Notes

Protein-methionine-sulfoxide reductase heme-binding subunit MsrQ (Flavocytochrome MsrQ)
