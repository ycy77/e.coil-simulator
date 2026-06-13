---
entity_id: "protein.P24180"
entity_type: "protein"
name: "acrE"
source_database: "UniProt"
source_id: "P24180"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305|PubMed:11274125}; Lipid-anchor {ECO:0000305|PubMed:11274125}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "acrE envC b3265 JW3233"
---

# acrE

`protein.P24180`

## Static

- Type: `protein`
- Source: `UniProt:P24180`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305|PubMed:11274125}; Lipid-anchor {ECO:0000305|PubMed:11274125}.

## Enriched Summary

FUNCTION: Part of the tripartite efflux system AcrEF-TolC. Involved in the efflux of indole and organic solvents. {ECO:0000269|PubMed:10518736, ECO:0000269|PubMed:11274125}. AcrE shares 65% amino acid identity with the membrane fusion protein EG11703-MONOMER "AcrA" of the AcrAB efflux pump complex . acrEF is not expressed at significant levels in wild-type K-12 strains (see ) but is expressed at high level upon integration of IS1 or IS2 into the upstream region of the operon or upon deletion of the PD00288 "H-NS repressor protein" ; when expressed AcrE functions in Escherichia coli as part of a drug efflux system with the AcrF RND type permease and the TolC outer membrane protein (see CPLX0-2141 for more details). Cloned AcrE is an inner membrane anchored lipoprotein .

## Biological Role

Component of multidrug efflux pump AcrEF-TolC (complex.ecocyc.CPLX0-2141).

## Annotation

FUNCTION: Part of the tripartite efflux system AcrEF-TolC. Involved in the efflux of indole and organic solvents. {ECO:0000269|PubMed:10518736, ECO:0000269|PubMed:11274125}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-2141|complex.ecocyc.CPLX0-2141]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6 | EcoCyc transporter component coefficient=6

## Incoming Edges (1)

- `encodes` <-- [[gene.b3265|gene.b3265]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P24180`
- `KEGG:ecj:JW3233;eco:b3265;ecoc:C3026_17760;`
- `GeneID:75206113;947706;`
- `GO:GO:0005886; GO:0009410; GO:0022857; GO:0046677; GO:0098567; GO:0140330; GO:1990281`

## Notes

Multidrug export protein AcrE (Acriflavine resistance protein E) (Protein EnvC)
