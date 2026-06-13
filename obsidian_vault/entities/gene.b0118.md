---
entity_id: "gene.b0118"
entity_type: "gene"
name: "acnB"
source_database: "NCBI RefSeq"
source_id: "gene-b0118"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0118"
  - "acnB"
---

# acnB

`gene.b0118`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0118`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

acnB (gene.b0118) is a gene entity. It encodes acnB (protein.P36683). Encoded protein function: FUNCTION: Involved in the catabolism of short chain fatty acids (SCFA) via the tricarboxylic acid (TCA)(acetyl degradation route) and the 2-methylcitrate cycle I (propionate degradation route). Catalyzes the reversible isomerization of citrate to isocitrate via cis-aconitate. Also catalyzes the hydration of 2-methyl-cis-aconitate to yield (2R,3S)-2-methylisocitrate. The apo form of AcnB functions as a RNA-binding regulatory protein. During oxidative stress inactive AcnB apo-enzyme without iron sulfur clusters binds the acnB mRNA 3' UTRs (untranslated regions), stabilizes acnB mRNA and increases AcnB synthesis, thus mediating a post-transcriptional positive autoregulatory switch. AcnB also decreases the stability of the sodA transcript. {ECO:0000269|PubMed:10585860, ECO:0000269|PubMed:10589714, ECO:0000269|PubMed:11932448, ECO:0000269|PubMed:12473114, ECO:0000269|PubMed:15882410, ECO:0000269|PubMed:8000525, ECO:0000269|PubMed:8932712}. EcoCyc product frame: ACONITATEDEHYDRB-MONOMER. EcoCyc synonyms: yacJ, yacI. Genomic coordinates: 131615-134212. EcoCyc protein note: There are two aconitases in E. coli, both of which catalyze the reversible isomerization of citrate and iso-citrate via cis-aconitate...

## Biological Role

Repressed by fis (protein.P0A6R3), arcA (protein.P0A9Q1). Activated by Cra-β-D-fructofuranose 1-phosphate (complex.ecocyc.CPLX-127), rpoD (protein.P00579).

## Enriched Pathways

- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01210` 2-Oxocarboxylic acid metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P36683|protein.P36683]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[complex.ecocyc.CPLX-127|complex.ecocyc.CPLX-127]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=acnB; function=+
- `represses` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=acnB; function=-
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `S` - regulator=ArcA; target=acnB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0000411,ECOCYC:EG12316,GeneID:944864`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:131615-134212:+; feature_type=gene
