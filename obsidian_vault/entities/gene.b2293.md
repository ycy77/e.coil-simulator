---
entity_id: "gene.b2293"
entity_type: "gene"
name: "hxpA"
source_database: "NCBI RefSeq"
source_id: "gene-b2293"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2293"
  - "hxpA"
---

# hxpA

`gene.b2293`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2293`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hxpA (gene.b2293) is a gene entity. It encodes hxpA (protein.P77625). Encoded protein function: FUNCTION: Sugar-phosphate phosphohydrolase that appears to contribute to butanol tolerance (PubMed:27941785). Catalyzes the dephosphorylation of D-mannitol 1-phosphate and D-sorbitol 6-phosphate (PubMed:27941785). Is also able to dephosphorylate other sugar phosphates in vitro including ribose-5-phosphate (Rib5P), 2-deoxyribose-5-phosphate, fructose-1-phosphate (Fru1P), fructose-6-phosphate (Fru6P), and glucose-6-phosphate (Glu6P) (PubMed:16990279). Selectively hydrolyzes beta-D-glucose-1-phosphate (bGlu1P) and has no activity with the alpha form (PubMed:16990279). {ECO:0000269|PubMed:15808744, ECO:0000269|PubMed:16990279, ECO:0000269|PubMed:27941785}. EcoCyc product frame: G7187-MONOMER. EcoCyc synonyms: yfbT. Genomic coordinates: 2411439-2412089. EcoCyc protein note: The hexitol phosphatase activity of HxpA was discovered in a large-scale metabolomics screen for enzymatic activities of uncharacterized proteins in E. coli . HxpA is a sugar phosphatase belonging to the superfamily of haloacid dehalogenase (HAD)-like hydrolases. It shows a low level of substrate discrimination among its preferred substrates, although it does selectively hydrolyze β-D-glucose-1-phosphate and has no activity with the α form...

## Biological Role

Repressed by glaR (protein.P37338).

## Enriched Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77625|protein.P77625]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P37338|protein.P37338]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=hxpA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0007567,ECOCYC:G7187,GeneID:946777`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2411439-2412089:-; feature_type=gene
