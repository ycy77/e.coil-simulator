---
entity_id: "gene.b3993"
entity_type: "gene"
name: "thiE"
source_database: "NCBI RefSeq"
source_id: "gene-b3993"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3993"
  - "thiE"
---

# thiE

`gene.b3993`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3993`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

thiE (gene.b3993) is a gene entity. It encodes thiE (protein.P30137). Encoded protein function: FUNCTION: Condenses 4-methyl-5-(beta-hydroxyethyl)thiazole monophosphate (THZ-P) and 2-methyl-4-amino-5-hydroxymethyl pyrimidine pyrophosphate (HMP-PP) to form thiamine monophosphate (TMP). {ECO:0000269|PubMed:15292217, ECO:0000269|Ref.5}. EcoCyc product frame: THIE-MONOMER. EcoCyc synonyms: thiA. Genomic coordinates: 4193569-4194204. EcoCyc protein note: Thiamine phosphate synthase (ThiE) is involved in the biosynthesis of thiamine. Thiamine biosynthesis involves the separate formation of a pyrimidine and a thiazole precursors, which are then coupled to form thiamine phosphate. ThiE combines the pyrimidine component AMINO-HYDROXYMETHYL-METHYLPYRIMIDINE-PP (HMP-PP) with either THZ-P (HET-P), its carboxylated version CPD-13576 (cHET-P), or the tautomeric form CPD-13575 (cThz*-P) to generate thiamine phosphate . ThiE was identified, overexpressed and found to be required for the linkage of thiazole and pyrimidine . Null mutants of thiE require thiamine for growth . The crystal structure of ThiE from Bacillus subtilis has been determined at 1.25 Å .

## Enriched Pathways

- `eco00730` Thiamine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P30137|protein.P30137]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0013055,ECOCYC:EG11586,GeneID:948491`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4193569-4194204:-; feature_type=gene
