---
entity_id: "gene.b4056"
entity_type: "gene"
name: "yjbQ"
source_database: "NCBI RefSeq"
source_id: "gene-b4056"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4056"
  - "yjbQ"
---

# yjbQ

`gene.b4056`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4056`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yjbQ (gene.b4056) is a gene entity. It encodes yjbQ (protein.P0AF48). Encoded protein function: UPF0047 protein YjbQ EcoCyc product frame: EG11935-MONOMER. Genomic coordinates: 4270238-4270654. EcoCyc protein note: Overexpression of YjbQ complements the thiamin auxotrophy of a thiE deletion mutant. The specific thiamine phosphate synthase (TPS) activity of YjbQ is thousands of times lower than that of ThiE; the His90 residue plays a critical role in TPS activity. The enzyme can be evolved into a more efficient TPS. TPS activity of YjbQ is not its primary physiological role . yjbQ was also isolated as a multicopy suppressor of the PLP auxotrophy of a pdxB deletion strain and may be part of a serendipitous metabolic pathway that produces an intermediate of the PYRIDOXSYN-PWY pathway, 3OH-4P-OH-ALPHA-KETOBUTYRATE, that lies downstream of PdxB . A yjbQ deletion mutant has no obvious growth defect, although a single thiE deletion mutant strain grows slightly better than a double thiE yjbQ deletion mutant . The average half life of yjbQR mRNA was determined to be 2.2 minutes .

## Biological Role

Repressed by lrp (protein.P0ACJ0), nac (protein.Q47005). Activated by gadE (protein.P63204).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AF48|protein.P0AF48]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P63204|protein.P63204]] `RegulonDB` `S` - regulator=GadE; target=yjbQ; function=+
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB|EcoCyc` `S` - regulator=Lrp; target=yjbQ; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=yjbQ; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0013286,ECOCYC:EG11935,GeneID:948561`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4270238-4270654:+; feature_type=gene
