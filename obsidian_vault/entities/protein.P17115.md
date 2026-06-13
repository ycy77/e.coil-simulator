---
entity_id: "protein.P17115"
entity_type: "protein"
name: "gutQ"
source_database: "UniProt"
source_id: "P17115"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gutQ srlQ b2708 JW5431"
---

# gutQ

`protein.P17115`

## Static

- Type: `protein`
- Source: `UniProt:P17115`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the reversible aldol-ketol isomerization between D-ribulose 5-phosphate (Ru5P) and D-arabinose 5-phosphate (A5P). It appears that the physiological function of G-API may be to synthesize the regulatory molecule A5P, which in turn participates in the induction of the gut operon through an unknown mechanism. It is also able of sustaining the biosynthetic pathway of 3-deoxy-D-manno-octulosonate (KDO), a unique 8-carbon sugar component of lipopolysaccharides (LPSs). {ECO:0000269|PubMed:16199563}. D-arabinose-5-phosphate is a precursor for 2-keto-3-deoxy-octulosonate (KDO), a constituent of the cell envelope lipopolysaccharide. Arabinose-5-phosphate isomerase is responsible for the interconversion of D-ribulose-5-phosphate and D-arabinose-5-phosphate, the first committed step in the biosynthesis of KDO. The enzyme was originally isolated and partially characterized from E. coli strain B . gutQ encodes the second of two D-arabinose 5-phosphate isomerases (API) in E. coli. Its biochemical properties are very similar to those of CPLX0-1262 KdsD, the first identified D-arabinose 5-phosphate isomerase. Strains containing single mutations in either the kdsD or gutQ genes are viable and have a functional LPS. A kdsD gutQ double mutant strain required the addition of exogenous arabinose 5-phosphate for viability...

## Biological Role

Catalyzes D-arabinose-5-phosphate aldose-ketose-isomerase (reaction.R01530). Component of D-arabinose 5-phosphate isomerase GutQ (complex.ecocyc.CPLX0-3929).

## Annotation

FUNCTION: Catalyzes the reversible aldol-ketol isomerization between D-ribulose 5-phosphate (Ru5P) and D-arabinose 5-phosphate (A5P). It appears that the physiological function of G-API may be to synthesize the regulatory molecule A5P, which in turn participates in the induction of the gut operon through an unknown mechanism. It is also able of sustaining the biosynthetic pathway of 3-deoxy-D-manno-octulosonate (KDO), a unique 8-carbon sugar component of lipopolysaccharides (LPSs). {ECO:0000269|PubMed:16199563}.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R01530|reaction.R01530]] `KEGG` `database` - via EC:5.3.1.13
- `is_component_of` --> [[complex.ecocyc.CPLX0-3929|complex.ecocyc.CPLX0-3929]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b2708|gene.b2708]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P17115`
- `KEGG:ecj:JW5431;eco:b2708;ecoc:C3026_14905;`
- `GeneID:947587;`
- `GO:GO:0005524; GO:0019146; GO:0019294; GO:0042802; GO:0044010; GO:0046872; GO:0051289`
- `EC:5.3.1.13`

## Notes

Arabinose 5-phosphate isomerase GutQ (API) (G-API) (EC 5.3.1.13) (Phosphosugar aldol-ketol isomerase)
