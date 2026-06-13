---
entity_id: "protein.P45395"
entity_type: "protein"
name: "kdsD"
source_database: "UniProt"
source_id: "P45395"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "kdsD yrbH b3197 JW3164"
---

# kdsD

`protein.P45395`

## Static

- Type: `protein`
- Source: `UniProt:P45395`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Involved in the biosynthesis of 3-deoxy-D-manno-octulosonate (KDO), a unique 8-carbon sugar component of lipopolysaccharides (LPSs). KdsD is not essential in the KDO biosynthesis and can be substituted by GutQ. Catalyzes the reversible aldol-ketol isomerization between D-ribulose 5-phosphate (Ru5P) and D-arabinose 5-phosphate (A5P). {ECO:0000269|PubMed:12805358, ECO:0000269|PubMed:16199563, ECO:0000269|PubMed:16765569, ECO:0000269|PubMed:20039350}. D-arabinose-5-phosphate is a precursor for KDO (2-keto-3-deoxy-octulosonate), a constituent of the cell envelope lipopolysaccharide. Arabinose-5-phosphate isomerase is responsible for the interconversion of D-ribulose-5-phosphate and D-arabinose-5-phosphate, the first committed step in the biosynthesis of KDO. The enzyme was originally isolated and partially characterized from E. coli strain B . KdsD is a tetramer in solution. The reaction kinetics, specificity, and optimal conditions have been characterized, and the physical characteristics of the active site are discussed . Substrate specificity was investigated by saturation transfer difference NMR spectroscopy . The structure of the sugar isomerase domain of KdsD was predicted using homology modeling; site-directed mutagenesis of the conserved Lys59 and His193 residues showed that they were important for catalysis or substrate recognition...

## Biological Role

Catalyzes D-arabinose-5-phosphate aldose-ketose-isomerase (reaction.R01530). Component of D-arabinose 5-phosphate isomerase KdsD (complex.ecocyc.CPLX0-1262).

## Enriched Pathways

- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Annotation

FUNCTION: Involved in the biosynthesis of 3-deoxy-D-manno-octulosonate (KDO), a unique 8-carbon sugar component of lipopolysaccharides (LPSs). KdsD is not essential in the KDO biosynthesis and can be substituted by GutQ. Catalyzes the reversible aldol-ketol isomerization between D-ribulose 5-phosphate (Ru5P) and D-arabinose 5-phosphate (A5P). {ECO:0000269|PubMed:12805358, ECO:0000269|PubMed:16199563, ECO:0000269|PubMed:16765569, ECO:0000269|PubMed:20039350}.

## Pathways

- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R01530|reaction.R01530]] `KEGG` `database` - via EC:5.3.1.13
- `is_component_of` --> [[complex.ecocyc.CPLX0-1262|complex.ecocyc.CPLX0-1262]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b3197|gene.b3197]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P45395`
- `KEGG:ecj:JW3164;eco:b3197;ecoc:C3026_17400;`
- `GeneID:93778784;947734;`
- `GO:GO:0019146; GO:0019294; GO:0042802; GO:0046872; GO:0051289; GO:0097367`
- `EC:5.3.1.13`

## Notes

Arabinose 5-phosphate isomerase KdsD (API) (L-API) (EC 5.3.1.13)
