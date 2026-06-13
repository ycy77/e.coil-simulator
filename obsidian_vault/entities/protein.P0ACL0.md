---
entity_id: "protein.P0ACL0"
entity_type: "protein"
name: "glpR"
source_database: "UniProt"
source_id: "P0ACL0"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "glpR b3423 JW3386"
---

# glpR

`protein.P0ACL0`

## Static

- Type: `protein`
- Source: `UniProt:P0ACL0`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Repressor of the glycerol-3-phosphate regulon. The sn-Glycerol-3-phosphate repressor," GlpR, acts as the repressor of the glycerol-3-phosphate regulon, which is organized in different operons . However, the array of promoters repressed by GlpR has been expanded .This regulator is part of the glpEGR operon, yet it can also be constitutively expressed as an independent (glpR) transcription unit . Various target genes of GlpR were found to be downregulated after 10 minutes of exposure to 2.5 mM H2O2; in accordance, the glpR gene was slightly upregulated. On the other hand, many genes of the GlpR regulon appear to be induced at pH 5.8, contributing to cell survival under this pH condition . The activity of the GlpR iModulon increases in cells evolved on glycerol as a carbon source . The operons regulated by GlpR are induced when Escherichia coli is grown in the presence of the inductor, glycerol, or glycerol-3-phosphate (G3P), and the absence of glucose . In the absence of the inductor, this repressor binds in tandem to inverted repeat sequences that consist of 20-nucleotide-long DNA target sites . In contrast, discovered operons whose regulation appears to be mediated by a single GlpR site per operon. Binding of GlpR to DNA is diminished in the presence of the inducers glycerol or G3P...

## Biological Role

Component of GlpR-glycerol (complex.ecocyc.CPLX0-8057), GlpR-glycerol-sn-3-phosphate (complex.ecocyc.MONOMER-54).

## Annotation

FUNCTION: Repressor of the glycerol-3-phosphate regulon.

## Outgoing Edges (11)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8057|complex.ecocyc.CPLX0-8057]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` --> [[complex.ecocyc.MONOMER-54|complex.ecocyc.MONOMER-54]] `EcoCyc` `database` - EcoCyc component coefficient=
- `represses` --> [[gene.b2239|gene.b2239]] `RegulonDB` `C` - regulator=GlpR; target=glpQ; function=-
- `represses` --> [[gene.b2240|gene.b2240]] `RegulonDB` `C` - regulator=GlpR; target=glpT; function=-
- `represses` --> [[gene.b2241|gene.b2241]] `RegulonDB` `C` - regulator=GlpR; target=glpA; function=-
- `represses` --> [[gene.b2242|gene.b2242]] `RegulonDB` `C` - regulator=GlpR; target=glpB; function=-
- `represses` --> [[gene.b2243|gene.b2243]] `RegulonDB` `C` - regulator=GlpR; target=glpC; function=-
- `represses` --> [[gene.b3426|gene.b3426]] `RegulonDB` `S` - regulator=GlpR; target=glpD; function=-
- `represses` --> [[gene.b3925|gene.b3925]] `RegulonDB` `S` - regulator=GlpR; target=glpX; function=-
- `represses` --> [[gene.b3926|gene.b3926]] `RegulonDB` `S` - regulator=GlpR; target=glpK; function=-
- `represses` --> [[gene.b3927|gene.b3927]] `RegulonDB` `S` - regulator=GlpR; target=glpF; function=-

## Incoming Edges (0)

_None._

## External IDs

- `UniProt:P0ACL0`
- `KEGG:ecj:JW3386;ecoc:C3026_18560;`
- `GeneID:93778573;`
- `GO:GO:0000987; GO:0006071; GO:0006355; GO:0045892; GO:0098531`

## Notes

Glycerol-3-phosphate regulon repressor
