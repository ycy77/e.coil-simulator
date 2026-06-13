---
entity_id: "protein.P24181"
entity_type: "protein"
name: "acrF"
source_database: "UniProt"
source_id: "P24181"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:11274125, ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:11274125, ECO:0000269|PubMed:15919996}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "acrF envD b3266 JW3234"
---

# acrF

`protein.P24181`

## Static

- Type: `protein`
- Source: `UniProt:P24181`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:11274125, ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:11274125, ECO:0000269|PubMed:15919996}.

## Enriched Summary

FUNCTION: Part of the tripartite efflux system AcrEF-TolC. Involved in the efflux of indole and organic solvents. {ECO:0000269|PubMed:10518736, ECO:0000269|PubMed:11274125}. AcrF shares 77% amino acid sequence identity with ACRB-MONOMER "AcrB" of the AcrAB multidrug efflux system . acrEF is not expressed at significant levels in wild-type K-12 strains (see ) but is expressed upon integration of IS1 or IS2 into the upstream region of the operon or upon deletion of the PD00288 "H-NS repressor protein" ; when expressed AcrF functions in Escherichia coli as part of a drug efflux system with the AcrE membrane fusion protein and the TolC outer membrane protein (see CPLX0-2141 for more details). acrF is one of 35 efflux-encoding genes that have been deleted or inactivated in 'Efflux KnockOut-35' (EKO-35) - a K-12 BW25133-derived strain that lacks 35 efflux pumps and can be used as a platform to study their function . The acrF Keio collection mutant (BW25113 ΔacrF::kan) shows a significant increase in swimming motility .

## Biological Role

Component of multidrug efflux pump AcrEF-TolC (complex.ecocyc.CPLX0-2141).

## Annotation

FUNCTION: Part of the tripartite efflux system AcrEF-TolC. Involved in the efflux of indole and organic solvents. {ECO:0000269|PubMed:10518736, ECO:0000269|PubMed:11274125}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-2141|complex.ecocyc.CPLX0-2141]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3 | EcoCyc transporter component coefficient=3

## Incoming Edges (1)

- `encodes` <-- [[gene.b3266|gene.b3266]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P24181`
- `KEGG:ecj:JW3234;eco:b3266;ecoc:C3026_17765;`
- `GeneID:947768;`
- `GO:GO:0005886; GO:0015562; GO:0042910; GO:0098567; GO:0140330; GO:1990281`

## Notes

Multidrug export protein AcrF (Acriflavine resistance protein F) (Protein EnvD)
