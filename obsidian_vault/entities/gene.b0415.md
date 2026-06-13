---
entity_id: "gene.b0415"
entity_type: "gene"
name: "ribE"
source_database: "NCBI RefSeq"
source_id: "gene-b0415"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0415"
  - "ribE"
---

# ribE

`gene.b0415`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0415`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ribE (gene.b0415) is a gene entity. It encodes ribE (protein.P61714). Encoded protein function: FUNCTION: Catalyzes the formation of 6,7-dimethyl-8-ribityllumazine by condensation of 5-amino-6-(D-ribitylamino)uracil with 3,4-dihydroxy-2-butanone 4-phosphate. This is the penultimate step in the biosynthesis of riboflavin. {ECO:0000269|PubMed:8969176}. EcoCyc product frame: LUMAZINESYN-MONOMER. EcoCyc synonyms: nusIII, ribH, ybaF. Genomic coordinates: 434647-435117. EcoCyc protein note: The ribE gene encodes lumazine synthase, an enzyme that catalyzes the penultimate step in the riboflavin biosynthesis pathway. The protein forms a hollow icosahedral capsid composed of 60 subunits. Unlike lumazine synthase from Bacillus subtilis, the E. coli enzyme is not physically associated with any other enzyme of the riboflavin biosynthetic pathway, including riboflavin synthase . ribE is an essential gene .

## Biological Role

Repressed by lrp (protein.P0ACJ0). Activated by rpoH (protein.P0AGB3).

## Enriched Pathways

- `eco00740` Riboflavin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P61714|protein.P61714]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=ribE; function=+
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0001444,ECOCYC:EG11322,GeneID:946453`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:434647-435117:+; feature_type=gene
