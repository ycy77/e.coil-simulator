---
entity_id: "protein.P0ABM1"
entity_type: "protein"
name: "ccmC"
source_database: "UniProt"
source_id: "P0ABM1"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ccmC yejT yejU b2199 JW2187"
---

# ccmC

`protein.P0ABM1`

## Static

- Type: `protein`
- Source: `UniProt:P0ABM1`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: Required for the export of heme to the periplasm for the biogenesis of c-type cytochromes. CcmC is an inner membrane protein required for for the transfer of heme to the periplasmic heme chaperone CCME-MONOMER CcmE during PWY-8147 "type I cytochrome c biogenesis". ccmC is part of an 8 gene cluster (ccmABCDEFGH) which bears sequence similarity to Bradyrhizobium japonicum genes that are required for the biogenesis of Cytochromes-c "c-type cytochromes"; an E. coli ΔccmA-H mutant strain (EC06) is not able to produce mature c-type cytochromes under anaerobic, nonfermentative growth conditions (see also ). An in-frame ccmC deletion mutant cannot synthesize holocytochrome c; CcmC is required for covalent incorporation of heme into the periplasmic heme chaperone CCME-MONOMER CcmE . CcmC is predicted to contain six transmembrane helices plus a periplasmic domain that contains the functionally important tryptophan-rich motif (the WWD domain) and two strictly conserved histidines implicated in heme binding (see also ). CcmC participates in what is sometimes referred to as 'step 1' of cyctochrome c biosynthesis which refers to the movement of heme across the membrane concomitant with the formation of a CcmC-heme-CcmE-CcmD complex and subsequent release of holoCcmE...

## Biological Role

Component of CcmCDE complex (complex.ecocyc.ABC-35-CPLX), CcmABCD release complex (complex.ecocyc.CPLX-9495).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Required for the export of heme to the periplasm for the biogenesis of c-type cytochromes.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.ABC-35-CPLX|complex.ecocyc.ABC-35-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` --> [[complex.ecocyc.CPLX-9495|complex.ecocyc.CPLX-9495]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2199|gene.b2199]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ABM1`
- `KEGG:ecj:JW2187;eco:b2199;ecoc:C3026_12290;`
- `GeneID:86860371;93774979;946703;`
- `GO:GO:0005886; GO:0015232; GO:0017003; GO:0017004; GO:0020037; GO:0043190; GO:1903607; GO:1904334`

## Notes

Heme exporter protein C (Cytochrome c-type biogenesis protein CcmC)
