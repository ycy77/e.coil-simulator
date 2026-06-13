---
entity_id: "gene.b3223"
entity_type: "gene"
name: "nanE"
source_database: "NCBI RefSeq"
source_id: "gene-b3223"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3223"
  - "nanE"
---

# nanE

`gene.b3223`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3223`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nanE (gene.b3223) is a gene entity. It encodes nanE (protein.P0A761). Encoded protein function: FUNCTION: Converts N-acetylmannosamine-6-phosphate (ManNAc-6-P) to N-acetylglucosamine-6-phosphate (GlcNAc-6-P). {ECO:0000305}. EcoCyc product frame: NANE-MONOMER. EcoCyc synonyms: yhcJ. Genomic coordinates: 3370347-3371036. EcoCyc protein note: NanE is predicted to encode N-acetylmannosamine-6-phosphate 2-epimerase, an enzyme involved in the utilization of N-acetylneuraminate and N-acetylmannosamine as carbon sources . NanE from the pathogenic E. coli strain K1 has been purified and assayed . NanE can act as an allosteric activator of GLUCOSAMINE-6-P-DEAMIN-MONOMER . A protein with N-acetylmannosamine-6-phosphate epimerase activity was purified from E. coli K92; its molecular weight is 38.4 kDa, and its sequence was highly similar to pgl, but not nanE . Transcription of the nanATEKQ (sialic acid catabolic) operon is repressed by NanR . Expression of nanE is necessary for growth on ManNAc in an mlc mutant background . A nanE mutant is unable to utilize N-acetylneuraminate or N-glycolylneuraminate as the sole carbon source . A nanE mutant strain shows enhanced ethanol and hydrogen production when grown anaerobically in LB-glycerol...

## Biological Role

Repressed by fis (protein.P0A6R3), nanR (protein.P0A8W0). Activated by crp (protein.P0ACJ8).

## Enriched Pathways

- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A761|protein.P0A761]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=nanE; function=+
- `represses` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=nanE; function=-
- `represses` <-- [[protein.P0A8W0|protein.P0A8W0]] `RegulonDB` `C` - regulator=NanR; target=nanE; function=-

## External IDs

- `Dbxref:ASAP:ABE-0010575,ECOCYC:G7677,GeneID:947745`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3370347-3371036:-; feature_type=gene
