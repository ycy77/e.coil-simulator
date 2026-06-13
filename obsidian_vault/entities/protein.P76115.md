---
entity_id: "protein.P76115"
entity_type: "protein"
name: "pqqU"
source_database: "UniProt"
source_id: "P76115"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000269|PubMed:32355044}; Multi-pass membrane protein {ECO:0000269|PubMed:32355044}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pqqU yncD b1451 JW1446"
---

# pqqU

`protein.P76115`

## Static

- Type: `protein`
- Source: `UniProt:P76115`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000269|PubMed:32355044}; Multi-pass membrane protein {ECO:0000269|PubMed:32355044}.

## Enriched Summary

FUNCTION: Mediates the TonB-dependent high affinity transport across the outer membrane of pyrroloquinoline quinone (PQQ), a redox cofactor required for the activity of Gcd and Asd dehydrogenases (PubMed:36054785). The uptake process is energised via the TonB-ExbBD complex (PubMed:36054785). Not involved in the transport of an iron-containing substrate under laboratory conditions (PubMed:32355044, PubMed:36054785). {ECO:0000269|PubMed:32355044, ECO:0000269|PubMed:36054785}. pqqU (formerly yncD) encodes an outer membrane protein that mediates binding and CPLX0-1923 TonB-dependent active transport of pyrroloquinoline quinone - a redox cofactor required by the dehydrogenases GLUCDEHYDROG-MONOMER Gcd and G6437-MONOMER YliI - across the outer membrane . PqqU supports the growth of a PTS-deficient E. coli strain in glucose minimal medium at low PQQ concentrations (~ 1nmol/L); at higher PQQ concentrations growth of this strain is PqqU-independent possibly due to porin-mediated PQQ diffusion . PqqU is a member of the Outer Membrane Receptor (OMR) family of TonB dependent transporters . A strain with a transposon insertion in yncD shows increased fitness during selection for thiamine diphosphate (TPP) production in a competitive growth assay; a yncD null mutant produces a higher extracellular TPP titer...

## Biological Role

Component of pyrroloquinoline quinone outer membrane transport complex (complex.ecocyc.CPLX0-9372).

## Annotation

FUNCTION: Mediates the TonB-dependent high affinity transport across the outer membrane of pyrroloquinoline quinone (PQQ), a redox cofactor required for the activity of Gcd and Asd dehydrogenases (PubMed:36054785). The uptake process is energised via the TonB-ExbBD complex (PubMed:36054785). Not involved in the transport of an iron-containing substrate under laboratory conditions (PubMed:32355044, PubMed:36054785). {ECO:0000269|PubMed:32355044, ECO:0000269|PubMed:36054785}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-9372|complex.ecocyc.CPLX0-9372]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1451|gene.b1451]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76115`
- `KEGG:ecj:JW1446;eco:b1451;ecoc:C3026_08440;`
- `GeneID:946015;`
- `GO:GO:0009279; GO:0015344; GO:0016020; GO:0030003; GO:0038023; GO:0044718; GO:1902495`

## Notes

Pyrroloquinoline quinone transporter (PQQ transporter) (TonB-dependent receptor PqqU)
