---
entity_id: "protein.P0ABM9"
entity_type: "protein"
name: "ccmH"
source_database: "UniProt"
source_id: "P0ABM9"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ccmH yejP b2194 JW2182"
---

# ccmH

`protein.P0ABM9`

## Static

- Type: `protein`
- Source: `UniProt:P0ABM9`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: May be required for the biogenesis of c-type cytochromes. Possible subunit of a heme lyase. CcmH and EG12054-MONOMER CcmF are the components of holocytochrome c synthase in the System I pathway of cytochome c maturation; CcmFH releases heme from holoCCME-MONOMER CcmE and transfers it to apocytochromes in the periplasm. ccmH is part of an 8 gene cluster (ccmABCDEFGH) which bears sequence similarity to Bradyrhizobium japonicum genes that are required for the biogenesis of Cytochromes-c "c-type cytochromes"; an E. coli ΔccmA-H mutant strain (EC06) is not able to produce mature c-type cytochromes under anaerobic, nonfermentative growth conditions (see also ). CcmH is anchored to the membrane by two transmembrane regions; the protein contains an (essential) N-terminal periplasmic oxidoreductase domain containing the CXXC active site motif and a second (non-essential) C-terminal periplasmic domain containing tetratricopeptide repeat (TPR) motifs . The oxidized form of EG12053-MONOMER CcmG accumulates in mutants defective in CcmF . CcmH copurifies with CcmF ; the purified CcmFH complex also contains β-heme which is a stable component of CcmF; the CcmFH complex functions as a cytochrome c synthetase and as a quinol:heme oxidoreductase (and see )...

## Biological Role

Catalyzes RXN-21422 (reaction.ecocyc.RXN-21422). Component of holocytochrome c synthase complex (complex.ecocyc.CPLX-9494).

## Annotation

FUNCTION: May be required for the biogenesis of c-type cytochromes. Possible subunit of a heme lyase.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN-21422|reaction.ecocyc.RXN-21422]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_component_of` --> [[complex.ecocyc.CPLX-9494|complex.ecocyc.CPLX-9494]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2194|gene.b2194]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ABM9`
- `KEGG:ecj:JW2182;eco:b2194;ecoc:C3026_12265;`
- `GeneID:75172321;946623;`
- `GO:GO:0005886; GO:0015035; GO:0017004; GO:0046872`

## Notes

Cytochrome c-type biogenesis protein CcmH
