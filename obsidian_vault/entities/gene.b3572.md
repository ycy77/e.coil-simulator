---
entity_id: "gene.b3572"
entity_type: "gene"
name: "avtA"
source_database: "NCBI RefSeq"
source_id: "gene-b3572"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3572"
  - "avtA"
---

# avtA

`gene.b3572`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3572`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

avtA (gene.b3572) is a gene entity. It encodes avtA (protein.P09053). Encoded protein function: FUNCTION: Involved in the biosynthesis of alanine. {ECO:0000269|PubMed:13034817, ECO:0000269|PubMed:20729367}. EcoCyc product frame: VALINE-PYRUVATE-AMINOTRANSFER-MONOMER. Genomic coordinates: 3739705-3740958. EcoCyc protein note: Valine-pyruvate aminotransferase (transaminase C) catalyzes the transamination reaction that converts α-keto-isovalerate to valine and alanine to pyruvate . This makes it the effective last step in potential synthetic routes to both alanine and valine. Transaminase C may also catalyze the interconversion of α-ketobutyrate and α-aminobutyrate . A homology model of the enzyme based on the crystal structure of AlaA has been generated . An ilvE avtA double mutant requires isoleucine and valine for growth . avtA is a multicopy suppressor of the isoleucine requirement of an ilvE mutant . An alaA avtA double mutant forms small colonies on agar plates. An alaA avtA alaC triple mutant has a slow growth phenotype in liquid medium. The defects of the double and triple mutants can be rescued by addition of alanine . Under competitive growth conditions in rich media, the ΔavtA mutation does not confer a disadvantage compared to wild type . AvtA expression is suppressed by excess alanine and leucine . AvtA: "alanine-valine transaminase"

## Biological Role

Repressed by lrp (protein.P0ACJ0). Activated by lrp (protein.P0ACJ0).

## Enriched Pathways

- `eco00290` Valine, leucine and isoleucine biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P09053|protein.P09053]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB|EcoCyc` `S` - regulator=Lrp; target=avtA; function=-+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB` `S` - regulator=Lrp; target=avtA; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0011671,ECOCYC:EG10107,GeneID:948087`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3739705-3740958:+; feature_type=gene
