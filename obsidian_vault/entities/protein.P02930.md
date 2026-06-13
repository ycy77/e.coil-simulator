---
entity_id: "protein.P02930"
entity_type: "protein"
name: "tolC"
source_database: "UniProt"
source_id: "P02930"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000269|PubMed:15228545, ECO:0000269|PubMed:16079137, ECO:0000269|PubMed:21778229, ECO:0000269|PubMed:6337123, ECO:0000269|PubMed:9044294}; Multi-pass membrane protein {ECO:0000269|PubMed:15228545, ECO:0000269|PubMed:16079137, ECO:0000269|PubMed:21778229, ECO:0000269|PubMed:6337123, ECO:0000269|PubMed:9044294}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "tolC colE1-i mtcB mukA refI toc weeA b3035 JW5503"
---

# tolC

`protein.P02930`

## Static

- Type: `protein`
- Source: `UniProt:P02930`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000269|PubMed:15228545, ECO:0000269|PubMed:16079137, ECO:0000269|PubMed:21778229, ECO:0000269|PubMed:6337123, ECO:0000269|PubMed:9044294}; Multi-pass membrane protein {ECO:0000269|PubMed:15228545, ECO:0000269|PubMed:16079137, ECO:0000269|PubMed:21778229, ECO:0000269|PubMed:6337123, ECO:0000269|PubMed:9044294}.

## Enriched Summary

FUNCTION: Outer membrane channel, which is required for the function of several efflux systems such as AcrAB-TolC, AcrEF-TolC, EmrAB-TolC and MacAB-TolC (PubMed:11274125, PubMed:15228545, PubMed:18955484, PubMed:28355133, PubMed:28504659, PubMed:31201302, PubMed:40083904, PubMed:40461577, PubMed:6337123). These systems are involved in export of antibiotics and other toxic compounds from the cell (PubMed:11274125, PubMed:18955484, PubMed:28504659). As part of the system, involved in the efflux of the immediate heme precursor, protoporphyrin IX (PPIX), which is probably an endogenous substrate (PubMed:25257218). Plays a role in substrate specificity during efflux (PubMed:32850959). TolC is also involved in import of colicin E1 into the cells (PubMed:23176499, PubMed:35199644). {ECO:0000269|PubMed:11274125, ECO:0000269|PubMed:15228545, ECO:0000269|PubMed:18955484, ECO:0000269|PubMed:23176499, ECO:0000269|PubMed:25257218, ECO:0000269|PubMed:28355133, ECO:0000269|PubMed:28504659, ECO:0000269|PubMed:31201302, ECO:0000269|PubMed:32850959, ECO:0000269|PubMed:35199644, ECO:0000269|PubMed:40083904, ECO:0000269|PubMed:40461577, ECO:0000269|PubMed:6337123}.

## Biological Role

Component of multidrug efflux pump EmrAB-TolC (complex.ecocyc.CPLX0-2121), multidrug efflux pump AcrEF-TolC (complex.ecocyc.CPLX0-2141), tripartite efflux pump EmrKY-TolC (complex.ecocyc.CPLX0-2161), multidrug efflux pump AcrAD-TolC (complex.ecocyc.CPLX0-3932), outer membrane channel TolC (complex.ecocyc.CPLX0-7964), ABC-type tripartite efflux pump (complex.ecocyc.TRANS-200-CPLX), multidrug efflux pump AcrAB-TolC (complex.ecocyc.TRANS-CPLX-201), multidrug efflux pump MdtABC-TolC (complex.ecocyc.TRANS-CPLX-202), and 1 more.

## Enriched Pathways

- `eco01501` beta-Lactam resistance (KEGG)
- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)
- `eco02020` Two-component system (KEGG)
- `eco03070` Bacterial secretion system (KEGG)

## Annotation

FUNCTION: Outer membrane channel, which is required for the function of several efflux systems such as AcrAB-TolC, AcrEF-TolC, EmrAB-TolC and MacAB-TolC (PubMed:11274125, PubMed:15228545, PubMed:18955484, PubMed:28355133, PubMed:28504659, PubMed:31201302, PubMed:40083904, PubMed:40461577, PubMed:6337123). These systems are involved in export of antibiotics and other toxic compounds from the cell (PubMed:11274125, PubMed:18955484, PubMed:28504659). As part of the system, involved in the efflux of the immediate heme precursor, protoporphyrin IX (PPIX), which is probably an endogenous substrate (PubMed:25257218). Plays a role in substrate specificity during efflux (PubMed:32850959). TolC is also involved in import of colicin E1 into the cells (PubMed:23176499, PubMed:35199644). {ECO:0000269|PubMed:11274125, ECO:0000269|PubMed:15228545, ECO:0000269|PubMed:18955484, ECO:0000269|PubMed:23176499, ECO:0000269|PubMed:25257218, ECO:0000269|PubMed:28355133, ECO:0000269|PubMed:28504659, ECO:0000269|PubMed:31201302, ECO:0000269|PubMed:32850959, ECO:0000269|PubMed:35199644, ECO:0000269|PubMed:40083904, ECO:0000269|PubMed:40461577, ECO:0000269|PubMed:6337123}.

## Pathways

- `eco01501` beta-Lactam resistance (KEGG)
- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)
- `eco02020` Two-component system (KEGG)
- `eco03070` Bacterial secretion system (KEGG)

## Outgoing Edges (9)

- `is_component_of` --> [[complex.ecocyc.CPLX0-2121|complex.ecocyc.CPLX0-2121]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=3 | EcoCyc transporter component coefficient=3
- `is_component_of` --> [[complex.ecocyc.CPLX0-2141|complex.ecocyc.CPLX0-2141]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=3 | EcoCyc transporter component coefficient=3
- `is_component_of` --> [[complex.ecocyc.CPLX0-2161|complex.ecocyc.CPLX0-2161]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=3 | EcoCyc transporter component coefficient=3
- `is_component_of` --> [[complex.ecocyc.CPLX0-3932|complex.ecocyc.CPLX0-3932]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=3 | EcoCyc transporter component coefficient=3
- `is_component_of` --> [[complex.ecocyc.CPLX0-7964|complex.ecocyc.CPLX0-7964]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3
- `is_component_of` --> [[complex.ecocyc.TRANS-200-CPLX|complex.ecocyc.TRANS-200-CPLX]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=3 | EcoCyc transporter component coefficient=3
- `is_component_of` --> [[complex.ecocyc.TRANS-CPLX-201|complex.ecocyc.TRANS-CPLX-201]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=3 | EcoCyc transporter component coefficient=3
- `is_component_of` --> [[complex.ecocyc.TRANS-CPLX-202|complex.ecocyc.TRANS-CPLX-202]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=3 | EcoCyc transporter component coefficient=3
- `is_component_of` --> [[complex.ecocyc.TRANS-CPLX-204|complex.ecocyc.TRANS-CPLX-204]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=3 | EcoCyc transporter component coefficient=3

## Incoming Edges (1)

- `encodes` <-- [[gene.b3035|gene.b3035]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P02930`
- `KEGG:ecj:JW5503;eco:b3035;ecoc:C3026_16575;`
- `GeneID:93778958;947521;`
- `GO:GO:0005216; GO:0009279; GO:0009410; GO:0009636; GO:0015125; GO:0015288; GO:0015562; GO:0015721; GO:0016020; GO:0034220; GO:0042802; GO:0042930; GO:0042931; GO:0046677; GO:0098567; GO:0140330; GO:1990196; GO:1990281; GO:1990961`

## Notes

Outer membrane protein TolC (Multidrug efflux pump subunit TolC) (Outer membrane factor TolC)
