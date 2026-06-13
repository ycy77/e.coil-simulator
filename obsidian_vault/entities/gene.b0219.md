---
entity_id: "gene.b0219"
entity_type: "gene"
name: "yafV"
source_database: "NCBI RefSeq"
source_id: "gene-b0219"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0219"
  - "yafV"
---

# yafV

`gene.b0219`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0219`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yafV (gene.b0219) is a gene entity. It encodes yafV (protein.Q47679). Encoded protein function: FUNCTION: Hydrolyzes alpha-ketoglutaramate (a-KGM) to alpha-ketoglutarate (alpha-KG) and ammonia, has weak activity on L-glutamine, almost no activity on deaminated glutathione (dGSH) and none on glutathione (By similarity). May function as a metabolite repair enzyme (By similarity). {ECO:0000250|UniProtKB:A0A140NDS5}. EcoCyc product frame: G6103-MONOMER. Genomic coordinates: 239419-240189. EcoCyc protein note: YafV is an ω-amidase that may function as a metabolite repair enzyme. α-ketoglutaramate (α-KGM) is the product of a potential side reaction of glutamine aminotransferases. The purified recombinant YafV expressed from an ASKA clone showed high activity toward α-KGM .

## Biological Role

Activated by nac (protein.Q47005).

## Enriched Pathways

- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q47679|protein.Q47679]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=yafV; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0000734,ECOCYC:G6103,GeneID:946585`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:239419-240189:-; feature_type=gene
